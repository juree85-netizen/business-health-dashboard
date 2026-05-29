#!/usr/bin/env python3

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'r') as f:
    content = f.read()

start_marker = '<p style="font-size:13px; font-weight:bold; color:#172B4D; margin:32px 0 6px;">업무 구분별 SR 진행현황</p>'
end_marker = '\n\n<hr>\n\n<h3>4. 6월 개발 지연 예고</h3>'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

assert start_idx != -1, "start marker not found"
assert end_idx != -1, "end marker not found"

new_section = '''<p style="font-size:13px; font-weight:bold; color:#172B4D; margin:32px 0 6px;">업무 구분별 SR 진행현황</p>
<table style="font-size:12px;">
  <thead>
    <tr>
      <th style="text-align:center; width:85px;">구분</th>
      <th style="text-align:center; width:100px;">업무 구분</th>
      <th style="text-align:left; width:145px; padding-left:8px;">세부 업무</th>
      <th style="width:95px;">진행 일정</th>
      <th style="width:120px;">업무 현황</th>
      <th style="width:88px;">SR No.</th>
      <th style="width:50px;">SR<br>요청자</th>
      <th style="width:68px;">SR 처리<br>담당자</th>
      <th style="width:85px;">SR 완료<br>요청일</th>
      <th>이슈</th>
      <th style="width:115px;">비고</th>
    </tr>
  </thead>
  <tbody>

    <!-- ===== 재무·효율/수익 ===== -->
    <tr>
      <td rowspan="9" class="sr-group">재무<br>효율/수익</td>
      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>
      <td class="gantt-sub-item">지표 수립</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1-3월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 산출식 정의</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1-3월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 계획</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1-3월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 디자인</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1-3월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td rowspan="5" class="activity-group">데이터 연계 및<br>화면 개발</td>
      <td class="gantt-sub-item">데이터 분석 및 연계</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1-2월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 기술정의서</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (2-3월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 모델링, 테이블 개발</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="font-size:11px;">진행 현황 미파악</td>
      <td style="text-align:center; font-size:11px;">S26040005889</td>
      <td style="text-align:center; font-size:11px;">유주리</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">2026-04-23</td>
      <td style="font-size:11px;">진행 현황 미파악</td>
      <td style="font-size:11px;">담당자 확인 후 공유</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">Tableau 화면 개발</td>
      <td style="text-align:center; font-size:11px; color:#FF8B00;">진행 중 (4-5월)</td>
      <td style="font-size:11px;">진행 현황 미파악</td>
      <td style="text-align:center; font-size:11px;">S26040005889</td>
      <td style="text-align:center; font-size:11px;">유주리</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">2026-04-23</td>
      <td style="font-size:11px;">진행 현황 미파악</td>
      <td style="font-size:11px;">담당자 확인 후 공유</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 정합성 검증</td>
      <td style="text-align:center; font-size:11px; color:#97A0AF;">예정 (5-6월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td style="font-size:11px;">5-6월 진행 예정</td>
    </tr>

    <!-- ===== 고객/상품·VoC ===== -->
    <tr>
      <td rowspan="9" class="sr-group">고객/상품<br>VoC</td>
      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>
      <td class="gantt-sub-item">지표 수립</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1-3월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 산출식 정의</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1-3월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 계획</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1-3월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 디자인</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1-3월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td rowspan="5" class="activity-group">데이터 연계 및<br>화면 개발</td>
      <td class="gantt-sub-item">데이터 분석 및 연계</td>
      <td style="text-align:center; font-size:11px; color:#FF8B00;">진행 중 (3-6월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 기술정의서</td>
      <td style="text-align:center; font-size:11px; color:#FF8B00;">진행 중 (3-4월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 모델링, 테이블 개발</td>
      <td style="text-align:center; font-size:11px; color:#FF8B00;">진행 중 (4-6월)</td>
      <td style="font-size:11px;">오은성 프로님 인터페이스 작업 선행 필요 (6월 완료 예정)</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td>
      <td style="font-size:11px;">오은성 프로님 인터페이스 작업 선행 필요 (6월 완료 예정). 일정 업데이트 공유</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">Tableau 화면 개발</td>
      <td style="text-align:center; font-size:11px; color:#97A0AF;">예정 (6월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center; font-size:11px;">S26040004737</td>
      <td style="text-align:center; font-size:11px;">유주리</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">2026-04-30</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 정합성 검증</td>
      <td style="text-align:center; font-size:11px; color:#97A0AF;">예정 (6-7월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>

    <!-- ===== 영업·사업기회 ===== -->
    <tr>
      <td rowspan="9" class="sr-group">영업<br>사업기회</td>
      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>
      <td class="gantt-sub-item">지표 수립</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1-3월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 산출식 정의</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1-3월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 계획</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1-3월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 디자인</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1-3월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td rowspan="5" class="activity-group">데이터 연계 및<br>화면 개발</td>
      <td class="gantt-sub-item">데이터 분석 및 연계</td>
      <td style="text-align:center; font-size:11px; color:#FF8B00;">진행 중 (3-5월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 기술정의서</td>
      <td style="text-align:center; font-size:11px; color:#FF8B00;">진행 중 (3-4월)</td>
      <td style="font-size:11px;">중복 데이터 문제로 뷰 테이블 스크립트 미완성</td>
      <td style="text-align:center; font-size:11px;">S26050000095</td>
      <td style="text-align:center; font-size:11px;">김범준</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">2026-05-14</td>
      <td style="font-size:11px;">중복 데이터 문제로 뷰 테이블 스크립트 미완성</td>
      <td style="font-size:11px;">이번 달 말 완료 가능 여부 확인 후 회신</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 모델링, 테이블 개발</td>
      <td style="text-align:center; font-size:11px; color:#FF8B00;">진행 중 (4-6월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">Tableau 화면 개발</td>
      <td style="text-align:center; font-size:11px; color:#FF8B00;">진행 중 (4-5월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 정합성 검증</td>
      <td style="text-align:center; font-size:11px; color:#FF8B00;">진행 중 (5-6월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>

    <!-- ===== 시장/고객·데이터 업데이트 ===== -->
    <tr>
      <td rowspan="9" class="sr-group">시장/고객<br>데이터 업데이트</td>
      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>
      <td class="gantt-sub-item">지표 수립</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 산출식 정의</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 계획</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 디자인</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td rowspan="5" class="activity-group">데이터 연계 및<br>화면 개발</td>
      <td class="gantt-sub-item">데이터 분석 및 연계</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 기술정의서</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 모델링, 테이블 개발</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1월)</td>
      <td style="font-size:11px;">엑셀 데이터 기반, 3년치 데이터 미표시 오류 / 엑셀 공유됨</td>
      <td style="text-align:center; font-size:11px;">S26030004582</td>
      <td style="text-align:center; font-size:11px;">유주리</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">2026-03-19</td>
      <td style="font-size:11px;">엑셀 데이터 기반, 3년치 데이터 미표시 오류 / 엑셀 공유됨</td>
      <td style="font-size:11px;">업데이트 엑셀 재공유 후 피드백</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">Tableau 화면 개발</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 정합성 검증</td>
      <td style="text-align:center; font-size:11px; color:#FF8B00;">진행 중 (3-5월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td><td>-</td>
    </tr>

    <!-- ===== 대시보드 운영 및 개선 업무 ===== -->
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
    </tr>

  </tbody>
</table>'''

content = content[:start_idx] + new_section + content[end_idx:]

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'w') as f:
    f.write(content)

print("완료!")
