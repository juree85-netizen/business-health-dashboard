# 작업 히스토리

사업건전성 대시보드 프로젝트 세션별 작업 기록

---

## 2026-05-04 (v2.8.0)

**완료 작업**
- 세션 히스토리 서브에이전트 설계 확정 (방향 B: 세션 시작/종료 시 루나가 서브에이전트 호출)
- 작업 히스토리 관리 파일(`work_history.md`) 신규 생성
- "루나" 호칭 시 문서허브 URL 표 포함 지침 메모리 업데이트

**생성/수정 파일**
- `/home/ubuntu/work_history.md` (신규)
- memory: `user_preferences.md`, `feedback_work_history_agent.md` 업데이트

**Git 태그:** v2.8.0

---

## 2026-05-04 (v2.8.1 ~ v2.9.1)

**완료 작업**

### v2.8.1 — Brity Automation 사업부 대시보드 검증 루프 이슈 수정
- Rule of 40 게이지 바 수정: -2.6% 음수값 → width 0% (오독 방지)
- Revenue 차트 기간 통일: 25.12까지 → 26.03까지 (15개월 확장)
- 이익률 0% 교차 시점 흑자전환 마커 추가 ('25.04)
- 영업이익 YoY 786.3% → "흑자전환 ('25.04)" 텍스트 교체
- NPS 기준연도 표기 수정: "vs. 전년" → "2026년 측정 예정"
- ARR↑ ACV↓ 관계 인사이트 1줄 추가 (ACV 카드 하단)
- 문서허브 HTML 목록에 사업부 대시보드 와이어프레임 등록

### nginx 포트 오류 수정
- 메모리/문서 URL 8080 → 8090으로 전면 수정
- nginx 설정 확인: 8090포트, dist/html/ 서빙 구조 파악

### v2.9.0 — 서비스 활성화 지표 수립 문서 3종 신규 생성
- HTML 정의서: 상품별 지표, 색상 범례 (추론값/확인필요/오타수정 구분)
- Excel 파일: openpyxl 스타일링 (셀 색상, 상품열 병합, 범례 시트)
- 문서허브 HTML 목록 및 엑셀 다운로드 목록 등록
- 오타 수정: Knox Teams "메신지 수신량" → "메시지 수신량"
- 빈 셀 보완: 동일 상품군 패턴 전파 및 지표 유형별 원천 데이터 추론

### v2.9.1 — nginx 404 근본 원인 해결
- 원인: npm run build가 dist/ 초기화 → 수동 복사 파일 삭제 반복
- /html/ alias: dist/html/ → /home/ubuntu/ 직접 서빙으로 변경
- /files/ alias: dist/files/ → /home/ubuntu/files/ 신규 추가
- 빌드와 HTML/파일 서빙 완전 분리 (복사 단계 불필요)
- dist-only 파일(VoC 와이어프레임, upload.html) /home/ubuntu/로 이전

**생성/수정 파일**
- `bizunit_dashboard_wireframe.html` (수정)
- `service_activation_indicators.html` (신규)
- `service_activation_indicators.xlsx` (신규)
- `files/efficiency_profit_dev_request.xlsx`, `files/service_activation_indicators.xlsx`, `files/voc_interface_request.xlsx` (신규)
- `/etc/nginx/sites-enabled/docs-hub` (수정)
- memory: `reference_docs_hub_url.md` 8090 포트로 수정

**Git 태그:** v2.8.1 / v2.9.0 / v2.9.1

---

## 2026-05-04 (세션 시작)

### 세션 시작
- 사용자 호칭: 루나
- 긴급 미완료 작업: 없음

---

## 2026-04-30 (v2.6.0)

**완료 작업**
- Knox Meeting VoC 와이어프레임 수정
  - 헤더 기준월 26년 03월 반영
  - 헤더 상품 필터 Knox Meeting 추가
  - CSAT/NPS/CES (Knox Meeting) 표기 추가
  - VoC 4개 차트 분기(22.4Q~25.1Q) → 37개월 월별(23.03~26.03) 전환

**생성/수정 파일**
- `voc_dashboard_wireframe.html`

**Git 태그:** v2.6.0

---

## 2026-04-29 (v2.5.1)

**완료 작업**
- Knox Drive VoC 와이어프레임 검증루프 수정

**생성/수정 파일**
- `voc_dashboard_kd_wireframe.html`

**Git 태그:** v2.5.1

---

## 2026-04-28 (v2.5.0)

**완료 작업**
- Knox Drive VoC 와이어프레임 신규 제작 (실데이터 29개월 적용)

**생성/수정 파일**
- `voc_dashboard_kd_wireframe.html` (신규)

**Git 태그:** v2.5.0

---

## 2026-04-27 (v2.7.2)

**완료 작업**
- Brity Automation 사업부 대시보드 레이아웃 수정

**생성/수정 파일**
- `bizunit_dashboard_wireframe.html`

**Git 태그:** v2.7.2
