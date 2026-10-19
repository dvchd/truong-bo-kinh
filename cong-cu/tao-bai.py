#!/usr/bin/env python3
"""Dung khung mot bai kinh moi trong truong-bo-kinh.

    python3 cong-cu/tao-bai.py 5

- Tai api_dnN.json tu SuttaCentral (bilara, ban Sujato).
- Chia nguon thanh cac muc theo cac khoa `dnN:X.0` (moi khoa la mot tieu de muc).
- Sinh nguon/sections/*.md.
- Chep bo script tu bai 4 va doi so bai.
- In bang muc de bien soan dat tieu de tieng Viet.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, '04-kinh-sonadanda')

# (so bai, ten thu muc, ten tep ket qua, ten Pali khong dau)
SUITAS = {
    1: ('01-kinh-pham-vong', 'Kinh-Pham-Vong'),
    2: ('02-kinh-sa-mon-qua', 'Kinh-Sa-Mon-Qua'),
    3: ('03-kinh-ambattha', 'Kinh-Ambattha'),
    4: ('04-kinh-sonadanda', 'Kinh-Sonadanda'),
    5: ('05-kinh-kutadanta', 'Kinh-Kutadanta'),
    6: ('06-kinh-mahali', 'Kinh-Mahali'),
    7: ('07-kinh-jaliya', 'Kinh-Jaliya'),
    8: ('08-kinh-dai-su-tu-hong', 'Kinh-Dai-Su-Tu-Hong'),
    9: ('09-kinh-pottapada', 'Kinh-Pottapada'),
    10: ('10-kinh-subha', 'Kinh-Subha'),
    11: ('11-kinh-kevaddha', 'Kinh-Kevaddha'),
    12: ('12-kinh-lohicca', 'Kinh-Lohicca'),
    13: ('13-kinh-tam-minh', 'Kinh-Tam-Minh'),
    14: ('14-kinh-dai-bon', 'Kinh-Dai-Bon'),
    15: ('15-kinh-dai-duyen', 'Kinh-Dai-Duyen'),
    16: ('16-kinh-dai-bat-niet-ban', 'Kinh-Dai-Bat-Niet-Ban'),
    17: ('17-kinh-dai-thien-kien', 'Kinh-Dai-Thien-Kien'),
    18: ('18-kinh-janavasabha', 'Kinh-Janavasabha'),
    19: ('19-kinh-dai-dien-ton', 'Kinh-Dai-Dien-Ton'),
    20: ('20-kinh-dai-hoi', 'Kinh-Dai-Hoi'),
    21: ('21-kinh-sakkapanha', 'Kinh-Sakkapanha'),
    22: ('22-kinh-dai-niem-xu', 'Kinh-Dai-Niem-Xu'),
    23: ('23-kinh-payasi', 'Kinh-Payasi'),
    24: ('24-kinh-paṭika', 'Kinh-Patika'),
    25: ('25-kinh-udumbarika', 'Kinh-Udumbarika'),
    26: ('26-kinh-chuyen-luan-vuong', 'Kinh-Chuyen-Luan-Vuong'),
    27: ('27-kinh-khoi-the-nhan-bon', 'Kinh-Khoi-The-Nhan-Bon'),
    28: ('28-kinh-tu-hoan-hy', 'Kinh-Tu-Hoan-Hy'),
    29: ('29-kinh-dai-hy-kien', 'Kinh-Dai-Hy-Kien'),
    30: ('30-kinh-tuong-lakkhana', 'Kinh-Tuong-Lakkhana'),
    31: ('31-kinh-giao-tho', 'Kinh-Giao-Tho'),
    32: ('32-kinh-a-sat-nang', 'Kinh-A-Sat-Nang'),
    33: ('33-kinh-dai-chung', 'Kinh-Dai-Chung'),
    34: ('34-kinh-thap-thuong', 'Kinh-Thap-Thuong'),
}

SHORT = []
SCRIPTS = ['ghep.py', 'tao-muc-luc.py', 'kiem-tra-marker.py', 'ra-soat.py', 'tien-do.py']


def slug(text, limit=42):
    s = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode()
    s = re.sub(r'[^a-zA-Z0-9]+', '-', s).strip('-').lower()
    return s[:limit].rstrip('-')


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    n = int(sys.argv[1])
    global SHORT
    SHORT = [x.strip() for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else []
    folder, outname = SUITAS[n]
    d = os.path.join(ROOT, folder)
    tag = 'dn%d' % n

    raw = urllib.request.urlopen(
        'https://suttacentral.net/api/bilarasuttas/%s/sujato' % tag, timeout=60).read()
    api = json.loads(raw)
    os.makedirs(os.path.join(d, 'nguon', 'sections'), exist_ok=True)
    os.makedirs(os.path.join(d, 'ban-dich'), exist_ok=True)
    os.makedirs(os.path.join(d, 'ra-soat'), exist_ok=True)
    with open(os.path.join(d, 'nguon', 'api_%s.json' % tag), 'wb') as f:
        f.write(raw)

    keys = api['keys_order']
    titles = {k: (api['translation_text'].get(k) or '').strip() for k in keys}
    pli = {k: (api['root_text'].get(k) or '').strip() for k in keys}

    starts = [k for k in keys if k.endswith('.0')]
    if not starts or starts[0] != keys[0]:
        starts = [k for k in keys if not k.endswith('.0')][:1] + starts
    # gom lai: khoi dau bang cac khoa truoc tieu de dau tien (nhan de)
    first_heading = next(i for i, k in enumerate(keys) if k.endswith('.0'))
    blocks = []
    if first_heading:
        blocks.append(('00-title', 'Nhan de', keys[0], keys[first_heading - 1]))
    for i, k in enumerate(keys):
        if not k.endswith('.0'):
            continue
        nxt = next((x for x in keys[i + 1:] if x.endswith('.0')), None)
        end = keys[keys.index(nxt) - 1] if nxt else keys[-1]
        num = k.split(':')[1][:-2]
        label = re.sub(r'^\d+(\.\d+)*\.?\s*', '', titles.get(k, '')) or num
        idx = len(blocks) - (1 if blocks and blocks[0][0] == '00-title' else 0)
        short = SHORT[idx] if idx < len(SHORT) else slug(label, 30)
        blocks.append((('%02d' % len(blocks)) + '-' + short, 'Muc %s — %s' % (num, label), k, end))

    lines = [
        "FILES = [",
    ]
    for name, label, k0, k1 in blocks:
        lines.append("    (%-42r, %-62r, %r, %r)," % (name, label, k0, k1))
    lines.append("]")
    files_block = '\n'.join(lines)

    # tao-sections.py: chep tu bai 4, thay khoi FILES va so bai
    src = open(os.path.join(TEMPLATE, 'nguon', 'tao-sections.py'), encoding='utf-8').read()
    src = re.sub(r'^FILES = \[.*?^\]', files_block, src, flags=re.S | re.M)
    src = src.replace('dn4', tag)
    open(os.path.join(d, 'nguon', 'tao-sections.py'), 'w', encoding='utf-8').write(src)

    order = [b[0] for b in blocks]
    for s in SCRIPTS:
        t = open(os.path.join(TEMPLATE, s), encoding='utf-8').read()
        t = t.replace('dn4', tag).replace('DN 4', 'DN %d' % n).replace('DN4', 'DN%d' % n)
        t = t.replace('Kinh-Sonadanda', outname)
        if s == 'ghep.py':
            t = re.sub(r'^ORDER = \[.*?^\]', "ORDER = [\n" +
                       ''.join(" %r,\n" % x for x in order) + "]", t, flags=re.S | re.M)
        open(os.path.join(d, s), 'w', encoding='utf-8').write(t)

    subprocess.run([sys.executable, 'nguon/tao-sections.py'], cwd=d, check=True)

    print('\n%-28s %-10s %-10s %5s  %s' % ('tep', 'dau', 'cuoi', 'so', 'tieu de EN'))
    for name, label, k0, k1 in blocks:
        i0, i1 = keys.index(k0), keys.index(k1)
        print('%-28s %-10s %-10s %5d  %s' % (name, k0, k1, i1 - i0 + 1, titles.get(k0, '')[:60]))
    print('\ntong %d doan -> %s' % (len(keys), d))
    return 0


if __name__ == '__main__':
    sys.exit(main())
