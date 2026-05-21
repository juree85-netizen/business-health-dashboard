# 보고서 원형 카탈로그 (Report Archetypes — ideation reference)

**This file is a palette, not a template.** Use it to *ideate structure*
before writing. Never force a section onto a report just because the
archetype lists it. Real reports are overwhelmingly **hybrids** (a 기업개요
wrapped inside a 제언, a 주간보고 that folds a mini 현안보고 inside),
and the section mix should be driven by **what the input actually contains
and what the reader needs to understand**, not by this document.

---

## Two hard rules that override everything below

1. **Don't force sections.** If the input has no 경영실적 numbers, do not
   invent a 경영실적 block. If there is no SDS action to take, do not tack
   on a fake 제언 section. **An empty or invented section is worse than
   no section.** Prefer omission.

2. **Serve the reader.** The archetype lists a typical order, but reorder,
   merge, rename, or omit anything if it makes the brief easier to scan.
   A reader opening this report needs to understand the topic quickly —
   conformance to a pattern is never the goal.

Before writing, ask: *"If I strip this archetype down to only the blocks
my input actually supports, what's left?"* That stripped-down version is
your skeleton.

---

## Common DNA (모든 원형이 공유)

Regardless of archetype, these patterns recur across the sample corpus:

- **Opening = 한 줄 정의/요지 + 가장 임팩트 있는 수치/시점/주체.**
  서사·배경 설명 없이 곧바로 팩트. 예: `□ 설립 : '21年 (본사 : 美…)`
  한 줄 + 비즈니스 한 줄 정의.
- **Body = parallel 사실 블록.** 각 `□` 섹션은 독립된 한 가지 주제.
  섹션 간 순서는 추상 → 구체 (개요 → 구조 → 실적 → 경쟁 → 시사점).
- **마지막은 "우리 입장"에서 착지** (해당할 때만). 시사점·제언·향후
  계획·협업요청·결재 요청 중 상황에 맞는 것 하나. 필요 없으면 생략.
- **`→` 마커는 분석 → 행동의 다리.** 마지막 1~3개 불릿에서 자주 사용:
  "→ SDS는 …필요 / …추진 / …확보".
- **테이블은 반복·병렬 데이터가 있을 때만.** 텍스트 나열이 부자연스러운
  비교·수치·일정표에만 사용. 1~2행짜리 테이블은 피함.

---

## Archetype palette (8 types)

각 원형은 **트리거 신호**(입력에 어떤 단서가 있으면 이 원형을 떠올리면
좋은가), **자주 등장하는 섹션**(모두 넣으라는 뜻 아님), **오프닝/클로징
패턴**(샘플에서 관찰된 실제 문장)으로 구성.

### A. 기업/인물 개요

**When it applies**: 입력이 "이 회사/사람 뭐 하는 곳인가"에 답하는 성격.
"기업 개요", "회사 소개", "대표 프로필" 같은 키워드.

**Typical sections (drop freely)**:
- `□ 설립` — 연도 + 본사 소재지 + 1줄 비즈니스 정의
- `□ 대표` — 이름 + 4~6개 시대별 경력 (· 불릿)
- `□ 인력현황` / `□ 시가총액·기업가치` / `□ 주주현황`
- `□ 주요 사업` — 제품·세그먼트 나열
- `□ 경영실적` — 3년 재무 테이블 (매출/손익/CAGR)
- `□ 주요 현안` 또는 `□ 파트너십 현황`
- `□ 향후 전망` — 시사점은 여기에 녹이는 경우가 많음 (별도 "시사점"
  섹션으로 빠지지 않을 때도 있음)

**Opening example** (Cerebras):
```
□ 설립 : '16年 (본사 : 美 캘리포니아주 서니베일)
  - 세계 최대 규모의 웨이퍼 스케일 AI 칩을 설계·제조하여
    초고속 AI 추론 및 훈련 인프라를 제공하는 AI 반도체 전문기업
```

**Closing example** (implication woven into last bullets of 향후 전망):
```
- OpenAI의 $10B 파트너십은 단순 구매계약 이상으로 해석
- NVIDIA GPU 독점 극복을 위한 생태계 다변화 신호
- AI 하드웨어 경쟁 구도의 본격적 재편 예상
```

---

### B. 이벤트·인터뷰 요약

**When it applies**: 키노트, 컨퍼런스, 인터뷰, 발표문 같은 **단일 이벤트
요약**. "인터뷰 요약", "CES 발표", "키노트 정리" 키워드.

**Typical sections**:
- `□ 인터뷰/발표 개요` — 매체·연자·일자
- `□ [핵심 주제 1]` ~ `□ [핵심 주제 N]` — 질문형 헤딩이 자연스러움
  ("왜 …인가", "어떻게 …하는가")
- `□ SDS 시사점` 또는 `□ 기회·위협`

**Opening example** (Jensen Huang):
```
□ 인터뷰 개요
  - Jensen Huang (NVIDIA CEO), Dylan Patel (SemiAnalysis) 대담
  - NVIDIA 사업 모델을 '전자를 토큰으로 변환하는 회사'로 정의
```

**Closing example** (시사점 섹션, `→` 다용):
```
- (중립 플랫폼 포지셔닝) NVIDIA가 하이퍼스케일러와 경쟁하지 않는 설계
  → SDS도 MSP 사업 수행시 E2E AX 중립 파트너로서의 역할을 명확히 할 필요
```

**Distinctive**: 직접 인용 다용 ("~라고 강조"), 인용구에는 인물명으로
주석 앵커. 인터뷰 보고서에 한해 **`(Q) …` 주석으로 질문 원문을 보존**하는
특유의 용법이 있음 — 본문은 답변 요약, 주석은 원 질문. 답변 요약 문장
핵심 명사에 앵커. (젠슨황·Patel 대담 보고서 참고)

---

### C. 시장·산업 분석

**When it applies**: 산업 리포트 요약, 시장 규모·성장률 분석, 전망 보고.
BCG/McKinsey/IEA/a16z 같은 외부 리포트 소화, 또는 내부 시장 조망.

**Typical sections**:
- `□ Executive Summary` — 3~4개 핵심 메시지 불릿
- `□ 시장 규모·성장률` — 연도별 수치 + 테이블
- `□ 도입 현황 / 세그먼트 분석`
- `□ 경쟁 구도 / Player 분석`
- `□ 전망 / 리스크`
- `□ 제언` 또는 `□ SDS 시사점`

**Opening example** (기업용 생성형 AI 시장):
```
□ 시장 현황
  - 생성형 AI 시장 확대 : '23년 1.7B$ → '24년 11.5B$ → '25년 37B$
```

**Closing example**:
```
- '26年 전망 : 자율성 갖춘 AI Agent가 주류
  → ① AI가 프로그래밍에서 인간 능가
  → ② 제벤스의 역설 (비용 하락 → 수요 폭증)
  → ③ Explainability·거버넌스 필요성 증대
```

---

### D. 제품·기술 개요 / 비교

**When it applies**: 특정 기술·플랫폼·제품을 소개하거나 경쟁 제품과
비교. "기술 개요", "플랫폼 비교", "아키텍처 분석" 키워드.

**Typical sections**:
- `□ [제품/기술] 개요` — 정의 한 줄 + 핵심 효과 수치 + 발표 시점
- `□ 작동 방식 / 아키텍처` — 레이어·단계·구성요소 분해
- `□ 특장점 / 성능 지표` — 벤치마크 수치
- `□ 고객 도입 사례 / 적용 분야`
- `□ 경쟁 기술 비교` — 비교표 거의 필수
- `□ SDS 시사점` — 원가절감/신사업/고객가치 관점

**Opening example** (TurboQuant):
```
□ TurboQuant 개요 및 정의
  - LLM KV 캐시를 16비트 → 3비트까지 압축, 메모리 6배 절감
  - 별도 Fine-tuning 없이 기존 모델에 즉시 적용 가능 (Training-free)
```

**Closing example**:
```
- AI 추론 서비스 원가 절감 : 동일 GPU 인프라로 이론상 6배 쿼리 처리 可
- On-Prem AI 구축사업 확대 : 고객사 서버 환경에서 고성능 LLM 구동
```

**Distinctive**: 비교표가 핵심. 경쟁사 vs 자사, 기존 방식 vs 신기술.

---

### E. SDS 제언·대응 전략

**When it applies**: "그래서 우리 뭐 해야 하는가"에 답하는 성격. 위기
대응·전략 방향·대응방안 같은 결정 유도형. "제언", "대응방안", "전략"
키워드, 혹은 이벤트·시장 분석 뒤에 Action Item이 붙는 긴 보고서.

**Typical sections** (이 원형은 `Ⅰ./1.` 상위 계층을 쓰는 경우가 많음):
- `Ⅰ. 현황 / 배경` — 문제 상황, 위기 신호, 숫자
- `Ⅰ. 위협과 기회` — `□ [위협]` / `□ [기회]` 태그로 구분
- `Ⅰ. SDS 대응방향`
  - `1. 현 상황 진단`
  - `2. 대응방안` — `①②③` Action Item, 타임라인(ASAP/6개월/12개월)
    및 담당조직(`* AX센터`) 병기
- `[별첨]` 경쟁사 벤치마크 표 (Accenture, TCS, Capgemini 등)

**Opening example** (SDS 대응방향):
```
□ '26年 IT 서비스 업체 주가 충격 : SaaSapocalypse 시장 패닉
  - US S/W 주식 -6.2%, 글로벌 IT서비스 -5.1%, 인도 Nifty IT -6.8% ↓
```

**Closing example**:
```
③ 규제 대응 관련 서비스 상품화 추진 (12개월) * 클事, 솔事, 법무팀
   - AI 기본법 고영향 AI 영향평가 템플릿 표준화 等
```

**Distinctive**: `[위협]`/`[기회]` 태그, Action Item 타임라인, 담당조직
명시, 벤치마크 비교표.

---

### F. 주간업무보고

**When it applies**: "주간 업무 보고", "N월 N주차", "현안 보고" 키워드.
1~2 페이지, 진행 상태 위주.

**Typical sections**:
- 제목 인라인 (목차·커버 없음): `[부서] 주간 업무 보고 (N월 N주차)`
- `□ [주요 이슈 1]` (`~마감일`) — 진행률%, 격차, 조속 조치
- `□ [주요 이슈 2]` — 세부 상태 + 차주 계획
- `[TABLE: 진행률 matrix]` — 시스템 × 지표%
- `[TABLE: 연간 주요 업무]` — 전략 3~5건

**Opening example**:
```
□ 차세대TF 4차 통합테스트 수행 (~10/31)
  - 현재 89.8% 진행 중, 결함 조치 82.7%로 목표 95% 대비 낮아
    조속 조치를 촉구 中
```

**Closing example** (1인칭 선언형 어미 등장):
```
- 차주 Steering Committee(11/6)를 통해 차세대 구축 상세 현황을
  보고드리겠습니다
```

**Distinctive**: `☞`, `▲`, `(~날짜)` 기호. `-겠습니다` 같은 1인칭 선언형
어미가 명사형과 혼용됨. `- 이  상 -` 생략되기도 함.

---

### G. 업무계획 / 추진방향

**When it applies**: "업무계획", "추진방향", "CEO 보고", "전사 계획"
키워드. 5~10 페이지, 전략 깊이 있음.

**Typical sections** (`Ⅰ./1./□` 다층 구조 상시):
- `Ⅰ. [부서] 미션` — 2~3문장 전략 목표
- `Ⅰ. [연도] 추진 전략·방향` — 3~5 필러 (Foundation / Tech / Agentic 등)
- `Ⅰ. 추진 체계 및 주요업무`
  - `1) 추진체계`
  - `2) 월별 업무계획` — `[TABLE: 월 × 영역]` 로드맵
- `Ⅰ. 운영/변화관리 방안`
  - `[TABLE: R&R 및 주요업무 — 구분 × 역할 × 업무]`
- `□ 협업 요청사항`
- `[별첨1]`, `[별첨2]` — 조직도, 세부 스펙

**Opening example** (CEO 보고):
```
경영혁신팀 미션 | 사업의 지속성장을 지원하기 위해 업무수행에 필요한
                 프로세스·시스템을 제공하고, 이를 기반으로 AI 생산성
                 혁신을 추진
```

**Closing example** (향후계획 / 협업요청으로 마감):
```
- Cursor PoC 부서 중심 개발망 VDI 적용·PoC 수행 (~3월)
- 개발망 VDI 활용 대상 시스템 정비 (6월) 및 전사 확산 (지속)
```

**Distinctive**: `【1】 【2】` 대분류, `▶` 프로세스 흐름, R&R 매트릭스
및 월별 로드맵 테이블이 중심. 선언형 어미 ("추진한다", "강화한다")
자주 사용.

---

### H. 현안·이슈 보고

**When it applies**: 특정 프로젝트/정책의 이슈·진행경과·검토결과·
도입계획·활용방안. "이슈보고", "진행 경과", "검토 결과", "도입 계획",
"활용 방안" 키워드.

**Typical sections** (`1./2./3.` 숫자 계층 선호):
- `1. 배경 / 개요` — 왜 지금인가, 이해관계자
- `2. 진행경과 / 검토결과`
  - 심의 건 : `타당성 / ROI / 보안성` → `「적합」` / `「검토중」`
  - 이슈 건 : 지연·리스크·손해 → `[손해1]`, `[손해2]`
- `3. 향후계획 또는 협업 요청사항` — 일정(MM월) + 책임부서
- `[별첨1]` 공문내용 / `[별첨2]` 법무검토 / `[별첨3]` 보안성 검토
  — **별첨이 본문만큼 중요**, 증빙 성격

**Opening example** (상품교육포탈 이슈보고):
```
□ 상품교육포탈 프로젝트 개요
  - 업체(겟스마트)의 누적된 일정 지연으로 리스크 대비가 필요
```

**Closing example**:
```
- 계약서 계약 범위 內 잔여 업무 완료 확약 (업체 완료 목표일 '26.2월말)
```

**Distinctive**: `「적합」`, `(案)` 드래프트, `[손해1]` 리스크 카테고리,
심의 매트릭스 테이블.

---

## Hybrid is the norm (혼합형이 표준)

Most real reports **draw from multiple archetypes**. 분류에 매달리지 말고,
입력에서 실제로 답할 수 있는 블록들을 조합해서 조립하면 됨.

**Example 1 — KKR 투자 영향 분석 (E + A 혼합)**

One document combined:
- E-style opening: `□ 거래 개요` — 거래 구조·금액·일정
- E-style 분석: `□ 자금 활용방향`, `□ 투자시 주요 고려사항`
  (재무·규제·운영·거버넌스·조직 5개 리스크 축)
- E-style 제언: `□ 신사업 포지셔닝`, `< SDS 예상 실행과제 >`
- **A-style trailing 기업개요** (KKR 회사 설명):
  `□ 설립 / □ 대표 / □ 인력 / □ 시가총액 / □ 주요사업 / □ 경영실적`

Pattern: **이벤트·의사결정 중심의 E를 메인으로 하고, 배경 지식으로
A (기업개요)를 꼬리에 붙임.** 하나의 원형으로 끼워 맞추려 하지 말고
필요한 블록만 가져왔음.

**Example 2 — 경영진 보고(KKR, 단일 페이지 요약)**

Same topic, different audience (경영진 의사결정용):
- `□ 거래 개요` (E 도입)
- `□ 자금 활용 방향`, `□ 전략적 의미` (왜 지금인가)
- `□ 주요 리스크 & 대응 방향` — `[재무]/[규제]/[운영]/[거버넌스]/[조직]`
- `□ 실행 권고 : 즉시 착수해야 할 Top 5 과제` — `①②③④⑤`
- `※ 최종 판단 :` 한 줄 결론

Pattern: 같은 주제라도 **독자와 목적에 따라 섹션 취사선택이 달라짐**.
경영진 결재용은 기업개요 블록을 통째로 뺐고, 대신 `실행 권고 Top 5`와
`최종 판단` 한 줄이 더 비중 있음. 원형 E의 변주이지만 A 블록은 필요
없다고 판단해서 제외.

---

## Step 0 체크리스트 (보고서 작성 시작 전)

1. 입력 자료에서 **어떤 사실 블록이 실제로 뽑히는지** 먼저 확인
   (회사 정보인가? 수치·실적인가? 이벤트·발언인가? 프로젝트 상태인가?
   결정을 요구하는가?)
2. 가장 가까운 원형(들)을 떠올리되, **블록이 없으면 그 섹션은 빼고,
   있는데 원형에 없으면 추가**
3. 독자를 그려본다 — 임원인가 동료인가? 결재용인가 공유용인가?
   결재용이면 리스크·대응·실행권고가 앞쪽, 공유용이면 사실·맥락이 앞쪽
4. **쓸 수 있는 블록만으로 조립한 스켈레톤이 나왔으면** Step 1(조사)로
