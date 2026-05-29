#!/usr/bin/env python3
"""
업무 구분별 세부 진행현황 표에만 '26 추가 지표 수/지표 컬럼 추가
- 월별 업무 진척 표에는 영향 없도록 섹션 분리 후 처리
"""

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'r') as f:
    content = f.read()

# ── 섹션 분리: 업무 구분별 세부 진행현황 이전/이후 ──
ANCHOR = '<p style="font-size:13px; font-weight:bold; color:#172B4D; margin:32px 0 6px;">업무 구분별 세부 진행 현황</p>'
idx = content.index(ANCHOR)
before = content[:idx]
section = content[idx:]

# ── 1. colgroup ──
old_colg = (
    '    <col style="width:70px;"><col style="width:90px;"><col style="width:130px;">\n'
    '    <col style="width:75px;"><col style="width:50px;"><col style="width:50px;">\n'
    '    <col style="width:105px;"><col style="width:105px;"><col style="width:105px;">\n'
    '    <col style="width:85px;"><col style="width:48px;"><col style="width:65px;"><col style="width:80px;">'
)
new_colg = (
    '    <col style="width:70px;"><col style="width:44px;"><col style="width:120px;">'
    '<col style="width:90px;"><col style="width:130px;">\n'
    '    <col style="width:75px;"><col style="width:50px;"><col style="width:50px;">\n'
    '    <col style="width:105px;"><col style="width:105px;"><col style="width:105px;">\n'
    '    <col style="width:85px;"><col style="width:48px;"><col style="width:65px;"><col style="width:80px;">'
)
assert old_colg in section, "colgroup not found in section"
section = section.replace(old_colg, new_colg)
print("✓ colgroup 2 cols 추가")

# ── 2. thead ──
old_th = (
    '      <th style="text-align:center;">구분</th>\n'
    '      <th style="text-align:center;">주요 업무</th>'
)
new_th = (
    '      <th style="text-align:center;">구분</th>\n'
    '      <th style="text-align:center; background-color:#EAE6FF; color:#403294; white-space:nowrap;">\'26 추가<br>지표 수</th>\n'
    '      <th style="text-align:center; background-color:#EAE6FF; color:#403294;">\'26 추가 지표</th>\n'
    '      <th style="text-align:center;">주요 업무</th>'
)
assert old_th in section, "thead th not found"
section = section.replace(old_th, new_th)
print("✓ thead 2 th 추가")

# 공통 helper
def cnt_td(n, v):
    return (f'<td rowspan="{n}" style="text-align:center; font-weight:bold; font-size:12px; '
            f'color:#0052CC; vertical-align:middle;">{v}</td>')

def ind_td(n, v):
    return (f'<td rowspan="{n}" style="font-size:10px; vertical-align:top; '
            f'padding:3px 4px; line-height:1.6;">{v}</td>')

# ── 3. 재무·효율/수익 (rowspan=9) ──
재무_ind = 'CAC · LTV<br>LTV/CAC Ratio<br>Payback Period'
old_r = (
    '      <td rowspan="9" class="sr-group">재무<br>효율/수익</td>\n'
    '      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>'
)
new_r = (
    '      <td rowspan="9" class="sr-group">재무<br>효율/수익</td>\n'
    f'      {cnt_td(9, 4)}\n'
    f'      {ind_td(9, 재무_ind)}\n'
    '      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>'
)
assert old_r in section, "재무 section not found"
section = section.replace(old_r, new_r)
print("✓ 재무 2 cells 추가")

# ── 4. 고객/상품 (rowspan=9) ──
고객_ind = (
    '(VoC) VoC건수·발생률<br>VoC개선/오류 건수<br>'
    'VoC 리드타임<br>VoC 지연건수<br>'
    '(서비스) MAU<br>등록사용자 수<br>상품별 서비스 활성화 지표'
)
old_g = (
    '      <td rowspan="9" class="sr-group">고객/상품</td>\n'
    '      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>'
)
new_g = (
    '      <td rowspan="9" class="sr-group">고객/상품</td>\n'
    f'      {cnt_td(9, 8)}\n'
    f'      {ind_td(9, 고객_ind)}\n'
    '      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>'
)
assert old_g in section, "고객 section not found"
section = section.replace(old_g, new_g)
print("✓ 고객/상품 2 cells 추가")

# ── 5. 영업 (rowspan=9 → 후에 18로 변경) ──
영업_ind = (
    '(자사) 예상 매출액/건수<br>'
    'BO경과기간 · 상태변화율<br>'
    'Sales Lead time<br>'
    'Avg BO Amount<br>'
    'Win/Hit/Conversion Ratio<br>'
    '(파트너) 수주액<br>'
    'BO건수(등급별/상위10)'
)
old_y = (
    '      <td rowspan="9" class="sr-group">영업</td>\n'
    '      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>'
)
new_y = (
    '      <td rowspan="9" class="sr-group">영업</td>\n'
    f'      {cnt_td(9, 18)}\n'
    f'      {ind_td(9, 영업_ind)}\n'
    '      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>'
)
assert old_y in section, "영업 section not found"
section = section.replace(old_y, new_y)
print("✓ 영업 2 cells 추가")

# ── 6. 대시보드 개선 (rowspan=2) ──
old_di = (
    '      <td rowspan="2" class="sr-group">대시보드 개선</td>\n'
    '      <td class="activity-group">성능 개선</td>'
)
new_di = (
    '      <td rowspan="2" class="sr-group">대시보드 개선</td>\n'
    f'      {cnt_td(2, "-")}\n'
    f'      {ind_td(2, "-")}\n'
    '      <td class="activity-group">성능 개선</td>'
)
assert old_di in section, "대시보드 개선 not found"
section = section.replace(old_di, new_di)
print("✓ 대시보드 개선 2 cells 추가")

# ── 7. 대시보드 운영 (rowspan=3) ──
old_do = (
    '      <td rowspan="3" class="sr-group">대시보드 운영</td>\n'
    '      <td class="activity-group">데이터 업로드</td>'
)
new_do = (
    '      <td rowspan="3" class="sr-group">대시보드 운영</td>\n'
    f'      {cnt_td(3, "-")}\n'
    f'      {ind_td(3, "-")}\n'
    '      <td class="activity-group">데이터 업로드</td>'
)
assert old_do in section, "대시보드 운영 not found"
section = section.replace(old_do, new_do)
print("✓ 대시보드 운영 2 cells 추가")

content = before + section
with open('/home/ubuntu/files/meeting_summary_20260521.html', 'w') as f:
    f.write(content)
print("\n파일 저장 완료!")
