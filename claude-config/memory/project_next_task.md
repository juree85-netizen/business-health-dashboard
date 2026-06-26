---
name: ""
description: 다음 대화 시작 시 루나가 먼저 안내해야 할 미완료 작업
metadata: 
  node_type: memory
  type: project
  originSessionId: current
---

## 다음 세션 우선 안내 항목

**최신 스냅샷**
- 메인(business-health-dashboard): v4.25.1 (2026-06-25)
- 셀레요(selleyo): selleyo-v1.6 + React Native 확정 반영 (2026-06-18)

---

## [우선] Coupa 보고서 FCF 수치 수정 (2026-06-26 세션 미완료)

파일: `/home/ubuntu/files/coupa_investment_report.html`

SEC 10-K 검증 결과 아래 3건 수정 필요:

| 항목 | 현재 보고서 | 수정값 | 기준 |
|------|-----------|--------|------|
| FY2021 FCF | +$108M | **+$113.5M** | Adj.FCF (8-K 공시) |
| FY2021 FCF 마진 | 20% | **20.9%** | Adj.FCF 마진 |
| FY2022 FCF | +$158M | **+$155.6M** | Adj.FCF (8-K 공시) |
| FY2022 FCF 마진 | 22% | **21.5%** | Adj.FCF 마진 |
| FY2023 Q1~Q3 누적 순손실 | -$241.5M | **-$235.9M** | Q3 FY2023 8-K 공시 |

※ 매출·순손실 수치는 모두 정확 (수정 불필요)
※ FCF 정의: 영업CF - 설비투자 + 전환사채 할인상환 + 인수관련 주식보상 일시지급

---

## 셀레요 미완료 작업

1. `status.md` 업데이트 (법률 1/1, 론칭 2/2 완성으로 수정 필요)
2. 셀레요 개발 환경 세팅 (집에서 본인 PC로 진행 예정)
   - git clone → npm install → npx expo start → Expo Go 실기기 확인
3. 자막 추출 방식 결정 (7월 3주 전까지): YouTube Transcript API + Whisper fallback 방향 잡혀있음
