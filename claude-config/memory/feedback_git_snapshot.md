---
name: 문서 저장 및 스냅샷 정책
description: 업데이트 시 docs-hub 빌드+깃헙 저장 기본, 스냅샷/태그는 별도 요청 시만
type: feedback
originSessionId: 2ee254d0-6942-470c-9dd0-3e6468e8aabf
---
문서 업데이트 시마다 반드시 두 가지를 함께 실행:
1. docs-hub 재빌드 (`npm run collect && npm run build`, `/home/ubuntu/docs-hub` 기준)
2. GitHub 두 repo 모두 push — `business-health-dashboard` (master) + `biz-healthcheck-docs-hub` (main)

**Why:** 문서허브와 소스 repo가 항상 동기화되어야 함. 사용자가 매 업데이트마다 기본으로 요청함.

**스냅샷(git tag) + 버전관리**는 사용자가 명시적으로 요청할 때만 수행.
기준: 외부 전달 가능 수준으로 완성됐을 때, 또는 핵심 내용(산식·범위 등) 확정 시점.

**링크 검증:** 빌드 후 반드시 주요 HTML 링크를 `curl -o /dev/null -w "%{http_code}"` 로 확인 (8080/8090 포트 모두). 200이 아닌 응답이 있으면 스냅샷 전에 수정.

**How to apply:** 모든 문서 수정 후 docs-hub 빌드 → 링크 검증(curl) → 두 repo push 순서로 실행. 태그는 "스냅샷", "버전 저장" 등 명시적 요청 시만.
