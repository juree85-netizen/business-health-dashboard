---
name: project_wireframe_docshub_sync
description: html/*.html(nginx 문서허브)과 docs-hub/public/html/*.html(GitHub Pages 배포 소스) 이중 관리 구조 및 자동 동기화 훅
metadata: 
  node_type: memory
  type: project
  originSessionId: 87553c37-f078-4e38-a1b6-27ecfa748aba
---

business-health-dashboard 저장소(`/home/ubuntu`)에는 와이어프레임 파일이 두 곳에 존재한다.

- `html/*.html` — nginx가 8090포트로 직접 서빙하는 문서허브 원본([[reference_docs_hub_url]]). 와이어프레임 작업(챗봇, 툴팁 등)은 보통 이 경로에 먼저 반영됨.
- `docs-hub/public/html/*.html` — Astro 프로젝트(docs-hub)의 public 자산. `.github/workflows/deploy-pages.yml`이 이걸 빌드해서 `https://juree85-netizen.github.io/business-health-dashboard/`로 배포함.

**Why:** 2026-07-16, 사용자가 GitHub Pages 라이브 사이트(growth_wireframe.html)에서 챗봇이 안 보인다고 보고 → 확인 결과 `html/`은 최신(챗봇 반영)인데 `docs-hub/public/html/`은 예전 커밋에 머물러 있었음. 14개 와이어프레임 파일 전부 어긋나 있었고, 수동 복사로 1회 동기화함(커밋 `8980cb6`).

**How to apply:** 재발 방지를 위해 `.githooks/pre-commit` 훅 추가(커밋 `c2fb340`) — `html/*.html` 커밋 시 이미 `docs-hub/public/html/`에 존재하는 동일 파일을 자동 복사/스테이징함. 활성화하려면 `git config core.hooksPath .githooks` 필요(로컬 설정이라 클론마다 1회 실행 필요). AWS 세션(루나)은 이미 설정 완료. [[feedback_workflow_two_sessions]]에 따라 회사 Windows 세션에서도 pull 후 이 설정을 한 번 실행해야 함 — 아직 미확인 상태.
