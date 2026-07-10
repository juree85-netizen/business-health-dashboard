---
name: feedback_public_repo_data_separation
description: business-health-dashboard(public) 저장소에 개인/재무 데이터가 담긴 스크립트·폴더를 절대 커밋하지 않는다
metadata: 
  node_type: memory
  type: feedback
  originSessionId: eda9367b-03fe-4759-ad42-82e5aeb23359
---

`business-health-dashboard`는 **public** GitHub 저장소다. 사업건전성 대시보드 관련 산출물(와이어프레임, 개발요청서, 지표 문서 등) 외에 **개인적인 내용이나 실제 재무 데이터가 담긴 폴더/스크립트는 절대 이 저장소에 커밋하지 않는다.**

**Why:** 2026-07-10, `realestate_monitor/monitor.py`(부동산 실거래가 모니터링 스크립트, [[호피(시장가격 PM) 에이전트]])가 2026-06-17부터 이 public 저장소에 커밋되어 있었고, 코드 안에 실제 취득가(29.6억)·목표 매물 가격대(35~45억)·아파트 실명이 하드코딩된 채로 3주간 공개 노출됐다. git-filter-repo로 히스토리·태그 전체에서 제거하고 별도 private 저장소(`juree85-netizen/realestate-monitor`)로 분리했다. 다행히 포크·스타·PR·이슈가 0건이라 외부 열람 흔적은 없었지만, 히스토리 재작성(force-push) 과정에서 작업 디렉토리 파일까지 함께 삭제되어 크론이 깨질 뻔한 부수 사고도 있었다.

**How to apply:**
- 새로운 개인용 자동화(부동산 모니터링, 일기 발송 등)를 만들 때는 **처음부터** 별도 private 저장소를 쓰거나, `/home/ubuntu/.gitignore`에 해당 폴더를 등록해서 `git add -A`류 명령에도 안 딸려가게 막는다. ([[feedback_git_snapshot]] 스냅샷 저장 루틴을 실행하기 전에 반드시 확인)
- 커밋 전에 `git status`로 의도치 않은 폴더가 스테이징되지 않았는지 확인하는 습관을 유지한다.
- 현재 `.gitignore`에 등록된 개인/비공개 폴더: `diary/`, `realestate_monitor/`, `selleyo/`, `selleyo-hub/`, `selleyo-app/`, `vera-hub/`.
- git 히스토리 재작성(force-push)이 필요한 경우, 반드시 사전에 ① 다른 clone 존재 여부 확인 ② `.git` 백업 ③ 재작성 후 working tree 파일이 실제로 남아있는지(특히 cron 등 실행 중인 스크립트) 검증까지 세트로 수행한다.
