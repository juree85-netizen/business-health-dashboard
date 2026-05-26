#!/usr/bin/env python3

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'r') as f:
    content = f.read()

# ─── 1. 고객/상품 > 데이터 모델링 행: SR 정보 추가 + 비고 변경 ───
old = '''    <tr>
      <td class="gantt-sub-item">데이터 모델링, 테이블 개발</td>
      <td style="text-align:center; font-size:11px; color:#FF8B00;">진행 중 (4-6월)</td>
      <td style="font-size:11px;">오은성 프로님 인터페이스 작업 선행 필요 (6월 완료 예정)</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td style="font-size:11px;">오은성 프로님 인터페이스 작업 선행 필요 (6월 완료 예정). 일정 업데이트 공유</td>
    </tr>'''
new = '''    <tr>
      <td class="gantt-sub-item">데이터 모델링, 테이블 개발</td>
      <td style="text-align:center; font-size:11px; color:#FF8B00;">진행 중 (4-6월)</td>
      <td style="font-size:11px;">오은성 프로님 인터페이스 작업 선행 필요 (6월 완료 예정)</td>
      <td style="text-align:center; font-size:11px;">S26040004737</td>
      <td style="text-align:center; font-size:11px;">유주리</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">2026-04-30</td>
      <td style="font-size:11px;">오은성 프로님 일정 업데이트 공유 예정</td>
    </tr>'''
assert old in content, "고객/상품 데이터 모델링 행 not found"
content = content.replace(old, new)
print("✓ 고객/상품 > 데이터 모델링: SR 정보 추가 + 비고 변경")

# ─── 2. 영업 > 데이터 연계 및 화면 개발 섹션 전체 교체
#        (지표 기술정의서 SR 삭제 → 데이터 모델링 + Tableau 화면 개발에 이동) ───
old = '''    <tr>
      <td rowspan="5" class="activity-group">데이터 연계 및<br>화면 개발</td>
      <td class="gantt-sub-item">데이터 분석 및 연계</td>
      <td style="text-align:center; font-size:11px; color:#FF8B00;">진행 중 (3-5월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 기술정의서</td>
      <td style="text-align:center; font-size:11px; color:#FF8B00;">진행 중 (3-4월)</td>
      <td style="font-size:11px;">중복 데이터 문제로 뷰 테이블 스크립트 미완성</td>
      <td style="text-align:center; font-size:11px;">S26050000095</td>
      <td style="text-align:center; font-size:11px;">김범준</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">2026-05-14</td>
      <td style="font-size:11px;">이번 달 말 완료 가능 여부 확인 후 회신</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 모델링, 테이블 개발</td>
      <td style="text-align:center; font-size:11px; color:#FF8B00;">진행 중 (4-6월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">Tableau 화면 개발</td>
      <td style="text-align:center; font-size:11px; color:#FF8B00;">진행 중 (4-5월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 정합성 검증</td>
      <td style="text-align:center; font-size:11px; color:#FF8B00;">진행 중 (5-6월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td>
    </tr>'''
new = '''    <tr>
      <td rowspan="5" class="activity-group">데이터 연계 및<br>화면 개발</td>
      <td class="gantt-sub-item">데이터 분석 및 연계</td>
      <td style="text-align:center; font-size:11px; color:#FF8B00;">진행 중 (3-5월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 기술정의서</td>
      <td style="text-align:center; font-size:11px; color:#FF8B00;">진행 중 (3-4월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 모델링, 테이블 개발</td>
      <td style="text-align:center; font-size:11px; color:#FF8B00;">진행 중 (4-6월)</td>
      <td style="font-size:11px;">중복 데이터 문제로 뷰 테이블 스크립트 미완성</td>
      <td style="text-align:center; font-size:11px;">S26050000095</td>
      <td style="text-align:center; font-size:11px;">김범준</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">2026-05-14</td>
      <td style="font-size:11px;">이번 달 말 완료 가능 여부 확인 후 회신</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">Tableau 화면 개발</td>
      <td style="text-align:center; font-size:11px; color:#FF8B00;">진행 중 (4-5월)</td>
      <td style="font-size:11px;">중복 데이터 문제로 뷰 테이블 스크립트 미완성</td>
      <td style="text-align:center; font-size:11px;">S26050000095</td>
      <td style="text-align:center; font-size:11px;">김범준</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">2026-05-14</td>
      <td style="font-size:11px;">이번 달 말 완료 가능 여부 확인 후 회신</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 정합성 검증</td>
      <td style="text-align:center; font-size:11px; color:#FF8B00;">진행 중 (5-6월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td>
    </tr>'''
assert old in content, "영업 데이터 연계 섹션 not found"
content = content.replace(old, new)
print("✓ 영업 > SR: 기술정의서→ 데이터 모델링 + Tableau 이동")

# ─── 3. 시장/고객 > Simple SR 표 행 삭제 ───
old = '''    <tr>
      <td><strong>시장/고객 · 데이터 업데이트</strong></td>
      <td>S26030004582</td>
      <td>유주리</td>
      <td>-</td>
      <td>2026-03-19</td>
      <td><span class="badge-wip">진행 중</span></td>
      <td><span class="badge-check">확인 필요</span></td>
      <td>업데이트 엑셀 재공유 후 피드백</td>
    </tr>
    <tr>
      <td><strong>대시보드 개선</strong></td>'''
new = '''    <tr>
      <td><strong>대시보드 개선</strong></td>'''
assert old in content, "시장/고객 simple SR 행 not found"
content = content.replace(old, new)
print("✓ 시장/고객 simple SR 표 행 삭제")

# ─── 4. 시장/고객 > Gantt 표 섹션 삭제 (9행) ───
old = '''
    <!-- ===== 시장/고객·데이터 업데이트 ===== -->
    <tr>
      <td rowspan="9" class="sr-group">시장/고객<br>데이터 업데이트</td>
      <td rowspan="9" class="sr-group" style="font-size:11px;">S26030004582</td>
      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>
      <td class="gantt-sub-item">지표 수립</td>
      <td class="cell-done"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 산출식 정의</td>
      <td class="cell-done"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 계획</td>
      <td class="cell-done"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 디자인</td>
      <td class="cell-done"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td rowspan="5" class="activity-group">데이터 연계 및<br>화면 개발</td>
      <td class="gantt-sub-item">데이터 분석 및 연계</td>
      <td class="cell-done"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 기술정의서</td>
      <td class="cell-done"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 모델링, 테이블 개발</td>
      <td class="cell-done"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">Tableau 화면 개발</td>
      <td class="cell-done"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 정합성 검증</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-wip"></td>
      <td class="cell-wip"></td><td class="cell-wip"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>
'''
new = '\n'
assert old in content, "시장/고객 Gantt 섹션 not found"
content = content.replace(old, new)
print("✓ 시장/고객 Gantt 표 섹션 삭제")

# ─── 5. 시장/고객 > Detailed SR 표 섹션 삭제 (9행) ───
old = '''
    <!-- ===== 시장/고객·데이터 업데이트 ===== -->
    <tr>
      <td rowspan="9" class="sr-group">시장/고객<br>데이터 업데이트</td>
      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>
      <td class="gantt-sub-item">지표 수립</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 산출식 정의</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 계획</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 디자인</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td>
    </tr>
    <tr>
      <td rowspan="5" class="activity-group">데이터 연계 및<br>화면 개발</td>
      <td class="gantt-sub-item">데이터 분석 및 연계</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 기술정의서</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 모델링, 테이블 개발</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1월)</td>
      <td style="font-size:11px;">엑셀 데이터 기반, 3년치 데이터 미표시 오류 / 엑셀 공유됨</td>
      <td style="text-align:center; font-size:11px;">S26030004582</td>
      <td style="text-align:center; font-size:11px;">유주리</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">2026-03-19</td>
      <td style="font-size:11px;">업데이트 엑셀 재공유 후 피드백</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">Tableau 화면 개발</td>
      <td style="text-align:center; font-size:11px; color:#00875A;">완료 (1월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 정합성 검증</td>
      <td style="text-align:center; font-size:11px; color:#FF8B00;">진행 중 (3-5월)</td>
      <td style="text-align:center;">-</td>
      <td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td><td style="text-align:center;">-</td>
      <td>-</td>
    </tr>
'''
new = '\n'
assert old in content, "시장/고객 detailed SR 섹션 not found"
content = content.replace(old, new)
print("✓ 시장/고객 detailed SR 표 섹션 삭제")

# ─── 6. 대시보드 운영 > 데이터 수작업 업로드: 시장/고객 SR 정보 이동 ───
old = '''    <tr>
      <td class="activity-group">데이터 수작업 업로드</td>
      <td class="gantt-sub-item">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
    </tr>'''
new = '''    <tr>
      <td class="activity-group">데이터 수작업 업로드</td>
      <td class="gantt-sub-item">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="font-size:11px;">엑셀 데이터 기반, 3년치 데이터 미표시 오류 / 엑셀 공유됨</td>
      <td style="text-align:center; font-size:11px;">S26030004582</td>
      <td style="text-align:center; font-size:11px;">유주리</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">2026-03-19</td>
      <td style="font-size:11px;">업데이트 엑셀 재공유 후 피드백</td>
    </tr>'''
assert old in content, "데이터 수작업 업로드 행 not found"
content = content.replace(old, new)
print("✓ 대시보드 운영 > 데이터 수작업 업로드: 시장/고객 SR 정보 이동")

# ─── 7. 제목 변경: 업무 구분별 SR 진행현황 → 업무 구분별 세부 진행 현황 ───
content = content.replace(
    '<p style="font-size:13px; font-weight:bold; color:#172B4D; margin:32px 0 6px;">업무 구분별 SR 진행현황</p>',
    '<p style="font-size:13px; font-weight:bold; color:#172B4D; margin:32px 0 6px;">업무 구분별 세부 진행 현황</p>'
)
print("✓ 업무 구분별 SR 진행현황 → 업무 구분별 세부 진행 현황")

# ─── 8. SR 진행현황 표를 업무 구분별 세부 진행 현황 표 아래로 이동 ───
SR_LABEL_START = '<p style="font-size:13px; font-weight:bold; color:#172B4D; margin:12px 0 6px;">SR 진행현황</p>\n'
GANTT_LABEL = '<p style="font-size:13px; font-weight:bold; color:#172B4D; margin:24px 0 6px;">월별 업무 진척</p>\n'

pos_sr_label = content.index(SR_LABEL_START)
pos_gantt_label = content.index(GANTT_LABEL)

# SR 블록 추출 (p 태그부터 Gantt 레이블 직전까지)
sr_block = content[pos_sr_label:pos_gantt_label]

# 현재 위치에서 SR 블록 제거 (Gantt 레이블부터 이어지게)
content = content[:pos_sr_label] + content[pos_gantt_label:]

# detailed SR 표 끝 위치 찾기 (</table>\n\n<hr>)
DETAIL_END = '</table>\n\n<hr>'
pos_detail_end = content.index(DETAIL_END)

# SR 블록 레이블 마진 수정 후 삽입
sr_block_new = sr_block.replace('margin:12px 0 6px;">', 'margin:32px 0 6px;">')
content = (content[:pos_detail_end + len('</table>')] +
           '\n\n' + sr_block_new.rstrip('\n') +
           '\n\n<hr>' +
           content[pos_detail_end + len(DETAIL_END):])
print("✓ SR 진행현황 표: 업무 구분별 세부 진행 현황 아래로 이동")

# ─── 9. 6월 개발 지연 예고 → 이슈 사항으로 제목 변경 + 맨 아래로 이동 ───
#        전체 액션 아이템 번호 3 → 2로 변경
SECTION_6월_OLD = '''<hr>

<h3>2. 6월 개발 지연 예고</h3>
<ul>
  <li><strong>원인 2가지:</strong>
    <ul>
      <li>데이터 레이크 전체 개인정보 암호화 작업 (6월 말 마감)</li>
      <li>NiFi → Airflow 전환 작업 (1월부터 지연되어 6월 마감)</li>
    </ul>
  </li>
  <li><strong>결론:</strong> 단순 작업(엑셀 업로드 등)은 우선순위 조정하여 진행, 복잡한 작업은 일정 공유 필요</li>
</ul>

<hr>

<h3>3. 전체 액션 아이템</h3>'''

ISSUE_CONTENT = '''<h3>이슈 사항</h3>
<ul>
  <li><strong>원인 2가지:</strong>
    <ul>
      <li>데이터 레이크 전체 개인정보 암호화 작업 (6월 말 마감)</li>
      <li>NiFi → Airflow 전환 작업 (1월부터 지연되어 6월 마감)</li>
    </ul>
  </li>
  <li><strong>결론:</strong> 단순 작업(엑셀 업로드 등)은 우선순위 조정하여 진행, 복잡한 작업은 일정 공유 필요</li>
</ul>'''

assert SECTION_6월_OLD in content, "6월 개발 지연 섹션 not found"
# 6월 개발 지연 제거 + 전체 액션 아이템 번호 변경
content = content.replace(SECTION_6월_OLD, '<hr>\n\n<h3>2. 전체 액션 아이템</h3>')

# 맨 아래 (</body> 직전)에 이슈 사항 삽입
assert '</table>\n\n</body>\n</html>' in content, "file ending not found"
content = content.replace(
    '</table>\n\n</body>\n</html>',
    '</table>\n\n<hr>\n\n' + ISSUE_CONTENT + '\n\n</body>\n</html>'
)
print("✓ 6월 개발 지연 예고 → 이슈 사항 (맨 아래로 이동), 전체 액션 아이템 → 2번")

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'w') as f:
    f.write(content)
print("파일 저장 완료!")
