---
name: reference_skill_file_transfer
description: Windows 사내 PC → AWS 서버로 바이너리 파일(.skill/.zip) 전송 시 겪은 제약 및 임시 해결책 (2026-06-25 기준 미해결 과제 포함)
metadata: 
  node_type: memory
  type: reference
  originSessionId: 4c22513e-4188-4d8a-a88f-6d6051365117
---

## 상황 요약

**날짜**: 2026-06-25  
**목적**: 동료(Jaden)가 이메일로 보낸 `samsung-word-writer-v260625-1030.skill` 파일을 AWS 서버(`13.49.177.238`)의 `/home/ubuntu/.claude/skills/sds-word-writer/`에 설치

`.skill` 파일 = ZIP 파일의 확장자만 바꾼 것 (magic bytes: `PK\x03\x04`)

---

## 시도한 방법과 실패 원인

### ❌ 방법 1: SCP (SSH 직접 전송)
```powershell
scp C:\Users\SDS\.claude\samsung-word-writer-v260625-1030.skill ubuntu@13.49.177.238:/home/ubuntu/
```
- **실패 원인**: 사내 네트워크에서 SSH(port 22) 아웃바운드 차단 → Connection timed out
- **근본 원인**: 사내 방화벽 or AWS Security Group에서 포트 22 차단

### ❌ 방법 2: GitHub 웹 업로드 (branch로 파일 추가)
- GitHub 웹 UI → "Upload files" → `.skill` 파일 드래그
- **실패 원인**: "Something went really wrong, and we can't process that file."
- `.zip`으로 이름 바꿔서 재시도해도 동일 오류
- **근본 원인**: GitHub 웹 업로드가 특정 바이너리 파일 형식 거부

### ❌ 방법 3: GitHub Release 첨부파일
- New Release → Attach file 방식으로 시도
- **실패 원인**: 동일하게 "Something went really wrong" 오류
- **근본 원인**: GitHub Release도 동일한 제한 적용

---

## ✅ 임시 해결책: PowerShell base64 인코딩 → 채팅 붙여넣기

### 흐름
1. **Windows PowerShell**에서 base64 인코딩 후 클립보드 복사
   ```powershell
   [Convert]::ToBase64String([IO.File]::ReadAllBytes("C:\Users\SDS\.claude\samsung-word-writer-v260625-1030.skill")) | Set-Clipboard
   ```
   - 실행 후 아무 출력 없음 = 정상 (클립보드에 복사된 것)

2. **Claude Code 채팅창**에 붙여넣기 (Ctrl+V)
   - 249,280자의 base64 문자열 전송됨

3. **서버에서** 세션 JSONL 파일에서 base64 추출 → 디코딩 → 설치
   ```python
   # /home/ubuntu/.claude/projects/-home-ubuntu/<session-id>.jsonl 파일에서 추출
   import json, re, base64, zipfile
   # ... 정규식으로 'UEsDB' 시작 문자열 찾아 디코딩
   ```

4. 설치 결과: 17개 파일 정상 설치

### 한계점
- 파일이 크면 채팅창 붙여넣기 자체가 느리거나 실패할 수 있음
- base64는 원본보다 ~33% 크기 증가 → 큰 파일은 부담
- 매번 수동 작업 필요 (자동화 불가)

---

## 미해결 과제 — 나중에 찾을 해결책

### 근본 원인 1: SSH 포트 차단
- 확인 필요: AWS Security Group inbound/outbound 규칙
- 확인 필요: 사내 방화벽 정책 (IT 보안팀 문의)
- **대안 검토**:
  - HTTPS 포트(443) 기반 파일 업로드 엔드포인트를 서버에 구축 (Flask/FastAPI 간단 API)
  - AWS S3 presigned URL 경유 업로드 → 서버에서 S3 다운로드
  - AWS SSM Session Manager (포트 없이 AWS 콘솔 통해 접속)
  - SFTP/SCP over HTTPS (AWS Transfer Family)

### 근본 원인 2: GitHub 바이너리 업로드 거부
- `.skill`/`.zip` 파일 직접 업로드 불가 (GitHub 웹 UI 제한)
- **대안 검토**:
  - GitHub CLI(`gh`)를 Windows에 설치하면 Release 첨부 가능할 수 있음
  - base64 텍스트 파일로 GitHub에 올린 뒤 서버에서 디코딩

### 우선순위 높은 해결책
1. **서버에 간단한 파일 업로드 HTTP 엔드포인트 구축** — nginx 뒤에 Python FastAPI로 `/upload` 경로 추가, 인증 토큰 방식. HTTPS 443 포트 사용 가능하다면 사내에서도 접근 가능.
2. **AWS SSM 확인** — EC2 인스턴스에 SSM Agent 설치되어 있으면 AWS 콘솔에서 포트 없이 파일 전송 가능.
