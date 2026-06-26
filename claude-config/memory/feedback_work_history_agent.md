---
name: 작업 히스토리 서브에이전트 운영 규칙
description: 세션 시작/종료 시 작업 히스토리를 서브에이전트로 관리하는 방식과 저장 위치
type: feedback
originSessionId: aeebd23d-2e49-4db8-a017-cec6df63ddd8
---
세션 히스토리는 **서브에이전트(general-purpose) 위임 방식(B)**으로 관리한다.

- **저장 위치:** `/home/ubuntu/work_history.md`
- **세션 시작 시:** 최근 3건 요약을 현황 브리핑 표에 포함
- **세션 종료(마무리 요청) 시:** 루나가 Agent 도구로 서브에이전트를 호출해 해당 세션 항목(날짜, 완료 작업, 생성/수정 파일, git 태그)을 `work_history.md` 상단에 추가 기록
- **git 스냅샷 시:** `work_history.md`도 함께 커밋 대상에 포함

**Why:** 세션마다 무엇을 했는지 명시적으로 추적하고 싶어함. 자동보다 세션 단위 명시 관리를 선호.

**How to apply:** 마무리 요청("마무리해줘", "오늘 여기까지", "스냅샷" 등) 감지 시 서브에이전트 호출 후 work_history.md 업데이트 → git 커밋/태그/푸시 순서로 실행.
