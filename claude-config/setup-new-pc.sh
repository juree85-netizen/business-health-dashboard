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

# memory 복사 (OS별 경로 자동 감지)
echo "[3/4] memory 동기화..."
# Claude Code 메모리 경로 = ~/.claude/projects/<escaped-working-dir>/memory/
# Linux/Mac: /home/ubuntu → -home-ubuntu
# Windows(Git Bash): /c/Users/SDS → C--Users-SDS (드라이브 레터 대문자, :와 \ 모두 -)
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" || "$OS" == "Windows_NT" ]]; then
  # Windows: /c/Users/SDS → C--Users-SDS
  DRIVE=$(echo "$HOME" | cut -d'/' -f2 | tr 'a-z' 'A-Z')
  REST=$(echo "$HOME" | cut -d'/' -f3- | sed 's|/|-|g')
  HOME_ESCAPED="${DRIVE}--${REST}"
else
  # Linux/Mac: /home/ubuntu → -home-ubuntu
  HOME_ESCAPED=$(echo "$HOME" | sed 's|/|-|g')
fi
echo "  감지된 메모리 경로 키: ${HOME_ESCAPED}"
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
echo "메모리 저장 위치: $MEMORY_DIR"
echo "claude 명령어로 재시작하면 메모리·에이전트·커맨드가 모두 로드됩니다."
