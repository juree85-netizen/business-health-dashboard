---
name: 사업건전성 대시보드 지표 정의 기준서
description: 59개 전체 지표 정의 및 산출식 — 효율/수익 개발 요청서 TBD 항목 산식 근거
type: project
originSessionId: 2ee254d0-6942-470c-9dd0-3e6468e8aabf
---
59개 지표 정의 기준서 (Finance Growth 39개 / Finance Efficiency&Profit 16개 / Customer 3개 / Product 1개)

**Why:** 효율/수익 개발 요청서 v0.2의 TBD 항목(Row 1·3·4·5·6) 산식을 이 기준서에서 발췌하여 채워야 함.

**How to apply:** 개발 요청서 산식 작성 시 아래 확정 산식을 기준으로 사용.

---

## 효율/수익 페이지 관련 핵심 지표 산식

### Row 1 — Sales Efficiency (분기 기준)
- **Gross Sales Efficiency** = 당 분기 총 신규 ARR ÷ 전 분기 총 영업/마케팅 비용(판매비)
  - 총 신규 ARR = New ARR + Expansion ARR (신규·기존 고객 합산)
  - 분기 ARR = 분기 MRR 합 × 4
  - 적정 수준: 0.8~1.2 (B2B SaaS 기준)
- **Net Sales Efficiency** = 당 분기 Net New ARR ÷ 전 분기 총 영업/마케팅 비용(판매비)
  - Net New ARR = New ARR + Expansion ARR - Contraction ARR - Churn ARR = 당기ARR - 전기ARR
  - 적정 수준: 0.6~0.8 (성장단계 기준)

### Row 3 — ARPA 추이 (분기별)
- **Average ACV** = ACV 총합 ÷ 총 고객 수
  - ACV = [TCV - 일회성 매출] ÷ 총 계약기간(연수)
- **ARPA by MRR** = MRR ÷ 총 유료 고객사 수

### Row 4 — 효율 지표
- **Revenue on FTE** = Revenue ÷ FTE 수
  - FTE 수 = 상품별 인건비 합 ÷ 회사 평균 인건비
  - 포함 비용: 직접인건비 + 인건비성 복리후생비 + 간미총계 + 판매자체(전마) + 판매배부(전마배부, 상품기획/사업관리)
  - 포함 인력: 상품기획/사업관리, 개발, 딜리버리, 운영, 영업(전마)
- **Rule of 40** = % ARR Growth YoY + EBITDA 마진
  - % ARR Growth = (당기ARR - 전기ARR) ÷ 전기ARR × 100
  - EBITDA 마진 = EBITDA ÷ 매출 × 100
  - 적정 수준: 40% 이상

### Row 5 — 수익성 추이 (월별)
- **% Gross Margin** = (매출 - 직접원가 - 간접원가) ÷ 매출 × 100
- **% Operating Margin** = (매출 - 직접원가 - 간접원가 - 판매비 - 일반비) ÷ 매출 × 100

### Row 6 — 목표 대비 실적
- Revenue vs. Plan: 실적 vs Plan 데이터 비교 (데이터 출처 개발팀 확인 필요)
- Operating Profit vs. Plan: 실적 vs Plan 데이터 비교

---

## 기타 주요 지표 산식 요약

| 지표 | 산식 |
|------|------|
| MRR | 반복 정기 라이선스 매출의 합 |
| ARR | MRR × 12 |
| Net New ARR | New ARR + Expansion ARR - Contraction ARR - Churn ARR |
| % ARR Growth | (당기ARR - 전기ARR) ÷ 전기ARR |
| NRR | (전기ARR + 확장ARR - 축소ARR - 이탈ARR) ÷ 전기ARR × 100 |
| ARPA | MRR ÷ 총 유료 고객사 수 |
| LTV | ARPA ÷ 이탈률 (또는 ARPA × GM% ÷ MRR이탈률) |
| CAC | 전 분기 영업/마케팅 비용 ÷ 당 분기 신규 고객 수 |
| CAC Payback | CAC ÷ ARPA (또는 CAC ÷ (ARPA × GM%)) |
| % Customer Churn | 당기 이탈 고객 수 ÷ 전기 고객 수 × 100 |
