---
name: 문서허브 고정 URL
description: 문서허브(docs-hub) 접속 주소 — 8090 포트, nginx가 /home/ubuntu/docs-hub/dist/html/ 서빙
type: reference
originSessionId: 40b6c213-ce9d-4b28-99f4-8d97f2716d5b
modified: 2026-10-01T06:48:04.958Z
---
문서허브 URL: **http://13.49.177.238:8090**

HTML 파일 서빙 경로: `http://13.49.177.238:8090/html/<파일명>.html`

**구조 (v2.9.1 이후 — nginx alias 직접 서빙):**
- `/html/` → `alias /home/ubuntu/` (HTML 파일 직접 서빙, dist/ 경유 없음)
- `/files/` → `alias /home/ubuntu/files/` (Excel 등 다운로드 파일)
- docs-hub 정적 페이지: `npm run build` → `dist/` (별도 경로)

**⚠ 홈 디렉터리 전체가 인터넷에 서빙됨 (2026-10-01 차단 규칙 추가):** `/html/`·fallback이 `/home/ubuntu` 전체를 가리켜 `.git/config`(토큰), `.claude/` 메모리, private 폴더까지 URL로 열리던 것을 발견. `/etc/nginx/sites-enabled/docs-hub`에 정규식 location 2개로 차단함 — ① `/.`로 시작하는 모든 숨김 경로 ② `vera-hub|personal|diary|realestate_monitor|kidscafe_monitor|selleyo|selleyo-hub|selleyo-app`. 원본 설정 백업: `~/.local/share/nginx-backups/`. 새 private 폴더를 홈에 만들면 이 차단 목록에도 추가할 것([[feedback_public_repo_data_separation]]). 홈 최상위의 일반 파일은 여전히 공개되므로 민감 파일을 홈 최상위에 두지 말 것.

**How to apply:** HTML 파일은 `/home/ubuntu/`에 저장하면 바로 서빙됨. `npm run build` 후 cp 불필요. 사용자에게 URL 안내 시 8090 포트 사용.
