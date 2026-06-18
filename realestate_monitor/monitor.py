#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import tempfile
import shutil
import requests
import xml.etree.ElementTree as ET
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# ── .env 로드 ────────────────────────────────────────────────────────────────
def load_env(path):
    env = {}
    try:
        with open(path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    k, v = line.split('=', 1)
                    env[k.strip()] = v.strip()
    except FileNotFoundError:
        pass
    return env

ENV_PATH = os.path.join(os.path.dirname(__file__), '.env')
env = load_env(ENV_PATH)

API_KEY          = env.get('MOLIT_API_KEY', '')
GMAIL_ADDRESS    = env.get('GMAIL_ADDRESS', '')
GMAIL_PASSWORD   = env.get('GMAIL_APP_PASSWORD', '')
RECIPIENTS       = [r.strip() for r in env.get('RECIPIENTS', '').split(',') if r.strip()]
GITHUB_TOKEN     = env.get('GITHUB_TOKEN', '')
GITHUB_REPO      = env.get('GITHUB_REPO', 'juree85-netizen/realestate-report')
PAGES_URL        = f"https://juree85-netizen.github.io/realestate-report/"

# ── 상수 ─────────────────────────────────────────────────────────────────────
API_URL = "https://apis.data.go.kr/1613000/RTMSDataSvcAptTrade/getRTMSDataSvcAptTrade"

DISTRICTS = {
    '11680': {'name': '강남구', 'dongs': ['대치동', '도곡동', '역삼동']},
    '11650': {'name': '서초구', 'dongs': ['반포동', '잠원동']},
    '11710': {'name': '송파구', 'dongs': ['잠실동', '신천동']},
}

PRICE_MIN = 350000   # 35억 (만원 단위)
PRICE_MAX = 450000   # 45억
AREA_MAX  = 100.0    # 전용면적 상한 (㎡)

TRIIUM_APT          = '트리지움'
TRIIUM_DONG         = '잠실동'
TRIIUM_AREA         = 59.0    # 25평형 전용면적 (±5㎡ 허용)
TRIIUM_ACQUISITION  = 296000  # 취득가 29.6억 (만원)

APT_UNITS = {
    '은마':          4424,
    '선경':          3500,
    '타워팰리스':    2130,
    '렉슬':          1200,
    '아크로리버파크': 1612,
    '래미안퍼스티지': 2444,
    '반포자이':      3410,
    '힐스테이트':    3885,
    '엘스':          5678,
    '리센츠':        5563,
    '트리지움':      3696,
    '파크리오':      6864,
    '주공5단지':     3930,
    '신반포':        2496,
    '잠실파크리오':  6864,
}

# ── 날짜 헬퍼 ────────────────────────────────────────────────────────────────
def prev_months(n=3):
    now = datetime.now()
    result = []
    y, m = now.year, now.month
    for _ in range(n):
        result.append(f"{y}{m:02d}")
        m -= 1
        if m == 0:
            m = 12
            y -= 1
    return result

def ym_of(date_str):
    return date_str.replace('.', '')[:6]

# ── API 조회 ─────────────────────────────────────────────────────────────────
def fetch_transactions(lawd_cd, deal_ymd):
    params = {
        'serviceKey': API_KEY,
        'LAWD_CD':    lawd_cd,
        'DEAL_YMD':   deal_ymd,
        'numOfRows':  1000,
        'pageNo':     1,
    }
    try:
        resp = requests.get(API_URL, params=params, timeout=30)
        resp.raise_for_status()
        root = ET.fromstring(resp.content)
        items = []
        for item in root.findall('.//item'):
            price_str = item.findtext('dealAmount', '').replace(',', '').strip()
            if not price_str:
                continue
            try:
                price = int(price_str)
            except ValueError:
                continue
            area_str = item.findtext('excluUseAr', '0').strip()
            items.append({
                'apt':        item.findtext('aptNm', '').strip(),
                'dong':       item.findtext('umdNm', '').strip(),
                'area':       float(area_str) if area_str else 0.0,
                'floor':      item.findtext('floor', '').strip(),
                'price':      price,
                'build_year': item.findtext('buildYear', '').strip(),
                'date':       "{}.{}.{}".format(
                                  item.findtext('dealYear', '').strip(),
                                  item.findtext('dealMonth', '').strip().zfill(2),
                                  item.findtext('dealDay', '').strip().zfill(2)),
            })
        return items
    except Exception as e:
        print(f"  API 오류 ({lawd_cd} {deal_ymd}): {e}")
        return []

# ── 데이터 수집 ───────────────────────────────────────────────────────────────
def collect():
    months = prev_months(3)
    interest, triium = [], []
    seen_i, seen_t = set(), set()

    for lawd_cd, dist in DISTRICTS.items():
        for ym in months:
            print(f"  조회: {dist['name']} {ym}")
            for tx in fetch_transactions(lawd_cd, ym):
                key = (tx['apt'], tx['dong'], tx['date'], tx['price'])

                if (PRICE_MIN <= tx['price'] <= PRICE_MAX
                        and tx['dong'] in dist['dongs']
                        and tx['area'] < AREA_MAX
                        and key not in seen_i):
                    seen_i.add(key)
                    interest.append({**tx, 'district': dist['name']})

                if (TRIIUM_APT in tx['apt']
                        and tx['dong'] == TRIIUM_DONG
                        and abs(tx['area'] - TRIIUM_AREA) <= 5
                        and key not in seen_t):
                    seen_t.add(key)
                    triium.append({**tx, 'district': '송파구'})

    interest.sort(key=lambda x: x['date'], reverse=True)
    triium.sort(key=lambda x: x['date'], reverse=True)
    return interest, triium

# ── 공통 헬퍼 ─────────────────────────────────────────────────────────────────
def compute_derived(interest, triium):
    now = datetime.now()
    triium_price = triium[0]['price'] if triium else None
    curr_ym = f"{now.year}{now.month:02d}"
    prev_m = now.month - 1
    prev_y = now.year
    if prev_m == 0:
        prev_m = 12
        prev_y -= 1
    prev_ym = f"{prev_y}{prev_m:02d}"

    triium_prev_price = None
    for t in triium:
        if ym_of(t['date']) == prev_ym:
            triium_prev_price = t['price']
            break

    prev_prices = {}
    for tx in interest:
        if ym_of(tx['date']) == prev_ym:
            area_bucket = round(tx['area'] / 5) * 5
            key = (tx['apt'], tx['dong'], area_bucket)
            if key not in prev_prices or tx['date'] > prev_prices[key][0]:
                prev_prices[key] = (tx['date'], tx['price'])

    if triium_price is not None:
        sorted_interest = sorted(interest, key=lambda x: abs(x['price'] - triium_price))
    else:
        sorted_interest = interest

    return triium_price, triium_prev_price, prev_prices, curr_ym, sorted_interest, now

def diff_str(p, triium_price):
    if triium_price is None:
        return '—'
    d = (p - triium_price) / 10000
    return f"{'+'if d>=0 else ''}{d:.1f}억"

def diff_color(p, triium_price):
    if triium_price is None:
        return '#333'
    return '#c0392b' if p > triium_price else ('#2980b9' if p < triium_price else '#333')

def gap_change_html(tx, triium_price, triium_prev_price, prev_prices, curr_ym):
    if triium_price is None or ym_of(tx['date']) != curr_ym:
        return '—'
    area_bucket = round(tx['area'] / 5) * 5
    key = (tx['apt'], tx['dong'], area_bucket)
    if key not in prev_prices:
        return '<span style="color:#888">신규</span>'
    prev_price = prev_prices[key][1]
    ref_prev = triium_prev_price if triium_prev_price else triium_price
    delta = ((tx['price'] - triium_price) - (prev_price - ref_prev)) / 10000
    if abs(delta) < 0.05:
        return '±0'
    color = '#c0392b' if delta > 0 else '#2980b9'
    sign = '+' if delta > 0 else ''
    return f'<span style="color:{color}">{sign}{delta:.1f}억</span>'

def triium_card_html(triium):
    if triium:
        t = triium[0]
        return f"""
        <div style="background:#f0f4ff;border-left:4px solid #4a6fa5;padding:16px;margin:20px 0;border-radius:4px">
          <div style="font-size:13px;color:#666;margin-bottom:6px">📍 보유 매물 최신 실거래가</div>
          <div style="font-size:22px;font-weight:bold;color:#2c3e50">
            잠실 트리지움 25평형 ({t['area']:.1f}㎡) &nbsp;
            <span style="color:#4a6fa5">{t['price']/10000:.1f}억</span>
          </div>
          <div style="font-size:12px;color:#888;margin-top:4px">거래일: {t['date']} | {t['floor']}층</div>
        </div>"""
    else:
        return """
        <div style="background:#fff3cd;border-left:4px solid #ffc107;padding:14px;margin:20px 0;border-radius:4px">
          <div style="font-size:13px;color:#856404">⚠️ 잠실 트리지움 25평형 — 최근 3개월 실거래 없음</div>
        </div>"""

# ── 이메일 HTML (간결 버전) ───────────────────────────────────────────────────
def build_email_html(interest, triium):
    today = datetime.now().strftime('%Y년 %m월 %d일')
    triium_price, triium_prev_price, prev_prices, curr_ym, sorted_interest, now = compute_derived(interest, triium)

    # 요약 한줄
    min_price = min(tx['price'] for tx in interest) / 10000 if interest else 0
    # 전월 격차 가장 많이 줄어든 매물 찾기
    best_apt = ''
    best_delta = 0
    for tx in sorted_interest[:20]:
        if ym_of(tx['date']) == curr_ym and triium_price:
            area_bucket = round(tx['area'] / 5) * 5
            key = (tx['apt'], tx['dong'], area_bucket)
            if key in prev_prices:
                ref_prev = triium_prev_price if triium_prev_price else triium_price
                delta = ((tx['price'] - triium_price) - (prev_prices[key][1] - ref_prev)) / 10000
                if delta < best_delta:
                    best_delta = delta
                    best_apt = tx['apt']

    summary_extra = f" &nbsp;|&nbsp; 격차 축소: {best_apt} {best_delta:.1f}억" if best_apt else ''

    if triium_price is not None:
        acq_diff = (triium_price - TRIIUM_ACQUISITION) / 10000
        acq_sign = '+' if acq_diff >= 0 else ''
        acq_color = '#c0392b' if acq_diff > 0 else ('#2980b9' if acq_diff < 0 else '#555')
        triium_summary = (
            f" &nbsp;|&nbsp; 🏚️ 트리지움 <strong>{triium_price/10000:.1f}억</strong>"
            f" <span style='color:{acq_color}'>({acq_sign}{acq_diff:.1f}억 vs 취득가)</span>"
        )
    else:
        triium_summary = ''

    summary_html = f"""
    <div style="background:#eaf4fb;border-left:4px solid #2980b9;padding:12px 16px;margin:16px 0;border-radius:4px;font-size:14px;color:#1a5276">
      관심 매물 <strong>{len(interest)}건</strong> &nbsp;|&nbsp; 최저가 <strong>{min_price:.1f}억</strong>{triium_summary}{summary_extra}
    </div>"""

    # Top 5 표
    top5_rows = ''
    for tx in sorted_interest[:5]:
        gap = gap_change_html(tx, triium_price, triium_prev_price, prev_prices, curr_ym)
        top5_rows += f"""
        <tr style="border-bottom:1px solid #eee">
          <td style="padding:7px 8px">{tx['apt']}</td>
          <td style="padding:7px 8px;text-align:center">{tx['area']:.0f}㎡</td>
          <td style="padding:7px 8px;text-align:right;font-weight:bold">{tx['price']/10000:.1f}억</td>
          <td style="padding:7px 8px;text-align:right;font-weight:bold;color:{diff_color(tx['price'], triium_price)}">{diff_str(tx['price'], triium_price)}</td>
          <td style="padding:7px 8px;text-align:right">{gap}</td>
          <td style="padding:7px 8px;text-align:center;color:#888">{tx['date']}</td>
        </tr>"""

    return f"""<!DOCTYPE html>
<html><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="font-family:'Apple SD Gothic Neo',Arial,sans-serif;max-width:680px;margin:0 auto;padding:20px;color:#333;font-size:14px">
  <h2 style="color:#2c3e50;border-bottom:2px solid #4a6fa5;padding-bottom:10px">
    🏠 부동산 실거래가 리포트 — {today}
  </h2>

  {summary_html}
  {triium_card_html(triium)}

  <h3 style="color:#2c3e50;margin-top:28px">주목 매물 Top 5</h3>
  <p style="font-size:12px;color:#999;margin-top:-8px">트리지움 대비 가격 차이가 가장 적은 순</p>

  <div style="overflow-x:auto">
  <table style="width:100%;border-collapse:collapse;font-size:13px">
    <thead>
      <tr style="background:#4a6fa5;color:#fff">
        <th style="padding:9px 8px;text-align:left">아파트</th>
        <th style="padding:9px 8px;text-align:center">면적</th>
        <th style="padding:9px 8px;text-align:right">거래가</th>
        <th style="padding:9px 8px;text-align:right">트리지움 대비</th>
        <th style="padding:9px 8px;text-align:right">전월 격차변화</th>
        <th style="padding:9px 8px;text-align:center">거래일</th>
      </tr>
    </thead>
    <tbody>{top5_rows}</tbody>
  </table>
  </div>

  <div style="text-align:center;margin:28px 0">
    <a href="{PAGES_URL}" style="display:inline-block;background:#4a6fa5;color:#fff;padding:14px 32px;border-radius:6px;text-decoration:none;font-size:15px;font-weight:bold">
      전체 {len(interest)}건 보기 →
    </a>
  </div>

  <p style="font-size:11px;color:#bbb;margin-top:20px;border-top:1px solid #eee;padding-top:12px">
    출처: 국토교통부 아파트매매 실거래 상세 자료 (data.go.kr) · 자동발송 by 호피<br>
    전월 격차변화는 이번달 거래 건만 표시
  </p>
</body></html>"""

# ── 전체 리포트 HTML (GitHub Pages용) ────────────────────────────────────────
def build_full_report_html(interest, triium):
    today_str = datetime.now().strftime('%Y년 %m월 %d일')
    today_short = datetime.now().strftime('%Y.%m.%d')
    months = prev_months(3)
    period = f"{months[-1][:4]}.{months[-1][4:]} ~ {months[0][:4]}.{months[0][4:]}"

    triium_price, triium_prev_price, prev_prices, curr_ym, sorted_interest, now = compute_derived(interest, triium)

    min_price = min(tx['price'] for tx in interest) / 10000 if interest else 0

    rows = ''
    for tx in sorted_interest:
        gap = gap_change_html(tx, triium_price, triium_prev_price, prev_prices, curr_ym)
        rows += f"""
        <tr>
          <td>{tx['district']}</td>
          <td>{tx['dong']}</td>
          <td>{tx['apt']}</td>
          <td style="text-align:center">{tx['area']:.0f}㎡</td>
          <td style="text-align:center">{tx['floor']}층</td>
          <td style="text-align:right;font-weight:bold">{tx['price']/10000:.1f}억</td>
          <td style="text-align:right;font-weight:bold;color:{diff_color(tx['price'], triium_price)}">{diff_str(tx['price'], triium_price)}</td>
          <td style="text-align:right">{gap}</td>
          <td style="text-align:center;color:#888">{tx['date']}</td>
        </tr>"""

    if not rows:
        rows = '<tr><td colspan="9" style="padding:16px;text-align:center;color:#aaa">해당 기간 실거래 없음</td></tr>'

    return f"""<!DOCTYPE html>
<html lang="ko"><head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>호피 부동산 리포트 — {today_short}</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Apple SD Gothic Neo', Arial, sans-serif; color: #333; font-size: 14px; background: #f8f9fa; }}
  .container {{ max-width: 1100px; margin: 0 auto; padding: 20px 16px; }}
  h1 {{ color: #2c3e50; font-size: 20px; border-bottom: 2px solid #4a6fa5; padding-bottom: 10px; margin-bottom: 16px; }}
  .summary {{ background: #eaf4fb; border-left: 4px solid #2980b9; padding: 12px 16px; border-radius: 4px; margin-bottom: 16px; font-size: 14px; color: #1a5276; }}
  .triium-card {{ background: #f0f4ff; border-left: 4px solid #4a6fa5; padding: 14px 16px; border-radius: 4px; margin-bottom: 20px; }}
  .triium-card .price {{ font-size: 20px; font-weight: bold; color: #4a6fa5; }}
  .triium-card .meta {{ font-size: 12px; color: #888; margin-top: 4px; }}
  .table-wrap {{ overflow-x: auto; -webkit-overflow-scrolling: touch; }}
  table {{ width: 100%; border-collapse: collapse; background: #fff; font-size: 13px; }}
  thead tr {{ background: #4a6fa5; color: #fff; }}
  th, td {{ padding: 8px 10px; border-bottom: 1px solid #eee; white-space: nowrap; }}
  th {{ text-align: left; }}
  tbody tr:hover {{ background: #f5f8ff; }}
  .footer {{ font-size: 11px; color: #bbb; margin-top: 20px; padding-top: 12px; border-top: 1px solid #eee; }}
</style>
</head>
<body>
<div class="container">
  <h1>🏠 부동산 실거래가 리포트 — {today_str}</h1>

  <div class="summary">
    관심 매물 <strong>{len(interest)}건</strong> &nbsp;|&nbsp;
    조회 구역: 강남·서초·송파구 &nbsp;|&nbsp;
    기간: {period} &nbsp;|&nbsp;
    최저가: <strong>{min_price:.1f}억</strong>
  </div>

  {triium_card_html(triium)}

  <div class="table-wrap">
  <table>
    <thead>
      <tr>
        <th>구</th>
        <th>법정동</th>
        <th>아파트</th>
        <th style="text-align:center">면적</th>
        <th style="text-align:center">층</th>
        <th style="text-align:right">거래가</th>
        <th style="text-align:right">트리지움 대비</th>
        <th style="text-align:right">전월 격차변화</th>
        <th style="text-align:center">거래일</th>
      </tr>
    </thead>
    <tbody>{rows}</tbody>
  </table>
  </div>

  <p class="footer">
    출처: 국토교통부 아파트매매 실거래 상세 자료 (data.go.kr) · 자동발송 by 호피<br>
    전월 격차변화는 이번달 거래 건만 표시
  </p>
</div>
</body></html>"""

# ── GitHub Pages push ─────────────────────────────────────────────────────────
def push_to_ghpages(html_content):
    if not GITHUB_TOKEN:
        print("  ⚠️ GITHUB_TOKEN 없음 — GitHub Pages 업로드 건너뜀")
        return

    tmpdir = tempfile.mkdtemp()
    try:
        repo_url = f"https://juree85-netizen:{GITHUB_TOKEN}@github.com/{GITHUB_REPO}.git"
        subprocess.run(['git', 'clone', '--branch', 'gh-pages', '--depth', '1', repo_url, tmpdir],
                       check=True, capture_output=True)

        index_path = os.path.join(tmpdir, 'index.html')
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        today = datetime.now().strftime('%Y-%m-%d')
        subprocess.run(['git', '-C', tmpdir, 'config', 'user.email', 'juree85@gmail.com'], check=True, capture_output=True)
        subprocess.run(['git', '-C', tmpdir, 'config', 'user.name', 'juree85'], check=True, capture_output=True)
        subprocess.run(['git', '-C', tmpdir, 'add', 'index.html'], check=True, capture_output=True)
        subprocess.run(['git', '-C', tmpdir, 'commit', '-m', f'리포트 업데이트 {today}'],
                       check=True, capture_output=True)
        subprocess.run(['git', '-C', tmpdir, 'push', 'origin', 'gh-pages'],
                       check=True, capture_output=True)
        print(f"  ✅ GitHub Pages 업로드 완료 → {PAGES_URL}")
    except subprocess.CalledProcessError as e:
        print(f"  ⚠️ GitHub Pages push 실패: {e.stderr.decode() if e.stderr else e}")
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)

# ── 메일 발송 ─────────────────────────────────────────────────────────────────
def send_mail(html):
    import uuid
    now = datetime.now()
    subject = f"[호피] 부동산 실거래가 리포트 — {now.strftime('%Y.%m.%d')}"
    msg = MIMEMultipart('alternative')
    msg['Subject']    = subject
    msg['From']       = f"호피 부동산알리미 <{GMAIL_ADDRESS}>"
    msg['To']         = ', '.join(RECIPIENTS)
    msg['Reply-To']   = GMAIL_ADDRESS
    msg['Message-ID'] = f"<hopi-{now.strftime('%Y%m%d%H%M%S')}-{uuid.uuid4().hex[:8]}@hopi.report>"
    msg['X-Mailer']   = 'Hopi-RealEstate-Monitor/1.0'
    msg.attach(MIMEText(html, 'html', 'utf-8'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.set_debuglevel(0)
            s.starttls()
            s.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
            refused = s.sendmail(GMAIL_ADDRESS, RECIPIENTS, msg.as_string())
            if refused:
                print(f"  ⚠️ 일부 수신자 거부됨: {refused}")
            else:
                print(f"  ✅ 메일 발송 완료 → {', '.join(RECIPIENTS)}")
    except smtplib.SMTPAuthenticationError as e:
        print(f"  ❌ SMTP 인증 실패: {e}")
        raise
    except smtplib.SMTPRecipientsRefused as e:
        print(f"  ❌ 수신자 전체 거부: {e}")
        raise
    except smtplib.SMTPException as e:
        print(f"  ❌ SMTP 오류: {e}")
        raise
    except Exception as e:
        print(f"  ❌ 메일 발송 실패 (기타): {e}")
        raise

# ── 메인 ─────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    try:
        print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] 실거래가 조회 시작")
        interest, triium = collect()
        print(f"  관심 매물 {len(interest)}건 / 트리지움 {len(triium)}건")

        full_html = build_full_report_html(interest, triium)
        push_to_ghpages(full_html)

        email_html = build_email_html(interest, triium)
        send_mail(email_html)
        print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] 정상 종료")
    except Exception as e:
        print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] 비정상 종료: {e}")
        import traceback
        traceback.print_exc()
