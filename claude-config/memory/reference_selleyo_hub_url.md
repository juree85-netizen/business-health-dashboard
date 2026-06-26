---
name: selleyo-url
description: "셀레요 앱 기획 문서허브 위치 — 8092 포트, 별도 private 레포(github.com/juree85-netizen/selleyo)"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 64af459e-c4eb-44a5-ac4f-06b56714b139
---

문서허브 URL: **http://13.49.177.238:8092**

- 소스 경로: `/home/ubuntu/selleyo-hub/` (Astro Starlight 기반 정적 사이트)
- 빌드: `npm run build` → `dist/` → nginx가 `dist/`를 8092로 서빙 (8090 메인 문서허브는 `/home/ubuntu/` 직접 alias 서빙이라 방식이 다름, [[reference_docs_hub_url]] 참고)
- 콘텐츠 경로: `src/content/docs/` 하위 (예: `screens/wireframe.md`, `biz/budget.md`, `biz/team.md`, `status.md`)
- git: 메인(business-health-dashboard) 레포와 완전히 별도인 `github.com/juree85-netizen/selleyo` private 레포. 메인 레포 `.gitignore`에 `selleyo-hub/` 등록되어 추적 제외됨
- `/home/ubuntu/selleyo/` (구 경로, selleyo_plan.md만 보관)는 더 이상 활성 작업 위치 아님 — 현재는 selleyo-hub가 메인 작업 공간

**How to apply:** "셀피" 호출 시 산출물은 `selleyo-hub/src/content/docs/`에 작성 → `npm run build`로 정상 렌더링 확인 → git commit/tag(`selleyo-vX.Y`)/push. `.md` 파일에 Starlight `<Card>` 등 `.mdx` 전용 컴포넌트를 쓰면 렌더링이 깨지므로 순수 마크다운만 사용할 것 (2026-06-16 실제 발생한 버그).
</content>
