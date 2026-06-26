---
name: 문서허브 고정 URL
description: 문서허브(docs-hub) 접속 주소 — 8090 포트, nginx가 /home/ubuntu/docs-hub/dist/html/ 서빙
type: reference
originSessionId: 40b6c213-ce9d-4b28-99f4-8d97f2716d5b
---
문서허브 URL: **http://13.49.177.238:8090**

HTML 파일 서빙 경로: `http://13.49.177.238:8090/html/<파일명>.html`

**구조 (v2.9.1 이후 — nginx alias 직접 서빙):**
- `/html/` → `alias /home/ubuntu/` (HTML 파일 직접 서빙, dist/ 경유 없음)
- `/files/` → `alias /home/ubuntu/files/` (Excel 등 다운로드 파일)
- docs-hub 정적 페이지: `npm run build` → `dist/` (별도 경로)

**How to apply:** HTML 파일은 `/home/ubuntu/`에 저장하면 바로 서빙됨. `npm run build` 후 cp 불필요. 사용자에게 URL 안내 시 8090 포트 사용.
