---
name: url
description: "베라허브(vera-hub, Astro 프로젝트) 접속 주소 — 8091 포트, 저장소는 private 유지"
metadata: 
  node_type: memory
  type: reference
  originSessionId: c608bdf1-eac4-4649-a027-2374cb6ba0a3
  modified: 2026-07-24T01:34:29.717Z
---

베라허브 URL: **http://13.49.177.238:8091**

- nginx 8091 포트가 `/home/ubuntu/vera-hub/dist`를 root로 직접 서빙 (docs-hub 8090, selleyo-hub 8092와 동일 패턴 — [[reference_docs_hub_url]])
- GitHub 저장소(github.com/juree85-netizen/vera-hub)는 **private 유지**. GitHub Pages는 private 저장소에서 무료로 못 쓰므로, 빌드 결과물(dist/)만 EC2에 배포하는 방식으로 대체함 (2026-07-24 결정)
- 소스 수정 후 배포 반영하려면 vera-hub 디렉토리에서 `npm run build` 실행 → dist/ 갱신됨 (nginx 재시작 불필요, 정적 파일 서빙이라 즉시 반영)

**How to apply:** 베라허브 관련 작업 시 URL 안내는 8091 포트 사용. private 저장소 그대로 두고 페이지만 보여주고 싶다는 요청이 다시 나오면 이 패턴(EC2 dist 배포) 재사용.
