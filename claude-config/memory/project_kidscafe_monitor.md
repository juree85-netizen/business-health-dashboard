---
name: project_kidscafe_monitor
description: 서울형키즈카페 주말 빈자리 알림 시스템 — 9개구/연나이 2세/오전 제외 조건으로 하루 3회 이메일 발송
metadata: 
  node_type: memory
  type: project
  originSessionId: 8b641f79-faf0-47e8-910c-bade19ca65b5
  modified: 2026-08-05T09:17:24.248Z
---

2026-08-05, 서울형키즈카페(우리동네키움포털 umppa.seoul.go.kr) 주말 빈자리를 자동으로 이메일 알림받는 시스템을 구축함.

## 조건
- 대상 자치구(9개): 강남/광진/도봉/서초/성북/송파/종로/중/중랑구
- 대상 연령: 연나이 2세 (사이트 q_useAge 필터 기준)
- 대상 요일: 토/일만
- 제외: 오전 회차 (1회차, 보통 09:30~11:30 또는 09:40~11:40)
- 알림 채널: 이메일 (juree85@gmail.com)
- 확인 주기: 하루 3회 — KST 08:00/13:00/19:00 (cron은 UTC 23:00/04:00/10:00로 등록, 서버 시간대가 UTC라서 +9h 보정 필요)
- 알림 내용: 매 확인 시점의 "현재 전체 빈자리 리스트"를 통짜로 발송 (변동분만 알리는 방식이 아님)

## 기술 구조
- 시설 목록: `GET umppa.seoul.go.kr/icare/user/kidsCafe/BD_selectKidsCafeList.do?q_atdrcCode=<구코드>&q_useAge=2` — 로그인 없이 HTML에서 시설명/fcltyId/이용연령/주소 파싱 (BeautifulSoup)
- 회차별 잔여석: `POST umppa.seoul.go.kr/icare/user/kidsCafeResve/ND_selectResveTmeList.do` body `q_fcltyId&q_resveDe(YYYY-MM-DD)&q_dayNo=1` — 로그인 없이 JSON으로 회차별 정원(usePsncpa)/예약인원(resveNmpr) 반환. 잔여 = usePsncpa - resveNmpr
- 예약 자체(신청)는 로그인 필요하지만, 조회는 로그인 불필요 — 이 시스템은 조회/알림까지만 하고 실제 예약은 사용자가 직접 함

## 인프라
- 스크립트: `/home/ubuntu/kidscafe_monitor/monitor.py` (Python 3, requests+bs4, dotenv 없이 자체 .env 파서 — [[project_business_health_dashboard]]와 무관한 별도 개인용 프로젝트)
- Gmail SMTP 발신 계정은 부동산 모니터링(호피, `/home/ubuntu/realestate_monitor`)과 동일한 juree85@gmail.com 앱 비밀번호를 재사용
- cron: `/etc/crontab` 아님, `crontab -l`로 등록 (실행 유저 crontab)
- private GitHub repo: `juree85-netizen/kidscafe-monitor` (gh CLI 없어서 GitHub REST API로 직접 repo 생성 후 토큰 임베디드 https remote로 push)
- `/home/ubuntu/.gitignore`에 `kidscafe_monitor/` 추가함 — public 대시보드 저장소에 개인 정보/자격증명 노출 방지 원칙([[feedback_public_repo_data_separation]]) 그대로 적용

## 알려진 한계 / 확인 필요 사항
- 예약 오픈 주기가 "매주 화요일" 순차 개시라서, 실제로 열려있는 주말은 보통 1~2주 앞까지만 존재함 (그 이상 날짜는 API가 빈 배열 반환 → 자동으로 무시됨, 별도 처리 불필요)
- 일부 시설은 이용연령 범위(예: 0~6세)와 별개로 "돌봄서비스"(보호자 미동반) 항목에 한해 36개월 이상만 가능하다는 개별 공지가 있음 — 보호자 동반 이용에는 영향 없음, 별도 필터링 안 함
- "예약 신청" 링크가 외부 사이트(예: 공예마을점 → craftmuseum.seoul.go.kr)로 연결되는 시설은 이 시스템의 API로 조회 불가하여 자동 제외됨
