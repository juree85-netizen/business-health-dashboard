---
title: /brand-house — 브랜드·포지셔닝 메시지 설계 스킬
description: 기업·제품·아이디어를 단 한 문장으로 정의한다. Brand House 구조(Essence→Promise→RTBs→Values)로 누구에게 무엇을 약속하는지 정리하고, 30초 Elevator Pitch까지 출력. 5레이어 중 05 메시지 레이어 담당.
---

import { Aside } from '@astrojs/starlight/components';

> **strategy-canvas가 "무엇을 할지"를 결정했다면, brand-house는 "그것을 어떻게 말할지"를 설계한다.**  
> Brand Essence(한 줄) → Target → Promise → RTBs → Values → Elevator Pitch.

**최종 수정:** '26.06.10 &nbsp;|&nbsp; **위치:** `~/.claude/skills/brand-house/` &nbsp;|&nbsp; **레이어:** 05 메시지 (COMMUNICATE)

---

## 📥 다운로드 및 설치

| | 링크 |
|--|------|
| **GitHub 레포** | [github.com/juree85-netizen/my-prompts](https://github.com/juree85-netizen/my-prompts) |
| **파일 직접 다운로드** | [brand-house.md](https://raw.githubusercontent.com/juree85-netizen/my-prompts/main/brand-house.md) |

**Claude Code 설치 (터미널 1줄):**

```bash
mkdir -p ~/.claude/skills/brand-house && curl -o ~/.claude/skills/brand-house/SKILL.md https://raw.githubusercontent.com/juree85-netizen/my-prompts/main/brand-house.md
```

---

## 호출 방법

```
/brand-house [기업·제품·아이디어·서비스]
```

| 트리거 표현 | 예시 |
|-------------|------|
| 한 문장으로 정리해줘 | `Coupa를 한 문장으로 정리해줘` |
| 포지셔닝 | `우리 서비스 포지셔닝 잡아줘` |
| 핵심 메시지 | `이 제품의 핵심 메시지가 뭐야?` |
| 어떻게 설명할까 | `Medallia를 임원한테 어떻게 설명할까?` |
| 브랜드 정의 | `AI 스킬 프레임워크 브랜드 정의 해줘` |

---

## Brand House 구조

```
┌─────────────────────────────────────────────────────┐
│                  Brand Essence (지붕)                │
│        차별점 + 가치가 담긴 단 한 줄                 │
└──────────────────────┬──────────────────────────────┘
                       │
        ┌──────────────┴──────────────┐
        │       Brand Promise (기둥)   │
        │  기능적 약속 | 감성적 약속   │
        └──────────────┬──────────────┘
                       │
        ┌──────────────┴──────────────┐
        │    RTBs + Values (기반)      │
        │  믿어야 할 이유 + 말투/가치  │
        └─────────────────────────────┘
```

---

## 출력 흐름

```
Section 0.  Brand Essence (지붕 — 핵심 한 줄, 20~35자)
    ↓
Section 1.  Target — 누구에게
    핵심 대상 / Pain / 원하는 것 / 지금 대안
    ↓
Section 2.  Brand Promise — 무엇을 약속하는가
    기능적 약속 | 감성적 약속 | 경쟁 대비 차별점
    ↓
Section 3.  RTBs — Reasons to Believe
    약속을 뒷받침하는 팩트·수치·사례
    ↓
Section 4.  Brand Values & Tone — 어떻게 말하는가
    핵심 가치 / 말투 / 쓰는 표현 / 쓰지 않는 표현
    ↓
Section 5.  Positioning Statement + Elevator Pitch (30초)
```

---

## Brand Essence 작성 기준

| 기준 | 설명 |
|------|------|
| 20~35자 | 너무 길면 기억에 남지 않는다 |
| 차별점 포함 | 경쟁자와 바꿔 써도 말이 되면 실패 |
| 가치 포함 | "무엇을 한다"가 아니라 "고객에게 무엇을 가능하게 한다" |
| 설명 불필요 | 읽는 순간 이해되어야 한다 |

---

## 기획자의 사고 레이어에서의 위치

| 레이어 | 목적 | 스킬 |
|--------|------|------|
| 01 이해 | 이게 뭐야? | /concept-map |
| 02 작동원리 | 왜 이렇게 움직여? | /mental-model |
| 03 진단 | 어디가 문제야? | /business-diagnosis |
| 04 설계 | 그래서 뭘 해야 해? | /strategy-canvas |
| **05 메시지** | **한 문장으로?** | **/brand-house** |

<Aside type="tip">
**/strategy-canvas → /brand-house** 순서가 가장 자연스럽습니다.  
전략이 결정된 뒤, 그것을 설득력 있게 한 문장으로 만드는 것이 brand-house의 역할입니다.
</Aside>

---

## 스킬 파일 구성

| 파일 | 설명 |
|------|------|
| `~/.claude/skills/brand-house/SKILL.md` | 실행 원칙 + 출력 구조 정의 |
| [github.com/juree85-netizen/my-prompts](https://github.com/juree85-netizen/my-prompts) | GitHub 원본 레포 (공개) |
