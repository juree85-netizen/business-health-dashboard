#!/usr/bin/env python3
"""
업무 구분별 세부 진행현황 표 전면 재편:
- 컬럼 추가: Owner, 담당, 산출물 (신규)
- 컬럼명 변경: 업무 구분→주요 업무, 세부 업무→상세 업무, 진행 일정→일정
- 비고 위치: SR 컬럼 앞으로 이동
- 전체 데이터 갱신 (사용자 제공 기준)
"""

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'r') as f:
    content = f.read()

# ─── 구 테이블 시작/끝 마커 ───
OLD_START = '<p style="font-size:13px; font-weight:bold; color:#172B4D; margin:32px 0 6px;">업무 구분별 세부 진행 현황</p>\n<table style="font-size:12px;">'
OLD_END   = '\n\n  </tbody>\n</table>\n\n<p style="font-size:13px; font-weight:bold; color:#172B4D; margin:32px 0 6px;">SR 진행현황</p>'

assert OLD_START in content, "테이블 시작 마커 not found"
assert OLD_END   in content, "테이블 끝 마커 not found"

# ─── 셀 헬퍼 ───
def c(val, align='center', color=None, bold=False):
    s = f'text-align:{align}; font-size:11px;'
    if color:  s += f' color:{color};'
    if bold:   s += ' font-weight:bold;'
    return f'      <td style="{s}">{val}</td>'

def cl(val):  # left-aligned text cell
    return f'      <td style="font-size:11px;">{val}</td>'

GREEN  = '#00875A'
ORANGE = '#FF8B00'
GRAY   = '#97A0AF'

def done(period): return c(f'완료 ({period})', color=GREEN)
def wip(period):  return c(f'진행 중 ({period})', color=ORANGE)
def plan(period): return c(f'예정 ({period})', color=GRAY)
def dash():       return c('-')
def dashes(n):    return '\n'.join([dash()] * n)

DELIV_STD = 'DB 테이블 요구사항 정의서,<br>DB 테이블 설계서, SR 요청서'
DELIV_TAB = '화면 기능 개발 요구사항<br>정의서, SR 요청서'

# ─── 신규 테이블 HTML ───
NEW_TABLE = '''\
<p style="font-size:13px; font-weight:bold; color:#172B4D; margin:32px 0 6px;">업무 구분별 세부 진행 현황</p>
<table style="font-size:11px; table-layout:fixed; width:100%;">
  <colgroup>
    <col style="width:70px;"><col style="width:90px;"><col style="width:130px;">
    <col style="width:75px;"><col style="width:50px;"><col style="width:50px;">
    <col style="width:105px;"><col style="width:105px;"><col style="width:105px;">
    <col style="width:85px;"><col style="width:48px;"><col style="width:65px;"><col style="width:80px;">
  </colgroup>
  <thead>
    <tr>
      <th style="text-align:center;">구분</th>
      <th style="text-align:center;">주요 업무</th>
      <th style="text-align:left; padding-left:8px;">상세 업무</th>
      <th>일정</th>
      <th>Owner</th>
      <th>담당</th>
      <th>산출물</th>
      <th>업무 현황</th>
      <th>비고</th>
      <th>SR No.</th>
      <th>SR<br>요청자</th>
      <th>SR 처리<br>담당자</th>
      <th>SR 완료<br>요청일</th>
    </tr>
  </thead>
  <tbody>

    <!-- ===== 재무·효율/수익 ===== -->
    <tr>
      <td rowspan="9" class="sr-group">재무<br>효율/수익</td>
      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>
      <td class="gantt-sub-item">지표 수립</td>
''' + done('1-3월') + '\n' + dash() + '\n' + dash() + '\n' + cl('지표 정의서') + '\n' + dash() + '\n' + dash() + '\n' + dashes(4) + '''
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 산출식 정의</td>
''' + done('1-3월') + '\n' + dash() + '\n' + dash() + '\n' + cl('지표 정의서') + '\n' + dash() + '\n' + dash() + '\n' + dashes(4) + '''
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 계획</td>
''' + done('1-3월') + '\n' + dash() + '\n' + dash() + '\n' + cl('화면 기획서') + '\n' + dash() + '\n' + dash() + '\n' + dashes(4) + '''
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 디자인</td>
''' + done('1-3월') + '\n' + dash() + '\n' + dash() + '\n' + cl('화면 시안') + '\n' + dash() + '\n' + dash() + '\n' + dashes(4) + '''
    </tr>
    <tr>
      <td rowspan="5" class="activity-group">데이터 연계 및<br>화면 개발</td>
      <td class="gantt-sub-item">데이터 분석 및 연계</td>
''' + done('1-2월') + '\n' + dash() + '\n' + dash() + '\n' + cl('데이터 분석서') + '\n' + cl('Orderlist 데이터 연계 완료') + '\n' + dash() + '\n' + dashes(4) + '''
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 기술정의서</td>
''' + done('2-3월') + '\n' + dash() + '\n' + dash() + '\n' + cl('지표 기술 정의서') + '\n' + dash() + '\n' + dash() + '\n' + dashes(4) + '''
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 모델링,<br>테이블 개발</td>
''' + dash() + '\n' + dash() + '\n' + dash() + '\n' + cl(DELIV_STD) + '\n' + cl('(SDSC) 진행 현황 미파악') + '\n' + cl('(SDSC) 담당자 확인 후 공유') + '''
      <td style="text-align:center; font-size:11px;">S26040005889</td>
      <td style="text-align:center; font-size:11px;">유주리</td>
      <td style="text-align:center; font-size:11px;">김연홍</td>
      <td style="text-align:center; font-size:11px;">2026-04-23</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">Tableau 화면 개발</td>
''' + wip('4-5월') + '\n' + dash() + '\n' + dash() + '\n' + cl(DELIV_TAB) + '\n' + cl('(SDSC) 진행 현황 미파악') + '\n' + cl('(SDSC) 담당자 확인 후 공유') + '''
      <td style="text-align:center; font-size:11px;">S26040005889</td>
      <td style="text-align:center; font-size:11px;">유주리</td>
      <td style="text-align:center; font-size:11px;">김연홍</td>
      <td style="text-align:center; font-size:11px;">2026-04-23</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 정합성 검증</td>
''' + plan('5-6월') + '\n' + dash() + '\n' + dash() + '\n' + dash() + '\n' + cl('(SDSC) 5-6월 진행 예정') + '\n' + dash() + '\n' + dashes(4) + '''
    </tr>

    <!-- ===== 고객/상품 ===== -->
    <tr>
      <td rowspan="9" class="sr-group">고객/상품</td>
      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>
      <td class="gantt-sub-item">지표 수립</td>
''' + done('1-3월') + '\n' + dash() + '\n' + dash() + '\n' + cl('지표 정의서') + '\n' + dash() + '\n' + dash() + '\n' + dashes(4) + '''
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 산출식 정의</td>
''' + done('1-3월') + '\n' + dash() + '\n' + dash() + '\n' + cl('지표 정의서') + '\n' + dash() + '\n' + dash() + '\n' + dashes(4) + '''
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 계획</td>
''' + done('1-3월') + '\n' + dash() + '\n' + dash() + '\n' + cl('화면 기획서') + '\n' + dash() + '\n' + dash() + '\n' + dashes(4) + '''
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 디자인</td>
''' + done('1-3월') + '\n' + dash() + '\n' + dash() + '\n' + cl('화면 시안') + '\n' + dash() + '\n' + dash() + '\n' + dashes(4) + '''
    </tr>
    <tr>
      <td rowspan="5" class="activity-group">데이터 연계 및<br>화면 개발</td>
      <td class="gantt-sub-item">데이터 분석 및 연계</td>
''' + wip('3-6월') + '\n' + dash() + '\n' + dash() + '\n' + cl('데이터 분석서') + '\n' + dash() + '\n' + dash() + '\n' + dashes(4) + '''
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 기술정의서</td>
''' + done('3-4월') + '\n' + dash() + '\n' + dash() + '\n' + cl('지표 기술 정의서') + '\n' + dash() + '\n' + dash() + '\n' + dashes(4) + '''
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 모델링,<br>테이블 개발</td>
''' + wip('4-6월') + '\n' + dash() + '\n' + dash() + '\n' + cl(DELIV_STD) + '\n' + cl('(상품CS관리그룹) 오은성 프로님 인터페이스 작업 선행 필요 (6월 완료 예정)') + '\n' + cl('(상품CS관리그룹) 오은성 프로님 일정 업데이트 공유 예정') + '''
      <td style="text-align:center; font-size:11px;">S26040004737</td>
      <td style="text-align:center; font-size:11px;">유주리</td>
      <td style="text-align:center; font-size:11px;">오은성</td>
      <td style="text-align:center; font-size:11px;">2026-04-30</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">Tableau 화면 개발</td>
''' + plan('6월') + '\n' + dash() + '\n' + dash() + '\n' + cl(DELIV_TAB) + '\n' + dash() + '\n' + dash() + '''
      <td style="text-align:center; font-size:11px;">S26040004737</td>
      <td style="text-align:center; font-size:11px;">유주리</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">2026-04-30</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 정합성 검증</td>
''' + plan('6-7월') + '\n' + dash() + '\n' + dash() + '\n' + dash() + '\n' + dash() + '\n' + dash() + '\n' + dashes(4) + '''
    </tr>

    <!-- ===== 영업 ===== -->
    <tr>
      <td rowspan="9" class="sr-group">영업</td>
      <td rowspan="4" class="activity-group">지표 수립 및<br>화면 기획</td>
      <td class="gantt-sub-item">지표 수립</td>
''' + done('1-3월') + '\n' + dash() + '\n' + dash() + '\n' + cl('지표 정의서') + '\n' + dash() + '\n' + dash() + '\n' + dashes(4) + '''
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 산출식 정의</td>
''' + done('1-3월') + '\n' + dash() + '\n' + dash() + '\n' + cl('지표 정의서') + '\n' + dash() + '\n' + dash() + '\n' + dashes(4) + '''
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 계획</td>
''' + done('1-3월') + '\n' + dash() + '\n' + dash() + '\n' + cl('화면 기획서') + '\n' + dash() + '\n' + dash() + '\n' + dashes(4) + '''
    </tr>
    <tr>
      <td class="gantt-sub-item">화면 디자인</td>
''' + done('1-3월') + '\n' + dash() + '\n' + dash() + '\n' + cl('화면 시안') + '\n' + dash() + '\n' + dash() + '\n' + dashes(4) + '''
    </tr>
    <tr>
      <td rowspan="5" class="activity-group">데이터 연계 및<br>화면 개발</td>
      <td class="gantt-sub-item">데이터 분석 및 연계</td>
''' + wip('3-5월') + '\n' + dash() + '\n' + dash() + '\n' + cl('데이터 분석서') + '\n' + dash() + '\n' + dash() + '\n' + dashes(4) + '''
    </tr>
    <tr>
      <td class="gantt-sub-item">지표 기술정의서</td>
''' + wip('3-4월') + '\n' + dash() + '\n' + dash() + '\n' + cl('지표 기술 정의서') + '\n' + dash() + '\n' + dash() + '\n' + dashes(4) + '''
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 모델링,<br>테이블 개발</td>
''' + wip('4-6월') + '\n' + dash() + '\n' + dash() + '\n' + cl(DELIV_STD) + '\n' + cl('중복 데이터 문제로 뷰 테이블 스크립트 미완성') + '\n' + cl('이번 달 말 완료 가능 여부 확인 후 회신') + '''
      <td style="text-align:center; font-size:11px;">S26050000095</td>
      <td style="text-align:center; font-size:11px;">김범준</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">2026-05-14</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">Tableau 화면 개발</td>
''' + wip('4-5월') + '\n' + dash() + '\n' + dash() + '\n' + cl(DELIV_TAB) + '\n' + dash() + '\n' + dash() + '''
      <td style="text-align:center; font-size:11px;">S26050000095</td>
      <td style="text-align:center; font-size:11px;">김범준</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">2026-05-14</td>
    </tr>
    <tr>
      <td class="gantt-sub-item">데이터 정합성 검증</td>
''' + wip('5-6월') + '\n' + dash() + '\n' + dash() + '\n' + dash() + '\n' + dash() + '\n' + dash() + '\n' + dashes(4) + '''
    </tr>

    <!-- ===== 대시보드 개선 ===== -->
    <tr>
      <td rowspan="2" class="sr-group">대시보드 개선</td>
      <td class="activity-group">성능 개선</td>
      <td class="gantt-sub-item">-</td>
''' + done('3-4월') + '\n' + dash() + '\n' + dash() + '\n' + dash() + '\n' + cl('Tableau 통합 문서 분리하여 화면 로딩 및 처리 속도 개선 (기존 45초 → 10초로 단축)') + '\n' + dash() + '''
      <td style="text-align:center; font-size:11px;">S26030007696</td>
      <td style="text-align:center; font-size:11px;">유주리</td>
      <td style="text-align:center; font-size:11px;">염효결</td>
      <td style="text-align:center; font-size:11px;">2026-03-28</td>
    </tr>
    <tr>
      <td class="activity-group">속도 개선 후<br>화면 수정</td>
      <td class="gantt-sub-item">-</td>
''' + plan('6월 1주') + '\n' + dash() + '\n' + dash() + '\n' + dash() + '\n' + cl('기존 설계와 달라진 부분 다수 발견 (오른쪽 정렬, 기준 연월 표시, 한 화면 레이아웃 등)') + '\n' + cl('솔루션전략이 이슈 리스트업 후 메일 공유 예정') + '\n' + dashes(4) + '''
    </tr>

    <!-- ===== 대시보드 운영 ===== -->
    <tr>
      <td rowspan="3" class="sr-group">대시보드 운영</td>
      <td class="activity-group">데이터 업로드</td>
      <td class="gantt-sub-item">기준 연월 오류</td>
''' + dash() + '\n' + dash() + '\n' + dash() + '\n' + dash() + '\n' + cl('화면에 4월이 아닌 3월로 표시됨 (4월 실적 미반영)') + '\n' + cl('회의 후 즉시 확인') + '\n' + dashes(4) + '''
    </tr>
    <tr>
      <td class="activity-group">데이터 수작업 업로드</td>
      <td class="gantt-sub-item">데이터 수작업 업로드<br>(시장/고객)</td>
''' + plan('5월') + '\n' + dash() + '\n' + dash() + '\n' + dash() + '\n' + cl('엑셀 데이터 기반, 3년치 데이터 미표시 오류 / 엑셀 공유됨') + '\n' + cl('업데이트 엑셀 재공유 후 피드백') + '''
      <td style="text-align:center; font-size:11px;">S26030004582</td>
      <td style="text-align:center; font-size:11px;">유주리</td>
      <td style="text-align:center; font-size:11px;">-</td>
      <td style="text-align:center; font-size:11px;">2026-03-19</td>
    </tr>
    <tr>
      <td class="activity-group">데이터 정합성 검증</td>
      <td class="gantt-sub-item">-</td>
''' + dash() + '\n' + dash() + '\n' + dash() + '\n' + dash() + '\n' + dash() + '\n' + dash() + '\n' + dashes(4) + '''
    </tr>

  </tbody>
</table>'''

# ─── 구 테이블 전체 교체 ───
old_section = OLD_START + content[content.index(OLD_START) + len(OLD_START): content.index(OLD_END) + len(OLD_END) - len('\n\n<p style="font-size:13px; font-weight:bold; color:#172B4D; margin:32px 0 6px;">SR 진행현황</p>')]

# Find and replace between the two markers
start_idx = content.index(OLD_START)
end_tag = '</table>'
# Find the </table> that closes the 세부 진행현황 table
# It's the one just before the SR 진행현황 paragraph
sr_idx = content.index('\n<p style="font-size:13px; font-weight:bold; color:#172B4D; margin:32px 0 6px;">SR 진행현황</p>')
# Work backward from sr_idx to find </table>
end_idx = content.rindex(end_tag, 0, sr_idx) + len(end_tag)

old_block = content[start_idx:end_idx]
content = content[:start_idx] + NEW_TABLE + content[end_idx:]

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'w') as f:
    f.write(content)
print("✓ 업무 구분별 세부 진행현황 표 전면 재편 완료")
print(f"  교체 블록: {len(old_block)} → {len(NEW_TABLE)} 문자")
