#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Medallia 사례보고서 — analysis-report-standard.md 기준 Word 문서 생성
"""
import sys, os
from docx import Document
from docx.shared import Pt, Mm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BATANG = '바탕체'
PT_BODY  = 14
PT_TITLE = 20
PT_PGNUM = 12

# ── 폰트 헬퍼 ──────────────────────────────────────────────────────────────────

def set_font(run, size=PT_BODY, bold=False, italic=False, underline=False, color=None):
    run.font.name = BATANG
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.underline = underline
    if color:
        run.font.color.rgb = RGBColor(*color)
    rpr = run._r.get_or_add_rPr()
    rf = rpr.find(qn('w:rFonts'))
    if rf is None:
        rf = OxmlElement('w:rFonts'); rpr.insert(0, rf)
    for a in ('w:ascii','w:hAnsi','w:eastAsia','w:cs'):
        rf.set(qn(a), BATANG)

def set_pf(para, before=0, after=0, align=WD_ALIGN_PARAGRAPH.LEFT):
    pf = para.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after  = Pt(after)
    pf.line_spacing_rule = WD_LINE_SPACING.SINGLE
    para.alignment = align

def add_run(para, text, **kw):
    r = para.add_run(text)
    set_font(r, **kw)
    return r

# ── 문서 초기 설정 ────────────────────────────────────────────────────────────

def setup_doc():
    doc = Document()
    sec = doc.sections[0]
    sec.page_width      = Mm(210)
    sec.page_height     = Mm(297)
    sec.top_margin      = Mm(20)
    sec.bottom_margin   = Mm(20)
    sec.left_margin     = Mm(20)
    sec.right_margin    = Mm(20)
    sec.footer_distance = Mm(8)
    # Normal 스타일 — 바탕체 14pt
    sty = doc.styles['Normal']
    sty.font.name = BATANG
    sty.font.size = Pt(PT_BODY)
    el = sty.element
    rpr = el.find(qn('w:rPr'))
    if rpr is None:
        rpr = OxmlElement('w:rPr'); el.append(rpr)
    rf = rpr.find(qn('w:rFonts'))
    if rf is None:
        rf = OxmlElement('w:rFonts'); rpr.insert(0, rf)
    for a in ('w:ascii','w:hAnsi','w:eastAsia','w:cs'):
        rf.set(qn(a), BATANG)
    return doc

# ── 바닥글 페이지 번호 ─────────────────────────────────────────────────────────

def add_footer(doc):
    sec = doc.sections[0]
    ftr = sec.footer
    ftr.is_linked_to_previous = False
    para = ftr.paragraphs[0] if ftr.paragraphs else ftr.add_paragraph()
    for ch in list(para._p): para._p.remove(ch)
    set_pf(para, align=WD_ALIGN_PARAGRAPH.CENTER)
    add_run(para, '- ', size=PT_PGNUM)
    # PAGE 필드
    for ftype in ('begin', None, 'end'):
        r = para.add_run()
        set_font(r, size=PT_PGNUM)
        if ftype in ('begin','end'):
            fc = OxmlElement('w:fldChar')
            fc.set(qn('w:fldCharType'), ftype)
            r._r.append(fc)
        else:
            it = OxmlElement('w:instrText')
            it.set(qn('xml:space'), 'preserve')
            it.text = ' PAGE '
            r._r.append(it)
    add_run(para, ' -', size=PT_PGNUM)

# ── 요약 표 (1행 3열) ──────────────────────────────────────────────────────────

def add_summary_table(doc, lines):
    tbl = doc.add_table(rows=1, cols=3)
    tbl.alignment = WD_TABLE_ALIGNMENT.LEFT
    tpr = tbl._tbl.find(qn('w:tblPr'))
    if tpr is None:
        tpr = OxmlElement('w:tblPr'); tbl._tbl.insert(0, tpr)
    # 전체 테두리 제거
    tb = OxmlElement('w:tblBorders')
    for s in ('top','left','bottom','right','insideH','insideV'):
        e = OxmlElement(f'w:{s}'); e.set(qn('w:val'),'nil'); tb.append(e)
    tpr.append(tb)
    # 자동 맞춤 해제
    tl = OxmlElement('w:tblLayout'); tl.set(qn('w:type'),'fixed'); tpr.append(tl)

    def cell_w(cell, dxa):
        cp = cell._tc.get_or_add_tcPr()
        cw = OxmlElement('w:tcW')
        cw.set(qn('w:w'), str(dxa)); cw.set(qn('w:type'),'dxa')
        cp.append(cw)

    def cell_margin(cell, l=0, r=0, t=0, b=0):
        cp = cell._tc.get_or_add_tcPr()
        cm = OxmlElement('w:tcMar')
        for s,v in (('left',l),('right',r),('top',t),('bottom',b)):
            e = OxmlElement(f'w:{s}')
            e.set(qn('w:w'),str(v)); e.set(qn('w:type'),'dxa')
            cm.append(e)
        cp.append(cm)

    def cell_borders(cell, has, nil):
        cp = cell._tc.get_or_add_tcPr()
        cb = OxmlElement('w:tcBorders')
        for s in has:
            e = OxmlElement(f'w:{s}')
            e.set(qn('w:val'),'single'); e.set(qn('w:sz'),'4')
            e.set(qn('w:color'),'000000'); cb.append(e)
        for s in nil:
            e = OxmlElement(f'w:{s}'); e.set(qn('w:val'),'nil'); cb.append(e)
        cp.append(cb)

    NARROW = 140    # 7pt × 20 = 140 twips
    CWIDE  = 9353   # 165mm × 56.69 ≈ 9353 twips
    LC = tbl.cell(0,0); MC = tbl.cell(0,1); RC = tbl.cell(0,2)
    cell_w(LC, NARROW); cell_w(MC, CWIDE); cell_w(RC, NARROW)
    cell_margin(LC); cell_margin(RC)
    cell_margin(MC, l=28, r=28)   # 좌우 1.4pt
    cell_borders(LC, ['top','left','bottom'], ['right'])
    cell_borders(MC, [], ['top','left','bottom','right'])
    cell_borders(RC, ['top','right','bottom'], ['left'])
    # 좌우 셀 빈 단락
    for cell in (LC, RC):
        set_pf(cell.paragraphs[0])
    # 가운데 셀 — 3줄
    for i, line in enumerate(lines[:3]):
        p = MC.paragraphs[0] if i == 0 else MC.add_paragraph()
        set_pf(p, before=0, after=9)
        add_run(p, ' ' + line)   # 선행 Space 1칸

# ── 일반 표 ───────────────────────────────────────────────────────────────────

def add_table(doc, headers, rows):
    tbl = doc.add_table(rows=1+len(rows), cols=len(headers))
    tbl.style = 'Table Grid'
    tbl.alignment = WD_TABLE_ALIGNMENT.LEFT
    tpr = tbl._tbl.find(qn('w:tblPr'))
    if tpr is None:
        tpr = OxmlElement('w:tblPr'); tbl._tbl.insert(0, tpr)
    tw = OxmlElement('w:tblW')
    tw.set(qn('w:w'),'5000'); tw.set(qn('w:type'),'pct'); tpr.append(tw)
    # 헤더
    for ci, h in enumerate(headers):
        cell = tbl.rows[0].cells[ci]
        cp = cell._tc.get_or_add_tcPr()
        shd = OxmlElement('w:shd')
        shd.set(qn('w:val'),'clear'); shd.set(qn('w:color'),'auto')
        shd.set(qn('w:fill'),'1E1E1E'); cp.append(shd)
        p = cell.paragraphs[0]
        set_pf(p, before=1, after=1, align=WD_ALIGN_PARAGRAPH.CENTER)
        add_run(p, h, size=13, bold=True, color=(0xFF,0xFF,0xFF))
    # 데이터
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            cell = tbl.rows[1+ri].cells[ci]
            p = cell.paragraphs[0]
            set_pf(p, before=1, after=1)
            add_run(p, str(val), size=13)

# ── 페이지 나누기 ─────────────────────────────────────────────────────────────

def page_break(doc):
    p = doc.add_paragraph()
    r = p.add_run()
    br = OxmlElement('w:br'); br.set(qn('w:type'),'page'); r._r.append(br)
    set_pf(p)

# ── 콘텐츠 정의 ───────────────────────────────────────────────────────────────

REPORT = [
    # ── 요약 ──
    ('summary', [
        "'21.7月 Thoma Bravo의 Medallia 인수($6.4B)는 고배수 LBO·변동금리·성장률 과대 추정이 복합 작용하여 '26年 에쿼티 $5B 전액 손실로 귀결됨",
        "이자비용($300M)의 EBITDA($200M) 초과 및 FCF 전액 이자 투입으로 인한 제품 혁신 중단이 핵심 실패 원인으로 판단됨",
        "표면 지표(매출·EBITDA) 중심 평가 한계 보완을 위해 FCF 및 EV/Par Coverage 지표를 사업건전성 대시보드에 추가 검토 필요",
    ]),
    # ── 1. 보고 개요 ──
    ('lv1','1. 보고 개요'),
    ('lv2','분석 배경'),
    ('lv3',"'21.7月 Thoma Bravo, Medallia를 $6.4B(매출 9배)에 인수·상장폐지"),
    ('lv3',"'22~'23年 美 연준 금리 인상(SOFR 5.4%)으로 이자부담 급증 — 연이자 $135M → $300M"),
    ('lv3',"'26年 채권단(Blackstone 等)에 경영권 이전 결정 → 에쿼티 $5B 전액 손실 확정"),
    ('lv2','분석 목적'),
    ('lv3',"PE·LBO 구조의 구조적 실패 원인 진단"),
    ('lv3',"성장률·EBITDA 중심 평가의 한계 확인"),
    ('lv3',"Rule of 40·FCF·NRR 기반 건전성 평가 체계 도출"),
    ('lv3',"사업건전성 대시보드 운영 방향 시사점 제시"),
    ('lv2','분석 범위'),
    ('lv3',"분석 대상: Medallia, Inc. / Thoma Bravo, LP"),
    ('lv3',"분석 기간: '01年 설립 ~ '26年 경영권 이전"),
    ('lv3',"재무 수치 출처: OnlyCFO('26.5月), Bloomberg('26.4月) 분석 기반 추정치"),
    # ── 2. 주요 발견사항 ──
    ('lv1','2. 주요 발견사항'),
    ('lv2','핵심 판단'),
    ('lv3',"이자비용($300M)이 EBITDA($200M)를 초과하는 구조적 적자 — 표면 지표만으로는 실패 감지 불가"),
    ('lv3',"변동금리 LBO 구조에서 금리 상승 리스크 미반영이 핵심 취약점"),
    ('lv3',"FCF 전액 이자 투입으로 AI 시대 제품 혁신 불가 → 고객 이탈 가속화 악순환"),
    ('arrow','고배수 LBO + 변동금리 + 성장 과대 추정의 3중 실패 구조'),
    ('lv2','주요 발견'),
    ('lv3',"PIK 조항 발동으로 부채 $1.8B → $2.8B 복리 팽창 (약 $1B 누적)"),
    ('lv3',"EBITDA 양호($200M)에도 이자조차 감당 불가 — 전통적 재무 건전성 기준의 중요성 확인"),
    ('lv3',"M&A·IPO 시장 동결로 PE 통상 회수 수단 전면 차단"),
    ('lv2','의사결정 포인트'),
    ('lv3',"SaaS 기업가치 평가 時 SaaS 특화 지표와 전통 재무 지표 병행 관리 필요"),
    ('lv3',"변동금리 조달 구조 채택 時 금리 시나리오 분석 의무화 검토 필요"),
    # ── 3. 분석 내용 ──
    ('lv1','3. 분석 내용'),
    ('lv2','Medallia 기업 현황'),
    ('lv3',"설립: '01年, 미국 샌프란시스코 소재 CX(고객경험) 관리 플랫폼 전문기업"),
    ('lv3',"주요 오퍼링: 고객 피드백 수집·분석, NPS(고객순추천지수) 측정, EX(직원경험) 플랫폼"),
    ('lv3',"고객군: 금융·항공·호텔·통신 글로벌 대기업(Fortune 500 다수)"),
    ('lv3',"'19.7月 NYSE 상장(MDLA) → '21.10月 Thoma Bravo 인수로 상장폐지"),
    ('lv2','주요 재무 현황 (비상장 전환 후)'),
    ('table',
     ['항목','수치','비고'],
     [
         ['연간 매출(추정)','약 $700M','인수 당시 기준'],
         ['연간 EBITDA','약 $200M','표면상 양호'],
         ['부채 잔액','약 $2.8B','PIK 이자 누적 ($1.8B → 팽창)'],
         ['연간 이자비용','약 $300M','EBITDA 초과 — 구조적 적자'],
         ['인수 Valuation',"$6.4B (매출 9배)","'21年 저금리 환경 기준"],
     ]),
    ('lv5',"이자비용($300M) > EBITDA($200M) — EBITDA 기준으로는 건전해 보이나 실제 구조적 파산 진행 中"),
    ('lv5',"PIK(Payment-in-Kind): 현금 이자 대신 미납 이자를 원금에 가산하는 방식 (원금 복리 팽창 구조)"),
    ('lv2','인수·투자 주요 이력'),
    ('lv3',"'01年: 美 샌프란시스코 설립, CX 피드백 관리 솔루션으로 엔터프라이즈 시장 진입"),
    ('lv3',"'15~'18年: VC·성장단계 PE로부터 복수 투자 유치, Fortune 500 고객 확보로 시장 지위 강화"),
    ('lv3',"'19.7月: NYSE 상장(MDLA), 공모가 $21. FY2020 연매출 $477M, 순손실 -$149M"),
    ('lv3',"'21.7月: Thoma Bravo, $6.4B에 주식 100% 인수·상장폐지"),
    ('lv4',"인수배수: 연매출 약 9배 (고성장 SaaS 프리미엄 적용)"),
    ('lv4',"조달구조: 에쿼티 약 $4.6B + 변동금리 부채 $1.8B (당시 LIBOR 0.75%)"),
    ('lv4',"내재 취약점: 변동금리 구조 — 금리 상승 時 이자부담 LIBOR/SOFR 연동으로 자동 급증"),
    ('lv3',"'22~'23年: 美 연준 금리 인상(SOFR 5.4%)으로 이자부담 급증"),
    ('lv4',"연이자 $135M → $300M으로 2배 이상 급등 (SOFR 연동 변동금리 직격)"),
    ('lv4',"PIK 조항 발동: 현금 이자 납부 불가 → 미납 이자를 원금에 가산하는 방식 전환"),
    ('lv4',"부채 팽창: $1.8B → 약 $2.8B (약 $1B이 이자로 원금에 누적 편입)"),
    ('lv3',"'24~'25年: M&A 시장 동결·IPO 시장 폐쇄로 회수 경로 차단"),
    ('lv4',"전략적 매각·레버리지 리캡·IPO 재추진 검토 → 고부채($2.8B) 구조로 협상 결렬"),
    ('lv4',"FCF 전액 이자 상환 투입 → 제품 로드맵 사실상 동결"),
    ('lv3',"'26年: TB, 채권단(Blackstone 等)에 경영권 이전 결정 → $5B 투자 전액 손실 확정"),
    ('lv4',"Debt-to-Equity Swap: 채권단 보유 $2.8B 채권을 지분으로 전환, 구(舊) 에쿼티 전액 소멸"),
    ('lv4',"Blackstone 주도 채권단 → 실질 최대주주 전환. PE 투자 역사상 최대 규모 SaaS LBO 실패 사례"),
    ('lv2','구조적 실패 요인 진단'),
    ('table',
     ['실패 요인','내용'],
     [
         ['① 부채구조 취약성',"변동금리 대출 → 금리 인상으로 이자 $135M → $300M. PIK 이자 누적으로 원금 $1.8B → $2.8B"],
         ['② 성장률 과대 추정',"고성장 지속 전제로 매출 9배 밸류에이션 적용. 경기 둔화·AI 경쟁 심화로 성장 정체"],
         ['③ 출구 경로 차단',"M&A 시장 동결, IPO 시장 폐쇄. $2.8B 부채 구조가 잠재 인수자 협상 결렬 야기"],
         ['④ 혁신 투자 소진',"FCF 전액 이자 상환 투입 → AI 시대 신제품 개발 불가. NRR 하락 → FCF 악화 악순환"],
     ]),
    ('lv2','예상 파급 효과'),
    ('lv3',"Medallia 고객사: 투자·개발 축소로 서비스 품질 저하 및 로드맵 불확실성 증가"),
    ('lv4',"Qualtrics·Salesforce 等 경쟁사의 Medallia 고객 유치 공세 강화 — 이탈 가속화 우려"),
    ('lv3',"PE 업계: 유사 구조(고배수 LBO + 변동금리) 소프트웨어 기업 연쇄 부실화 시그널"),
    ('lv3',"민간 신용 시장: Blackstone 等 채권자도 원금 전액 회수 불확실 → Private Credit 시장 리스크 현실화"),
    ('lv3',"소프트웨어 M&A 시장: 고부채 매물 디스카운트 딜 증가, 전략적 인수자(Strategic Buyer)에게 유리한 시장 형성"),
    ('lv2',"동일 구조 위험 노출 대표 사례 ('21~'22年 고배수 LBO 인수 기업)"),
    ('table',
     ['기업명','PE 인수사','인수 시기','인수금액','사업 영역'],
     [
         ['Proofpoint','Thoma Bravo',"'21.4月",'$12.3B','사이버보안 SaaS'],
         ['RealPage','Thoma Bravo',"'21.4月",'$10.2B','부동산 관리 SaaS'],
         ['Stamps.com','Thoma Bravo',"'21.10月",'$6.6B','우편·배송 SaaS'],
         ['Zendesk','Permira·H&F',"'22.11月",'$10.2B','CX SaaS'],
         ['Avalara','Vista Equity',"'22.10月",'$8.4B','세금 자동화 SaaS'],
         ['SailPoint','Thoma Bravo',"'22.4月",'$6.9B','ID 보안 SaaS'],
     ]),
    ('lv5',"'21~'22年 저금리 환경에서 9~10배 이상 배수로 인수된 소프트웨어 기업 상당수가 동일한 구조적 문제(고부채 + 변동금리)에 직면할 것으로 전망 (OnlyCFO 추산)"),
    # ── 4. 리스크 및 제약 ──
    ('lv1','4. 리스크 및 제약'),
    ('lv2','불확실성'),
    ('lv3',"'21年 비상장 전환 후 재무 정보 비공개 — 이자비용·EBITDA·FCF 등 핵심 수치는 추정치"),
    ('lv3',"채권단 원금 회수율, Medallia 현재 매출·고객 이탈 규모 미확인"),
    ('lv2','미확인 정보'),
    ('lv3',"PIK 이자 적용 이후 확정 부채 규모 (약 $2.8B는 추정값)"),
    ('lv3',"채권단 구조조정 이후 Medallia 사업 지속 여부 및 매각 일정"),
    ('lv3',"'26.4.30 Bloomberg 보도 이후 추가 협상 경과"),
    ('lv2','실행상 유의사항'),
    ('lv3',"사업건전성 대시보드 적용 時 산식·멀티플 기준을 내부 사업부와 협의 후 확정 필요"),
    ('lv3',"국내 B2B SaaS 시장 멀티플(5~8배 예상)은 시범 산출 후 검증 필요"),
    ('lv3',"Medallia 사례는 외부 PE 투자 구조 기반 — 내부 SaaS 운영 기준 적용 時 조정 필요"),
    # ── 5. 시사점 및 권고안 ──
    ('lv1','5. 시사점 및 권고안'),
    ('lv2','SaaS 기업가치 평가 기준 확장 필요'),
    ('table',
     ['평가 기준 유형','주요 지표','Medallia 사례에서의 의미'],
     [
         ['SaaS 특화 기준','ARR 성장률, Rule of 40, NRR','성장·수익·고객유지 균형 측정 — 세 지표 모두에서 사전 경고 신호 有'],
         ['전통적 기준','누적 차입금액, 누적 적자금액, FCF','$2.8B 부채 팽창·EBITDA 초과 이자는 전통 기준으로만 가시화 가능한 구조적 위험'],
     ]),
    ('lv2','사업건전성 대시보드 현금흐름 지표 관리 검토'),
    ('lv3',"FCF = 영업이익(영업현금흐름) − CAPEX"),
    ('lv3',"EV(Enterprise Value) = Annual FCF × Multiple(시장 평균 멀티플 × 할인률)"),
    ('lv3',"EV/Par Coverage Ratio = EV ÷ Loan Par(누적 차입금/적자금액) → 1 이상 유지 필요"),
    ('lv4',"1 미만 時: 기업가치가 누적 부채를 커버하지 못하는 구조적 위험 신호"),
    ('lv4',"Medallia의 경우 EV 급락 + Loan Par $2.8B 팽창으로 임계치 이하 하락 → 경영권 상실"),
    ('lv5',"내부 적용 기준(안): Annual FCF = 영업현금흐름 기준 / Multiple = 국내 B2B SaaS 시장 평균(5~8배 예상) / Loan Par = 누적 차입금 또는 누적 적자 금액 — 시범 산출 후 사업부 협의를 통해 기준 확정 필요"),
    ('arrow','FCF 및 EV/Par Coverage 지표를 대시보드에 추가함으로써 표면 지표(매출·EBITDA) 중심 평가 한계 보완 및 구조적 재무 리스크 조기 감지 체계 구축 가능'),
    ('lv2','후속 조치 권고'),
    ('lv3',"FCF 지표 시범 산출 → 사업부 협의 → 대시보드 적용 기준 확정"),
    ('lv3',"변동금리 조달 구조 채택 時 금리 시나리오 분석 프로세스 신설 검토"),
    ('lv3',"Rule of 40·NRR·FCF 3대 지표 통합 건전성 모니터링 체계 수립"),
    # ── 별첨 1 ──
    ('pagebreak',),
    ('lv1','별첨 1. Medallia 상세 프로필'),
    ('lv2','기업 기본 정보'),
    ('table',
     ['항목','내용'],
     [
         ['기업명','Medallia, Inc.'],
         ['설립',"'01年 (미국 캘리포니아)"],
         ['창립자','Borge Hald, Amy Pressman (Fortune 500 기업 임원 컨설팅 경험 기반 창업)'],
         ['본사','San Francisco, CA'],
         ['임직원 수',"약 2,037명 ('21.1月 기준)"],
         ['상장 이력',"'19.7月 NYSE 상장 (MDLA, 공모가 $21) → '21.10月 Thoma Bravo 인수로 상장폐지"],
         ['현재 상태',"채권단(Blackstone 等) 관리하 구조조정 中 ('26年)"],
     ]),
    ('lv2','제품·솔루션 구성'),
    ('table',
     ['카테고리','주요 솔루션'],
     [
         ['고객경험(CX)','고객경험 관리(CEM), 디지털 경험 분석, 경험 오케스트레이션, 개인화 메시징'],
         ['직원경험(EX)','직원 리스닝(Listening), 직원 활성화(Activation) 플랫폼'],
         ['컨택센터','대화형 인텔리전스, 상담원 코칭, 품질 관리, 지능형 콜백'],
         ['AI·분석',"Frontline-Ready AI™ — 별도 교육 없이 현장 즉시 활용 가능한 내장형 AI"],
         ['시장조사','애자일 리서치(Agile Research), 비디오 조사'],
     ]),
    ('lv2','주요 고객 및 시장 지위'),
    ('lv3',"주요 글로벌 고객: Airbnb, Volvo Cars, 3M, Johnson & Johnson, MetLife, PetSmart 等 Fortune 500 다수"),
    ('lv3',"주요 산업군: 금융 서비스, 항공, 호텔·숙박, 통신, 소매, B2B 기업"),
    ('lv3',"Gartner Magic Quadrant '26年 'Leader' 선정 (CX 관리 플랫폼 부문)"),
    ('lv3',"주요 경쟁사: Qualtrics(SAP 계열), NICE Satmetrix, Salesforce Experience Cloud, Sprinklr"),
    ('lv2','재무 현황 (상장폐지 직전 공개 기준)'),
    ('table',
     ['항목','수치','기준'],
     [
         ['연간 매출','$477M',"FY2020 (상장 당시 공개)"],
         ['순손실','-$149M','FY2020'],
         ['인수 후 추정 매출','약 $700M대',"'21年 인수 당시 기준 (추정)"],
     ]),
    ('lv5',"'21年 상장폐지 후 재무 정보 비공개. 이자비용 급증으로 인한 FCF 악화는 기사(OnlyCFO, '26.5月) 분석 기반"),
    # ── 별첨 2 ──
    ('pagebreak',),
    ('lv1','별첨 2. Thoma Bravo 상세 프로필'),
    ('lv2','기업 기본 정보'),
    ('table',
     ['항목','내용'],
     [
         ['기업명','Thoma Bravo, LP'],
         ['설립',"'08年 공식 설립 (전신: '80年 설립된 Golder Thoma & Co.)"],
         ['본사','San Francisco, CA / Chicago, IL'],
         ['운용자산(AUM)',"$183B 이상 ('25.12.31 기준)"],
         ['누적 거래 건수','565건 이상 완료, 누적 대표 가치 $305B 이상'],
         ['특화 분야','엔터프라이즈 소프트웨어, 인프라 소프트웨어, 사이버보안, 기술 서비스'],
     ]),
    ('lv2','주요 포트폴리오'),
    ('table',
     ['기업명','분야','인수금액'],
     [
         ['Proofpoint','엔터프라이즈 사이버보안','$12.3B'],
         ['Anaplan','기업 계획(Planning) 플랫폼','$10.7B'],
         ['Stamps.com','우편·배송 SaaS','$6.6B'],
         ['Medallia','CX 관리 플랫폼','$6.4B (손실 확정)'],
         ['Coupa Software','조달 자동화','$6.15B'],
         ['Sophos','엔드포인트 보안','$3.9B'],
     ]),
    ('lv2','인수 실패 메커니즘 요약'),
    ('lv3',"인수 時 변동금리 $1.8B 조달 (LIBOR 0.75%) → 연준 인상으로 SOFR 5.4% 도달"),
    ('lv3',"연이자 $135M → $300M 급등 → PIK 이자 누적으로 원금 $1.8B → $2.8B (복리 방식, 약 $1B 누적)"),
    ('lv3',"EBITDA $200M으로 이자조차 충당 불가 → 채무불이행(Default) → 경영권 상실"),
    # ── 별첨 3 ──
    ('pagebreak',),
    ('lv1','별첨 3. 참고문헌'),
    ('lv2','분석 기사'),
    ('lv3',"OnlyCFO, \"Thoma Bravo's $5B Medallia Loss | The PE Reckoning is Coming...\" ('26.5月) — onlycfo.io"),
    ('lv3',"Bloomberg, \"Thoma Bravo Declines to Invest More in Troubled Medallia\" ('26.4月) — bloomberg.com"),
    ('lv2','기업 공식 자료'),
    ('lv3',"Medallia 공식 홈페이지 — medallia.com"),
    ('lv3',"Thoma Bravo 공식 홈페이지 — thomabravo.com"),
    ('lv3',"Thoma Bravo, \"Medallia to be Acquired by Thoma Bravo for $6.4 Billion\" (보도자료, '21.7月)"),
    ('lv3',"PR Newswire, \"Medallia Announces Pricing of Initial Public Offering\" ('19.7月)"),
    ('lv2','개념 참고'),
    ('lv3',"Wikipedia, \"Medallia\" — en.wikipedia.org"),
    ('lv3',"Wikipedia, \"Thoma Bravo\" — en.wikipedia.org"),
    ('lv3',"Wikipedia, \"Rule of 40\" — en.wikipedia.org"),
    ('lv3',"McKinsey, \"SaaS and the Rule of 40\" — mckinsey.com"),
]

# ── 문서 빌드 ─────────────────────────────────────────────────────────────────

def build(output_path):
    doc = setup_doc()
    add_footer(doc)

    # 제목
    p = doc.add_paragraph()
    set_pf(p, before=0, after=12, align=WD_ALIGN_PARAGRAPH.CENTER)
    add_run(p, 'Medallia 사례로 본 SaaS 기업 가치 평가 기준',
            size=PT_TITLE, bold=True, underline=True)

    # 날짜 · 소속
    p = doc.add_paragraph()
    set_pf(p, before=0, after=9, align=WD_ALIGN_PARAGRAPH.RIGHT)
    add_run(p, "'26.05.08  솔루션전략그룹")

    # 콘텐츠 렌더
    for item in REPORT:
        k = item[0]
        if k == 'summary':
            add_summary_table(doc, item[1])
        elif k == 'lv1':
            p = doc.add_paragraph(); set_pf(p, before=16, after=12)
            add_run(p, item[1], bold=True)
        elif k == 'lv2':
            p = doc.add_paragraph(); set_pf(p, before=0, after=9)
            add_run(p, ' □ ' + item[1], bold=True)
        elif k == 'lv3':
            p = doc.add_paragraph(); set_pf(p, before=0, after=9)
            add_run(p, '   - ' + item[1])
        elif k == 'lv4':
            p = doc.add_paragraph(); set_pf(p, before=0, after=9)
            add_run(p, '     · ' + item[1])
        elif k == 'lv5':
            p = doc.add_paragraph(); set_pf(p, before=0, after=9)
            add_run(p, '   ※ ' + item[1])
        elif k == 'arrow':
            p = doc.add_paragraph(); set_pf(p, before=0, after=9)
            add_run(p, '→ ' + item[1], bold=True)
        elif k == 'table':
            add_table(doc, item[1], item[2])
            gap = doc.add_paragraph(); set_pf(gap, after=6)
        elif k == 'pagebreak':
            page_break(doc)

    # 끝 표시
    p = doc.add_paragraph()
    set_pf(p, before=12, after=0, align=WD_ALIGN_PARAGRAPH.RIGHT)
    add_run(p, '- 以 上 -')

    doc.save(output_path)
    return output_path

if __name__ == '__main__':
    OUT = '/home/ubuntu/files/medallia_report_final.docx'
    try:
        result = build(OUT)
        size = os.path.getsize(result)
        print(f'완료: {result}  ({size:,} bytes, {size/1024:.1f} KB)')
    except Exception:
        import traceback; traceback.print_exc(); sys.exit(1)
