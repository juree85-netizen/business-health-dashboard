#!/usr/bin/env python3
"""
전체 일정표 스케줄 바 추가 스크립트
열 순서: '25/12, '26/1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 (총 13개)
"""

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'r') as f:
    content = f.read()

E = 'cell-empty'
D = 'cell-done'
W = 'cell-wip'
P = 'cell-plan'

# 13개 열: '25/12, '26/1~12
# 추론 근거:
# - 효율/수익·VoC·영업: 상세 Gantt 표(SR S26040005889, S26040004737, S26050000095) 기반
# - 서비스활성화: service_activation_indicators.xlsx 존재 → 4-5월 착수
# - 시장: 기존 dashboard에 시장/고객 지표 이미 존재 (1-3월 완료), 데이터 업데이트 진행
# - 파트너: 메모리 "파트너 DB화 5월 개발 착수" 기반
# - On-prem/글로벌SaaS: 2026 하반기 예정
# - 3-6번 과제: 2026 하반기 이후

schedules = [
    # ── 1. 신규 지표 추가 ──
    ('　[효율/수익] 지표 추가',
     [E, D, D, D, D, W, P, P, E, E, E, E, E]),
    ('　[VoC] 지표 추가',
     [E, D, D, D, D, W, P, P, E, E, E, E, E]),
    ('　[서비스활성화] 지표 추가',
     [E, E, E, E, W, W, P, P, P, E, E, E, E]),
    ('　[시장] 지표 추가',
     [E, D, D, D, W, W, E, E, E, E, E, E, E]),
    ('　[영업] 지표 추가',
     [E, D, D, D, D, W, P, P, E, E, E, E, E]),
    ('　[파트너] 지표 추가',
     [E, E, E, E, E, W, W, P, P, E, E, E, E]),
    # ── 2. 신규 상품 추가 ──
    ('　[On-prem] 상품/지표 추가',
     [E, E, E, E, E, E, E, P, P, P, E, E, E]),
    ('　[글로벌SaaS] 상품/지표 추가',
     [E, E, E, E, E, E, E, E, P, P, P, E, E]),
    # ── 3. 사업팀의 대시보드 활용 극대화 ──
    ('　상품별 정기 리뷰 세션',
     [E, D, D, D, D, W, P, P, P, P, P, P, P]),
    ('　사업부 회의체 정보 제공',
     [E, E, E, E, E, W, P, P, P, P, P, P, P]),
    # ── 4. 사업건전성 상태 판단 기준 수립 ──
    ('　성장단계 및 상품특성 정의',
     [E, E, E, E, E, W, P, P, E, E, E, E, E]),
    ('　영역별 지표, 기준값 설정',
     [E, E, E, E, E, E, E, P, P, P, E, E, E]),
    ('　건전성 상태 정의',
     [E, E, E, E, E, E, E, E, E, P, P, E, E]),
    # ── 5. 사업건전성 KPI 후보 Pool 제공 ──
    ('　상품별 핵심지표 선정',
     [E, E, E, E, E, E, E, P, P, P, E, E, E]),
    ('　시뮬레이션 후 기준값 설정',
     [E, E, E, E, E, E, E, E, E, P, P, E, E]),
    ('　후보 Pool 지원팀 제공, 협의',
     [E, E, E, E, E, E, E, E, E, E, P, P, P]),
    # ── 6. 차세대 시스템 전환 ──
    ('　현황 파악 및 분석',
     [E, D, D, D, E, E, E, E, E, E, E, E, E]),
    ('　데이터 연계',
     [E, E, E, E, P, P, P, E, E, E, E, E, E]),
    ('　데이터 모델링, 테이블 개발',
     [E, E, E, E, E, E, E, P, P, P, P, E, E]),
]

LABEL_STYLE = 'padding-left:22px; background-color:#FAFBFC; font-size:11px; color:#344563;'
empty_13 = '<td class="cell-empty"></td>' * 13

def make_cells(pattern):
    return ''.join(f'<td class="{c}"></td>' for c in pattern)

ok = 0
for label, pattern in schedules:
    old = (
        f'      <td style="{LABEL_STYLE}">{label}</td>\n'
        f'      {empty_13}\n'
        f'    </tr>'
    )
    new = (
        f'      <td style="{LABEL_STYLE}">{label}</td>\n'
        f'      {make_cells(pattern)}\n'
        f'    </tr>'
    )
    if old in content:
        content = content.replace(old, new)
        ok += 1
        print(f"✓ {label.strip()}")
    else:
        print(f"✗ NOT FOUND: {label.strip()}")

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'w') as f:
    f.write(content)
print(f"\n완료: {ok}/{len(schedules)}개 행 업데이트, 파일 저장!")
