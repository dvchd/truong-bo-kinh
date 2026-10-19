#!/usr/bin/env python3
"""Kiem tra so-tay/: (1) moi so hieu doan dnN:x.y co that trong ban dich,
(2) moi link noi bo ton tai, (3) khong co ngoac kep cong."""
import glob, os, re, sys

# 1. tap hop segment keys
keys = set()
for n in range(1, 35):
    d = glob.glob('%02d-*/' % n)[0]
    for f in glob.glob(d + 'Kinh-*.md'):
        for m in re.finditer(r'<!-- seg: (dn\d+:[0-9.\-]+) -->', open(f, encoding='utf-8').read()):
            keys.add(m.group(1))

bad_seg, bad_link, curly = [], [], []
for f in sorted(glob.glob('so-tay/*.md')):
    s = open(f, encoding='utf-8').read()
    for m in re.finditer(r'\bdn(\d+):([0-9.\-]+)', s):
        k = 'dn%s:%s' % (m.group(1), m.group(2))
        if k not in keys:
            bad_seg.append((f, k))
    base = os.path.dirname(f)
    for m in re.finditer(r'\]\((?!http)([^)#]+\.md)\)', s):
        p = os.path.normpath(os.path.join(base, m.group(1)))
        if not os.path.exists(p):
            bad_link.append((f, m.group(1)))
    if re.search(r'[“”‘’]', s):
        curly.append(f)

print('so hieu doan da kiem:', len(keys))
for f, k in bad_seg: print('  SEG KHONG CO:', f, k)
for f, p in bad_link: print('  LINK HONG:', f, p)
for f in curly: print('  NGOAC KEP CONG:', f)
ok = not (bad_seg or bad_link or curly)
print('KET LUAN:', 'DAT' if ok else 'CO %d LOI' % (len(bad_seg) + len(bad_link) + len(curly)))
sys.exit(0 if ok else 1)
