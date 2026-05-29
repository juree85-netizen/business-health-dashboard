#!/usr/bin/env python3

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'r') as f:
    content = f.read()

# ─── 1. 회의 내용 요약 섹션 1·2 삭제 + 번호 재정렬 ───
old = '''<h3>1. 속도 개선 후 화면 이슈</h3>
<ul>
  <li>기존 설계와 달라진 부분 다수 발견 (오른쪽 정렬, 기준 연월 표시, 한 화면 레이아웃 등)</li>
  <li><strong>액션:</strong> 솔루션전략이 이슈 리스트업 후 메일 공유 예정</li>
</ul>

<hr>

<h3>2. 기준 연월 오류</h3>
<ul>
  <li>화면에 4월이 아닌 3월로 표시됨 (4월 실적 미반영)</li>
  <li><strong>액션:</strong> 회의 후 즉시 확인</li>
</ul>

<hr>

<h3>3. '신규 지표/상품 추가' 관련 업무 진척</h3>'''
new = "<h3>1. '신규 지표/상품 추가' 관련 업무 진척</h3>"
assert old in content, "섹션1·2 삭제 대상 not found"
content = content.replace(old, new)
print("✓ 섹션 1·2 삭제 + 재번호")

content = content.replace('<h3>4. 6월 개발 지연 예고</h3>', '<h3>2. 6월 개발 지연 예고</h3>')
content = content.replace('<h3>5. 전체 액션 아이템</h3>', '<h3>3. 전체 액션 아이템</h3>')
print("✓ 섹션 번호 재정렬")

# ─── 2. 구분: 대시보드 운영 및 개선 업무 → 대시보드 개선 업무 ───
old = '대시보드 운영 및<br>개선 업무'
new = '대시보드 개선 업무'
assert old in content, "대시보드 운영 및 개선 업무 not found"
content = content.replace(old, new)
print("✓ 대시보드 개선 업무 명칭 변경")

# ─── 3. 월간 데이터 반영 및 검증 → 대시보드 운영 (2행으로 확장) ───
old = '''    <!-- ===== 월간 데이터 반영 및 검증 ===== -->
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

new = '''    <!-- ===== 대시보드 운영 ===== -->
    <tr>
      <td rowspan="2" style="background-color:#172B4D; color:white; font-weight:bold; text-align:center; vertical-align:middle; font-size:12px; padding:6px 8px;">대시보드 운영</td>
      <td class="activity-group">데이터 업로드</td>
      <td class="gantt-sub-item">기준 연월 오류</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="font-size:11px;">화면에 4월이 아닌 3월로 표시됨 (4월 실적 미반영)</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="font-size:11px;">화면에 4월이 아닌 3월로 표시됨 (4월 실적 미반영)</td>
      <td style="font-size:11px;">회의 후 즉시 확인</td>
    </tr>
    <tr>
      <td class="activity-group">데이터 정합성 검증</td>
      <td class="gantt-sub-item">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
    </tr>'''

assert old in content, "월간 데이터 반영 및 검증 not found"
content = content.replace(old, new)
print("✓ 대시보드 운영 2행 구조 적용")

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'w') as f:
    f.write(content)

print("파일 저장 완료!")
