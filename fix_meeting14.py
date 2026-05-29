#!/usr/bin/env python3
"""
업무 구분별 세부 진행현황 표(섹션 분리 후 처리):
1. 시장 섹션 삽입 (고객/상품 ~ 영업 사이)
2. 파트너 행 삽입 (영업 자사 마지막 행 뒤)
3. 영업 rowspan 9→18
"""

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'r') as f:
    content = f.read()

ANCHOR = '<p style="font-size:13px; font-weight:bold; color:#172B4D; margin:32px 0 6px;">업무 구분별 세부 진행 현황</p>'
idx = content.index(ANCHOR)
before = content[:idx]
section = content[idx:]

# ─────────────────────────────────────────
# 공통 helpers
# ─────────────────────────────────────────
def cell(v, color=None):
    c = f' color:{color};' if color else ''
    return f'<td style="text-align:center; font-size:11px;{c}">{v}</td>'

def scell(v):
    return f'<td style="font-size:11px;">{v}</td>'

def sub(v):
    return f'<td class="gantt-sub-item">{v}</td>'

def act(v, rs):
    return f'<td rowspan="{rs}" class="activity-group">{v}</td>'

D = '#00875A'; W = '#FF8B00'; P = '#97A0AF'

def row(*cells):
    inner = '\n      '.join(cells)
    return f'    <tr>\n      {inner}\n    </tr>'

def plain_row(sub_v, sched_v, sched_c=D, san='-', huh='-', bi='-'):
    """행 (sr/cnt/ind/act 없이): sub + 일정 + Owner + 담당 + 산출물 + 업무현황 + 비고 + SR×4"""
    return row(sub(sub_v), cell(sched_v, sched_c),
               cell('-'), cell('-'),
               scell(san), scell(huh), scell(bi),
               cell('-'), cell('-'), cell('-'), cell('-'))

# ─────────────────────────────────────────
# 시장 섹션 (9 rows, 15 cols per row)
# ─────────────────────────────────────────
시장_ind = ('시장/상품 CAGR<br>상품 시장 점유율<br>'
           '상품 매출액 대비<br>S&amp;M/R&amp;D비용 비율')
시장_sr  = '<td rowspan="9" class="sr-group">시장</td>'
시장_cnt = ('<td rowspan="9" style="text-align:center; font-weight:bold; font-size:12px; '
           'color:#0052CC; vertical-align:middle;">4</td>')
시장_itd = ('<td rowspan="9" style="font-size:10px; vertical-align:top; '
           'padding:3px 4px; line-height:1.6;">' + 시장_ind + '</td>')

시장_rows = '\n'.join([
    row(시장_sr, 시장_cnt, 시장_itd,
        act('지표 수립 및<br>화면 기획', 4),
        sub('지표 수립'), cell('완료 (1-3월)', D),
        cell('-'), cell('-'),
        scell('지표 정의서'), scell('-'), scell('-'),
        cell('-'), cell('-'), cell('-'), cell('-')),
    plain_row('지표 산출식 정의', '완료 (1-3월)', D, '지표 정의서'),
    plain_row('화면 계획', '완료 (1-3월)', D, '화면 기획서'),
    plain_row('화면 디자인', '완료 (1-3월)', D, '화면 시안'),
    row(act('데이터 연계 및<br>화면 개발', 5),
        sub('데이터 분석 및 연계'), cell('완료 (1-3월)', D),
        cell('-'), cell('-'),
        scell('데이터 분석서'),
        scell('엑셀 업로드 방식 (자체 수집)'), scell('-'),
        cell('-'), cell('-'), cell('-'), cell('-')),
    plain_row('지표 기술정의서', '완료 (1-3월)', D, '지표 기술 정의서'),
    plain_row('데이터 모델링,<br>테이블 개발', '완료 (1-3월)', D, '-', '엑셀 업로드 방식 (DB 연계 불필요)'),
    row(sub('Tableau 화면 개발'), cell('완료 (1/22)', D),
        cell('-'), cell('-'),
        scell('화면 기능 개발 요구사항 정의서'),
        scell('1/22 완료'), scell('-'),
        cell('-'), cell('-'), cell('-'), cell('-')),
    row(sub('데이터 정합성 검증'), cell('진행 중 (3-5월)', W),
        cell('-'), cell('-'), scell('-'),
        scell('중기 사업로드맵 업로드 완료,<br>R&amp;D 투자 데이터 업로드 요청 완료 (3/18)'),
        scell('-'),
        cell('-'), cell('-'), cell('-'), cell('-')),
])

# ─────────────────────────────────────────
# 파트너 행 (9 rows, 영업 rowspan 내 - sr/cnt/ind 없음)
# ─────────────────────────────────────────
파트너_rows = '\n'.join([
    row(act('파트너<br>지표 수립 및<br>화면 기획', 4),
        sub('지표 수립'), cell('예정 (5월)', P),
        cell('-'), cell('-'), scell('-'),
        scell('파트너허브 지표 정의 예정'), scell('-'),
        cell('-'), cell('-'), cell('-'), cell('-')),
    plain_row('지표 산출식 정의', '예정 (5월)', P),
    plain_row('화면 계획', '예정 (5월)', P),
    plain_row('화면 디자인', '예정 (5월)', P),
    row(act('파트너<br>데이터 연계 및<br>화면 개발', 5),
        sub('데이터 분석 및 연계'), cell('예정 (6월)', P),
        cell('-'), cell('-'), scell('-'),
        scell('파트너허브 데이터 분석/수집 및 연결'),
        scell('-'),
        cell('-'), cell('-'), cell('-'), cell('-')),
    plain_row('지표 기술정의서', '예정 (6월)', P),
    plain_row('데이터 모델링,<br>테이블 개발', '예정 (6-8월)', P),
    plain_row('Tableau 화면 개발', '예정 (6-8월)', P,
              '화면 기능 개발 요구사항 정의서', '일정: 8/31'),
    plain_row('데이터 정합성 검증', '예정 (8월)', P),
])

# ─────────────────────────────────────────
# 1. 시장 섹션 삽입 (고객/상품 ~ 영업 사이)
# ─────────────────────────────────────────
old_ymark = '\n\n    <!-- ===== 영업 ===== -->'
new_ymark = f'\n\n    <!-- ===== 시장 ===== -->\n{시장_rows}\n\n    <!-- ===== 영업 ===== -->'
assert section.count(old_ymark) == 1, f"영업 marker count: {section.count(old_ymark)}"
section = section.replace(old_ymark, new_ymark)
print("✓ 시장 섹션 삽입")

# ─────────────────────────────────────────
# 2. 영업 rowspan 9→18
# ─────────────────────────────────────────
old_y_sr = '<td rowspan="9" class="sr-group">영업</td>'
new_y_sr = '<td rowspan="18" class="sr-group">영업</td>'
assert section.count(old_y_sr) == 1, f"영업 sr-group count: {section.count(old_y_sr)}"
section = section.replace(old_y_sr, new_y_sr)

old_y_cnt = ('<td rowspan="9" style="text-align:center; font-weight:bold; font-size:12px; '
             'color:#0052CC; vertical-align:middle;">18</td>')
new_y_cnt = ('<td rowspan="18" style="text-align:center; font-weight:bold; font-size:12px; '
             'color:#0052CC; vertical-align:middle;">18</td>')
assert old_y_cnt in section, "영업 cnt_td not found"
section = section.replace(old_y_cnt, new_y_cnt)

old_y_ind = ('<td rowspan="9" style="font-size:10px; vertical-align:top; '
             'padding:3px 4px; line-height:1.6;">(자사)')
new_y_ind = ('<td rowspan="18" style="font-size:10px; vertical-align:top; '
             'padding:3px 4px; line-height:1.6;">(자사)')
assert old_y_ind in section, "영업 ind_td not found"
section = section.replace(old_y_ind, new_y_ind)
print("✓ 영업 rowspan 9→18")

# ─────────────────────────────────────────
# 3. 파트너 행 삽입 (영업 자사 마지막 ~ 대시보드 개선 사이)
# ─────────────────────────────────────────
old_dbmark = '\n\n    <!-- ===== 대시보드 개선 ===== -->'
new_dbmark = (f'\n\n    <!-- ===== 영업: 파트너 ===== -->\n{파트너_rows}'
              f'\n\n    <!-- ===== 대시보드 개선 ===== -->')
assert section.count(old_dbmark) == 1, f"대시보드 개선 marker count: {section.count(old_dbmark)}"
section = section.replace(old_dbmark, new_dbmark)
print("✓ 파트너 행 삽입")

content = before + section
with open('/home/ubuntu/files/meeting_summary_20260521.html', 'w') as f:
    f.write(content)
print("\n파일 저장 완료!")
