#!/usr/bin/env python3

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'r') as f:
    content = f.read()

# ─────────────────────────────────────────────────────────────
# 1. 대시보드 운영 및 개선 업무 행 확장 + 월간 데이터 반영 및 검증 추가
# ─────────────────────────────────────────────────────────────
OLD_SR = '''    <!-- ===== 대시보드 운영 및 개선 업무 ===== -->
    <tr class="gantt-cat">
      <td>대시보드 운영 및 개선 업무</td>
      <td colspan="2" style="font-size:11px; font-weight:normal;">성능 개선 (SR 완료)</td>
      <td style="text-align:center; font-size:11px; color:#e0ffe0;">완료 (3-4월)</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">S26030007696</td>
      <td style="text-align:center; font-size:11px;">유주리</td>
      <td style="text-align:center; font-size:11px;">염효결</td>
      <td style="text-align:center; font-size:11px;">2026-03-28</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
    </tr>'''

NEW_SR = '''    <!-- ===== 대시보드 운영 및 개선 업무 ===== -->
    <tr>
      <td rowspan="2" style="background-color:#172B4D; color:white; font-weight:bold; text-align:center; vertical-align:middle; font-size:12px; padding:6px 8px;">대시보드 운영 및<br>개선 업무</td>
      <td class="activity-group">성능 개선</td>
      <td class="gantt-sub-item">-</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (3-4월)</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">S26030007696</td>
      <td style="text-align:center; font-size:11px;">유주리</td>
      <td style="text-align:center; font-size:11px;">염효결</td>
      <td style="text-align:center; font-size:11px;">2026-03-28</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
    </tr>
    <tr>
      <td class="activity-group">속도 개선 후<br>화면 수정</td>
      <td class="gantt-sub-item">-</td>
      <td style="text-align:center; font-size:11px; color:#97A0AF;">예정 (6월 1주)</td>
      <td style="font-size:11px;">기존 설계와 달라진 부분 다수 발견 (오른쪽 정렬, 기준 연월 표시, 한 화면 레이아웃 등)</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="font-size:11px;">기존 설계와 달라진 부분 다수 발견 (오른쪽 정렬, 기준 연월 표시, 한 화면 레이아웃 등)</td>
      <td style="font-size:11px;">솔루션전략이 이슈 리스트업 후 메일 공유 예정</td>
    </tr>

    <!-- ===== 월간 데이터 반영 및 검증 ===== -->
    <tr>
      <td style="background-color:#172B4D; color:white; font-weight:bold; text-align:center; vertical-align:middle; font-size:12px; padding:6px 8px;">월간 데이터<br>반영 및 검증</td>
      <td class="activity-group">기준 연월 오류</td>
      <td class="gantt-sub-item">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="font-size:11px;">화면에 4월이 아닌 3월로 표시됨 (4월 실적 미반영)</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="font-size:11px;">화면에 4월이 아닌 3월로 표시됨 (4월 실적 미반영)</td>
      <td style="font-size:11px;">회의 후 즉시 확인</td>
    </tr>'''

assert OLD_SR in content, "OLD_SR not found"
content = content.replace(OLD_SR, NEW_SR)
print("✓ SR 테이블 수정 완료")

# ─────────────────────────────────────────────────────────────
# 2. '26년 추진 업무 전체 일정표 — 문서 앞에 삽입
# ─────────────────────────────────────────────────────────────
E = '<td class="cell-empty"></td>'
E13 = (E * 13)

def item_row(name):
    return f'    <tr>\n      <td style="padding-left:22px; background-color:#FAFBFC; font-size:11px; color:#344563;">{name}</td>\n      {E13}\n    </tr>\n'

def cat_row(name):
    return f'    <tr class="gantt-cat">\n      <td colspan="14" style="padding-left:8px;">{name}</td>\n    </tr>\n'

TH = '<th style="text-align:center; background-color:#0052CC; color:white; white-space:nowrap;">'
TH25 = '<th style="text-align:center; background-color:#344563; color:white; white-space:nowrap;">'

SCHEDULE_TABLE = f'''<h2>□ '26년 추진 업무 전체 일정표</h2>
<table style="font-size:11px; table-layout:fixed; width:100%;">
  <colgroup>
    <col style="width:200px;">
    <col style="width:38px;"><col style="width:38px;"><col style="width:38px;"><col style="width:38px;">
    <col style="width:38px;"><col style="width:38px;"><col style="width:38px;"><col style="width:38px;">
    <col style="width:38px;"><col style="width:38px;"><col style="width:38px;"><col style="width:38px;">
    <col style="width:38px;">
  </colgroup>
  <thead>
    <tr>
      <th rowspan="2" style="text-align:left; padding-left:8px; background-color:#172B4D; color:white;">구분</th>
      {TH25}'25</th>
      <th colspan="12" style="text-align:center; background-color:#0052CC; color:white;">'26</th>
    </tr>
    <tr>
      {TH25}12</th>
      {TH}1</th>{TH}2</th>{TH}3</th>{TH}4</th>{TH}5</th>{TH}6</th>
      {TH}7</th>{TH}8</th>{TH}9</th>{TH}10</th>{TH}11</th>{TH}12</th>
    </tr>
  </thead>
  <tbody>
{cat_row("1. 신규 지표 추가")}{item_row("　[효율/수익] 지표 추가")}{item_row("　[VoC] 지표 추가")}{item_row("　[서비스활성화] 지표 추가")}{item_row("　[시장] 지표 추가")}{item_row("　[영업] 지표 추가")}{item_row("　[파트너] 지표 추가")}{cat_row("2. 신규 상품 추가")}{item_row("　[On-prem] 상품/지표 추가")}{item_row("　[글로벌SaaS] 상품/지표 추가")}{cat_row("3. 사업팀의 대시보드 활용 극대화")}{item_row("　상품별 정기 리뷰 세션")}{item_row("　사업부 회의체 정보 제공")}{cat_row("4. 사업건전성 상태 판단 기준 수립")}{item_row("　성장단계 및 상품특성 정의")}{item_row("　영역별 지표, 기준값 설정")}{item_row("　건전성 상태 정의")}{cat_row("5. 사업건전성 KPI 후보 Pool 제공")}{item_row("　상품별 핵심지표 선정")}{item_row("　시뮬레이션 후 기준값 설정")}{item_row("　후보 Pool 지원팀 제공, 협의")}{cat_row("6. 차세대 시스템 전환")}{item_row("　현황 파악 및 분석")}{item_row("　데이터 연계")}{item_row("　데이터 모델링, 테이블 개발")}  </tbody>
</table>
<p style="font-size:11px; color:#6B778C; margin:4px 0 24px;">※ 1/2번 과제는 대시보드 개발 프로세스에 맞추어 별도의 세부 일정으로 구분/관리함</p>

<hr>

'''

INSERT_BEFORE = '<h2>회의 내용 요약</h2>'
assert INSERT_BEFORE in content, "INSERT_BEFORE not found"
content = content.replace(INSERT_BEFORE, SCHEDULE_TABLE + INSERT_BEFORE)
print("✓ 전체 일정표 삽입 완료")

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'w') as f:
    f.write(content)

print("파일 저장 완료!")
