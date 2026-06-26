---
name: fabrix-ai
description: "사업건전성 대시보드 AI 고도화를 위해 사내 AI 솔루션 FabriX 활용 가능성을 AI Development Group에 문의, 공식 채널 안내받음 (2026-06-16)"
metadata: 
  node_type: memory
  type: project
  originSessionId: 64af459e-c4eb-44a5-ac4f-06b56714b139
---

## 배경
보안 정책상 외부 AI 서비스 연동이 어려워, 사내 AI 솔루션 FabriX를 [[project_business_health_dashboard]] AI 고도화에 활용할 수 있는지 검토 중.

## 추진 예정 과제 (2026-06-16 문의 기준)
1. AI 기반 웹 대시보드 재구축 — Tableau 의존도 제거, AI가 프론트/백엔드/SQL 생성
2. AI 기반 데이터 모델 개선 — ERD·테이블 정의·SQL 쿼리 AI 설계
3. AI 기반 시안 생성 + 데이터 시뮬레이션 — 설계 단계 KPI 정합성 사전 검증
4. 자동 분석 + 인사이트 리포트 메일 푸시 — 지표 변화 자동 감지 및 자동 발송

데이터는 사내 임팔라DB(데이터레이크)에 저장.

## AI Development Group 답변 요지 (하혜란 매니저, hyeran.ha@samsung.com)
- #1,2 (개발단계 AI 활용): FabriX는 코드생성 특화 모델/서비스가 아님 → 사내 코드 어시스턴트 **'AI Pro'** 권장
- #3,4 (운영 Agent 제작): FabriX는 DB 직접 접근 기능 없음 → DB 접근용 MCP를 별도 생성 후 Agent 제작 시 활용, 또는 데이터 파일 업로드 분석 방식. AI 모델만 필요하면 FabriX **LLM OpenAPI** 활용
- 상세 요구사항 협의는 전담 부서/인력 지정이 필요해 공식 채널로 안내 → **fabrix.cs@samsung.com**

## 진행 상태
- 2026-06-16: fabrix.cs@samsung.com 앞 상세 협의 요청 메일 초안 작성 완료 (하혜란 답변 메일을 전달하는 방식 + 새 본문, CC: 하혜란 + 기존 내부 참조자 전체). 발송은 사용자가 직접 진행 예정
- 다음 확인 필요: 메일 발송 완료 여부, fabrix.cs 회신 또는 미팅 결과

**Why:** AI Pro(코드 어시스턴트)와 FabriX(MCP/Agent/LLM OpenAPI)의 역할 구분, 그리고 이 구분의 근거(하혜란 매니저 답변)를 다시 설명하지 않아도 되도록 기록.
**How to apply:** 이후 "AI 활용", "FabriX", "AI Pro" 관련 질문이나 fabrix.cs 회신이 오면 이 메모리를 기준으로 답변하고 진행 상태를 갱신할 것.
</content>
