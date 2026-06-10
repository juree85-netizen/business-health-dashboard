---
title: /strategy-canvas — 전략 선택지 설계 스킬
description: 문제 정의 이후 "그래서 무엇을 해야 하는가"를 답한다. 현재 상태 → 전략 선택지(MECE) → Trade-off → 권고 전략 → 실행 로드맵 순서로 출력. business-diagnosis 이후 사용하면 가장 강력.
---

import { Aside } from '@astrojs/starlight/components';

> **문제를 알았다면 다음 질문은 "그래서 뭘 해야 하지?"**  
> /strategy-canvas는 선택지를 만들고, 버릴 것을 결정하고, 권고 전략과 실행 로드맵까지 도출한다.

**최종 수정:** '26.06.10 &nbsp;|&nbsp; **위치:** `~/.claude/skills/strategy-canvas/` &nbsp;|&nbsp; **레이어:** 05 전략 (RECOMMEND)

---

## 📥 다운로드 및 설치

| | 링크 |
|--|------|
| **GitHub 레포** | [github.com/juree85-netizen/my-prompts](https://github.com/juree85-netizen/my-prompts) |
| **파일 직접 다운로드** | [strategy-canvas.md](https://raw.githubusercontent.com/juree85-netizen/my-prompts/main/strategy-canvas.md) |

**Claude Code 설치 (터미널 1줄):**

```bash
mkdir -p ~/.claude/skills/strategy-canvas && curl -o ~/.claude/skills/strategy-canvas/SKILL.md https://raw.githubusercontent.com/juree85-netizen/my-prompts/main/strategy-canvas.md
```

---

## 호출 방법

```
/strategy-canvas [대상 또는 전략 질문]
```

| 트리거 표현 | 예시 |
|-------------|------|
| 그래서 어떻게 해야 해 | `Rossum은 이제 어떻게 해야 해?` |
| 전략적 선택지 | `Coupa의 전략적 선택지를 정리해줘` |
| 어떤 방향으로 가야 해 | `파트너 사업부가 어떤 방향으로 가야 할지` |
| 전략 수립 | `신규 시장 진입 전략 수립해줘` |

---

## 출력 흐름

```
Section 0.  전략 질문 + 맥락 (제약 조건 포함)
    ↓
Section 1.  현재 상태 (As-Is)
    핵심 현황 / 가장 큰 제약 / 의사결정 기준 / 아무것도 안 하면?
    ↓
Section 2.  전략 선택지 (2~4개, MECE)
    각 선택지: 핵심 방향 / 핵심 가정 / 리소스 / 임팩트 / 버리는 것
    ↓
Section 3.  Trade-off 매트릭스
    임팩트 / 실행 가능성 / 리스크 / 소요 시간
    ↓
Section 4.  권고 전략
    선택 + 이유 + 버린 것 이유 + 핵심 전제 조건
    ↓
Section 5.  실행 로드맵
    즉시 / 단기(1~3개월) / 중기(3~6개월) / 전략적 베팅(6개월+)
    ↓
Section 6.  4P 전략
    Product / Price / Place / Promotion — As-Is → To-Be + 핵심 레버
    ↓
Section 7.  GTM (Go-to-Market) 전략
    타겟 세그먼트 / 가치 제안 / 진입 채널 / 초기 트랙션 / Land→Expand→Scale
```

---

## Section 6 — 4P 전략

권고 전략을 실행하기 위한 마케팅 믹스를 정의한다.

| 4P | 현재 (As-Is) | 전략 방향 (To-Be) | 핵심 결정 |
|----|------------|-----------------|---------|
| **Product** (제품·서비스) | [현재 무엇을 제공하는가] | [무엇을 바꾸거나 추가하는가] | [핵심 변화 한 줄] |
| **Price** (가격·수익 모델) | [현재 가격 구조] | [어떤 모델로 전환하는가] | [핵심 변화 한 줄] |
| **Place** (채널·유통) | [현재 접점] | [어느 채널을 강화·신규 개척하는가] | [핵심 변화 한 줄] |
| **Promotion** (마케팅·홍보) | [현재 커뮤니케이션] | [어떤 메시지·채널로 전달하는가] | [핵심 변화 한 줄] |

> **4P 핵심 레버:** 권고 전략에서 가장 크게 움직여야 하는 P가 무엇인지, 그 이유를 명시한다.

---

## Section 7 — GTM (Go-to-Market) 전략

시장 진입 또는 재진입 경로를 설계한다.

| 항목 | 내용 |
|------|------|
| **타겟 세그먼트** | [누구에게 먼저 — 기업 규모 / 산업 / 직무 / 지역] |
| **핵심 가치 제안** | [왜 이 고객에게 선택받는가 — 경쟁 대비 차별점] |
| **진입 채널** | [어떤 경로로 도달하는가 — 직접영업 / 파트너 / 인바운드 등] |
| **초기 트랙션 목표** | [첫 3개월 내 만들어야 할 지표 — 계약 수 / MQL / ARR 등] |
| **파트너·에코시스템** | [함께 움직일 플레이어 — SI / ISV / 채널파트너 등] |
| **킬러 레퍼런스** | [첫 번째로 잡아야 할 고객 유형 — 레퍼런스가 되는 이유] |

**GTM 단계별 모션:**

| 단계 | 타겟 | 메시지 | 채널 | 목표 지표 |
|------|------|--------|------|---------|
| **1단계 — 랜드** | [첫 진입 세그먼트] | [핵심 메시지] | [채널] | [지표] |
| **2단계 — 익스팬드** | [확장 세그먼트] | [메시지 변화] | [채널] | [지표] |
| **3단계 — 스케일** | [전체 시장] | [브랜드 메시지] | [채널] | [지표] |

> **GTM 핵심 베팅:** 이 GTM이 성공하려면 무엇이 맞아야 하는가 — 검증해야 할 핵심 가정을 명시한다.

---

<Aside type="caution">
**재진입 조건** — 02 포지셔닝(brand-house)에서 핵심 포지셔닝이 설득력을 잃는다면, 전략 선택 자체가 흔들리고 있다는 신호다. strategy-canvas로 돌아와 권고 전략의 전제 조건을 재검토한다.
</Aside>

## 기획자의 사고 레이어에서의 위치

| 레이어 | 목적 | 스킬 |
|--------|------|------|
| 01 이해 | 이게 뭐야? | /concept-map |
| 02 포지셔닝 | 이 기업의 포지셔닝은? | /brand-house |
| 03 비즈니스 성장 및 작동원리 | 왜 이렇게 움직여? | /mental-model |
| 04 비즈니스 진단 | 어디가 문제야? | /business-diagnosis |
| **05 전략** | **그래서 뭘 해야 해?** | **/strategy-canvas** |

<Aside type="tip">
**/business-diagnosis → /strategy-canvas** 순서로 사용하면 가장 효과적입니다.  
business-diagnosis가 Root Cause Block과 우선순위를 확정하면, strategy-canvas는 그것을 전략 선택지로 전환합니다.
</Aside>

---

## 스킬 파일 구성

| 파일 | 설명 |
|------|------|
| `~/.claude/skills/strategy-canvas/SKILL.md` | 실행 원칙 + 출력 구조 정의 |
| [github.com/juree85-netizen/my-prompts](https://github.com/juree85-netizen/my-prompts) | GitHub 원본 레포 (공개) |
