---
name: 효율/수익 지표 정의 및 화면설계 (확정본)
description: Finance(Efficiency/Profit) 지표 - LTV/CAC/ARPA 산식 확정, 상품별 산출 가능 여부, 화면 설계 스펙, 와이어프레임 파일 위치
type: project
originSessionId: 555e405c-a337-4618-bd32-2cd8e2758734
---
# 효율/수익 지표 주요 결정 사항 (2026-04-17 기준)

## 핵심 산식 확정

- **ARPA** = `sum(vf219) ÷ 고객 수` (해당 연도 vf219 ≠ 0인 고객 수 기준)
  - R(Revenue) = **Recurring Revenue (라이선스/기술지원 + 운영)** 기준
  - RC/NRC 데이터 분리 불가 → 실무상 vf219(매출총계) 전체를 Recurring으로 간주하여 사용
- **LTV** = `ARPA ÷ 이탈률`
  - 이탈률 = `(1 - (N-1년 sum(vf219) ÷ N-2년 sum(vf219))) × 100` ※ N-1년 ≥ N-2년이면 0
  - 이탈률 = 0이면 LTV / LTV/CAC / CAC Payback 모두 빈칸
- **CAC** = `N-2년 sum(vf599) ÷ N-1년 신규 고객 수`
  - 신규 고객 = `(N-2년 vf219 = 0) & (N-1년 vf219 ≠ 0)`
- **LTV/CAC** = `LTV ÷ CAC`
- **CAC Payback** = `(CAC ÷ ARPA) × 12` (단위: **개월**)

## 상품 분류

- **✅ 전체 산출 가능 (11개)**: ZTM, Nexprime SCM, Nexprime SCM Mobile, Nexprime SCM (All), Nexprime HCM, Knox Portal, Knox Meeting, Knox EFSS/Drive, Knox (All), EMM Cloud, Brity Automation
- **❌ LTV/LTV:CAC/CAC Payback N/A**: EMS, EMS (All) — Recurring 비중 약 9%, 데이터 분리 불가 (CAC만 산출)

## 데이터 소스

- 데이터 인터페이스 별도 개발 불필요 — **orderlist로 이미 수신 중**
- 매출 컬럼: vf219 (매출총계), 영업비용 컬럼: vf599 (판매비총계)

## 화면 설계 스펙 (6개 Row, 12개 카드)

| Row | 카드 (좌) | 카드 (우) |
|-----|----------|----------|
| 1 | Gross Sales Efficiency (바 차트, %) | Net Sales Efficiency (바 차트, %) |
| 2 | CAC/LTV/LTV:CAC Ratio (콤비네이션) | CAC Payback Period (라인, 개월) |
| 3 | ARPA by ACV (다중 라인) | ARPA by MRR (다중 라인) |
| 4 | Revenue on FTE (라인, 반기) | Rule of 40 (3중 라인) |
| 5 | Revenue & Profit (KPI + 콤비네이션, 대형) | % Gross Margin & OP (KPI + 라인, 대형) |
| 6 | Revenue vs. Plan (KPI + 트리플바, 대형) | Operating Profit vs. Plan (KPI + 트리플바, 대형) |

- 색상: 라이트블루 #90CAF9 / 다크블루 #1E88E5 / 오렌지 #FF9800 / 퍼플 #7E57C2 / 그레이 #9E9E9E
- 사이드바: 딥 네이비 #1E2A3A~#2C3E50 / 현재 페이지 하이라이트: #17B9A6

## 파일 위치

- 지표 정의서 + 화면 설계 스펙: `/home/ubuntu/efficiency_profit_indicators.md`
- 와이어프레임 HTML: `/home/ubuntu/efficiency_profit_wireframe.html`
- 접속 주소 (HTTP 서버 실행 중): `http://13.49.177.238:8080/efficiency_profit_wireframe.html`

## 남은 작업

- [ ] 개발 가이드 섹션 추가 (집계 로직, 배치 처리 방법)
- [ ] VoC 쪽 작업 이어서 진행
