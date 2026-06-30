---
name: feedback-workflow-two-sessions
description: 두 Claude 세션(루나 AWS vs 회사 Windows) 역할 분담 규칙 — 어느 창에서 무슨 작업을 할지
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 88b42291-974d-4b5e-bebc-f3b60b35b69a
---

루나(AWS, juree85)와 회사 Windows Claude는 역할이 다르다. 작업 시작 전 어느 창에서 할지 먼저 판단한다.

**Why:** 회사 PC는 삼성 DLP 정책으로 외부 GitHub push가 차단됨 (HTTP 403, remote 메시지 없음). 읽기(fetch)는 되고 쓰기(push)만 막힘.

**역할 분담:**

| 작업 유형 | 담당 |
|-----------|------|
| 문서허브 HTML 편집·배포 (push 포함) | 루나(AWS)에서 직접 |
| 새 보고서·분석 (공개 자료 기반) | 루나(AWS)에서 직접 |
| DRM/K드라이브 내부 자료 열기·추출 | 회사 Windows Claude |
| 사내 Word(.docx) 생성 | 회사 Windows Claude |
| 사내 자료 → 문서허브 반영 | 회사 PC 추출 → 루나에 텍스트 전달 → 루나가 적용·push |

**How to apply:**
- 문서허브·GitHub 관련 요청이 오면 루나에서 바로 처리 (핸드오프 불필요)
- "회사 PC에서만 열리는 자료"가 출처일 때만 Windows → 루나 핸드오프
- 핸드오프 시: Windows Claude가 교정 내용을 텍스트로 정리 → 루나가 파일에 적용 → 루나가 commit + push
