---
title: /business-diagnosis — BMC × 맥킨지 7단계 사업 진단 스킬 (v2)
description: BMC로 Root Cause Block을 특정하고, 문제 유형 분류 후 맥킨지 7단계로 Issue Tree → Priority Score → Elevator Pitch를 도출한다. "/business-diagnosis" 또는 "/problem-canvas" 명령, "사업 문제", "비즈니스 진단" 등에 자동 적용.
---

import { Aside } from '@astrojs/starlight/components';

> **BMC는 문제 위치를 찾는 도구, 맥킨지 7단계는 원인 제거 및 실행 우선순위 설계 도구.**  
> BMC 진단 결과(Root Cause Block)는 반드시 McKinsey Step 2(Issue Tree)의 최상위 노드로 연결됩니다.

**최종 수정:** '26.06.09 &nbsp;|&nbsp; **위치:** `~/.claude/skills/business-diagnosis/` &nbsp;|&nbsp; **이전 이름:** `problem-canvas`

---

## 📥 다운로드 및 설치

| | 링크 |
|--|------|
| **GitHub 레포** | [github.com/juree85-netizen/my-prompts](https://github.com/juree85-netizen/my-prompts) |
| **v2 파일 다운로드** | [business-diagnosis.md](https://raw.githubusercontent.com/juree85-netizen/my-prompts/main/business-diagnosis.md) |
| **v1 파일 다운로드** | [problem-canvas.md](https://raw.githubusercontent.com/juree85-netizen/my-prompts/main/problem-canvas.md) |

**Claude Code 설치 (터미널 1줄):**

```bash
mkdir -p ~/.claude/skills/business-diagnosis && curl -o ~/.claude/skills/business-diagnosis/SKILL.md https://raw.githubusercontent.com/juree85-netizen/my-prompts/main/business-diagnosis.md
```

---

## v2 개선 내역 (problem-canvas → business-diagnosis)

| # | 개선 항목 | 변경 내용 |
|---|-----------|-----------|
| 1 | BMC 진단 규칙 | Root Cause Block 판단 기준 추가 (결과 vs 원인 구분) |
| 2 | 문제 유형 분류 | Growth / Profitability / Operation / Organization / Strategy |
| 3 | Issue Tree 템플릿 | 문제 유형별 4개 템플릿 (매출·수익·운영·전략) |
| 4 | 우선순위 계산식 | Impact × Feasibility (각 1~5, 만점 25점) |
| 5 | So What 규칙 | 1문장·20~40자·"핵심은 ○○, 해결책은 ○○" 형식 고정 |
| 6 | Elevator Pitch 규칙 | 4문장 구조 (현재 문제→원인→해결책→기대 효과) |
| 7 | 핵심 연결 규칙 | BMC Root Cause → Issue Tree 최상위 노드 의무 연결 |

---

## 호출 방법

```
/business-diagnosis [문제 상황 또는 기업명]
/problem-canvas [문제 상황]   ← 하위 호환 유지
```

슬래시 명령 없이도 자동 트리거됩니다.

| 트리거 표현 | 예시 |
|-------------|------|
| 사업 문제 / 비즈니스 진단 | `고객 재구매율이 낮은 문제를 진단해줘` |
| BMC 분석 | `우리 사업 BMC로 분석해줘` |
| 맥킨지 방식으로 | `이 문제 맥킨지 방식으로 풀어줘` |
| 어떻게 해결할까 | `매출이 3개월째 정체된 이유와 해결책` |

---

## 출력 흐름

```
Step 0.  문제 유형 분류 (Growth / Profitability / ...)
    ↓
Phase 1. BMC Root Cause Block 특정
    ↓      결과 블록(R$·C$) 아닌 원인 블록을 추적
         Root Cause Block → Issue Tree 최상위 노드로 연결
    ↓
Step 1.  문제 정의 (SMART)
Step 2.  Issue Tree (유형별 템플릿, 최상위 노드 = Root Cause)
Step 3.  우선순위 (Impact × Feasibility, 25점 만점)
Step 4.  분석 계획
Step 5.  핵심 발견사항
Step 6.  So What? (1문장, 20~40자)
Step 7.  권고안 + Elevator Pitch (4문장)
```

---

## BMC Root Cause 진단 규칙

**결과(Symptom)와 원인(Cause)을 구분한다.**

| 증상 | ❌ 잘못된 판단 | ✅ 올바른 Root Cause Block |
|------|-------------|--------------------------|
| 매출 감소 | R$ | VP / CH / CR 우선 검토 |
| 고객 이탈 증가 | CR | VP(가치 부족) 또는 CH(접점 문제) |
| 신규 고객 확보 실패 | CS | CH(채널 부재) 또는 VP(소구력 약화) |
| 원가 상승 | — | C$ (직접 원인) |
| 파트너 이탈 | KP | VP(파트너 가치 부족) 또는 R$(배분 구조) |

**Root Cause 판단 순서**:
1. 증상의 "바로 앞 단계" 블록 추적
2. 복수 블록이 의심될 경우 → "더 먼저 발생한 것"이 Root Cause
3. R$·C$는 결과 블록인 경우가 많음 — 원인 블록 먼저 탐색

---

## 문제 유형 분류

| 유형 | 대표 증상 |
|------|-----------|
| **Growth** | 매출 정체, 신규 고객 확보 실패, 점유율 하락 |
| **Profitability** | 매출 증가에도 이익 감소, 원가율 상승 |
| **Operation** | 프로세스 병목, 납기 지연, 품질 저하 |
| **Organization** | 핵심인력 이탈, 사일로, 의사결정 지연 |
| **Strategy** | 시장 변화 대응 실패, 경쟁 우위 소멸, 비즈니스 모델 노후화 |

---

## 우선순위 계산식

```
Priority Score = Impact × Feasibility

Impact      1~5점 (사업 전체에 미치는 영향)
Feasibility 1~5점 (현실적 해결 가능성)
만점        25점
```

---

## 실전 예시 — 삼성SDS

> `/business-diagnosis 삼성SDS` 실행 결과 요약

### Step 0. 사업 프로파일 + 문제 유형

| 항목 | 내용 |
|------|------|
| 사업 유형 | B2B — IT서비스(SI/ITO) + 클라우드·AI + 물류IT |
| 문제 유형 | **Strategy** |
| 선택 이유 | 매출 정체나 마진 하락이 아닌, 비즈니스 모델 자체가 "삼성 계열사 전용"으로 고착 |

### Phase 1. BMC Root Cause

```
🔴CS   🟡VP   🟡CH
       ——     🟡R$
🟡KR   ——     🟡KP
              ——

🔴 Root Cause: CS (외부 고객 세그먼트 미정의)
🟡 연쇄 영향: VP → CH → R$ / KR / KP
```

**Root Cause 추적 경로:**
```
외부 매출 정체(R$)
    ← 외부 채널 없음(CH)
        ← 외부 VP 불명확(VP)
            ← 외부 고객 세그먼트 미정의(CS)  ← Root Cause
```

### Step 2. Issue Tree (Strategy 템플릿 적용)

```
외부 시장 성장 정체 [Root: CS 미정의]
├── A. 외부 ICP 자체가 없음
│   ├── A-1. 타겟 ICP(업종·규모·Pain Point) 미정의
│   └── A-2. 외부 고객 니즈 조사·검증 체계 부재
├── B. 외부 VP 미개발 (A의 결과)
│   ├── B-1. "왜 SDS인가" 설득 논리 없음
│   └── B-2. 외부 레퍼런스 부재 → VP 검증 불가 악순환
└── C. 채널·역량 미구축 (B의 결과)
    ├── C-1. 외부 전담 영업 조직 미성숙
    └── C-2. ISV·파트너 생태계 부재
```

### Step 3. Priority Score

| 이슈 | Impact | Feasibility | Score | 순위 |
|------|--------|------------|-------|------|
| A-1. 타겟 ICP 정의 | 5 | 5 | **25** | 1 |
| C-1. 외부 영업 조직 분리 | 4 | 4 | **16** | 2 |
| A-2. 외부 고객 니즈 조사 | 4 | 4 | **16** | 2 |
| B-1. 외부 VP 개발 | 5 | 3 | **15** | 3 |
| B-2. 레퍼런스 고객 확보 | 5 | 3 | **15** | 3 |
| C-2. ISV 파트너 생태계 | 3 | 2 | **6** | 5 |

### Step 6. So What?

> **핵심은 '외부 ICP 미정의'이며, ICP 수립 후 VP·채널 순서로 재건하는 것이 유일한 경로다.**

### Step 7. Elevator Pitch (4문장)

> 1. **현재 문제**: 삼성SDS의 외부 매출은 3년째 30% 미만으로 정체되어 있고, 클라우드·AI 전환 선언에도 불구하고 계열사 의존 구조는 전혀 개선되지 않고 있습니다.
> 2. **근본 원인**: 문제의 본질은 매출 구조가 아니라 외부 고객 세그먼트를 한 번도 제대로 정의한 적이 없다는 것이며, ICP 없이 만든 VP와 채널은 계열사 전용으로만 최적화되어 있습니다.
> 3. **해결책**: 클라우드·AI 사업부에서 업종 3개·Pain Point 5개 기준의 외부 ICP를 즉시 수립하고, 이를 기반으로 레퍼런스 고객 20개를 손실 감수 수주로 확보해 VP를 검증합니다.
> 4. **기대 효과**: ICP 기반 VP가 검증되면 외부 영업·파트너 투자의 근거가 생기고, 2~3년 내 외부 매출 비중 50% 달성과 계열사 의존 구조 탈출이 현실적 목표가 됩니다.

---

## 스킬 파일 구성 및 다운로드

| 파일 | 설명 |
|------|------|
| `~/.claude/skills/business-diagnosis/SKILL.md` | v2 전체 실행 규칙 |
| `~/.claude/skills/problem-canvas/SKILL.md` | v1 유지 (하위 호환) |
| [github.com/juree85-netizen/my-prompts](https://github.com/juree85-netizen/my-prompts) | GitHub 원본 레포 (공개) |

### 다운로드

- **GitHub 레포:** [https://github.com/juree85-netizen/my-prompts](https://github.com/juree85-netizen/my-prompts)
- **v2 파일 직접 다운로드:** [business-diagnosis.md](https://raw.githubusercontent.com/juree85-netizen/my-prompts/main/business-diagnosis.md)
- **v1 파일 직접 다운로드:** [problem-canvas.md](https://raw.githubusercontent.com/juree85-netizen/my-prompts/main/problem-canvas.md)

### Claude Code 설치 방법

```bash
# v2 설치 (권장)
mkdir -p ~/.claude/skills/business-diagnosis
curl -o ~/.claude/skills/business-diagnosis/SKILL.md \
  https://raw.githubusercontent.com/juree85-netizen/my-prompts/main/business-diagnosis.md

# v1 설치 (하위 호환)
mkdir -p ~/.claude/skills/problem-canvas
curl -o ~/.claude/skills/problem-canvas/SKILL.md \
  https://raw.githubusercontent.com/juree85-netizen/my-prompts/main/problem-canvas.md
```
