#!/usr/bin/env python3
import csv

WW010_MAP = {
    'Brity Automation': '32000080 , 32000058 , 32000072',
    'EMM': '30000122',
    'Knox (All)': '30000126 , 30000021 , 30000020 , 30000019 , 30000125 , 30000018 , 30000017',
    'Nexprime HCM': '32000088 , 32000087',
    'Nexprime SCM (All)': '32000074 , 32000109 , 32000085',
    'ZTM': '32000115 , 32000114',
}

ALL_CATS = ['tam','ext_sam','rnd','tam_grw','sam_grw','sales_rto','sales_marketing','rnd_rto','revenue_grw','revenue','marketshare']

# [upload_year, year, product, domestic_global, on_prem_cloud, biz_type, tam, ext_sam, rnd, snm]
SOURCE = [
    # === Brity Automation ===
    (2025,2025,'Brity Automation','Domestic','On-prem','SI/SM',3038,1259,0,0),
    (2025,2026,'Brity Automation','Domestic','On-prem','SI/SM',3060,1270,0,0),
    (2025,2027,'Brity Automation','Domestic','On-prem','SI/SM',3076,1275,0,0),
    (2025,2028,'Brity Automation','Domestic','On-prem','SI/SM',3041,1270,0,0),
    (2025,2025,'Brity Automation','Domestic','On-prem','Solution',743,374,0,0),
    (2025,2026,'Brity Automation','Domestic','On-prem','Solution',847,424,0,0),
    (2025,2027,'Brity Automation','Domestic','On-prem','Solution',971,489,0,0),
    (2025,2028,'Brity Automation','Domestic','On-prem','Solution',1105,560,0,0),
    (2025,2025,'Brity Automation','Domestic','Cloud','MSP',601,331,0,0),
    (2025,2026,'Brity Automation','Domestic','Cloud','MSP',671,375,0,0),
    (2025,2027,'Brity Automation','Domestic','Cloud','MSP',738,413,0,0),
    (2025,2028,'Brity Automation','Domestic','Cloud','MSP',809,454,0,0),
    (2025,2023,'Brity Automation','Domestic','Cloud','SaaS',0,0,33.5,0),
    (2025,2024,'Brity Automation','Domestic','Cloud','SaaS',0,0,50.1,0),
    (2025,2025,'Brity Automation','Domestic','Cloud','SaaS',124,46,35.1,0),
    (2025,2026,'Brity Automation','Domestic','Cloud','SaaS',171,63,35.5,0),
    (2025,2027,'Brity Automation','Domestic','Cloud','SaaS',233,87,36.9,0),
    (2025,2028,'Brity Automation','Domestic','Cloud','SaaS',316,118,38.4,0),
    (2025,2025,'Brity Automation','Global','On-prem','SI/SM',0,0,0,0),
    (2025,2026,'Brity Automation','Global','On-prem','SI/SM',0,0,0,0),
    (2025,2027,'Brity Automation','Global','On-prem','SI/SM',0,0,0,0),
    (2025,2028,'Brity Automation','Global','On-prem','SI/SM',0,0,0,0),
    (2025,2025,'Brity Automation','Global','On-prem','Solution',0,0,0,0),
    (2025,2026,'Brity Automation','Global','On-prem','Solution',0,0,0,0),
    (2025,2027,'Brity Automation','Global','On-prem','Solution',0,0,0,0),
    (2025,2028,'Brity Automation','Global','On-prem','Solution',0,0,0,0),
    (2025,2025,'Brity Automation','Global','Cloud','MSP',0,0,0,0),
    (2025,2026,'Brity Automation','Global','Cloud','MSP',0,0,0,0),
    (2025,2027,'Brity Automation','Global','Cloud','MSP',0,0,0,0),
    (2025,2028,'Brity Automation','Global','Cloud','MSP',0,0,0,0),
    (2025,2025,'Brity Automation','Global','Cloud','SaaS',0,0,0,0),
    (2025,2026,'Brity Automation','Global','Cloud','SaaS',0,0,0,0),
    (2025,2027,'Brity Automation','Global','Cloud','SaaS',0,0,0,0),
    (2025,2028,'Brity Automation','Global','Cloud','SaaS',0,0,0,0),
    # === Knox (All) ===
    (2025,2025,'Knox (All)','Domestic','On-prem','SI/SM',0,0,0,0),
    (2025,2026,'Knox (All)','Domestic','On-prem','SI/SM',0,0,0,0),
    (2025,2027,'Knox (All)','Domestic','On-prem','SI/SM',0,0,0,0),
    (2025,2028,'Knox (All)','Domestic','On-prem','SI/SM',0,0,0,0),
    (2025,2025,'Knox (All)','Domestic','On-prem','Solution',1240,0,0,0),
    (2025,2026,'Knox (All)','Domestic','On-prem','Solution',1296,0,0,0),
    (2025,2027,'Knox (All)','Domestic','On-prem','Solution',1349,0,0,0),
    (2025,2028,'Knox (All)','Domestic','On-prem','Solution',1397,0,0,0),
    (2025,2025,'Knox (All)','Domestic','Cloud','MSP',0,0,0,0),
    (2025,2026,'Knox (All)','Domestic','Cloud','MSP',0,0,0,0),
    (2025,2027,'Knox (All)','Domestic','Cloud','MSP',0,0,0,0),
    (2025,2028,'Knox (All)','Domestic','Cloud','MSP',0,0,0,0),
    (2025,2025,'Knox (All)','Domestic','Cloud','SaaS',8017,4362,0,0),
    (2025,2026,'Knox (All)','Domestic','Cloud','SaaS',9830,5694,0,0),
    (2025,2027,'Knox (All)','Domestic','Cloud','SaaS',12044,7391,0,0),
    (2025,2028,'Knox (All)','Domestic','Cloud','SaaS',14150,8974,0,0),
    (2025,2025,'Knox (All)','Global','On-prem','SI/SM',0,0,0,0),
    (2025,2026,'Knox (All)','Global','On-prem','SI/SM',0,0,0,0),
    (2025,2027,'Knox (All)','Global','On-prem','SI/SM',0,0,0,0),
    (2025,2028,'Knox (All)','Global','On-prem','SI/SM',0,0,0,0),
    (2025,2025,'Knox (All)','Global','On-prem','Solution',0,0,0,0),
    (2025,2026,'Knox (All)','Global','On-prem','Solution',0,0,0,0),
    (2025,2027,'Knox (All)','Global','On-prem','Solution',0,0,0,0),
    (2025,2028,'Knox (All)','Global','On-prem','Solution',0,0,0,0),
    (2025,2025,'Knox (All)','Global','Cloud','MSP',0,0,0,0),
    (2025,2026,'Knox (All)','Global','Cloud','MSP',0,0,0,0),
    (2025,2027,'Knox (All)','Global','Cloud','MSP',0,0,0,0),
    (2025,2028,'Knox (All)','Global','Cloud','MSP',0,0,0,0),
    (2025,2025,'Knox (All)','Global','Cloud','SaaS',0,0,0,0),
    (2025,2026,'Knox (All)','Global','Cloud','SaaS',0,0,0,0),
    (2025,2027,'Knox (All)','Global','Cloud','SaaS',0,0,0,0),
    (2025,2028,'Knox (All)','Global','Cloud','SaaS',0,0,0,0),
    # === Nexprime HCM ===
    (2025,2025,'Nexprime HCM','Domestic','On-prem','SI/SM',3375,0,0,0),
    (2025,2026,'Nexprime HCM','Domestic','On-prem','SI/SM',3342,0,0,0),
    (2025,2027,'Nexprime HCM','Domestic','On-prem','SI/SM',3255,0,0,0),
    (2025,2028,'Nexprime HCM','Domestic','On-prem','SI/SM',3121,0,0,0),
    (2025,2025,'Nexprime HCM','Domestic','On-prem','Solution',490,0,0,0),
    (2025,2026,'Nexprime HCM','Domestic','On-prem','Solution',511,0,0,0),
    (2025,2027,'Nexprime HCM','Domestic','On-prem','Solution',530,0,0,0),
    (2025,2028,'Nexprime HCM','Domestic','On-prem','Solution',548,0,0,0),
    (2025,2025,'Nexprime HCM','Domestic','Cloud','MSP',1953,736,0,0),
    (2025,2026,'Nexprime HCM','Domestic','Cloud','MSP',2238,862,0,0),
    (2025,2027,'Nexprime HCM','Domestic','Cloud','MSP',2481,970,0,0),
    (2025,2028,'Nexprime HCM','Domestic','Cloud','MSP',2722,1077,0,0),
    (2025,2023,'Nexprime HCM','Domestic','Cloud','SaaS',0,0,0.0,0),
    (2025,2024,'Nexprime HCM','Domestic','Cloud','SaaS',0,0,8.6,0),
    (2025,2025,'Nexprime HCM','Domestic','Cloud','SaaS',1743,712,10.4,0),
    (2025,2026,'Nexprime HCM','Domestic','Cloud','SaaS',2061,847,8.5,0),
    (2025,2027,'Nexprime HCM','Domestic','Cloud','SaaS',2423,1004,9.0,0),
    (2025,2028,'Nexprime HCM','Domestic','Cloud','SaaS',2811,1176,9.2,0),
    (2025,2025,'Nexprime HCM','Global','On-prem','SI/SM',0,0,0,0),
    (2025,2026,'Nexprime HCM','Global','On-prem','SI/SM',0,0,0,0),
    (2025,2027,'Nexprime HCM','Global','On-prem','SI/SM',0,0,0,0),
    (2025,2028,'Nexprime HCM','Global','On-prem','SI/SM',0,0,0,0),
    (2025,2025,'Nexprime HCM','Global','On-prem','Solution',0,0,0,0),
    (2025,2026,'Nexprime HCM','Global','On-prem','Solution',0,0,0,0),
    (2025,2027,'Nexprime HCM','Global','On-prem','Solution',0,0,0,0),
    (2025,2028,'Nexprime HCM','Global','On-prem','Solution',0,0,0,0),
    (2025,2025,'Nexprime HCM','Global','Cloud','MSP',0,0,0,0),
    (2025,2026,'Nexprime HCM','Global','Cloud','MSP',0,0,0,0),
    (2025,2027,'Nexprime HCM','Global','Cloud','MSP',0,0,0,0),
    (2025,2028,'Nexprime HCM','Global','Cloud','MSP',0,0,0,0),
    (2025,2025,'Nexprime HCM','Global','Cloud','SaaS',0,0,0,0),
    (2025,2026,'Nexprime HCM','Global','Cloud','SaaS',0,0,0,0),
    (2025,2027,'Nexprime HCM','Global','Cloud','SaaS',0,0,0,0),
    (2025,2028,'Nexprime HCM','Global','Cloud','SaaS',0,0,0,0),
    # === Nexprime SCM (All) ===
    (2025,2025,'Nexprime SCM (All)','Domestic','On-prem','SI/SM',1615,0,0,0),
    (2025,2026,'Nexprime SCM (All)','Domestic','On-prem','SI/SM',1590,0,0,0),
    (2025,2027,'Nexprime SCM (All)','Domestic','On-prem','SI/SM',1546,0,0,0),
    (2025,2028,'Nexprime SCM (All)','Domestic','On-prem','SI/SM',1495,0,0,0),
    (2025,2025,'Nexprime SCM (All)','Domestic','On-prem','Solution',406,0,0,0),
    (2025,2026,'Nexprime SCM (All)','Domestic','On-prem','Solution',420,0,0,0),
    (2025,2027,'Nexprime SCM (All)','Domestic','On-prem','Solution',431,0,0,0),
    (2025,2028,'Nexprime SCM (All)','Domestic','On-prem','Solution',440,0,0,0),
    (2025,2025,'Nexprime SCM (All)','Domestic','Cloud','MSP',554,118,0,0),
    (2025,2026,'Nexprime SCM (All)','Domestic','Cloud','MSP',623,135,0,0),
    (2025,2027,'Nexprime SCM (All)','Domestic','Cloud','MSP',672,149,0,0),
    (2025,2028,'Nexprime SCM (All)','Domestic','Cloud','MSP',717,161,0,0),
    (2025,2023,'Nexprime SCM (All)','Domestic','Cloud','SaaS',0,0,14.4,0),
    (2025,2024,'Nexprime SCM (All)','Domestic','Cloud','SaaS',0,0,21.0,0),
    (2025,2025,'Nexprime SCM (All)','Domestic','Cloud','SaaS',250,16,19.8,0),
    (2025,2026,'Nexprime SCM (All)','Domestic','Cloud','SaaS',296,19,21.2,0),
    (2025,2027,'Nexprime SCM (All)','Domestic','Cloud','SaaS',342,22,22.4,0),
    (2025,2028,'Nexprime SCM (All)','Domestic','Cloud','SaaS',386,25,24.3,0),
    (2025,2025,'Nexprime SCM (All)','Global','On-prem','SI/SM',0,0,0,0),
    (2025,2026,'Nexprime SCM (All)','Global','On-prem','SI/SM',0,0,0,0),
    (2025,2027,'Nexprime SCM (All)','Global','On-prem','SI/SM',0,0,0,0),
    (2025,2028,'Nexprime SCM (All)','Global','On-prem','SI/SM',0,0,0,0),
    (2025,2025,'Nexprime SCM (All)','Global','On-prem','Solution',40000,0,0,0),
    (2025,2026,'Nexprime SCM (All)','Global','On-prem','Solution',41000,0,0,0),
    (2025,2027,'Nexprime SCM (All)','Global','On-prem','Solution',41000,0,0,0),
    (2025,2028,'Nexprime SCM (All)','Global','On-prem','Solution',41000,0,0,0),
    (2025,2025,'Nexprime SCM (All)','Global','Cloud','MSP',0,1203,0,0),
    (2025,2026,'Nexprime SCM (All)','Global','Cloud','MSP',0,1301,0,0),
    (2025,2027,'Nexprime SCM (All)','Global','Cloud','MSP',0,1413,0,0),
    (2025,2028,'Nexprime SCM (All)','Global','Cloud','MSP',0,1525,0,0),
    (2025,2025,'Nexprime SCM (All)','Global','Cloud','SaaS',41000,238,0,0),
    (2025,2026,'Nexprime SCM (All)','Global','Cloud','SaaS',48000,280,0,0),
    (2025,2027,'Nexprime SCM (All)','Global','Cloud','SaaS',54000,336,0,0),
    (2025,2028,'Nexprime SCM (All)','Global','Cloud','SaaS',62000,392,0,0),
    # === EMM ===
    (2025,2025,'EMM','Domestic','On-prem','SI/SM',0,0,0,0),
    (2025,2026,'EMM','Domestic','On-prem','SI/SM',0,0,0,0),
    (2025,2027,'EMM','Domestic','On-prem','SI/SM',0,0,0,0),
    (2025,2028,'EMM','Domestic','On-prem','SI/SM',0,0,0,0),
    (2025,2025,'EMM','Domestic','On-prem','Solution',0,0,0,0),
    (2025,2026,'EMM','Domestic','On-prem','Solution',0,0,0,0),
    (2025,2027,'EMM','Domestic','On-prem','Solution',0,0,0,0),
    (2025,2028,'EMM','Domestic','On-prem','Solution',0,0,0,0),
    (2025,2025,'EMM','Domestic','Cloud','MSP',0,0,0,0),
    (2025,2026,'EMM','Domestic','Cloud','MSP',0,0,0,0),
    (2025,2027,'EMM','Domestic','Cloud','MSP',0,0,0,0),
    (2025,2028,'EMM','Domestic','Cloud','MSP',0,0,0,0),
    (2025,2025,'EMM','Domestic','Cloud','SaaS',0,0,0,0),
    (2025,2026,'EMM','Domestic','Cloud','SaaS',0,0,0,0),
    (2025,2027,'EMM','Domestic','Cloud','SaaS',0,0,0,0),
    (2025,2028,'EMM','Domestic','Cloud','SaaS',0,0,0,0),
    (2025,2025,'EMM','Global','On-prem','SI/SM',0,0,0,0),
    (2025,2026,'EMM','Global','On-prem','SI/SM',0,0,0,0),
    (2025,2027,'EMM','Global','On-prem','SI/SM',0,0,0,0),
    (2025,2028,'EMM','Global','On-prem','SI/SM',0,0,0,0),
    (2025,2025,'EMM','Global','On-prem','Solution',18000,0,0,0),
    (2025,2026,'EMM','Global','On-prem','Solution',18000,0,0,0),
    (2025,2027,'EMM','Global','On-prem','Solution',19000,0,0,0),
    (2025,2028,'EMM','Global','On-prem','Solution',19000,0,0,0),
    (2025,2025,'EMM','Global','Cloud','MSP',0,0,0,0),
    (2025,2026,'EMM','Global','Cloud','MSP',0,0,0,0),
    (2025,2027,'EMM','Global','Cloud','MSP',0,0,0,0),
    (2025,2028,'EMM','Global','Cloud','MSP',0,0,0,0),
    (2025,2025,'EMM','Global','Cloud','SaaS',68000,0,0,0),
    (2025,2026,'EMM','Global','Cloud','SaaS',75000,0,0,0),
    (2025,2027,'EMM','Global','Cloud','SaaS',81000,0,0,0),
    (2025,2028,'EMM','Global','Cloud','SaaS',86000,0,0,0),
    # === ZTM ===
    (2025,2025,'ZTM','Domestic','On-prem','SI/SM',0,0,0,0),
    (2025,2026,'ZTM','Domestic','On-prem','SI/SM',0,0,0,0),
    (2025,2027,'ZTM','Domestic','On-prem','SI/SM',0,0,0,0),
    (2025,2028,'ZTM','Domestic','On-prem','SI/SM',0,0,0,0),
    (2025,2025,'ZTM','Domestic','On-prem','Solution',0,0,0,0),
    (2025,2026,'ZTM','Domestic','On-prem','Solution',0,0,0,0),
    (2025,2027,'ZTM','Domestic','On-prem','Solution',0,0,0,0),
    (2025,2028,'ZTM','Domestic','On-prem','Solution',0,0,0,0),
    (2025,2025,'ZTM','Domestic','Cloud','MSP',0,0,0,0),
    (2025,2026,'ZTM','Domestic','Cloud','MSP',0,0,0,0),
    (2025,2027,'ZTM','Domestic','Cloud','MSP',0,0,0,0),
    (2025,2028,'ZTM','Domestic','Cloud','MSP',0,0,0,0),
    (2025,2025,'ZTM','Domestic','Cloud','SaaS',0,0,0,0),
    (2025,2026,'ZTM','Domestic','Cloud','SaaS',0,0,0,0),
    (2025,2027,'ZTM','Domestic','Cloud','SaaS',0,0,0,0),
    (2025,2028,'ZTM','Domestic','Cloud','SaaS',0,0,0,0),
    (2025,2025,'ZTM','Global','On-prem','SI/SM',0,0,0,0),
    (2025,2026,'ZTM','Global','On-prem','SI/SM',0,0,0,0),
    (2025,2027,'ZTM','Global','On-prem','SI/SM',0,0,0,0),
    (2025,2028,'ZTM','Global','On-prem','SI/SM',0,0,0,0),
    (2025,2025,'ZTM','Global','On-prem','Solution',0,0,0,0),
    (2025,2026,'ZTM','Global','On-prem','Solution',0,0,0,0),
    (2025,2027,'ZTM','Global','On-prem','Solution',0,0,0,0),
    (2025,2028,'ZTM','Global','On-prem','Solution',0,0,0,0),
    (2025,2025,'ZTM','Global','Cloud','MSP',0,0,0,0),
    (2025,2026,'ZTM','Global','Cloud','MSP',0,0,0,0),
    (2025,2027,'ZTM','Global','Cloud','MSP',0,0,0,0),
    (2025,2028,'ZTM','Global','Cloud','MSP',0,0,0,0),
    (2025,2025,'ZTM','Global','Cloud','SaaS',59000,26818,0,0),
    (2025,2026,'ZTM','Global','Cloud','SaaS',59000,26909,0,0),
    (2025,2027,'ZTM','Global','Cloud','SaaS',61000,27584,0,0),
    (2025,2028,'ZTM','Global','Cloud','SaaS',63000,28455,0,0),
]

header = ['year','category','value','product','domestic_global','on_prem_cloud','biz_type','ww010','upload_year']
rows = []

# 전년도 TAM/SAM 조회용 인덱스 구축
# key: (product, domestic_global, on_prem_cloud, biz_type, year)
lookup = {}
for r in SOURCE:
    uy, yr, pr, dg, oc, bt, tam, ext_sam, rnd, snm = r
    lookup[(pr, dg, oc, bt, yr)] = (float(tam), float(ext_sam))

def calc_grw(curr, prev):
    """성장률 = (현재 - 전년) / 전년 (ratio 형태, e.g. 0.07 = 7%)"""
    if prev and prev > 0:
        return (curr - prev) / prev
    return 0.0

for r in SOURCE:
    uy, yr, pr, dg, oc, bt, tam, ext_sam, rnd, snm = r
    ww010 = WW010_MAP.get(pr, '')
    tam_f, ext_sam_f, rnd_f, snm_f = float(tam), float(ext_sam), float(rnd), float(snm)

    # 전년도 TAM/SAM 조회
    prev = lookup.get((pr, dg, oc, bt, yr - 1))
    prev_tam = prev[0] if prev else 0.0
    prev_sam = prev[1] if prev else 0.0

    # tam_grw, sam_grw 산출 (전년 기준값 있을 때만)
    tam_grw = calc_grw(tam_f, prev_tam)
    sam_grw = calc_grw(ext_sam_f, prev_sam)

    # DB 출처 및 수식 명시 (value 컬럼에 문자열로 기입)
    FORMULA = {
        'revenue':         'l_sap.orderlist > vf219',
        'sales_marketing': 'l_sap.orderlist > vf599',
        'revenue_grw':     '(vf219_N - vf219_N-1) / vf219_N-1',
        'rnd_rto':         'rnd / vf219 * 100',
        'sales_rto':       'vf599 / vf219 * 100',
        'marketshare':     'vf219 / TAM',
    }

    src_numeric = {
        'tam':     tam_f,
        'ext_sam': ext_sam_f,
        'rnd':     rnd_f,
        'tam_grw': tam_grw,
        'sam_grw': sam_grw,
    }

    for cat in ALL_CATS:
        if cat in FORMULA:
            val = FORMULA[cat]          # 수식 문자열
        else:
            val = f'{src_numeric.get(cat, 0.0):.4f}'   # 숫자
        rows.append([yr, cat, val, pr, dg, oc, bt, ww010, uy])

out_path = '/home/ubuntu/files/market_data_converted.tsv'
with open(out_path, 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f, delimiter='\t')
    w.writerow(header)
    w.writerows(rows)

print(f"완료: {len(SOURCE)}개 소스 행 → {len(rows)}개 출력 행")
print(f"저장: {out_path}")

# 샘플 출력 (첫 5행)
print("\n--- 샘플 (첫 5행) ---")
print('\t'.join(header))
for r in rows[:5]:
    print('\t'.join(str(x) for x in r))
