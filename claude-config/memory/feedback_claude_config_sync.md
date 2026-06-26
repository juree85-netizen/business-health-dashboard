---
name: feedback_claude_config_sync
description: 메모리·에이전트·커맨드 업데이트 시 claude-config/ 동기화 및 GitHub push 규칙
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c2c6491b-7e54-4982-b4b8-523da2cacecd
---

메모리 파일(`.claude/projects/-home-ubuntu/memory/`)을 저장·수정할 때마다, 또는 에이전트/커맨드 파일이 바뀔 때마다 `claude-config/` 폴더를 동기화하고 GitHub에 push한다.

**Why:** 다른 계정이나 환경으로 이전할 때 git clone 하나로 루나 전체 맥락을 복원할 수 있게 하기 위함.

**How to apply:**
메모리 write/edit 후, 또는 git 스냅샷 커밋 시 아래 명령을 함께 실행:
```bash
cp /home/ubuntu/.claude/projects/-home-ubuntu/memory/*.md /home/ubuntu/claude-config/memory/
cp /home/ubuntu/.claude/agents/*.md /home/ubuntu/claude-config/agents/
cp /home/ubuntu/.claude/commands/*.md /home/ubuntu/claude-config/commands/
git add claude-config/
# 기존 스냅샷 커밋에 포함하거나, 단독 커밋으로 push
```

[[feedback_git_snapshot]]
