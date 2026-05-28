---
title: sds-word-writer 스킬 가이드
description: Samsung SDS 임원 보고서 스타일로 Word(.docx) 문서를 자동 생성하는 Python 기반 스킬
---

> Samsung SDS 사내 보고서 스타일로 JSON 콘텐츠를 Word(.docx) 문서로 변환하는 Python 기반 스킬입니다.  
> 루나(Claude Code)가 Word 변환 요청 시 이 스킬의 생성 엔진과 서식 규칙을 자동 적용합니다.

**설치일:** '26.05.21 &nbsp; | &nbsp; **출처:** [GitHub — bennhee4sds-sudo/shared](https://github.com/bennhee4sds-sudo/shared/tree/main/Skills/sds-word-writer)

---

## 파일 구성

| 경로 | 설명 |
|------|------|
| `skills/sds-word-writer/SKILL.md` | 스킬 개요 및 사용 가이드 |
| `skills/sds-word-writer/scripts/generate.py` | Word 생성 엔진 (1,792줄) |
| `skills/sds-word-writer/references/tone.md` | SDS 임원 보고서 문체 규칙 |
| `skills/sds-word-writer/references/content-schema.md` | JSON 콘텐츠 스키마 |
| `skills/sds-word-writer/references/report-archetypes.md` | 8가지 보고서 유형 팔레트 |
| `skills/sds-word-writer/requirements.txt` | 의존성 (`python-docx==1.2.0`) |

---

## 주요 기능

- **SDS 서식 자동 적용** — 바탕체, 장체 95%, 14pt 본문, 9pt 파란 주석 텍스트박스
- **불릿 계층 지원** — `□ → - → ·` 고정 순서, 로마자·숫자 상위 계층 선택
- **표 자동 정렬** — 금액·수치 우측, 비교 숫자 가운데, 텍스트 좌측 자동 판정
- **병합 셀 표** — `colspan` / `rowspan` 지원
- **이미지 삽입** — PNG/JPEG 헤더 직접 읽어 종횡비 보존
- **주석(Annotation)** — 앵커 단어 아래 파란 9pt 텍스트박스 자동 배치
- **이상 표** — `- 이  상 -` 자동 삽입 (본문·별첨 각각)
- **페이지 번호** — `- N -` 형식 바닥글 자동 생성

---

## 사용법

```bash
python skills/sds-word-writer/scripts/generate.py <content.json> <output.docx>
```

### content.json 기본 구조

```json
{
  "title": "문서 제목",
  "date": "'26. 5. 21 (木)",
  "sections": [
    {
      "heading": "섹션 제목",
      "bullets": [
        { "kind": "dash", "text": "본문 내용" },
        { "kind": "dot",  "text": "세부 내용" }
      ]
    }
  ],
  "appendices": []
}
```

---

## 문체 핵심 규칙 요약

| 항목 | 규칙 |
|------|------|
| **문장 끝** | 명사형·압축형 (`~함`, `~됨`, `~예정`) — `-습니다` 금지 |
| **줄 길이** | 30~55자 목표, 초과 시 6칸 들여쓰기로 연장 |
| **한자** | 단일 문자 화이트리스트만 (`高·中·低`, `年·月·週`, `社`, `有·無`) |
| **주석** | ① 맥락 보강 / ② 약어 풀이 / ③ 출처 인용 (우선순위 순) |
| **메타 문장** | "본 보고서는~", "검토 범위" 섹션 등 자기 참조 콘텐츠 금지 |

---

## 보고서 유형 (8가지)

| 유형 | 적용 상황 |
|------|-----------|
| A. 기업/인물 개요 | 회사·인물 소개 |
| B. 이벤트·인터뷰 요약 | 키노트, 컨퍼런스, 인터뷰 |
| C. 시장·산업 분석 | 시장 규모·성장률·전망 |
| D. 제품·기술 비교 | 기술 소개, 경쟁 제품 비교 |
| E. SDS 제언·대응 전략 | 위기 대응, 전략 방향 |
| F. 주간업무보고 | 진행 상태, 현안 보고 |
| G. 업무계획·추진방향 | 연간 계획, CEO 보고 |
| H. 현안·이슈 보고 | 프로젝트 이슈, 진행 경과 |
