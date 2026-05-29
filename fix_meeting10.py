#!/usr/bin/env python3
"""
1. <h2>회의 내용 요약</h2> 삭제
2. 대시보드 운영 스케줄 바 채우기
   - 데이터 업로드: 5월=wip (오류 발견)
   - 데이터 수작업 업로드: 3~5월=wip (3월 SR, 미완료)
   - 데이터 정합성 검증: 빈칸 유지
"""

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'r') as f:
    content = f.read()

# ─── 1. 회의 내용 요약 h2 삭제 ───
old1 = '<h2>회의 내용 요약</h2>\n\n'
assert old1 in content, "회의 내용 요약 h2 not found"
content = content.replace(old1, '')
print("✓ <h2>회의 내용 요약</h2> 삭제")

# ─── 2. 데이터 업로드: 5월=wip ───
old2 = '''      <td class="activity-group">데이터 업로드</td>
      <td class="gantt-sub-item"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>'''
new2 = '''      <td class="activity-group">데이터 업로드</td>
      <td class="gantt-sub-item"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-wip"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>'''
assert old2 in content, "데이터 업로드 행 not found"
content = content.replace(old2, new2)
print("✓ 데이터 업로드: 5월 wip")

# ─── 3. 데이터 수작업 업로드: 3~5월=wip ───
old3 = '''      <td class="activity-group">데이터 수작업 업로드</td>
      <td class="gantt-sub-item"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>'''
new3 = '''      <td class="activity-group">데이터 수작업 업로드</td>
      <td class="gantt-sub-item"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-wip"></td>
      <td class="cell-wip"></td><td class="cell-wip"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>'''
assert old3 in content, "데이터 수작업 업로드 행 not found"
content = content.replace(old3, new3)
print("✓ 데이터 수작업 업로드: 3~5월 wip")

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'w') as f:
    f.write(content)
print("파일 저장 완료!")
