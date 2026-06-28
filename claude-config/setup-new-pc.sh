#!/bin/bash
# Claude Code 설정 동기화 스크립트
# 새 PC에서 최초 1회 실행하거나, 업데이트 시 실행

REPO_DIR="$(cd "$(dirname "$0")" && pwd)"
CLAUDE_DIR="$HOME/.claude"

echo "=== Claude Config Sync ==="
echo "소스: $REPO_DIR"
echo "대상: $CLAUDE_DIR"
echo ""

# 디렉토리 생성
mkdir -p "$CLAUDE_DIR/agents"
mkdir -p "$CLAUDE_DIR/commands"

# agents 복사
echo "[1/4] agents 동기화..."
cp -rv "$REPO_DIR/agents/"* "$CLAUDE_DIR/agents/"

# commands 복사
echo "[2/4] commands 동기화..."
cp -rv "$REPO_DIR/commands/"* "$CLAUDE_DIR/commands/"

# memory 복사 (프로젝트 경로 자동 감지)
echo "[3/4] memory 동기화..."
# Claude Code는 홈 디렉토리 기준으로 프로젝트 경로를 생성
# 예: /home/ubuntu → ~/.claude/projects/-home-ubuntu/memory/
HOME_ESCAPED=$(echo "$HOME" | sed 's|/|-|g')
MEMORY_DIR="$CLAUDE_DIR/projects/${HOME_ESCAPED}/memory"
mkdir -p "$MEMORY_DIR"
cp -rv "$REPO_DIR/memory/"* "$MEMORY_DIR/"

# settings.json 복사 (기존 파일 백업 후 덮어쓰기)
echo "[4/4] settings.json 동기화..."
if [ -f "$CLAUDE_DIR/settings.json" ]; then
  cp "$CLAUDE_DIR/settings.json" "$CLAUDE_DIR/settings.json.bak"
  echo "  기존 settings.json → settings.json.bak 백업 완료"
fi
cp "$REPO_DIR/settings.json" "$CLAUDE_DIR/settings.json"

echo ""
echo "=== 완료 ==="
echo "claude 명령어로 재시작하면 메모리·에이전트·커맨드가 모두 로드됩니다."
