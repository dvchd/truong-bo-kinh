#!/usr/bin/env python3
"""Tìm các ĐOẠN VĂN LẶP LẠI giữa các cặp bài kinh (≥ 40 từ liên tục)."""
import glob, json, re
from collections import defaultdict

def clean(t):
    t = re.sub(r'\[Chú thích:[^\]]*\]', ' ', t)
    t = re.sub(r'<!--.*?-->', ' ', t)
    t = re.sub(r'[#*_`>\[\]|]', ' ', t)
    return re.sub(r'\s+', ' ', t).strip().lower()

def load(n):
    d = glob.glob('%02d-*/' % n)[0]
    f = glob.glob(d + 'Kinh-*.md')[0]
    txt = open(f, encoding='utf-8').read()
    parts = re.split(r'^<!-- seg: (dn\d+:[^ ]+) -->$', txt, flags=re.M)
    toks, key_of, pos = [], [], []
    for i in range(1, len(parts), 2):
        key, body = parts[i], clean(parts[i+1])
        for t in body.split():
            toks.append(t); key_of.append(key)
    return toks, key_of

N = 8
books = {}
for n in range(1, 35):
    books[n] = load(n)

grams = {}
for n, (toks, key_of) in books.items():
    g = defaultdict(list)
    for i in range(len(toks) - N + 1):
        g[' '.join(toks[i:i+N])].append(i)
    grams[n] = g

pairs = []
data = json.load(open('so-tay/du-lieu-lien-ket.json'))
for r in data:
    if r['grams'] < 150: continue
    pairs.append((r['a'], r['b']))

out = []
for a, b in pairs[:30]:
    ga, gb = grams[a], grams[b]
    common = set(ga) & set(gb)
    if not common: continue
    diag = defaultdict(list)
    for g in common:
        for pa in ga[g]:
            for pb in gb[g]:
                diag[pa - pb].append((pa, pb))
    runs = []
    for d, ps in diag.items():
        ps.sort()
        start = prev = None; cnt = 0
        for pa, pb in ps:
            if prev is not None and pa == prev + 1:
                cnt += 1
            else:
                if cnt >= 40: runs.append((start, cnt, start - d))
                start = pa; cnt = 1
            prev = pa
        if cnt >= 40: runs.append((start, cnt, start - d))
    runs.sort(key=lambda r: -r[1])
    ta, tb = books[a][0], books[b][0]
    for st, ln, pb in runs[:6]:
        out.append(dict(a=a, b=b, a_seg=books[a][1][st], a_end=books[a][1][min(st+ln, len(ta)-1)],
                        b_seg=books[b][1][pb], b_end=books[b][1][min(pb+ln, len(tb)-1)],
                        words=ln, sample=' '.join(ta[st:st+14])))

json.dump(out, open('so-tay/du-lieu-doan-lap.json', 'w'), ensure_ascii=False, indent=1)
print('%d doan lap >= 40 tu' % len(out))
for r in out[:18]:
    print('DN%d %s..%s  <->  DN%d %s..%s  [%d tu]  %s' % (r['a'], r['a_seg'], r['a_end'], r['b'], r['b_seg'], r['b_end'], r['words'], r['sample'][:70]))
