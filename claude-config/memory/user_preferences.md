---
name: 사용자 작업 시작 트리거 및 호칭
description: 루나라고 부르면 메모리/산출물/스냅샷 전체 현황을 먼저 보여주고 업무 시작
type: feedback
originSessionId: 89362005-0a54-4cb2-a41b-30e0e435a3b7
---
사용자는 나를 **루나**라고 부름.

"루나"라고 호칭하면 → 업무 시작 전에 아래 세 가지를 모두 보여줄 것.

1. **메모리 (프로젝트 컨텍스트)** — memory 폴더의 project_* 파일 목록 + 한줄 설명
2. **산출물 파일** — /home/ubuntu/ 의 html/md/txt/csv/xlsx 파일 목록 + 한줄 설명
3. **git 스냅샷** — `git tag --sort=-version:refname` + `git log --oneline -10`
4. **문서허브 목록 및 주소** — 아래 URL 표를 항상 포함할 것. (nginx: 8090 / node serve: 8080)

   **[와이어프레임 / 기획 문서]**

   | 문서 | URL |
   |------|-----|
   | 메인 허브 | `http://13.49.177.238:8090/` |
   | HTML 문서 목록 | `http://13.49.177.238:8090/html-docs/` |
   | 추진 배경 및 목적 | `http://13.49.177.238:8090/html/dashboard_background_purpose.html` |
   | 효율/수익 와이어프레임 | `http://13.49.177.238:8090/html/efficiency_profit_wireframe.html` |
   | 효율/수익 개발 요청서 | `http://13.49.177.238:8090/html/efficiency_profit_dev_request.html` |
   | VoC 대시보드 와이어프레임 | `http://13.49.177.238:8090/html/voc_dashboard_wireframe.html` |
   | VoC KD 와이어프레임 | `http://13.49.177.238:8090/html/voc_dashboard_kd_wireframe.html` |
   | VoC 개발 요청서 | `http://13.49.177.238:8090/html/voc_dev_request.html` |
   | 재무(시장) 와이어프레임 | `http://13.49.177.238:8090/html/market_wireframe.html` |
   | 영업 메인 와이어프레임 | `http://13.49.177.238:8090/html/sales_main_wireframe.html` |
   | 영업 필터 와이어프레임 | `http://13.49.177.238:8090/html/sales_filter_wireframe.html` |
   | CS 고객 현황 와이어프레임 | `http://13.49.177.238:8090/html/customer_status_wireframe.html` |
   | 지표 정보 페이지 | `http://13.49.177.238:8090/html/indicator_info_wireframe.html` |
   | 사업건전성 상태 와이어프레임 | `http://13.49.177.238:8090/html/biz_health_status_wireframe.html` |
   | 사업 단위 대시보드 와이어프레임 | `http://13.49.177.238:8090/html/bizunit_dashboard_wireframe.html` |
   | 서비스 활성화 지표 | `http://13.49.177.238:8090/html/service_activation_indicators.html` |
   | 보고서 포맷 가이드 | `http://13.49.177.238:8090/html/report_format_guide.html` |

   **[Medallia 분석 보고서]**

   | 문서 | URL |
   |------|-----|
   | Medallia 최종 보고서 (v2.0) | `http://13.49.177.238:8090/html/medallia_report_final.html` |
   | Medallia v2 피드백 반영본 | `http://13.49.177.238:8090/html/medallia_report_v2_feedback.html` |
   | Medallia GPT 분석 (20260514) | `http://13.49.177.238:8090/html/medallia_gpt_analysis_20260514.html` |
   | Medallia 회의 요약 (20260514) | `http://13.49.177.238:8090/html/medallia_meeting_summary_20260514.html` |
   | Medallia 보고서 아웃라인 | `http://13.49.177.238:8090/html/medallia_report_outline.html` |

   **[다운로드 파일 (files/)]**

   | 파일 | URL |
   |------|-----|
   | 효율/수익 개발요청서 xlsx | `http://13.49.177.238:8090/files/efficiency_profit_dev_request.xlsx` |
   | VoC 인터페이스 요청 xlsx | `http://13.49.177.238:8090/files/voc_interface_request.xlsx` |
   | 서비스 활성화 지표 xlsx | `http://13.49.177.238:8090/files/service_activation_indicators.xlsx` |

5. **최근 작업 히스토리** — `/home/ubuntu/work_history.md` 최근 2개 세션 요약 표시

6. **GitHub 저장소** — https://github.com/juree85-netizen/business-health-dashboard

**Why:** 사용자가 작업 맥락(메모리, 산출물, 버전, 문서허브, GitHub, 히스토리)을 한눈에 파악한 뒤 업무를 시작하는 방식을 선호함.

**How to apply:** 대화 첫 마디에 "루나"가 포함되면 위 여섯 섹션을 표 형식으로 보여주고, 이후 요청 내용을 처리할 것.
