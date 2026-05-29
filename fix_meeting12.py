#!/usr/bin/env python3
"""
전체 일정표 + 이슈/액션 섹션 다중 수정:
1. 전체 일정표 '25년 12월 컬럼 삭제
2. gantt-cat CSS: #172B4D 진한 배경 → #E8EDF5 연한 배경, 흰 글씨 → 짙은 글씨
3. '구분' 헤더 색: #172B4D → #344563 (약간 연하게)
4. 이슈 사항: h3 번호 추가(3.), '1. 개발 지연' 서브헤딩 추가
5. 전체 액션 아이템: 이미 2번이므로 완성된 1-2-3 번호 체계 유지
"""
import re

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'r') as f:
    content = f.read()

# ────────────────────────────────────────────────
# 1. gantt-cat CSS 색상 변경 (진함 → 연함, 흰 글씨 → 짙은 글씨)
# ────────────────────────────────────────────────
old_css = '''    .gantt-cat td {
      background-color: #172B4D;
      color: white;
      font-weight: bold;
      padding: 6px 12px;
    }'''
new_css = '''    .gantt-cat td {
      background-color: #E8EDF5;
      color: #172B4D;
      font-weight: bold;
      padding: 6px 12px;
    }'''
assert old_css in content, "gantt-cat CSS not found"
content = content.replace(old_css, new_css)
print("✓ gantt-cat 배경색 연하게 + 글씨 짙게")

# ────────────────────────────────────────────────
# 2. '구분' 헤더 색상: #172B4D → #344563
# ────────────────────────────────────────────────
old_gbn = 'background-color:#172B4D; color:white;">구분</th>'
new_gbn = 'background-color:#344563; color:white;">구분</th>'
assert old_gbn in content, "'구분' th not found"
content = content.replace(old_gbn, new_gbn)
print("✓ '구분' 헤더 색상 연하게")

# ────────────────────────────────────────────────
# 3. 전체 일정표 '25년 헤더 행 삭제 (thead row 1의 '25 th)
# ────────────────────────────────────────────────
old_h1 = '''      <th rowspan="2" style="text-align:left; padding-left:8px; background-color:#344563; color:white;">구분</th>
      <th style="text-align:center; background-color:#344563; color:white; white-space:nowrap;">'25</th>
      <th colspan="12" style="text-align:center; background-color:#0052CC; color:white;">'26</th>'''
new_h1 = '''      <th rowspan="2" style="text-align:left; padding-left:8px; background-color:#344563; color:white;">구분</th>
      <th colspan="12" style="text-align:center; background-color:#0052CC; color:white;">'26</th>'''
assert old_h1 in content, "thead row 1 not found"
content = content.replace(old_h1, new_h1)
print("✓ thead row1 '25 th 삭제")

# ────────────────────────────────────────────────
# 4. 전체 일정표 '25/12 month th 삭제 (thead row 2)
# ────────────────────────────────────────────────
old_h2 = '      <th style="text-align:center; background-color:#344563; color:white; white-space:nowrap;">12</th>\n      <th style="text-align:center; background-color:#0052CC; color:white; white-space:nowrap;">1</th>'
new_h2 = '      <th style="text-align:center; background-color:#0052CC; color:white; white-space:nowrap;">1</th>'
assert old_h2 in content, "thead row2 12 th not found"
content = content.replace(old_h2, new_h2)
print("✓ thead row2 '25/12 th 삭제")

# ────────────────────────────────────────────────
# 5. colgroup: col 하나 제거 (38px 13개 → 12개)
# ────────────────────────────────────────────────
old_col = '    <col style="width:38px;"><col style="width:38px;"><col style="width:38px;"><col style="width:38px;">\n    <col style="width:38px;"><col style="width:38px;"><col style="width:38px;"><col style="width:38px;">\n    <col style="width:38px;"><col style="width:38px;"><col style="width:38px;"><col style="width:38px;">\n    <col style="width:38px;">'
new_col = '    <col style="width:38px;"><col style="width:38px;"><col style="width:38px;"><col style="width:38px;">\n    <col style="width:38px;"><col style="width:38px;"><col style="width:38px;"><col style="width:38px;">\n    <col style="width:38px;"><col style="width:38px;"><col style="width:38px;"><col style="width:38px;">'
assert old_col in content, "colgroup not found"
content = content.replace(old_col, new_col)
print("✓ colgroup col 1개 제거 (13→12)")

# ────────────────────────────────────────────────
# 6. gantt-cat colspan 14 → 13
# ────────────────────────────────────────────────
count = content.count('colspan="14"')
content = content.replace('colspan="14"', 'colspan="13"')
print(f"✓ colspan 14→13 ({count}개)")

# ────────────────────────────────────────────────
# 7. 각 데이터 행의 첫 번째 cell-empty 제거 (='25/12 cell)
#    패턴: 서브 아이템 td 직후 줄의 첫 <td class="cell-empty"></td>
# ────────────────────────────────────────────────
pattern = r'(color:#344563;">　[^<]+</td>)\n(\s+)<td class="cell-empty"></td>'
before = len(re.findall(pattern, content))
content = re.sub(pattern, r'\1\n\2', content)
print(f"✓ 데이터 행 첫 번째 cell-empty 제거 ({before}개)")

# ────────────────────────────────────────────────
# 8. 이슈 사항 → 3. 이슈 사항, 서브헤딩 1. 개발 지연 추가
# ────────────────────────────────────────────────
old_issue = '<h3>이슈 사항</h3>\n<ul>\n  <li><strong>원인 2가지:</strong>'
new_issue = '<h3>3. 이슈 사항</h3>\n<h4 style="font-size:14px; color:#172B4D; margin:16px 0 6px;">1. 개발 지연</h4>\n<ul>\n  <li><strong>원인 2가지:</strong>'
assert old_issue in content, "이슈 사항 h3 not found"
content = content.replace(old_issue, new_issue)
print("✓ '3. 이슈 사항' + '1. 개발 지연' 서브헤딩 추가")

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'w') as f:
    f.write(content)
print("\n파일 저장 완료!")
