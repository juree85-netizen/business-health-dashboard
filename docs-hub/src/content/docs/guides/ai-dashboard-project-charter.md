---
title: AI 대시보드 검증 프로젝트 구조서
description: 검증 가설·현황·목표·환경 제약·팀 구성·사전 작업·AI 도구 역할 분담을 8개 섹션으로 정리한 프로젝트 기준 문서 (v1.1)
---

**작성일:** 2026-06-30 (v1.1)  
**담당:** 솔루션사업부 기획팀  
**데드라인:** 2026년 10월  
**상태:** 진행 중

---

## 문서 열기

<p>
  <a href="/ai_dashboard_project_charter.html" target="_blank" rel="noopener"
    style="display:inline-block;padding:0.6em 1.4em;background:#0f3460;color:#fff;border-radius:6px;font-weight:600;text-decoration:none;">
    📋 프로젝트 구조서 열기 ↗
  </a>
</p>

---

## 검증 가설

> 웹디자이너·Tableau 개발자·DB 전문가 없이, **AI만으로** 사업건전성 대시보드를 구축·운영·유지보수할 수 있는가?

---

## 8개 섹션 구성

| # | 섹션 | 내용 |
|---|------|------|
| — | **검증 가설** | 프로젝트 전체를 관통하는 핵심 질문 |
| 1 | 현황 | Tableau + Impala DB 운영 현황 및 문제 |
| 2 | 목표 | AS-IS(Tableau) → TO-BE(Web/WAS+AI) 구조 변화 |
| 3 | 검증 방식 | Windows PC 활용 검증 + 핵심 질문 3가지 |
| 4 | 환경 제약 | **AI 도구 역할 분담** (AIPro/FabriX ↔ Claude Enterprise) + 보안 제약 |
| 5 | 팀 구성 | 3인 + 미결 환경 설정 항목 |
| 6 | 사전 작업 | 완료된 것 6가지 (계획·DB·와이어프레임·지표·기술검토서·문서허브) |
| 7 | 검토 필요 | 아직 결정 안 된 것 5가지 |
| 8 | 전환 조건 | 검증 성공 → 실제 프로젝트 전환 기준 + 데드라인 |

---

## AI 도구 역할 분담 (핵심)

| 환경 | 도구 | 역할 |
|------|------|------|
| 사내 보안망 (Windows PC) | **AIPro / FabriX** | SQL 생성·검증, 데이터 모델 설계, KPI 산출 로직 확인 |
| 외부망 (개인PC / 외부 서버) | **Claude Enterprise** | 웹 대시보드 개발, 와이어프레임, 기획 문서, 인사이트 리포트 |

보안 경계 = AI 도구 경계. 두 도구는 대체재가 아니라 역할 분리 설계.
