#!/usr/bin/env python3

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'r') as f:
    content = f.read()

# ─── 1. 고객/상품 VoC → 고객/상품 ───
content = content.replace('고객/상품<br>VoC', '고객/상품')
content = content.replace('고객/상품 · VoC', '고객/상품')
content = content.replace('고객/상품·VoC', '고객/상품')
print("✓ 고객/상품 VoC → 고객/상품")

# ─── 2. 영업 사업기회 → 영업 ───
content = content.replace('영업<br>사업기회', '영업')
content = content.replace('영업 · 사업기회', '영업')
content = content.replace('영업·사업기회', '영업')
print("✓ 영업 사업기회 → 영업")

# ─── 3. 대시보드 개선 업무 → 대시보드 개선 ───
content = content.replace('대시보드 개선 업무', '대시보드 개선')
print("✓ 대시보드 개선 업무 → 대시보드 개선")

# ─── 4. 대시보드 개선 구분 셀: dark style → sr-group ───
old = '<td rowspan="2" style="background-color:#172B4D; color:white; font-weight:bold; text-align:center; vertical-align:middle; font-size:12px; padding:6px 8px;">대시보드 개선</td>'
new = '<td rowspan="2" class="sr-group">대시보드 개선</td>'
assert old in content, "대시보드 개선 구분 셀 not found"
content = content.replace(old, new)
print("✓ 대시보드 개선 스타일 → sr-group")

# ─── 5. 이슈 헤더 삭제 (첫 번째 SR 표) ───
old = '      <th>이슈</th>\n      <th>액션</th>'
new = '      <th>액션</th>'
assert old in content, "첫 번째 SR 이슈 헤더 not found"
content = content.replace(old, new)
print("✓ 첫 번째 SR 표 이슈 헤더 삭제")

# ─── 6. 이슈 셀 삭제 (첫 번째 SR 표 각 행) ───
for old, new in [
    ('<td>진행 현황 미파악</td>\n      <td>담당자 확인 후 공유</td>',
     '<td>담당자 확인 후 공유</td>'),
    ('<td>오은성 프로님 인터페이스 작업 선행 필요 (6월 완료 예정)</td>\n      <td>일정 업데이트 공유</td>',
     '<td>일정 업데이트 공유</td>'),
    ('<td>중복 데이터 문제로 뷰 테이블 스크립트 미완성</td>\n      <td>이번 달 말 완료 가능 여부 확인 후 회신</td>',
     '<td>이번 달 말 완료 가능 여부 확인 후 회신</td>'),
    ('<td>엑셀 데이터 기반, 3년치 데이터 미표시 오류 / 엑셀 공유됨</td>\n      <td>업데이트 엑셀 재공유 후 피드백</td>',
     '<td>업데이트 엑셀 재공유 후 피드백</td>'),
]:
    assert old in content, f"not found: {old[:40]}"
    content = content.replace(old, new)

# 대시보드 개선 행 (badge-done, 이슈=-, 액션=-)
old = '      <td><span class="badge-done">완료</span></td>\n      <td>-</td>\n      <td>-</td>\n    </tr>\n  </tbody>\n</table>'
new = '      <td><span class="badge-done">완료</span></td>\n      <td>-</td>\n    </tr>\n  </tbody>\n</table>'
assert old in content, "badge-done 이슈 셀 not found"
content = content.replace(old, new)
print("✓ 첫 번째 SR 표 이슈 셀 삭제")

# ─── 7. 이슈 헤더 삭제 (상세 SR 표) ───
old = '      <th>이슈</th>\n      <th style="width:115px;">비고</th>'
new = '      <th style="width:115px;">비고</th>'
assert old in content, "상세 SR 이슈 헤더 not found"
content = content.replace(old, new)
print("✓ 상세 SR 표 이슈 헤더 삭제")

# ─── 8. 이슈 셀 삭제 (상세 SR 표 특수 행들) ───
# 재무 (이슈=진행현황미파악, 비고=담당자확인) — 두 행 동일
old = '      <td style="font-size:11px;">진행 현황 미파악</td>\n      <td style="font-size:11px;">담당자 확인 후 공유</td>'
new = '      <td style="font-size:11px;">담당자 확인 후 공유</td>'
assert old in content, "재무 이슈 not found"
content = content.replace(old, new)

# 영업 기술정의서
old = '      <td style="font-size:11px;">중복 데이터 문제로 뷰 테이블 스크립트 미완성</td>\n      <td style="font-size:11px;">이번 달 말 완료 가능 여부 확인 후 회신</td>'
new = '      <td style="font-size:11px;">이번 달 말 완료 가능 여부 확인 후 회신</td>'
assert old in content, "영업 이슈 not found"
content = content.replace(old, new)

# 시장/고객 모델링
old = '      <td style="font-size:11px;">엑셀 데이터 기반, 3년치 데이터 미표시 오류 / 엑셀 공유됨</td>\n      <td style="font-size:11px;">업데이트 엑셀 재공유 후 피드백</td>'
new = '      <td style="font-size:11px;">업데이트 엑셀 재공유 후 피드백</td>'
assert old in content, "시장 이슈 not found"
content = content.replace(old, new)

# 고객/상품 모델링 (이슈=-, 비고=오은성...)
old = '\n      <td>-</td>\n      <td style="font-size:11px;">오은성 프로님 인터페이스 작업 선행 필요 (6월 완료 예정). 일정 업데이트 공유</td>'
new = '\n      <td style="font-size:11px;">오은성 프로님 인터페이스 작업 선행 필요 (6월 완료 예정). 일정 업데이트 공유</td>'
assert old in content, "고객/상품 이슈 not found"
content = content.replace(old, new)

# 재무 정합성 검증 (이슈=-, 비고=5-6월 진행 예정)
old = '      <td>-</td><td style="font-size:11px;">5-6월 진행 예정</td>'
new = '      <td style="font-size:11px;">5-6월 진행 예정</td>'
assert old in content, "재무 정합성 이슈 not found"
content = content.replace(old, new)

# 대시보드 개선 화면 수정 행
old = '      <td style="font-size:11px;">기존 설계와 달라진 부분 다수 발견 (오른쪽 정렬, 기준 연월 표시, 한 화면 레이아웃 등)</td>\n      <td style="font-size:11px;">솔루션전략이 이슈 리스트업 후 메일 공유 예정</td>'
new = '      <td style="font-size:11px;">솔루션전략이 이슈 리스트업 후 메일 공유 예정</td>'
assert old in content, "대시보드 개선 화면수정 이슈 not found"
content = content.replace(old, new)

# 대시보드 운영 데이터 업로드 (이슈=화면에 4월이..., 비고=회의 후 즉시 확인)
old = '      <td style="font-size:11px;">화면에 4월이 아닌 3월로 표시됨 (4월 실적 미반영)</td>\n      <td style="font-size:11px;">회의 후 즉시 확인</td>'
new = '      <td style="font-size:11px;">회의 후 즉시 확인</td>'
assert old in content, "대시보드 운영 이슈 not found"
content = content.replace(old, new)

print("✓ 상세 SR 표 특수 이슈 셀 삭제")

# ─── 9. 이슈 셀 삭제 (상세 SR 표 표준 행: <td>-</td><td>-</td>) ───
count = content.count('<td>-</td><td>-</td>')
content = content.replace('<td>-</td><td>-</td>', '<td>-</td>')
print(f"✓ 상세 SR 표 표준 이슈 삭제 ({count}개)")

# ─── 10. 대시보드 개선 성능 개선 행 이슈(-) 삭제 ───
old = ('      <td style="text-align:center; font-size:11px;">2026-03-28</td>\n'
       '      <td style="text-align:center; font-size:11px;">-</td>\n'
       '      <td style="text-align:center; font-size:11px;">-</td>\n'
       '    </tr>\n'
       '    <tr>\n'
       '      <td class="activity-group">속도 개선 후<br>화면 수정</td>')
new = ('      <td style="text-align:center; font-size:11px;">2026-03-28</td>\n'
       '      <td style="text-align:center; font-size:11px;">-</td>\n'
       '    </tr>\n'
       '    <tr>\n'
       '      <td class="activity-group">속도 개선 후<br>화면 수정</td>')
assert old in content, "대시보드 개선 성능 개선 이슈 not found"
content = content.replace(old, new)
print("✓ 대시보드 개선 성능 개선 행 이슈 삭제")

# ─── 11. 대시보드 운영 섹션: rowspan 2→3, sr-group, 수작업 업로드 행 추가, 정합성 이슈 삭제 ───
old = '''    <!-- ===== 대시보드 운영 ===== -->
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

new = '''    <!-- ===== 대시보드 운영 ===== -->
    <tr>
      <td rowspan="3" class="sr-group">대시보드 운영</td>
      <td class="activity-group">데이터 업로드</td>
      <td class="gantt-sub-item">기준 연월 오류</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="font-size:11px;">화면에 4월이 아닌 3월로 표시됨 (4월 실적 미반영)</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="font-size:11px;">회의 후 즉시 확인</td>
    </tr>
    <tr>
      <td class="activity-group">데이터 수작업 업로드</td>
      <td class="gantt-sub-item">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">-</td>
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
    </tr>'''

assert old in content, "대시보드 운영 섹션 not found"
content = content.replace(old, new)
print("✓ 대시보드 운영: rowspan 3, sr-group, 수작업 업로드 행 추가, 이슈 삭제")

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'w') as f:
    f.write(content)
print("파일 저장 완료!")
