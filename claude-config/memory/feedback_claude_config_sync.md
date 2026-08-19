---
name: feedback_claude_config_sync
description: 메모리·에이전트·커맨드 업데이트 시 claude-config/ 동기화 및 GitHub push 규칙
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c2c6491b-7e54-4982-b4b8-523da2cacecd
  modified: 2026-08-19T06:38:16.886Z
---

메모리 파일(`.claude/projects/-home-ubuntu/memory/`)을 저장·수정할 때마다, 또는 에이전트/커맨드 파일이 바뀔 때마다 `claude-config/` 폴더를 동기화하고 GitHub에 push한다.

**단, `claude-config/`는 `business-health-dashboard`라는 PUBLIC 저장소에 push된다.** 개인 인사/커리어/사내 갈등 관련 메모리(예: [[project_esg_transfer]])는 이 블랭킷 cp에서 반드시 제외하고, 대신 private repo인 `vera-hub/memory/`로 보낼 것. 제외 대상은 `/home/ubuntu/.gitignore`에 `claude-config/memory/project_esg_transfer.md`로 등록해 안전장치를 걸어두었음.

**Why:** 다른 계정이나 환경으로 이전할 때 git clone 하나로 루나 전체 맥락을 복원할 수 있게 하기 위함. 단 2026-08-19, `project_esg_transfer.md`(그룹장과의 부서이동 협상, 동료 실명 포함)가 이 블랭킷 cp 습관 때문에 public 저장소에 2커밋 걸쳐 노출되는 사고 발생 → git-filter-repo로 히스토리 전체에서 제거 + force-push, 내용은 vera-hub(private)로 이관 완료. [[feedback_public_repo_data_separation]]과 동일 계열 사고.

**How to apply:**
메모리 write/edit 후, 또는 git 스냅샷 커밋 시 아래 명령을 함께 실행:
```bash
cp /home/ubuntu/.claude/projects/-home-ubuntu/memory/*.md /home/ubuntu/claude-config/memory/
rm -f /home/ubuntu/claude-config/memory/project_esg_transfer.md   # public repo 제외 대상
cp /home/ubuntu/.claude/agents/*.md /home/ubuntu/claude-config/agents/
cp /home/ubuntu/.claude/commands/*.md /home/ubuntu/claude-config/commands/
git add claude-config/
# 기존 스냅샷 커밋에 포함하거나, 단독 커밋으로 push
```
새로운 개인 인사/커리어 관련 메모리를 만들 때는 **처음부터** 이 블랭킷 cp 대상에서 빼는 것을 우선 고려하고, 위 목록(project_esg_transfer.md)에 추가할지 판단할 것.

[[feedback_git_snapshot]]
