---
title: /mental-model — 비즈니스 작동원리 분석 스킬
description: 기업·제품·서비스가 왜 성장했는지(성장 서사)와 어떻게 돌아가는지(수익 구조·경쟁 방어력·성장 동력 3축)를 함께 분석한다. "/mental-model" 명령 또는 "왜 성장했지", "작동 원리", "플라이휠" 등의 요청에 자동 적용.
---

import { Aside } from '@astrojs/starlight/components';

> **성장 서사(왜 성장했는가)와 작동원리 3축(수익·방어력·성장)을 함께 분석한다.**  
> concept-map이 "어디에 있는가"를 설명한다면, mental-model은 "왜 그렇게 되는가"를 설명한다.

**최종 수정:** '26.06.10 &nbsp;|&nbsp; **위치:** `~/.claude/skills/mental-model/` &nbsp;|&nbsp; **레이어:** 02 작동원리 (ANALYZE)

---

## 📥 다운로드 및 설치

| | 링크 |
|--|------|
| **GitHub 레포** | [github.com/juree85-netizen/my-prompts](https://github.com/juree85-netizen/my-prompts) |
| **파일 직접 다운로드** | [mental-model.md](https://raw.githubusercontent.com/juree85-netizen/my-prompts/main/mental-model.md) |

**Claude Code 설치 (터미널 1줄):**

```bash
mkdir -p ~/.claude/skills/mental-model && curl -o ~/.claude/skills/mental-model/SKILL.md https://raw.githubusercontent.com/juree85-netizen/my-prompts/main/mental-model.md
```

---

## 호출 방법

```
/mental-model [기업명 또는 서비스명]
```

슬래시 명령 없이도 아래 표현으로 자동 트리거됩니다.

| 트리거 표현 | 예시 |
|-------------|------|
| 왜 성장했지 | `Coupa가 왜 성장했지?` |
| 작동 원리 | `Salesforce 작동 원리 알려줘` |
| 어떻게 돌아가는지 | `Medallia가 어떻게 돌아가는지 설명해줘` |
| 성장 구조 | `ServiceNow 성장 구조 분석해줘` |
| 플라이휠 | `Amazon의 플라이휠 설명해줘` |
| 비즈니스 메커니즘 | `Workday 비즈니스 메커니즘` |

---

## 출력 흐름

```
Section 0.  개체 유형 + 한 줄 요약
    ↓
Section 1.  성장 서사 — 왜 성장했는가 (인과 체인)
    계기 → 핵심 가설 → 성장 트리거 → 확장 구조 → 현재 위치
    ↓
Section 2.  작동원리 3축
    ① 수익 구조   — 어떻게 돈을 버는가
    ② 경쟁 방어력 — 왜 대체하기 어려운가
    ③ 성장 동력   — 무엇이 계속 성장하게 만드는가
    ↓
Section 3.  자기 강화 루프 (플라이휠)
    루프가 실제 존재하는 경우에만 출력
    ↓
Section 4.  한계와 리스크
    구조적 리스크 4가지 유형 (시장·경쟁·실행·규제)
    ↓
Section 5.  비유
    일상 언어로 한 문장
```

---


<Aside type="caution">
**재진입 조건** — 03 진단(business-diagnosis)에서 문제의 근원이 수익구조 또는 성장 메커니즘에 있다고 판단되면, mental-model로 돌아와 3축 분석을 보완한다.
</Aside>

## 기획자의 사고 레이어에서의 위치

| 레이어 | 목적 | 스킬 |
|--------|------|------|
| 01 이해 | 이게 뭐야, 어디에 있어? | /concept-map |
| **02 작동원리** | **왜 이렇게 움직여?** | **/mental-model** |
| 03 진단 | 어디가 문제야? | /business-diagnosis |
| 04 설계 | 뭘 해야 해? | /strategy-canvas |
| 05 메시지 | 한 문장으로? | /brand-house |

concept-map 이후, business-diagnosis 이전에 사용하면 가장 효과적입니다.  
**대상의 지형을 파악한 뒤 → 작동 원리를 이해하고 → 문제를 진단**하는 순서.

---

## 3축 상세

### ① 수익 구조
어떻게 돈을 버는가. 수익원·가격 구조·반복성을 분석.

### ② 경쟁 방어력 (Moat)
왜 대체하기 어려운가. 데이터 자산·네트워크 효과·전환 비용·브랜드·규모의 경제 5가지 기준으로 평가.

### ③ 성장 동력
무엇이 계속 성장하게 만드는가. PLG·엔터프라이즈 영업·파트너 생태계·M&A·신규 시장 등 엔진 유형과 다음 레버 분석.

---

## 스킬 파일 구성

| 파일 | 설명 |
|------|------|
| `~/.claude/skills/mental-model/SKILL.md` | 실행 원칙 + 출력 구조 정의 |
| [github.com/juree85-netizen/my-prompts](https://github.com/juree85-netizen/my-prompts) | GitHub 원본 레포 (공개) |
