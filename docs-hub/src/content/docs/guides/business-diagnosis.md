---
title: /business-diagnosis — BMC × 맥킨지 7단계 사업 진단 스킬 (v2)
description: BMC로 Root Cause Block을 특정하고, 문제 유형 분류 후 맥킨지 7단계로 Issue Tree → Priority Score → Elevator Pitch를 도출한다. "/business-diagnosis" 또는 "/problem-canvas" 명령, "사업 문제", "비즈니스 진단" 등에 자동 적용.
---

> **BMC는 문제 위치를 찾는 도구, 맥킨지 7단계는 원인 제거 및 실행 우선순위 설계 도구.**  
> BMC 진단 결과(Root Cause Block)는 반드시 McKinsey Step 2(Issue Tree)의 최상위 노드로 연결됩니다.

**등록일:** '26.06.09 &nbsp;|&nbsp; **위치:** `~/.claude/skills/business-diagnosis/` &nbsp;|&nbsp; **이전 이름:** `problem-canvas`

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
| 7 | 핵심 연결 규칙 | BMC → Root Cause → Issue Tree 최상위 노드 의무 연결 |

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

## BMC Root Cause 진단 규칙

**결과(Symptom)와 원인(Cause)을 구분한다.**

| 증상 | ❌ 잘못된 판단 | ✅ 올바른 Root Cause Block |
|------|-------------|--------------------------|
| 매출 감소 | R$ | VP / CH / CR 우선 검토 |
| 고객 이탈 증가 | CR | VP(가치 부족) 또는 CH(접점 문제) |
| 신규 고객 확보 실패 | CS | CH(채널 부재) 또는 VP(소구력 약화) |
| 원가 상승 | — | C$ (직접 원인) |
| 파트너 이탈 | KP | VP(파트너 가치 부족) 또는 R$(배분 구조) |

---

## 문제 유형 분류

| 유형 | 대표 증상 |
|------|-----------|
| **Growth** | 매출 정체, 신규 고객 확보 실패, 점유율 하락 |
| **Profitability** | 매출 증가에도 이익 감소, 원가율 상승 |
| **Operation** | 프로세스 병목, 납기 지연, 품질 저하 |
| **Organization** | 핵심인력 이탈, 사일로, 의사결정 지연 |
| **Strategy** | 시장 변화 대응 실패, 경쟁 우위 소멸 |

문제 유형이 결정되면 해당 유형의 **Issue Tree 템플릿**이 Step 2에 자동 적용됩니다.

---

## 우선순위 계산식

```
Priority Score = Impact × Feasibility

Impact    1~5점 (사업 전체에 미치는 영향)
Feasibility 1~5점 (현실적 해결 가능성)
만점      25점
```

---

## 출력 흐름

```
Step 0.  문제 유형 분류 (Growth / Profitability / ...)
    ↓
Phase 1. BMC Root Cause Block 특정
    ↓      (결과 블록 아닌 원인 블록)
         Root Cause Block → Issue Tree 최상위 노드로 연결
    ↓
Step 1.  문제 정의 (SMART)
Step 2.  Issue Tree (유형별 템플릿 기반, 최상위 노드 = Root Cause)
Step 3.  우선순위 (Impact × Feasibility, 25점 만점)
Step 4.  분석 계획
Step 5.  핵심 발견사항
Step 6.  So What? (1문장, 20~40자)
Step 7.  권고안 + Elevator Pitch (4문장)
```

---

## 스킬 파일 구성

| 파일 | 설명 |
|------|------|
| `~/.claude/skills/business-diagnosis/SKILL.md` | v2 전체 실행 규칙 |
| `~/.claude/skills/problem-canvas/SKILL.md` | v1 유지 (하위 호환) |
| `github.com/juree85-netizen/my-prompts` | Custom GPT용 원본 |
