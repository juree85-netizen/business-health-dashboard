# 작업 히스토리

사업건전성 대시보드 프로젝트 세션별 작업 기록

---

## 2026-06-24

**완료 작업**

### 재무 지표 해설 보고서 (`financial_metrics_guide_20260624.html`) 보강

#### §4-2 심화 추가 (p.5B~5C) — SaaS PE 인수 기업 B/S 항목 개념 해설
- 유동자산·비유동자산·유동부채·비유동부채·자본 항목별 개념 설명 (숫자 없이 항목만)
- PE 인수 직후 B/S 변화 포인트 (무형자산 급증, 부채 급증, 자본 변동) 설명 박스 추가

#### §4-4 재무제표 연결 고리 — 텍스트 → 3박스 시각 다이어그램 교체
- I/S 박스(①) + B/S 박스(②) + C/F 박스(③) CSS Grid 구조
- ①②③ 번호 화살표로 세 재무제표 연결 포인트 시각화

---

### 기업가치 평가·M&A 인수가액·PPA 해설 보고서 신규 생성 (`ma_valuation_guide_20260624.html`)

#### 7페이지 구성
- p1: 목차 + 핵심 개념 요약표 (7개 개념)
- p2: §1-1 오해 vs 실제 다이어그램 + 인과관계 방향 표, §1-2 EV트리 + 멀티플 비교표, §1-3 혼동 구조 개념 쌍
- p3: §2-1 DCF 3단계 다이어그램 + 한계
- p4: §2-3 LBO 모델 (인수구조→차입상환→Exit IRR) + §2-4 Strategic Premium
- p5: §3-1 PPA + §3-2 배분 다이어그램 (순자산①→무형자산②→Goodwill③)
- p6: §3-3 PPA 재무영향 + §3-4 Successor/Predecessor 비교표
- p7: §4-1 전체 흐름 3단계 + §4-2 사업부장 보고용 핵심 박스 + §4-3 집 살 때 비유

#### concept-map 내용 통합 (인수가액 vs 멀티플 인과관계)
- 인과관계 방향 표, EV트리, 혼동 구조 개념 쌍 §1에 통합

#### 사후 판단 편향(Hindsight Bias) 행간 보완 4건
- 당시 정보 기준 평가 원칙, PE Exit IRR 기준 명시 등 — 티나지 않게 삽입

---

### docs-hub 사이드바 등록
- `astro.config.mjs` — '기업 분석 보고서' 섹션에 재무 지표 해설 + 기업가치 평가 2개 항목 추가
- `src/content/docs/project/ma-valuation-guide.md` 신규 생성

---

### Coupa 재무 현황 SEC 검증 (분석, 파일 변경 없음)

#### 순이익 (GAAP) SEC 10-K 확인값 vs 사용자 제공 수치 비교
- FY2021 (Jan '21): SEC 확인 −$180.1M ↔ 기존 표 −$130M (과소 $50M)
- FY2022 (Jan '22): SEC 확인 −$379.0M ↔ 기존 표 −$235M (과소 $144M)
- FY2023 (Jan '23): 10-K 미제출 (TB 인수로 상장폐지), Q1~Q3 −$241.5M 확인

#### D&A SEC 10-K 확인값
- FY2021: $72.1M / FY2022: $146.4M (확정) / FY2023: 미공시 (추정 ~$175M)

#### GAAP EBITDA 역산 표 완성
- '20년: ~−$55M / '21년: ~−$165M / '22년: ~−$100~120M (추정)
- Adj. EBITDA와 GAAP EBITDA 이중 열 구조로 표 제시
- FCF가 GAAP EBITDA 대비 플러스인 이유: SBC 비현금 가산 효과 설명

#### '20~'22년 항목별 신뢰도 분류
- [SEC✓] / [부분] / [추정] / [미확인] 4단계 레이블로 항목별 확인 수준 명시

**생성/수정 파일**
- `financial_metrics_guide_20260624.html` (§4-2·§4-4 보강)
- `ma_valuation_guide_20260624.html` (신규 7페이지)
- `docs-hub/astro.config.mjs` (사이드바 2개 항목 추가)
- `docs-hub/src/content/docs/project/ma-valuation-guide.md` (신규)

**Git 커밋:** 9a1641d / 5867dc5 / 549d17e / f8f249d / 6e5049f

**상태:** 완료

---

## 2026-06-17

**완료 작업**

### 호피 (부동산 실거래가 모니터링)

#### 메일 템플릿 개편 — 정반합 분석 기반
- 요약 한줄 박스 추가 (관심 매물 N건 | 최저가 | 격차 축소 매물)
- 주목 매물 Top 5 표 (6컬럼, 트리지움 대비 차이 오름차순)
- 전체 N건 보기 링크 버튼 추가
- 컬럼 11개 → 6개로 축소, 세대수·연식 제거

#### GitHub Pages 연동 (https://juree85-netizen.github.io/realestate-report/)
- `juree85-netizen/realestate-report` public 레포 생성
- `monitor.py`에 전체 리포트 HTML 생성 + gh-pages 자동 push 로직 추가
- 전체 리포트: 전건 표시, 모바일 반응형, 9컬럼

---

### 셀피 (셀레요 PM)

#### 의사결정 3건 확정
- 이미지 생성: AI 일러스트 단독 (DALL-E, 프레임 캡처 Phase 2 보류)
- Phase2 마케팅 예산: 최소~중간 (150~280만원) 확정
- 충원 방식: 외주 없음, 본인+남편 2인 공동창업자 운영 체제

#### 미작성 문서 3건 완성 → 셀레요 문서 21/21 완성
- `/legal/copyright.md` — YouTube API 저작권 정책
- `/launch/beta.md` — 베타 테스트 계획 (50명, 6~7주)
- `/launch/strategy.md` — 론칭 전략 (유튜브 쇼츠 중심, Phase 3단계)

#### 셀레요 문서허브 GitHub Pages 연동
- `juree85-netizen/selleyo-docs` public 레포 생성
- AWS/GitHub Pages 빌드 분리 (dist/ vs dist-ghpages/, base path 분기)
- git post-commit hook으로 완전 자동화 (커밋 시 양쪽 자동 배포)
- URL: https://juree85-netizen.github.io/selleyo-docs/

**상태:** 완료

---

## 2026-06-16

**완료 작업**

### FabriX AI 활용 가능성 문의 대응
- 솔루션사업부 기획팀이 FabriX(사내 AI) 활용 가능성을 AI Development Group(하혜란 매니저)에 문의했고, 답변 메일 수신
- 답변 요지: #1,2(대시보드 재구축/데이터모델 개선)는 'AI Pro' 권장, #3,4(Agent 제작)는 FabriX MCP 호스팅+Agent 도구 또는 LLM OpenAPI 활용 가능, 상세 협의는 공식 채널(fabrix.cs@samsung.com) 안내
- fabrix.cs@samsung.com 앞 상세 협의 요청 메일 초안 작성 지원 (하혜란 답변 메일 전달 방식 + 새 본문 추가, CC: 하혜란+기존 내부 참조자 전체)
- 상태: 메일 발송은 사용자가 직접 진행 예정

### 셀레요(Selleyo) 프로젝트 — 화면설계·사업 섹션 완성 (13/21 → 16/21)
- "셀피" 호출 → 현황 브리핑 (13/21, selleyo-hub 8092포트, 별도 private 레포 github.com/juree85-netizen/selleyo)
- 다음 작업 우선순위 추천: 와이어프레임 → 사업(예산·팀구성) → 법률(저작권) → 론칭(베타·전략) 순서 제안 및 승인
- **v1.5**: 핵심 화면 4종(홈/레시피저장/요리준비/레시피북) 와이어프레임 작성 완료 — 화면설계 섹션 5/5 완성. 저작권 옵션 A(영상캡처)/B(AI일러스트) 미확정 상태를 토글 형태로 양립 처리. (commit 05ec97f, tag selleyo-v1.5)
  - 생성: `public/selleyo_wireframe.html`
  - 수정: `src/content/docs/screens/wireframe.md`, `src/content/docs/status.md`
- **v1.5.1**: wireframe.md 내 Starlight `<Card>` 컴포넌트가 .md 파일에서 렌더링되지 않는 버그 발견 및 수정 (.mdx 전용 컴포넌트 사용 실수 → 순수 마크다운 링크로 교체). (commit ee37075, tag selleyo-v1.5.1)
- **v1.6**: 예산 계획·팀 구성 문서 작성 완료 — 사업 섹션 4/4 완성 (전체 16/21). 1인 개발 체제를 기존 schedule.md 근거로 확정, Phase 1(~100만원)/Phase2(380~510만원)/Phase3(분기 150~250만원) 예산 가정안 제시. (commit c20660e, tag selleyo-v1.6)
  - 수정: `src/content/docs/biz/budget.md`, `src/content/docs/biz/team.md`, `src/content/docs/status.md`
- **사용자 확인 대기 중 (3건)**: ① 이미지 생성 옵션 기본값(A/B 동시 vs B단독, B단독 추천) ② Phase2 마케팅 예산 규모(최소~중간 추천) ③ Phase2~3 충원 방식(1인+부분외주 추천) — 다음 세션에서 답변 받아 반영 필요
- 남은 미작성: 법률·정책(저작권 정책) 1개, 론칭(베타테스트, 론칭전략) 2개 → 5/21 남음

**상태:** 완료 (다음 세션: 사용자 확인 3건 반영 후 법률·론칭 섹션 진행)

---

## 2026-06-12

**완료 작업**

### 셀레요 허브 (selleyo-hub, 8092) 문서 작성

#### selleyo-v1.2 — KPI / 성공 지표 문서 작성
- North Star Metric: 월간 요리 완료 세션 수 정의
- AARRR 프레임워크 기반 지표 체계 구성
- Phase 1~3 단계별 목표 수립
- Firebase 이벤트 7종 정의

#### selleyo-v1.3 — 개발 일정 문서 작성
- 2026.07~2027.06 전체 타임라인 수립
- Phase 1 주차별 세부 작업 계획
- 앱스토어 출시 목표: 2026.11

**진행현황:** 13/21 완성 (기획 4/4 완성, 사용자·시장 3/3 완성)

---

### 에이전트 체계 정비

- **대피 에이전트 신규 생성** — 사업건전성 대시보드 전담 PM, 지표산식/DB/회의체/현안 컨텍스트 내장
- **셀피 에이전트 이름 변경** — 기존 "셀레요 PM" → "셀피"
- **에이전트 구조 확정**
  - 루나(메인) → 대피 / 셀피 (프로젝트 PM)
  - 루나(메인) → 베라 / 와이어프레임디자이너 / 개발요청서리뷰어 (도메인 전문가)

**상태:** 완료

---

## 2026-06-01 (세션 종료)

**완료 작업**

### 루나 호출 → 현황 브리핑 (v4.10.0 기준)
- 루나 호칭으로 세션 시작, 메모리·산출물·Git 스냅샷 현황 브리핑 진행
- v4.10.0 기준 전체 프로젝트 상태 확인

### 프로젝트별 PM 에이전트 구상 논의 시작
- 프로젝트별 PM 에이전트 도입 방향 초기 논의
- 구체적인 설계는 다음 세션에서 진행 예정

**상태:** 완료 (다음 세션에서 PM 에이전트 설계 논의 예정)

---

## 2026-06-01 (v4.8.9 ~ v4.10.0)

**완료 작업**

### v4.8.9 — 5장 시사점 재구성 + 1-4장 팩트 검증
- 1-4장 전체 팩트 웹서치 검증 (17개 팩트 확인, 1개 수정: 276개 언어/손글씨 30개 언어 구분)
- 5장 '인수 후보 리스트' 2페이지 → '시사점 및 전략적 함의' 1페이지로 교체
- 표지 요약문·목차 동시 수정

### v4.9.0 — 용어 주석 (항상 보이는 파란 소형 글씨) 추가
- 약어·생소 용어 17개에 9.5px 파란 인라인 주석 추가 (첫 등장 위치 기준)
- ARR·GAAP·tuck-in·T-LLM·DOCile·Human-in-the-Loop·Forrester·Strong Performer·Series A·General Catalyst·PE·LBO·PIK·EV/Revenue·FCF·Rule of 40·NRR

### v4.9.1 — 인용문 국문화 + 별첨 1·2 추가
- 3장 Leagh Turner 인용문 국문 번역 (원문 소형 영문 병기)
- 1장·2장 헤딩에 '→ 별첨 1/2 참조' 표기
- 별첨 1: Coupa 상세 기업 개요 (기본정보·제품군·재무성과·M&A이력·경쟁사)
- 별첨 2: Rossum 상세 기업 개요 (기본정보·창업스토리·T-LLM 기술표·성과·자금조달·경쟁사)

### v4.9.2 — 참고자료 맨 뒤로 이동
- 페이지 순서: 본문(1~6) → 별첨 1 → 별첨 2 → 참고자료

### 개념설명 지형도 프롬프트 신규 작성
- 재사용 가능한 8항목 AI 설명 요청 프롬프트 (MECE + 층위 구조 포함)
- MD 파일: files/개념설명_지형도_프롬프트.md
- HTML 파일: files/개념설명_지형도_프롬프트.html
- docs-hub 가이드 등록: /guides/concept-map-prompt/
- Claude Code 스킬 생성: /concept-map (글로벌 스킬)

### v4.10.0 — 1장 M&A 시장 생태계 개요 추가 (Option A)
- 기존 1~5장 → 2~6장으로 번호 일괄 변경
- 1장 신규: M&A 시장 생태계 개요 (페이지 2)
  · 기업 외부 역량 취득 4가지 MECE 비교표
  · M&A 거래 유형별 지형도 (PE LBO·tuck-in·수평·수직)
  · 주요 참여자 구조 + 분석 범위 핵심 관찰 박스
- 문서허브 사이드바에 'Coupa·Rossum M&A 분석' 섹션 신규 등록

**생성/수정 파일**
- `coupa_rossum_report.html` (v4.8.9 ~ v4.10.0)
- `files/개념설명_지형도_프롬프트.md`
- `files/개념설명_지형도_프롬프트.html`
- `docs-hub/src/content/docs/guides/concept-map-prompt.md`
- `docs-hub/astro.config.mjs`
- `~/.claude/skills/concept-map/SKILL.md`

**Git 태그:** v4.8.9 (최신 커밋: 3a9bb67)

---

## 2026-06-01 (v4.8.9)

**완료 작업**

### v4.8.9 — 5장 시사점 재구성 + 1-4장 팩트 검증

1. **1-4장 전체 팩트 검증 (웹서치 기반)**
   - 1장: Coupa ARR $1B, 수익 $1.21B, GAAP 흑자, Cirtuo/Scoutbee/Tonkean 인수 상세 → 전부 확인
   - 2장: Gogár Forbes 30 Under 30('18), T-LLM 1,100만 건·92.5% 정확도, Aurora 1.5(2024.10.29) 25% 향상 → 확인
   - 2장 수정: "276개 언어 지원, 손글씨 처리 가능" → "276개 언어 지원 (손글씨는 30개 언어)"
   - 3장: 2024년 파트너십, Kirkland&Ellis(Coupa)/Orrick(Rossum)/Guggenheim(매각자문) → 확인
   - 4장: Medallia $6.4B(2021.07), PIK LBO 구조, 채권단 경영권 이전 진행 → 확인

2. **5장 '인수 후보 리스트' → '시사점 및 전략적 함의'로 전면 교체**
   - 2페이지(인수 프레임워크 + 후보 4개사) → 1페이지(시사점)로 압축
   - 구성: ①파트너십 선행-내재화 모델 유효성, ②PE LBO vs tuck-in 구조 차이, ③AI 대체 가능성 기준 부상, ④당사 함의(파트너 재검토/설계적 M&A/AI 내성 적용/후속 모니터링)
   - 표지 요약문·목차 항목 동시 수정

**생성/수정 파일**
- `coupa_rossum_report.html` (v4.8.9)

**Git 태그:** v4.8.9

---

## 2026-05-27 (v4.7.57)

**완료 작업**

### v4.7.57 — AI 리서치 워크플로우 슬라이드 전면 개선 (15→18장)

1. **경고 문구 삭제** — 배경·목적·제목 관련 빨간 박스 제거
2. **Step 02 슬라이드 Medallia 예시 링크 3개 박스 추가** — OnlyCFO, Bloomberg, Thoma Bravo
3. **전체 tip 박스 레이블 태그 구분 추가** — 🤖 AI 지시 (`tip-lbl-ai`) / ✍️ 공동저자 (`tip-lbl-human`) CSS 클래스
4. **GPT 리뷰 기반 슬라이드 전면 개선 (15→18장)**
   - 신규 슬라이드 3개: 보안 입력 기준(06/18), 좋은/나쁜 프롬프트 비교(13/18), AI 결과물 검증 5단계(16/18)
   - 전체 Workflow 슬라이드에 핵심 메시지 1문장 배너 추가
   - 소요 시간 문구 강화 (검증 책임 명시)
   - Medallia 사례에 신뢰도 분류 표 추가 (확정 사실/보도 기반/추정/해석)
   - 페이지 번호 전체 업데이트, 네비게이션 도트 확장

**생성/수정 파일**
- `files/ai_research_workflow_slides.html` (전면 개선)

**Git 태그:** v4.7.57

---

## 2026-05-14 (v4.3.0 ~ v4.3.3)

**완료 작업**

### v4.3.0 — 이해관계자 관점 분석 신규 페이지 추가 (4장)
- Thoma Bravo(PE 투자자) · Blackstone(채권자) 관점 분석표 신규 추가
  - 각 이해관계자별 단계/당시 판단/사후 평가 3열 구조
  - 이해관계자별 개선 기준 비교표 (FCF 기준·금리 헤지·PIK 제한·EV/Par 경보·Exit 조건·GenAI 평가)
- 기존 p5~p10 → p6~p11로 재번호 후 새 p5로 삽입
- 총 11페이지 구조 유지 (목차+p1~p11)

### v4.3.1 — 불필요 요소 삭제 + 국문화
- 관점 전환 compare box (`box-insight`) 삭제
- "v1.0에서는 '협상 난항'으로만 기술됐으나…" 메타 문장 삭제
- 트리거/근본 원인 표기 영→한 전환 ("방아쇠(트리거)", "근본 원인(Root Cause)" 표현 정리)

### v4.3.2 — "방아쇠" 표기 제거
- `방아쇠(트리거)` → `트리거` 2곳 수정 (4장 p3 본문)

### v4.3.3 — docs-hub MD 갱신 + Astro 빌드 + GitHub 저장
- `docs-hub/src/content/docs/project/medallia_report_v2_feedback.md` 전면 갱신
  (이해관계자 관점 분석 3개 표 추가, 목차 업데이트, 트리거 표현 통일)
- Astro 빌드 완료 (13 pages)
- `work_history.md` 현 세션 v4.3.0~v4.3.3 기록 추가

**생성/수정 파일 (v4.3.0~v4.3.3)**
- `medallia_report_v2_feedback.html` / `files/medallia_report_v2_feedback.html` (v4.3.0~v4.3.2 수정)
- `docs-hub/src/content/docs/project/medallia_report_v2_feedback.md` (v4.3.3 전면 갱신)
- `work_history.md` (현 세션)

**Git 태그:** v4.3.0 / v4.3.1 / v4.3.2 / v4.3.3

---

## 2026-05-14 (v4.2.3 ~ v4.2.5)

**완료 작업**

### v4.2.3 — v2.0 보고서 2장 시장 포지셔닝 + Qualtrics 비교 표 추가
- 기업 개요 하단에 시장 세그먼트 계층 표 신규 추가
  (CRM → CX Management → XM/VoC, Gartner MQ "Voice of the Customer" 공식 분류 명시)
- Qualtrics vs Medallia 포지셔닝 비교 표 신규 추가 (13개 항목: 기업·상품·AI·재무·Exit)
- 별첨 3에 Qualtrics(Silver Lake·CPP, '23년 $12.5B) 행 추가 (이전 v4.2.2에서 포함)
- 목차 2장 항목 업데이트

### v4.2.4 — 검증루프 4건 + □/① 혼재 서식 수정
- **서식** `.sq-num` CSS 클래스 신규 추가 (□ prefix 없는 번호 소제목 전용)
  - ①②③ 소제목 6곳 `class="sq"` → `class="sq-num"` 교체 (□와 ① 혼재 제거)
  - 3장: FCF추이·PIK시뮬레이션·EV/Par Coverage, 5장: ①②③ 전체
- **Critical** LIBOR 각주 이자 계산 오류 수정
  - "$1.8B × 0.75% ≈ $135M" (오류) → 기준금리 0.75% + credit spread 7.0% = 실효 7.5%, $1.8B × 7.5% ≈ $135M
- **Important** 본문 "(전면 보완)" 잔존 2건 제거 (4장 소제목, 5장 챕터 제목)
- **Important** 별첨 6 FCF Margin 셀에 "절대 이자 $135~300M으로 커버리지 별도 확인" 주석 추가
- **Minor** 목차 별첨 5 HTML 속성 중복(class 이중 선언) 제거

### v4.2.5 — docs-hub MD 갱신 + Astro 빌드 + work_history 업데이트
- `docs-hub/src/content/docs/project/medallia_report_v2_feedback.md` 전면 갱신
  (세그먼트 계층·Qualtrics 비교·LIBOR 수정 내용 반영)
- Astro 빌드 완료 (13 pages)
- `work_history.md` 현 세션 v4.2.3~v4.2.5 기록 추가

**생성/수정 파일 (v4.2.3~v4.2.5)**
- `medallia_report_v2_feedback.html` / `files/medallia_report_v2_feedback.html` (v4.2.3·v4.2.4 수정)
- `docs-hub/src/content/docs/project/medallia_report_v2_feedback.md` (v4.2.5 전면 갱신)
- `work_history.md` (현 세션)

**Git 태그:** v4.2.3 / v4.2.4 / v4.2.5

---

## 2026-05-14 (v4.0.0 ~ v4.2.2)

**완료 작업**

### v4.0.0 — Medallia 보고서 5장 구조 전면 개정
- 기존 4장 → 5장 구조 재편: 1.보고개요 / 2.Medallia개요 / 3.투자인수현황 / 4.주요분석 / 5.시사점
- 자금조달 구조 시각화 표, SOFR 이자율 추이표, 별첨 3(동일구조 위험사례) 신규 추가
- 별첨 4(참고문헌) 분리, 날짜 '26.05.14 업데이트
- `medallia_report_final.md` / `medallia_report_final.html` / `make_medallia_standard_report.py` 수정
- `files/medallia_report_final.html` / `files/medallia_report_final.docx` 생성

### v4.1.0 — Medallia 보고서 검토 및 M&A 전략 회의록 분석 HTML 생성
- 60분 회의 STT 기록 분석 → 4페이지 A4 형식 HTML 작성
- 회의 흐름 타임라인, 재무 수치 표, 실패 원인 3중 구조, Blackstone 포지션 분석,
  M&A 평가 기준표, 거시 리스크(OpenAI/SpaceX IPO), 후속 액션 아이템 7건 포함
- `medallia_meeting_summary_20260514.html` / `files/medallia_meeting_summary_20260514.html` 생성

### v4.1.1 — 회의록 분석 docs-hub 프로젝트 문서 등록
- `docs-hub/src/content/docs/project/medallia_meeting_summary_20260514.md` 신규 등록
- `docs-hub/src/content/docs/html-docs/index.mdx` 분석 보고서 섹션에 링크 추가
- Astro 빌드 완료 (12 pages)

### v4.1.2 — GPT 버전 Medallia M&A 평가 프레임워크 HTML 추가
- Claude 버전과 비교용 GPT 버전 HTML 배포
- `medallia_gpt_analysis_20260514.html` / `files/medallia_gpt_analysis_20260514.html` 생성

### v4.2.0 — Medallia 보고서 v2.0 사업부장님 피드백 반영 전면 재작성
- **관점 전환:** 외부 충격론(금리 인상) → 구조적 설계 실패론(FCF 커버리지 0.67×)
- 신규 추가 표: FCF 커버리지 추이 / PIK 원금 누적 시뮬레이션 / EV/Par Coverage 이탈 과정
- 신규 분석 섹션: GenAI 대체 가능성 레이어별 분석 / Exit 실패 구조적 원인 / Thoma Bravo 추가투자 거절 의미
- 별첨 3 보완: 현재 상태 컬럼 추가 + SailPoint vs Medallia 비교
- 별첨 5 신규: EBITDA vs FCF 해설
- 별첨 6 신규: SaaS M&A 평가 프레임워크 (11페이지, 4단계 기준표)
- 기존 v1.0 파일 변경 없음
- `medallia_report_v2_feedback.html` / `files/medallia_report_v2_feedback.html` 생성

### v4.2.2 — v2.0 보고서 검증루프 8개 항목 전체 수정
- [Fix 1] 1장·4장 본문 `<b>v2.0 추가:</b>` 메타태그 2건 제거 → 자연스러운 본문으로 통합
- [Fix 2] "의도적 고위험 베팅" → "사후적으로 FCF 전환 가정이 지나치게 낙관적이었음이 확인된다"로 완화
- [Fix 3] FCF 표 각주: FY2020(–$30M) → '21년(+$90M) 갭 설명 추가 (Thoma Bravo 비용 최적화)
- [Fix 4] EV/Par Coverage 표 각주: EV 추정 방법론 명시 (추정 매출 × EV/Revenue 멀티플 역산)
- [Fix 5] GenAI 섹션 앞 박스 삽입: "GenAI는 직접 현금 부족 원인이 아니라 Exit 가능성 차단 요인"
- [Fix 6] "- 以 上 -" 위치 수정: 5장 내부 → 별첨 1 페이지 상단(본문-별첨 경계)
- [Fix 7] 별첨 3 표: Qualtrics(Silver Lake·CPP, '23년 $12.5B) 행 신규 추가
- [Fix 8] 목차 "(신규)/(전면 보완)/(보완)/(강화)" 표기 전면 제거

### v4.2.1 — v2.0 보고서 docs-hub 등록 + work_history 업데이트
- `docs-hub/src/content/docs/project/medallia_report_v2_feedback.md` 신규 등록
- `docs-hub/src/content/docs/html-docs/index.mdx` v2.0 링크 + GPT 버전 링크 추가
- Astro 빌드 완료 (13 pages)
- `work_history.md` 현 세션 기록 추가

**생성/수정 파일**
- `medallia_report_final.md` / `.html` / `.docx` (v4.0.0 수정)
- `medallia_meeting_summary_20260514.html` (v4.1.0 신규)
- `medallia_gpt_analysis_20260514.html` (v4.1.2 신규)
- `medallia_report_v2_feedback.html` / `files/medallia_report_v2_feedback.html` (v4.2.0 신규 / v4.2.2~v4.2.4 수정)
- `docs-hub/src/content/docs/project/medallia_report_v2_feedback.md` (v4.2.1 신규 / v4.2.5 갱신)
- `docs-hub/src/content/docs/project/medallia_meeting_summary_20260514.md` (v4.1.1 신규)
- `docs-hub/src/content/docs/html-docs/index.mdx` (v4.1.1·v4.2.1 수정)
- `work_history.md` (현 세션)

**Git 태그:** v4.0.0 / v4.1.0 / v4.1.1 / v4.1.2 / v4.2.0 / v4.2.1 / v4.2.2 / v4.2.3 / v4.2.4 / v4.2.5

---

## 2026-05-08 (v3.9.0 ~ v3.9.5)

**완료 작업**

### v3.9.0 — Medallia 보고서 analysis-report-standard.md 기준 전면 재작성
- 분석보고서 작성 기준(analysis-report-standard.md) 기준으로 보고서 구조 재편
- `medallia_report_final.md`, `medallia_report.html`, `medallia_report_outline.html` 갱신

### v3.9.1 — 분석보고서 디자인 스펙 Claude 최적화 v2.0 작성
- `shared/analysis-report-standard.md` 451줄, Claude 최적화 버전 신규 작성

### v3.9.2 — docs-hub 등록 및 GitHub 푸시
- 분석보고서 작성 기준 v2.0 docs-hub Starlight 등록 및 빌드
- 세션 스냅샷 태그: v3.9.2-snapshot

### v3.9.3 — docs-hub HTML 목록에 디자인 스펙 가이드 링크 추가

### v3.9.4 — 자가검증 날짜형식 수정 ('26.4.30 → '26.04.30)

### v3.9.5 — Medallia 보고서 제목 일괄 변경
- '사업건전성 관리 기준의 재정립' → 'SaaS 기업 가치 평가 기준'

**생성/수정 파일**
- `shared/analysis-report-standard.md` (v2.0 신규)
- `medallia_report_final.md` / `medallia_report.html` / `medallia_report_outline.html` (수정)
- docs-hub Starlight 페이지 등록

**Git 태그:** v3.9.0 / v3.9.1 / v3.9.2 / v3.9.3 / v3.9.4 / v3.9.5

---

## 2026-05-07 (v3.7.7 ~ v3.8.3)

**완료 작업**

### v3.7.7 — Medallia 보고서 제목 변경 및 5장 신규 추가
- 보고서 제목 변경: "Medallia 사례로 본 SaaS 기업 가치 평가 기준"
- 5장(시사점 및 제언) 신규 추가
  - ① 투자실패 진단
  - ② 평가기준 확장
  - ③ FCF/EV-Par Coverage 지표 관리

### v3.7.8 — 페이지 헤더 제거 및 본문 구조 재배치
- 모든 페이지 헤더(문서제목·구분선) 제거
- 본문 첫 페이지에 제목·솔루션전략그룹 재배치
- 목차 요약박스 제거 → 본문 이동

### v3.7.9 ~ v3.8.0 — 요약문 통합 및 압축
- 요약문 + 도입문 단일 박스로 통합
- 3줄로 압축

### v3.8.1 — 검증루프(보고 수령자 관점) 전항목 반영
- 4장 삭제·5장→4장 재번호
- 목차 페이지번호 제거 (본문 p.1부터 시작)
- $4.6B/$5B 에쿼티 손실 구분 주석 추가
- 3장→4장 브리지 문장 추가
- 별첨 목차 페이지 레이블 정리
- 차트 해설 추가
- EV/Par Coverage 내부 기준(안) 주석 추가

### v3.8.2 — Markdown 버전 생성 및 docs-hub 등록
- Markdown 버전(`medallia_report_final.md`) 생성
- docs-hub Starlight 등록 및 빌드

### v3.8.3 — Word(.docx) 파일 재생성
- 디자인 스펙 가이드 완전 적용
  - 바탕체 14pt, A4, 여백 설정
  - 요약박스 1행3열 구성
  - 표 헤더 검정
  - 페이지번호 바닥글
  - 以上 마무리 문구

**생성/수정 파일**
- `medallia_report_final.md` (신규)
- `medallia_report_final.docx` (재생성)
- docs-hub Starlight 페이지 등록

**Git 태그:** v3.7.7 / v3.7.8 / v3.7.9 / v3.8.0 / v3.8.1 / v3.8.2 / v3.8.3

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
