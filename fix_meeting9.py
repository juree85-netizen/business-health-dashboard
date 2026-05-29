#!/usr/bin/env python3
"""
월별 업무 진척 표 - 대시보드 부분 재편
  기존: 대시보드 개선 12행 (지표수립4 + 데이터연계5 + 대시보드개선3)
  변경: 대시보드 개선 2행 (성능 개선 / 속도 개선 후 화면 수정)
       대시보드 운영 3행 (데이터 업로드 / 데이터 수작업 업로드 / 데이터 정합성 검증)
  → 업무 구분별 세부 진행현황 표의 구분 구조와 일치시킴
"""

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'r') as f:
    content = f.read()

old = '''    <!-- ===== 대시보드 개선 ===== -->
    <tr>
      <td rowspan="12" class="sr-group">대시보드 개선</td>
      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>
      <td class="gantt-sub-item">지표 수립</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 산출식 정의</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 계획</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 디자인</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td rowspan="5" class="activity-group">데이터 연계 및<br>화면 개발</td>
      <td class="gantt-sub-item">데이터 분석 및 연계</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 기술정의서</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 모델링, 테이블 개발</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">Tableau 화면 개발</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 정합성 검증</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td rowspan="3" class="activity-group">대시보드 개선</td>
      <td class="gantt-sub-item">데이터 업로드</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 정합성 검증</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">대시보드 성능 개선</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-wip"></td>
      <td class="cell-done"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>'''

new = '''    <!-- ===== 대시보드 개선 ===== -->
    <tr>
      <td rowspan="2" class="sr-group">대시보드 개선</td>
      <td class="activity-group">성능 개선</td>
      <td class="gantt-sub-item"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-wip"></td>
      <td class="cell-done"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="activity-group">속도 개선 후<br>화면 수정</td>
      <td class="gantt-sub-item"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-plan"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>

    <!-- ===== 대시보드 운영 ===== -->
    <tr>
      <td rowspan="3" class="sr-group">대시보드 운영</td>
      <td class="activity-group">데이터 업로드</td>
      <td class="gantt-sub-item"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="activity-group">데이터 수작업 업로드</td>
      <td class="gantt-sub-item"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="activity-group">데이터 정합성 검증</td>
      <td class="gantt-sub-item"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>'''

assert old in content, "대시보드 개선 섹션 not found"
content = content.replace(old, new)
print("✓ 대시보드 개선 2행 + 대시보드 운영 3행으로 교체")

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'w') as f:
    f.write(content)
print("파일 저장 완료!")
