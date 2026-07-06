---
title: AIPro / FabriX 활용 과제 기술 검토서
description: 사업건전성 대시보드 AI 고도화 — 4개 과제별 추진 배경·기술 문제 정리 (개발자 미팅 전 검토용)
---

**작성일:** 2026-06-15  
**담당:** 솔루션사업부 기획팀  
**상태:** 검토 중 (개발자 미팅 전)

---

## 문서 열기

<p>
  <a href="../../html/aipro_tasks_tech_review.html" target="_blank" rel="noopener"
    style="display:inline-block;padding:0.6em 1.4em;background:#0f3460;color:#fff;border-radius:6px;font-weight:600;text-decoration:none;">
    📋 AIPro / FabriX 기술 검토서 열기 ↗
  </a>
</p>

---

## 문서 목적

AIPro / FabriX를 활용하여 사업건전성 대시보드를 고도화하는 4개 과제 각각에 대해, 개발자 미팅 전에 확인해야 할 기술적 문제를 정리한 자료입니다.

---

## 4개 과제 요약

| 과제 | 내용 | 핵심 기술 문제 |
|------|------|----------------|
| **Task 01** | AI 기반 웹 대시보드 재구축 | 코드 실행 환경 · 맥락 유지 · DB 접속 |
| **Task 02** | AI 기반 데이터 모델 개선 | 원천 데이터 주입 · 비즈니스 로직 정밀도 · ERD 출력 |
| **Task 03** | AI 시안 생성 + 데이터 시뮬레이션 | HTML 렌더링 · 계산 실행 · 정합성 검출 |
| **Task 04** | 자동 분석 + 인사이트 리포트 메일 푸시 | DB 직접 읽기 vs 대시보드 읽기 · 스케줄링 · 메일 연동 |

---

## 공통 확인 사항 (미팅 우선순위)

1. AIPro / FabriX에서 사내 DB 직접 접속 가능 여부
2. 과제 4 데이터 수집 방식 — DB 직접 읽기(권장) vs 대시보드 읽기
3. AIPro / FabriX 코드 실행 환경 범위 (프론트/백엔드/SQL)
4. AIPro / FabriX 스케줄 자동 실행 지원 여부
5. AIPro / FabriX와 사내 메일 시스템 연동 가능 여부
