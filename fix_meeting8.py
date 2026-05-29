#!/usr/bin/env python3
"""월별 업무 진척 표에서 SR No. 컬럼만 삭제"""

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'r') as f:
    content = f.read()

# 1. 헤더 SR No. th 삭제
old = '      <th rowspan="2" style="width:90px; text-align:center; vertical-align:middle;">SR No.</th>\n'
assert old in content, "헤더 SR No. th not found"
content = content.replace(old, '')
print("✓ 헤더 SR No. th 삭제")

# 2. 각 그룹의 SR No. td 삭제 (4개)
replacements = [
    ('      <td rowspan="9" class="sr-group" style="font-size:11px;">S26040005889</td>\n', ''),
    ('      <td rowspan="9" class="sr-group" style="font-size:11px;">S26040004737</td>\n', ''),
    ('      <td rowspan="9" class="sr-group" style="font-size:11px;">S26050000095</td>\n', ''),
    ('      <td rowspan="12" class="sr-group" style="font-size:11px;">S26030007696</td>\n', ''),
]
for old, new in replacements:
    assert old in content, f"not found: {old.strip()}"
    content = content.replace(old, new)
    print(f"✓ 삭제: {old.strip()}")

with open('/home/ubuntu/files/meeting_summary_20260521.html', 'w') as f:
    f.write(content)
print("파일 저장 완료!")
