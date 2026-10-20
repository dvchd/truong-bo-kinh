#!/usr/bin/env python3
"""Rà soát toàn bộ 34 bản dịch (458 tệp): từ cấm, ngoặc kép cong, ba chấm ngoài chú thích,
ky hieu chua dich. Chay tu goc kho."""
import glob, os, re, sys

SKIP = {'00-gioi-thieu', 'bang-thuat-ngu', 'nguon-tham-khao'}
BANNED = ['như thị', 'nhất thời', 'bất khả tư nghì', 'vô lượng vô biên', 'chấp trước',
          'Phật giáo đồ', 'như trên', 'lược đi', 'nói rằng là', 'tiền thân là']
probs, files = [], 0
for n in range(1, 35):
    for f in sorted(glob.glob('%02d-*/ban-dich/*.md' % n)):
        b = os.path.basename(f)[:-3]
        if b in SKIP:
            continue
        files += 1
        t = open(f, encoding='utf-8').read()
        low, rel = t.lower(), f.split('/')[0]
        for w in BANNED:
            c = low.count(w.lower())
            if c:
                probs.append(('TU CAM', rel, b, w, c))
        if re.search(r'[“”‘’]', t):
            probs.append(('NGOAC KEP CONG', rel, b, '', 0))
        for m in re.finditer(r'\.\.\.', t):
            if 'Chú thích' not in t[max(0, m.start() - 45):m.start()]:
                probs.append(('BA CHAM', rel, b, t[max(0, m.start() - 45):m.end()].replace('\n', ' '), 1))
        for tok in ('TODO', 'XXX', 'FIXME', '???'):
            if tok in t:
                probs.append(('CHUA DICH', rel, b, tok, 1))
print('so tep da quet:', files)
for p in probs[:40]:
    print(' ', p)
print('TONG VAN DE:', len(probs))
sys.exit(0 if not probs else 1)
