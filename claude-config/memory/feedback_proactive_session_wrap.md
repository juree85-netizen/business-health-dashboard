---
name: feedback-proactive-session-wrap
description: 작업 완료 시 사용자 요청 없이도 메모리·워크히스토리·claude-config를 자동 업데이트해야 함
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 02df4ce3-ab62-400b-9b72-4ad5aad0686b
---

작업이 완료되면 사용자가 요청하기 전에 루나가 먼저 처리해야 할 것들:
1. project_next_task.md — 완료 항목 체크, 신규 미완료 항목 추가
2. work_history.md — 세션 작업 내용 기록 (general-purpose 서브에이전트)
3. claude-config/ 동기화 + GitHub push

**Why:** 사용자가 매번 "메모리 업데이트해줘", "워크히스토리 업데이트해줘"를 요청해야 하는 상황이 반복됨. 이는 루나가 알아서 챙겼어야 할 일.

**How to apply:** 대화에서 의미있는 작업(파일 수정, 보고서 업데이트, 삭제 등)이 완료되는 시점에 세션 마무리 여부를 판단하고, 마무리 흐름이면 자동으로 wrap-up 처리.
