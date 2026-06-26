---
name: 지표산출 로직 (신규) — Finance/Sales/CS/Market 전체 51개
description: DB 테이블·컬럼·적용 로직이 확정된 신규 지표 정의. 기존 효율/수익 로직 포함, Sales/CS/Market 신규 영역 포함.
type: project
originSessionId: 2ee254d0-6942-470c-9dd0-3e6468e8aabf
---
신규 지표산출 로직 전체 (Finance Efficiency/Profit 4개 + Sales 19개 + CS 13개 + Market 15개)

**Why:** 기획팀이 확정한 DB 테이블·컬럼·산출 로직 기준서. 개발 요청서 작성 및 SDSC 협의 시 이 기준을 사용.

**How to apply:** 개발 요청서 산식·테이블·컬럼 기재 시 이 문서 기준 사용. 기존 메모리(project_indicator_definitions.md)보다 이 파일이 더 상세하고 확정본임.

---

## 핵심 DB 테이블 정보

| 스키마.테이블 | 용도 |
|---|---|
| `l_sap.orderlist` | 매출총계(vf219), 판매비총계(vf599) — Finance/Market 지표 |
| `c_tabadmin.bo_opportunity` | 영업기회(BO) 기본 정보 — Sales 지표 |
| `c_tabadmin.bo_solution` | 영업기회별 솔루션 — Sales 지표 |
| `c_tableau.solution_if_voc` | VoC 건수·오류·실사용자 — CS 지표 |

---

## 전제조건 (필터 로직)

- **■ (Finance)**: `((ww010_txt에 Implementation 없는 솔루션) & (ww007=3)) + ((ww010_txt에 Implementation 있는 솔루션) & (ww006=S135, ITO))`
  - 컬럼: l_sap.orderlist의 ww007(3분류), ww010/ww010_txt(솔루션), ww006(사업유형)
- **★ (Sales)**: bo_opportunity와 bo_solution을 opportunity_id로 JOIN, solution_id 확보
  - currency_iso_code ≠ 'KRW'인 경우 등록일 분기말 환율로 KRW 환산
  - opportunity_status = E0008(Cleansed) 제외
- **● (Market)**: IDC Market Data 활용, 대외만 해당
- **◆ (Market)**: IDC 외 매출·원가 등 당기 금액은 전망치(속보) 반영

---

## 분석주기 기준

| 주기 | 범위 |
|---|---|
| Monthly | 실적 25개월 |
| Quarterly | 실적 13분기 + 당분기 (총 14개) |
| Half-Year | 실적 7반기 + 당반기 (총 8개) |
| Yearly | 실적 3년 + 당년 (총 4년) |

---

## Finance (Efficiency / Profit) — 4개 지표

### 1. LTV (Customer Lifetime Value)
- **테이블**: l_sap.orderlist / **컬럼**: vf219
- **산식**: LTV = AAPA ÷ Recurring ARR 매출 이탈률
  - AAPA = sum(vf219) ÷ 고객 Count (고객 1인당 연평균 반복 매출)
  - 이탈률 = (1 - (N-1년 sum(vf219) ÷ N-2년 sum(vf219))) × 100 (%)
  - 단, N-1년 ≥ N-2년이면 이탈률 = 0 → LTV/LTV:CAC/CAC Payback 모두 표시 안 함
- **주기**: Yearly N-1~N-3 / **당기 포함**: 안 함

### 2. CAC (Customer Acquisition Cost)
- **테이블**: l_sap.orderlist / **컬럼**: vf599(판매비총계)
- **산식**: N-1년 CAC = N-2년 sum(vf599) ÷ N-1년 신규 고객 수
  - 신규 고객: (N-2년 vf219=0) & (N-1년 vf219≠0)
- **주기**: Yearly N-1~N-3 / **당기 포함**: 안 함

### 3. LTV/CAC Ratio
- **산식**: N-1년 LTV ÷ N-1년 CAC (타 지표 조합)
- **주기**: Yearly N-1~N-3

### 4. CAC Payback Period
- **산식**: N-1년 CAC ÷ N-1년 AAPA (타 지표 조합)
- ※ AAPA가 연간(ARR) 기준이므로 결과는 년 단위. 개월 환산 시 ×12 필요 여부 확인 필요
- **주기**: Yearly N-1~N-3

---

## Sales — 19개 지표 (주요 항목)

### 공통 테이블/컬럼
- **bo_opportunity**: opportunity_id, amount, currency_iso_code, created_date, first_closed_date, drop_date, lost_date, opportunity_status
- **bo_solution**: opportunity_id, solution_id
- **opportunity_status 값**: E0002(In Process), E0003(Won), E0004(Lost), E0007(Drop), E0008(Cleansed)

### 핵심 지표 산식
- **New BO**: created_date가 N기 범위 내인 BO 건수/금액
- **Existing BO**: created_date < N기 시작일 & 미종결(Won/Drop/Lost 아님)인 BO
- **Won BO**: opportunity_status=E0003 & first_closed_date가 N기 범위
- **Drop BO**: opportunity_status=E0007 & drop_date가 N기 범위
- **Lost BO**: opportunity_status=E0004 & lost_date가 N기 범위
- **In-process BO**: created_date ≤ N기 종료일 & opportunity_status=E0002
- **Win ratio**: Won ÷ (Won + Lost) × 100
- **Hit ratio**: Won ÷ (Won + Lost + Drop) × 100
- **Conversion ratio**: Won ÷ (Won + Lost + Drop + In-process) × 100
- **Avg. Sales Lead Time (Won)**: ∑(first_closed_date - created_date) ÷ Won BO Count

---

## CS — 13개 지표 (주요 항목)

- **테이블**: c_tableau.solution_if_voc / **컬럼**: gubun, cnt
  - VoC 건수: gubun = 'VOC_CNT'인 cnt 합
  - 오류건수(=체감불만건수): gubun = 'DIS_SATIST'인 cnt 합
  - 실사용자수(MAU): gubun = 'MAU'인 cnt 합
- 개선 건수·VoC 처리 리드타임·지연건수: 별도 CS Dashboard 데이터 필요 (미확정)

---

## Market — 14개 지표 (주요 항목)

- **TAM/SAM**: IDC Market Data 별도 제공
- **Revenue_전체**: ∑(l_sap.orderlist.vf219) — 대내외 합산
- **Revenue_대외**: Group Out 해당분의 ∑(vf219)
- **Market Share**: Revenue_대외 ÷ SAM × 100
- **Sales Ratio**: ∑(vf599) ÷ Revenue_전체 × 100
- **R&D Ratio**: ∑(연구개발비) ÷ Revenue_전체 × 100 (Excel 별도 제공)

---

## 주의사항

1. **테이블 전체명**: `l_sap.orderlist` (스키마 l_sap 포함) — 개발 요청서에 `orderlist`만 기재 중이므로 확인 필요
2. **AAPA vs ARPA**: 이 문서는 AAPA(Average Recurring **ARR** Per Account) 사용. 연간 기준.
3. **CAC Payback 단위**: 문서 산식에 ×12 없음 → 결과가 년 단위인지 개월 단위인지 확인 필요
