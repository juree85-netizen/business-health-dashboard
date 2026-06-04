---
title: /corp-report — 기업조사 분석 보고서 스킬
description: 기업명을 입력하면 HTML 형식의 기업조사 분석 보고서를 자동 작성·문서허브 업로드하는 스킬
---

> 기업명(+ 선택: 대상 국가)을 입력하면 Boeing India 보고서 구조 기반의 기업조사 HTML 보고서를 자동 생성하고 문서허브에 업로드합니다.  
> 원문 자료를 함께 붙여넣으면 그것을 1차 소스로 사용하고, 없으면 웹 검색으로 보완합니다.

**등록일:** '26.06.04 &nbsp; | &nbsp; **위치:** `~/.claude/skills/corp-report/`

---

## 호출 방법

```
/corp-report [기업명]
/corp-report [기업명] [대상 국가/시장]
```

**예시:**
```
/corp-report Thoma Bravo
/corp-report Boeing India
/corp-report SAP Korea
/corp-report Salesforce
```

**원문 자료 함께 제공 시:**
```
/corp-report Boeing India

1. 인도 항공 산업
시장 규모는 '26년 $16.5B → '31년 $29.0B ...
```

---

## 출력물

| 항목 | 내용 |
|------|------|
| 파일 형식 | HTML (doc-page A4 레이아웃, Medallia/Coupa 보고서 동일 스타일) |
| 저장 위치 | `/home/ubuntu/[기업명]_report.html` |
| 문서허브 URL | `http://13.49.177.238:8090/html/[파일명].html` |
| git | 자동 커밋 + GitHub push |

---

## 보고서 구조 (Boeing India 목차 기반)

| 섹션 | 포함 조건 |
|------|----------|
| 1. 산업/시장 현황 | 항상 포함 |
| 2. 글로벌 본사 기업 개요 | 항상 포함 (설립·CEO·임직원·매출·사업영역) |
| 2. 사업 실적 표 | 5~10년 재무 추이 (데이터 있을 때) |
| 3. 현지 법인 현황 | 대상 국가 지정 시 추가 |
| 4. 시장 내 협력/전략 현황 | 현지 활동 있을 때 |
| 5. 조직 관계·의사결정 구도 | 데이터 있을 때 |
| 6. 삼성-[기업] 협업 이력 | 협업 이력 있을 때 |
| 별첨 1. 해외 법인 현황 | 분량 클 때 |
| 별첨 2. 주요 임원 프로필 | 임원 데이터 있을 때 |

---

## 스킬 파일 구성

| 파일 | 설명 |
|------|------|
| `SKILL.md` | 5단계 실행 흐름 정의 |
| `references/html-template.md` | CSS + 섹션별 HTML 구조 템플릿 |

---

## 작성된 보고서 목록

| 기업 | 작성일 | 링크 |
|------|--------|------|
| Thoma Bravo | '26.06.04 | [열기](/thoma_bravo_report.html){target="_blank"} |
