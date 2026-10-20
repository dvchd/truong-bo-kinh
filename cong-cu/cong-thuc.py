#!/usr/bin/env python3
"""Tìm CÔNG THỨC lặp lại trong bản dịch: cụm từ chung ở ≥5 bài, mở rộng tối đa,
ghi lai vi tri (segment) o tung bai."""
import glob, json, os, re
from collections import defaultdict

SKIP = {'00-gioi-thieu', 'bang-thuat-ngu', 'nguon-tham-khao'}

def clean(t):
    t = re.sub(r'\[Chú thích:[^\]]*\]', ' ', t)
    t = re.sub(r'<!--.*?-->', ' ', t)
    t = re.sub(r'[#*_`>\[\]|]', ' ', t)
    return re.sub(r'\s+', ' ', t).strip().lower()

def segments(n):
    d = glob.glob('%02d-*/' % n)[0] + 'ban-dich/'
    segs = {}
    for f in sorted(glob.glob(d + '*.md')):
        if os.path.basename(f)[:-3] in SKIP: continue
        txt = open(f, encoding='utf-8').read()
        parts = re.split(r'^<!-- seg: ([^ ]+) -->$', txt, flags=re.M)
        for i in range(1, len(parts), 2):
            segs[parts[i]] = clean(parts[i+1])
    return segs

seg = {n: segments(n) for n in range(1, 35)}
text = {n: ' '.join(seg[n][k] for k in seg[n]) for n in seg}

def seg_at(n, pos):
    i = 0
    for k, v in seg[n].items():
        ln = len(v.split())
        if i <= pos < i + ln: return k
        i += ln
    return list(seg[n])[-1]

def expand(bs, seed):
    """Mở rộng seed thành khối dài nhất có mặt trong mọi sách của bs."""
    a = bs[0]; t = text[a]; best = seed
    for m in re.finditer(re.escape(seed), t):
        lo, hi = m.start(), m.end()
        while hi < len(t):
            nxt = t[lo:hi+1]
            if nxt.endswith(' ') or t[hi] == ' ': pass
            hi2 = hi + 1
            cand = t[lo:hi2]
            if all(cand in text[b] for b in bs): hi = hi2
            else: break
        while lo > 0:
            cand = t[lo-1:hi]
            if all(cand in text[b] for b in bs): lo -= 1
            else: break
        # trim to word boundaries
        while lo < hi and t[lo] != ' ': lo += 1
        while hi > lo and t[hi-1] != ' ': hi -= 1
        block = t[lo:hi].strip()
        if len(block.split()) > len(best.split()): best = block
    return best

K = 14
idx = defaultdict(set)
for n, t in text.items():
    w = t.split(); seen = set()
    for i in range(len(w) - K + 1):
        seen.add(' '.join(w[i:i+K]))
    for g in seen: idx[g].add(n)

cands = sorted(((g, sorted(s, key=lambda b: len(text[b]))) for g, s in idx.items() if len(s) >= 5),
               key=lambda x: (-len(x[1]), -len(x[0])))
accepted = []
for g, bs in cands:
    if any(g in a['text'] for a in accepted): continue
    block = expand(bs, g)
    if len(block.split()) < 20: continue
    rec = {'text': block, 'words': len(block.split()), 'books': bs,
           'where': {str(b): seg_at(b, text[b].find(block)) for b in bs}}
    accepted.append(rec)
    if len(accepted) >= 16: break

json.dump(accepted, open('so-tay/du-lieu-cong-thuc.json', 'w'), ensure_ascii=False, indent=1)
print('%d cong thuc' % len(accepted))
for r in accepted:
    print('\n== %d tu · %d bai: %s' % (r['words'], len(r['books']), ','.join(map(str, r['books']))))
    print('   ' + r['text'][:160])
