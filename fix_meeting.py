#!/usr/bin/env python3

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'r') as f:
    content = f.read()

# ─── 1. SR 진행현황 첫 번째 표: 성능개선 → 대시보드 운영 및 개선 업무 ───
content = content.replace(
    '<td><strong>성능개선</strong></td>',
    '<td><strong>대시보드 운영 및 개선 업무</strong></td>'
)

# ─── 2. sr-group 성능개선 → 대시보드 운영 및 개선 업무 (Gantt + SR현황 표 각 1회) ───
content = content.replace(
    '<td rowspan="12" class="sr-group">성능개선</td>',
    '<td rowspan="12" class="sr-group">대시보드 운영 및 개선 업무</td>'
)

# ─── 3. 주석 ───
content = content.replace(
    '<!-- ===== 성능개선 ===== -->',
    '<!-- ===== 대시보드 운영 및 개선 업무 ===== -->'
)

# ═══════════════════════════════════════════════════════════
# Gantt 표 (월별 업무 진척) — 4개 섹션 rowspan 12→9 + 블록 삭제
# ═══════════════════════════════════════════════════════════

# ── 재무·효율/수익 rowspan ──
content = content.replace(
    '      <td rowspan="12" class="sr-group">재무<br>효율/수익</td>\n      <td rowspan="12" class="sr-group" style="font-size:11px;">S26040005889</td>\n      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>',
    '      <td rowspan="9" class="sr-group">재무<br>효율/수익</td>\n      <td rowspan="9" class="sr-group" style="font-size:11px;">S26040005889</td>\n      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>',
    1
)

# ── 재무 대시보드 운영 블록 삭제 (Gantt) ──
old = '''    <tr>
      <td rowspan="3" class="activity-group">대시보드 운영 및<br>개선 업무</td>
      <td class="gantt-sub-item">데이터 업로드</td>
      <td class="cell-done"></td><td class="cell-done"></td><td class="cell-done"></td>
      <td class="cell-done"></td><td class="cell-wip"></td><td class="cell-plan"></td>
      <td class="cell-plan"></td><td class="cell-plan"></td><td class="cell-plan"></td>
      <td class="cell-plan"></td><td class="cell-plan"></td><td class="cell-plan"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 정합성 검증</td>
      <td class="cell-done"></td><td class="cell-done"></td><td class="cell-done"></td>
      <td class="cell-done"></td><td class="cell-wip"></td><td class="cell-plan"></td>
      <td class="cell-plan"></td><td class="cell-plan"></td><td class="cell-plan"></td>
      <td class="cell-plan"></td><td class="cell-plan"></td><td class="cell-plan"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">대시보드 성능 개선</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>

    <!-- ===== 고객/상품·VoC ===== -->'''
new = '\n    <!-- ===== 고객/상품·VoC ===== -->'
content = content.replace(old, new)

# ── 고객/상품 rowspan ──
content = content.replace(
    '      <td rowspan="12" class="sr-group">고객/상품<br>VoC</td>\n      <td rowspan="12" class="sr-group" style="font-size:11px;">S26040004737</td>\n      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>',
    '      <td rowspan="9" class="sr-group">고객/상품<br>VoC</td>\n      <td rowspan="9" class="sr-group" style="font-size:11px;">S26040004737</td>\n      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>',
    1
)

# ── 고객/상품 대시보드 운영 블록 삭제 (Gantt) ──
old = '''    <tr>
      <td rowspan="3" class="activity-group">대시보드 운영 및<br>개선 업무</td>
      <td class="gantt-sub-item">데이터 업로드</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-plan"></td>
      <td class="cell-plan"></td><td class="cell-plan"></td><td class="cell-plan"></td>
      <td class="cell-plan"></td><td class="cell-plan"></td><td class="cell-plan"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 정합성 검증</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-plan"></td>
      <td class="cell-plan"></td><td class="cell-plan"></td><td class="cell-plan"></td>
      <td class="cell-plan"></td><td class="cell-plan"></td><td class="cell-plan"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">대시보드 성능 개선</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>

    <!-- ===== 영업·사업기회 ===== -->'''
new = '\n    <!-- ===== 영업·사업기회 ===== -->'
content = content.replace(old, new)

# ── 영업 rowspan ──
content = content.replace(
    '      <td rowspan="12" class="sr-group">영업<br>사업기회</td>\n      <td rowspan="12" class="sr-group" style="font-size:11px;">S26050000095</td>\n      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>',
    '      <td rowspan="9" class="sr-group">영업<br>사업기회</td>\n      <td rowspan="9" class="sr-group" style="font-size:11px;">S26050000095</td>\n      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>',
    1
)

# ── 영업 대시보드 운영 블록 삭제 (Gantt) ──
old = '''    <tr>
      <td rowspan="3" class="activity-group">대시보드 운영 및<br>개선 업무</td>
      <td class="gantt-sub-item">데이터 업로드</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-plan"></td>
      <td class="cell-plan"></td><td class="cell-plan"></td><td class="cell-plan"></td>
      <td class="cell-plan"></td><td class="cell-plan"></td><td class="cell-plan"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 정합성 검증</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-plan"></td>
      <td class="cell-plan"></td><td class="cell-plan"></td><td class="cell-plan"></td>
      <td class="cell-plan"></td><td class="cell-plan"></td><td class="cell-plan"></td>
    </tr>
    <tr>
      <td class="gantt-sub-item">대시보드 성능 개선</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>

    <!-- ===== 시장/고객·데이터 업데이트 ===== -->'''
new = '\n    <!-- ===== 시장/고객·데이터 업데이트 ===== -->'
content = content.replace(old, new)

# ── 시장/고객 rowspan ──
content = content.replace(
    '      <td rowspan="12" class="sr-group">시장/고객<br>데이터 업데이트</td>\n      <td rowspan="12" class="sr-group" style="font-size:11px;">S26030004582</td>\n      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>',
    '      <td rowspan="9" class="sr-group">시장/고객<br>데이터 업데이트</td>\n      <td rowspan="9" class="sr-group" style="font-size:11px;">S26030004582</td>\n      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>',
    1
)

# ── 시장/고객 대시보드 운영 블록 삭제 (Gantt) ──
old = '''    <tr>
      <td rowspan="3" class="activity-group">대시보드 운영 및<br>개선 업무</td>
      <td class="gantt-sub-item">데이터 업로드</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-wip"></td>
      <td class="cell-wip"></td><td class="cell-wip"></td><td class="cell-empty"></td>
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
    <tr>
      <td class="gantt-sub-item">대시보드 성능 개선</td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
      <td class="cell-empty"></td><td class="cell-empty"></td><td class="cell-empty"></td>
    </tr>

    <!-- ===== 대시보드 운영 및 개선 업무 ===== -->'''
new = '\n    <!-- ===== 대시보드 운영 및 개선 업무 ===== -->'
content = content.replace(old, new)

# ═══════════════════════════════════════════════════════════
# 업무 구분별 SR 진행현황 표 — 4개 섹션 rowspan + 블록 삭제
# ═══════════════════════════════════════════════════════════

# ── 재무 rowspan (SR현황 표) ──
content = content.replace(
    '      <td rowspan="12" class="sr-group">재무<br>효율/수익</td>\n      <td rowspan="12" class="sr-group" style="font-size:11px;">S26040005889</td>\n      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>',
    '      <td rowspan="9" class="sr-group">재무<br>효율/수익</td>\n      <td rowspan="9" class="sr-group" style="font-size:11px;">S26040005889</td>\n      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>'
)
content = content.replace(
    '      <td rowspan="12" style="text-align:center; vertical-align:middle;">유주리</td>\n      <td rowspan="12" style="text-align:center; vertical-align:middle;">-</td>\n      <td rowspan="12" style="text-align:center; vertical-align:middle;">2026-04-23</td>\n      <td rowspan="12" style="text-align:center; vertical-align:middle;"><span class="badge-wip">진행 중</span></td>\n      <td rowspan="12" style="text-align:center; vertical-align:middle;"><span class="badge-check">확인 필요</span></td>\n      <td rowspan="12" style="vertical-align:middle;">진행 현황 미파악</td>\n      <td rowspan="12" style="vertical-align:middle;">담당자 확인 후 공유</td>',
    '      <td rowspan="9" style="text-align:center; vertical-align:middle;">유주리</td>\n      <td rowspan="9" style="text-align:center; vertical-align:middle;">-</td>\n      <td rowspan="9" style="text-align:center; vertical-align:middle;">2026-04-23</td>\n      <td rowspan="9" style="text-align:center; vertical-align:middle;"><span class="badge-wip">진행 중</span></td>\n      <td rowspan="9" style="text-align:center; vertical-align:middle;"><span class="badge-check">확인 필요</span></td>\n      <td rowspan="9" style="vertical-align:middle;">진행 현황 미파악</td>\n      <td rowspan="9" style="vertical-align:middle;">담당자 확인 후 공유</td>'
)

# ── 고객/상품 rowspan (SR현황 표) ──
content = content.replace(
    '      <td rowspan="12" class="sr-group">고객/상품<br>VoC</td>\n      <td rowspan="12" class="sr-group" style="font-size:11px;">S26040004737</td>\n      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>',
    '      <td rowspan="9" class="sr-group">고객/상품<br>VoC</td>\n      <td rowspan="9" class="sr-group" style="font-size:11px;">S26040004737</td>\n      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>'
)
content = content.replace(
    '      <td rowspan="12" style="text-align:center; vertical-align:middle;">유주리</td>\n      <td rowspan="12" style="text-align:center; vertical-align:middle;">-</td>\n      <td rowspan="12" style="text-align:center; vertical-align:middle;">2026-04-30</td>\n      <td rowspan="12" style="text-align:center; vertical-align:middle;"><span class="badge-wip">진행 중</span></td>\n      <td rowspan="12" style="text-align:center; vertical-align:middle;"><span class="badge-wait">대기 중</span></td>\n      <td rowspan="12" style="vertical-align:middle;">오은성 프로님 인터페이스 작업 선행 필요 (6월 완료 예정)</td>\n      <td rowspan="12" style="vertical-align:middle;">일정 업데이트 공유</td>',
    '      <td rowspan="9" style="text-align:center; vertical-align:middle;">유주리</td>\n      <td rowspan="9" style="text-align:center; vertical-align:middle;">-</td>\n      <td rowspan="9" style="text-align:center; vertical-align:middle;">2026-04-30</td>\n      <td rowspan="9" style="text-align:center; vertical-align:middle;"><span class="badge-wip">진행 중</span></td>\n      <td rowspan="9" style="text-align:center; vertical-align:middle;"><span class="badge-wait">대기 중</span></td>\n      <td rowspan="9" style="vertical-align:middle;">오은성 프로님 인터페이스 작업 선행 필요 (6월 완료 예정)</td>\n      <td rowspan="9" style="vertical-align:middle;">일정 업데이트 공유</td>'
)

# ── 영업 rowspan (SR현황 표) ──
content = content.replace(
    '      <td rowspan="12" class="sr-group">영업<br>사업기회</td>\n      <td rowspan="12" class="sr-group" style="font-size:11px;">S26050000095</td>\n      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>',
    '      <td rowspan="9" class="sr-group">영업<br>사업기회</td>\n      <td rowspan="9" class="sr-group" style="font-size:11px;">S26050000095</td>\n      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>'
)
content = content.replace(
    '      <td rowspan="12" style="text-align:center; vertical-align:middle;">김범준</td>\n      <td rowspan="12" style="text-align:center; vertical-align:middle;">-</td>\n      <td rowspan="12" style="text-align:center; vertical-align:middle;">2026-05-14</td>\n      <td rowspan="12" style="text-align:center; vertical-align:middle;"><span class="badge-wip">진행 중</span></td>\n      <td rowspan="12" style="text-align:center; vertical-align:middle;"><span class="badge-wip">진행 중</span></td>\n      <td rowspan="12" style="vertical-align:middle;">중복 데이터 문제로 뷰 테이블 스크립트 미완성</td>\n      <td rowspan="12" style="vertical-align:middle;">이번 달 말 완료 가능 여부 확인 후 회신</td>',
    '      <td rowspan="9" style="text-align:center; vertical-align:middle;">김범준</td>\n      <td rowspan="9" style="text-align:center; vertical-align:middle;">-</td>\n      <td rowspan="9" style="text-align:center; vertical-align:middle;">2026-05-14</td>\n      <td rowspan="9" style="text-align:center; vertical-align:middle;"><span class="badge-wip">진행 중</span></td>\n      <td rowspan="9" style="text-align:center; vertical-align:middle;"><span class="badge-wip">진행 중</span></td>\n      <td rowspan="9" style="vertical-align:middle;">중복 데이터 문제로 뷰 테이블 스크립트 미완성</td>\n      <td rowspan="9" style="vertical-align:middle;">이번 달 말 완료 가능 여부 확인 후 회신</td>'
)

# ── 시장/고객 rowspan (SR현황 표) ──
content = content.replace(
    '      <td rowspan="12" class="sr-group">시장/고객<br>데이터 업데이트</td>\n      <td rowspan="12" class="sr-group" style="font-size:11px;">S26030004582</td>\n      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>',
    '      <td rowspan="9" class="sr-group">시장/고객<br>데이터 업데이트</td>\n      <td rowspan="9" class="sr-group" style="font-size:11px;">S26030004582</td>\n      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>'
)
content = content.replace(
    '      <td rowspan="12" style="text-align:center; vertical-align:middle;">유주리</td>\n      <td rowspan="12" style="text-align:center; vertical-align:middle;">-</td>\n      <td rowspan="12" style="text-align:center; vertical-align:middle;">2026-03-19</td>\n      <td rowspan="12" style="text-align:center; vertical-align:middle;"><span class="badge-wip">진행 중</span></td>\n      <td rowspan="12" style="text-align:center; vertical-align:middle;"><span class="badge-check">확인 필요</span></td>\n      <td rowspan="12" style="vertical-align:middle;">엑셀 데이터 기반, 3년치 데이터 미표시 오류 / 엑셀 공유됨</td>\n      <td rowspan="12" style="vertical-align:middle;">업데이트 엑셀 재공유 후 피드백</td>',
    '      <td rowspan="9" style="text-align:center; vertical-align:middle;">유주리</td>\n      <td rowspan="9" style="text-align:center; vertical-align:middle;">-</td>\n      <td rowspan="9" style="text-align:center; vertical-align:middle;">2026-03-19</td>\n      <td rowspan="9" style="text-align:center; vertical-align:middle;"><span class="badge-wip">진행 중</span></td>\n      <td rowspan="9" style="text-align:center; vertical-align:middle;"><span class="badge-check">확인 필요</span></td>\n      <td rowspan="9" style="vertical-align:middle;">엑셀 데이터 기반, 3년치 데이터 미표시 오류 / 엑셀 공유됨</td>\n      <td rowspan="9" style="vertical-align:middle;">업데이트 엑셀 재공유 후 피드백</td>'
)

# ── SR현황 표 대시보드 운영 블록 삭제 (4개 섹션) ──
# 재무 → 고객/상품 섹션으로 이어지는 블록
old = '''    <tr>
      <td rowspan="3" class="activity-group">대시보드 운영 및<br>개선 업무</td>
      <td class="gantt-sub-item">데이터 업로드</td>
    </tr>
    <tr><td class="gantt-sub-item">데이터 정합성 검증</td></tr>
    <tr><td class="gantt-sub-item">대시보드 성능 개선</td></tr>

    <!-- ===== 고객/상품·VoC ===== -->'''
new = '\n    <!-- ===== 고객/상품·VoC ===== -->'
content = content.replace(old, new)

# 고객/상품 → 영업
old = '''    <tr>
      <td rowspan="3" class="activity-group">대시보드 운영 및<br>개선 업무</td>
      <td class="gantt-sub-item">데이터 업로드</td>
    </tr>
    <tr><td class="gantt-sub-item">데이터 정합성 검증</td></tr>
    <tr><td class="gantt-sub-item">대시보드 성능 개선</td></tr>

    <!-- ===== 영업·사업기회 ===== -->'''
new = '\n    <!-- ===== 영업·사업기회 ===== -->'
content = content.replace(old, new)

# 영업 → 시장/고객
old = '''    <tr>
      <td rowspan="3" class="activity-group">대시보드 운영 및<br>개선 업무</td>
      <td class="gantt-sub-item">데이터 업로드</td>
    </tr>
    <tr><td class="gantt-sub-item">데이터 정합성 검증</td></tr>
    <tr><td class="gantt-sub-item">대시보드 성능 개선</td></tr>

    <!-- ===== 시장/고객·데이터 업데이트 ===== -->'''
new = '\n    <!-- ===== 시장/고객·데이터 업데이트 ===== -->'
content = content.replace(old, new)

# 시장/고객 → 대시보드 운영 및 개선 업무 (이미 주석 변경됨)
old = '''    <tr>
      <td rowspan="3" class="activity-group">대시보드 운영 및<br>개선 업무</td>
      <td class="gantt-sub-item">데이터 업로드</td>
    </tr>
    <tr><td class="gantt-sub-item">데이터 정합성 검증</td></tr>
    <tr><td class="gantt-sub-item">대시보드 성능 개선</td></tr>

    <!-- ===== 대시보드 운영 및 개선 업무 ===== -->'''
new = '\n    <!-- ===== 대시보드 운영 및 개선 업무 ===== -->'
content = content.replace(old, new)

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'w') as f:
    f.write(content)

print("완료!")
