---
name: reference_sds_gitlab_biz_health
description: 사내 GitLab 와이어프레임 미러링 대상 경로 및 AWS 세션 접근 불가 확인
metadata: 
  node_type: memory
  type: reference
  originSessionId: b569314b-3d9d-421d-bcf9-ccd126a58222
---

사내 GitLab 저장소: https://code.sdsdev.co.kr/Solution-Strategy-Group/biz-health-legacy/tree/main/wireframe

사용자가 GitHub(juree85-netizen/business-health-dashboard)의 와이어프레임 산출물을 이 경로(`wireframe/` 하위)로 복사하고 싶어함.

**Why:** AWS 세션(루나)에서 `code.sdsdev.co.kr`로 curl 접속 시도 결과 연결 자체가 실패함(사내망 전용 도메인으로 추정). 해당 호스트용 SSH/토큰 인증정보도 이 세션에 설정되어 있지 않음.

**How to apply:** 이 저장소로의 push/미러링 작업은 AWS 세션에서 직접 수행 불가 — [[feedback_workflow_two_sessions]] 규칙대로 회사 Windows 세션에서 처리하거나, 루나가 파일 묶음(zip 등)을 준비해 핸드오프해야 함. GitLab wireframe 폴더에 기존 파일이 있는지, 전체교체/병합 여부는 매번 확인 필요.
