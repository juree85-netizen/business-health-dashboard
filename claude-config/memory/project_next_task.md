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
- 메인(business-health-dashboard): v4.25.1 (2026-06-25) + 2026-06-30 FCF 수정 커밋
- 셀레요(selleyo): selleyo-v1.6 + React Native 확정 반영 (2026-06-18)

---

## [완료] Coupa 보고서 FCF 수치 수정 (2026-06-30)

- 현행 파일: `/home/ubuntu/coupa_rossum_report_v2_20260623.html` (v2로 일원화)
- 구버전 `files/coupa_investment_report.html` 삭제 완료
- FY2023 Q1~Q3 누적 순손실 -$241.5M → **-$235.9M** 반영 완료
- v2는 Adj.FCF 8-K 정확값($113.5M / $155.6M) 이미 반영 상태
- GitHub push 완료 (커밋 ea557c9, 500bd79)

---

## 셀레요 미완료 작업

1. `status.md` 업데이트 (법률 1/1, 론칭 2/2 완성으로 수정 필요)
2. 셀레요 개발 환경 세팅 (집에서 본인 PC로 진행 예정)
   - git clone → npm install → npx expo start → Expo Go 실기기 확인
3. 자막 추출 방식 결정 (7월 3주 전까지): YouTube Transcript API + Whisper fallback 방향 잡혀있음
