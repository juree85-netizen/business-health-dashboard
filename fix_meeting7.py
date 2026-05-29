#!/usr/bin/env python3
"""
월별 업무 진척 표 수정:
1. SR No. 컬럼 삭제 (헤더 + 각 그룹 td)
2. 지표 수립 및 화면 기획 / 데이터 연계 및 화면 개발 sub-item 행 전체 삭제
   → 재무·효율/수익, 고객/상품, 영업 섹션 소멸
   → 대시보드 개선: 9행 삭제 후 3행(대시보드 개선 activity)만 유지, rowspan 3으로 수정
"""

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'r') as f:
    content = f.read()

# ─── 1. 헤더: SR No. th 삭제 ───
old_hdr = '''      <th rowspan="2" style="width:90px; text-align:center; vertical-align:middle;">SR No.</th>
      <th rowspan="2" style="width:105px; text-align:center; vertical-align:middle;">업무 구분</th>'''
new_hdr = '''      <th rowspan="2" style="width:105px; text-align:center; vertical-align:middle;">업무 구분</th>'''
assert old_hdr in content, "헤더 SR No. th not found"
content = content.replace(old_hdr, new_hdr)
print("✓ 헤더 SR No. 컬럼 삭제")

# ─── 2. 재무·효율/수익 섹션 전체 삭제 (comment + 9행) ───
old_sct1 = '''
    <!-- ===== 재무·효율/수익 ===== -->
    <tr>
      <td rowspan="9" class="sr-group">재무<br>효율/수익</td>
      <td rowspan="9" class="sr-group" style="font-size:11px;">S26040005889</td>
      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>
      <td class="gantt-sub-item">지표 수립</td>
      <td class="cell-done"></td><td class="cell-done"></td><td class="cell-done"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 산출식 정의</td>
      <td class="cell-done"></td><td class="cell-done"></td><td class="cell-done"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 계획</td>
      <td class="cell-done"></td><td class="cell-done"></td><td class="cell-done"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 디자인</td>
      <td class="cell-done"></td><td class="cell-done"></td><td class="cell-done"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td rowspan="5" class="activity-group">데이터 연계 및<br>화면 개발</td>
      <td class="gantt-sub-item">데이터 분석 및 연계</td>
      <td class="cell-done"></td><td class="cell-done"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 기술정의서</td>
      <td class="cell-empty"></td><td class="cell-done"></td><td class="cell-done"></td>
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
      <td class="cell-wip"></td><td class="cell-wip"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 정합성 검증</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-wip"></td><td class="cell-plan"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
'''
assert old_sct1 in content, "재무·효율/수익 섹션 not found"
content = content.replace(old_sct1, '\n')
print("✓ 재무·효율/수익 섹션 삭제")

# ─── 3. 고객/상품 섹션 전체 삭제 (comment + 9행) ───
old_sct2 = '''    <!-- ===== 고객/상품 ===== -->
    <tr>
      <td rowspan="9" class="sr-group">고객/상품</td>
      <td rowspan="9" class="sr-group" style="font-size:11px;">S26040004737</td>
      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>
      <td class="gantt-sub-item">지표 수립</td>
      <td class="cell-done"></td><td class="cell-done"></td><td class="cell-done"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 산출식 정의</td>
      <td class="cell-done"></td><td class="cell-done"></td><td class="cell-done"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 계획</td>
      <td class="cell-done"></td><td class="cell-done"></td><td class="cell-done"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 디자인</td>
      <td class="cell-done"></td><td class="cell-done"></td><td class="cell-done"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td rowspan="5" class="activity-group">데이터 연계 및<br>화면 개발</td>
      <td class="gantt-sub-item">데이터 분석 및 연계</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-wip"></td>
      <td class="cell-wip"></td><td class="cell-wip"></td><td class="cell-plan"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 기술정의서</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-done"></td>
      <td class="cell-wip"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 모델링, 테이블 개발</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-wip"></td><td class="cell-wip"></td><td class="cell-plan"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">Tableau 화면 개발</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-plan"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 정합성 검증</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-plan"></td>
      <td class="cell-plan"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
'''
assert old_sct2 in content, "고객/상품 섹션 not found"
content = content.replace(old_sct2, '')
print("✓ 고객/상품 섹션 삭제")

# ─── 4. 영업 섹션 전체 삭제 (comment + 9행) ───
old_sct3 = '''    <!-- ===== 영업 ===== -->
    <tr>
      <td rowspan="9" class="sr-group">영업</td>
      <td rowspan="9" class="sr-group" style="font-size:11px;">S26050000095</td>
      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>
      <td class="gantt-sub-item">지표 수립</td>
      <td class="cell-done"></td><td class="cell-done"></td><td class="cell-done"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 산출식 정의</td>
      <td class="cell-done"></td><td class="cell-done"></td><td class="cell-done"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 계획</td>
      <td class="cell-done"></td><td class="cell-done"></td><td class="cell-done"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 디자인</td>
      <td class="cell-done"></td><td class="cell-done"></td><td class="cell-done"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td rowspan="5" class="activity-group">데이터 연계 및<br>화면 개발</td>
      <td class="gantt-sub-item">데이터 분석 및 연계</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-done"></td>
      <td class="cell-wip"></td><td class="cell-wip"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 기술정의서</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-done"></td>
      <td class="cell-wip"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 모델링, 테이블 개발</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-wip"></td><td class="cell-wip"></td><td class="cell-plan"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">Tableau 화면 개발</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-wip"></td><td class="cell-wip"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 정합성 검증</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-wip"></td><td class="cell-plan"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>

'''
assert old_sct3 in content, "영업 섹션 not found"
content = content.replace(old_sct3, '\n')
print("✓ 영업 섹션 삭제")

# ─── 5. 대시보드 개선: 첫 9행(지표수립+데이터연계) 삭제 + rowspan 12→3, SR No. td 제거 ───
old_db = '''    <!-- ===== 대시보드 개선 ===== -->
    <tr>
      <td rowspan="12" class="sr-group">대시보드 개선</td>
      <td rowspan="12" class="sr-group" style="font-size:11px;">S26030007696</td>
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
      <td rowspan="3" class="activity-group">대시보드 개선</td>'''

new_db = '''    <!-- ===== 대시보드 개선 ===== -->
    <tr>
      <td rowspan="3" class="sr-group">대시보드 개선</td>
      <td rowspan="3" class="activity-group">대시보드 개선</td>'''

assert old_db in content, "대시보드 개선 섹션 not found"
content = content.replace(old_db, new_db)
print("✓ 대시보드 개선: 9행 삭제 + rowspan 3, SR No. td 제거")

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'w') as f:
    f.write(content)
print("파일 저장 완료!")
