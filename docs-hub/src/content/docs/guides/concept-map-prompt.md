---
title: /concept-map — 개념 설명 지형도 스킬
description: 개념·기술·기업·제품·시장을 지형도 방식으로 분석한다. 구조·위치·경쟁 관계·시장 맥락 파악에 사용. "/concept-map" 명령 또는 "개념도", "지형도", "구조적으로 설명" 등의 요청에 자동 적용.
---

> 개념명을 입력하면 **개체 분류(0번) + 8개 항목**으로 구조화된 설명을 생성합니다.  
> MECE 원칙 + 지형도 기반 설명으로 개념의 시장·기술 맥락을 입체적으로 파악할 수 있습니다.

**최종 수정:** '26.06.09 &nbsp; | &nbsp; **위치:** `~/.claude/skills/concept-map/`

---

## 📥 다운로드 및 설치

| | 링크 |
|--|------|
| **GitHub 레포** | [github.com/juree85-netizen/my-prompts](https://github.com/juree85-netizen/my-prompts) |
| **파일 직접 다운로드** | [concept-map.md](https://raw.githubusercontent.com/juree85-netizen/my-prompts/main/concept-map.md) |

**Claude Code 설치 (터미널 1줄):**

```bash
mkdir -p ~/.claude/skills/concept-map && curl -o ~/.claude/skills/concept-map/SKILL.md https://raw.githubusercontent.com/juree85-netizen/my-prompts/main/concept-map.md
```

---

## 호출 방법

```
/concept-map [설명할 개념]
```

슬래시 명령 없이도 아래 표현으로 자동 트리거됩니다.

| 트리거 표현 | 예시 |
|-------------|------|
| `/concept-map` | `/concept-map LBO` |
| 개념도 / 지형도 | `IDP 지형도 그려줘` |
| 구조적으로 설명 | `T-LLM 구조적으로 설명해줘` |
| 시장에서 어떤 위치 | `SaaS 시장에서 어떤 위치야?` |
| 경쟁 관계 | `PE 펀드 경쟁 관계 알려줘` |
| 어떤 회사야 / 어떤 기술이야 | `Rossum 어떤 회사야?` |

---

## 개체 분류 규칙 (v2 신규)

설명 시작 시 대상을 아래 6가지 중 하나로 분류하고 **반드시 표시**합니다.

| 분류 | 기준 | 예시 |
|------|------|------|
| 기업(Company) | 법인 조직. 제품·서비스를 만드는 주체 | Rossum, Salesforce |
| 제품(Product) | 기업이 출시한 소프트웨어·하드웨어·서비스 | Rossum Aurora, Slack |
| 기술(Technology) | 특정 방법론·알고리즘·아키텍처 패턴 | T-LLM, RAG, LBO |
| 시장(Market) | 수요·공급이 형성된 산업 카테고리 | IDP, SaaS, ERP |
| 표준/프로토콜(Standard) | 업계 합의로 만들어진 규격·인터페이스 | REST API, OAuth |
| 플랫폼(Platform) | 다수의 공급자·소비자를 연결하는 생태계 기반 | AWS, Salesforce AppExchange |

출력 예시:
```
Rossum → 기업
Rossum Aurora → 제품
T-LLM → 기술
IDP → 시장
```

---

## 출력 구조 — 0 + 8개 항목

| # | 항목 | 설명 |
|---|------|------|
| 0 | **개체 분류** | 6가지 유형 중 하나로 분류 + 한 줄 요약 |
| 1 | 상위 개념 | 더 큰 범주 (기술 계층 / 산업 분류 / 시장 카테고리) |
| 2 | 존재 목적 | 어떤 문제·공백을 해결하기 위해 등장했는가 |
| 3 | 동일 층위 비교 (MECE) | 같은 레벨의 유사 개념·제품·기업 비교 |
| 4 | 대체재 / 경쟁재 (MECE) | 직접 경쟁 vs 간접 대체 구분 |
| 5 | 하위 구성요소 (MECE) | 모듈·기능·레이어·역할로 분류 |
| 6 | 실제 사용 예시 | 실제 기업·제품 적용 사례 2~3개 |
| 7 | 트리 구조 | 계층 시각화 (`├──` 형식) |
| 8 | 비유 | 비기술자도 이해할 수 있는 일상 언어 비유 |

---

## 핵심 원칙

| 원칙 | 내용 |
|------|------|
| 개체 분류 우선 | 설명 전에 기업/제품/기술/시장 등 6가지로 분류 |
| 지형도 우선 | 정의보다 "어디에 속하는가"를 먼저 설명 |
| 4가지 구분 | 기술 / 기업 / 제품 / 시장을 혼용하지 않고 명시 |
| MECE 분류 | 3·4·5번 항목은 겹치지 않고 빠짐없이 구성 |
| 층위 구조 | 상위 · 동일 층위 · 하위를 명확히 나눠 설명 |
| 비교 중심 | 단독 설명보다 같은 층위의 다른 것과 비교 |
| 구조 시각화 | 트리로 계층을 한눈에 파악 |
| 비유 포함 | 추상적 개념을 일상 언어로 착지 |

---

## 스킬 파일 구성 및 다운로드

| 파일 | 설명 |
|------|------|
| `~/.claude/skills/concept-map/SKILL.md` | 개체 분류 규칙 + 8개 항목 출력 규칙 정의 |
| [github.com/juree85-netizen/my-prompts](https://github.com/juree85-netizen/my-prompts) | GitHub 원본 레포 (공개) |

### 다운로드

- **GitHub 레포:** [https://github.com/juree85-netizen/my-prompts](https://github.com/juree85-netizen/my-prompts)
- **파일 직접 다운로드:** [concept-map.md](https://raw.githubusercontent.com/juree85-netizen/my-prompts/main/concept-map.md)

### Claude Code 설치 방법

```bash
# 1. 스킬 디렉토리 생성
mkdir -p ~/.claude/skills/concept-map

# 2. 파일 다운로드
curl -o ~/.claude/skills/concept-map/SKILL.md \
  https://raw.githubusercontent.com/juree85-netizen/my-prompts/main/concept-map.md
```

---

## 재사용 프롬프트 (ChatGPT 등 외부 AI용)

> Claude Code `/concept-map` 스킬과 동일한 구조로 외부 AI에서 사용할 때 아래 프롬프트를 복사·붙여넣기

```
설명할 개념: ___________

먼저, 설명 대상을 아래 6가지 중 하나로 분류하고 출력 첫 줄에 표시해줘.
- 기업(Company): 법인 조직
- 제품(Product): 기업이 출시한 소프트웨어·하드웨어·서비스
- 기술(Technology): 방법론·알고리즘·아키텍처 패턴
- 시장(Market): 수요·공급이 형성된 산업 카테고리
- 표준/프로토콜(Standard): 업계 합의 규격
- 플랫폼(Platform): 공급자·소비자를 연결하는 생태계 기반

예: Rossum → 기업 / 한 줄 요약: IDP 시장에서 AI 기반 문서 처리 소프트웨어를 만드는 체코 스타트업

그 다음, 위 개념을 아래 8가지 항목으로 설명해줘.
단순 정의가 아니라, 이 개념이 속한 시장·기술 지형도 안에서 위치와 맥락을 이해할 수 있도록 설명해줘.

설명 전체에서 기술 / 기업 / 제품 / 시장을 구분해서 서술해줘.
예: "Rossum은 기업이고, Aurora는 제품이며, T-LLM은 기술이고, IDP는 시장이다."

분류가 필요한 항목(3, 4, 5번)은 MECE 원칙에 따라
겹치지 않고(Mutually Exclusive) 빠짐없이(Collectively Exhaustive) 구성해줘.

### 1. 상위 개념
이 개념이 속한 더 큰 범주는 무엇인가?
기술 계층인지, 산업 분류인지, 시장 카테고리인지 명시해줘.

### 2. 존재 목적
왜 이 개념·제품·기술이 등장했는가?
어떤 문제나 공백을 해결하기 위해 존재하는가?

### 3. 동일 층위 비교 (MECE)
같은 레벨에 있는 유사 개념·제품·기업은 무엇인가?
서로 겹치지 않게, 빠짐없이 구분해서 각각 2~3줄로 비교해줘.

### 4. 대체재 / 경쟁재 (MECE)
이것을 대체할 수 있는 것은 무엇인가?
직접 경쟁(같은 방식)과 간접 대체(다른 방식으로 같은 목적 달성)를 나눠서 설명해줘.

### 5. 하위 구성요소 (MECE)
이 개념을 구성하는 하위 요소들은 무엇인가?
겹치지 않고 빠짐없이 모듈·기능·레이어·역할로 나눠줘.

### 6. 실제 사용 예시
실제 기업이나 제품에서 어떻게 쓰이는가?
구체적인 사례 2~3개를 들어줘.

### 7. 트리 구조
아래 형식으로 계층 구조를 시각화해줘.

[최상위 개념]
├── [상위 개념]
│   ├── [설명할 개념]  ← 여기
│   │   ├── [하위 요소 1]
│   │   └── [하위 요소 2]
│   └── [동일 층위 비교 개념]
└── [다른 상위 개념]

### 8. 비유
이 개념을 일상적인 언어나 상황으로 비유해줘.
기술을 모르는 사람도 이해할 수 있도록.
```
