#!/usr/bin/env python3
"""Phan tich trung lap van ban giua cac bai kinh trong Truong Bo Kinh.

Doc cac tep Kinh-*.md, cat theo marker segment, roi tim cac doan van giong nhau
giua cac bai. Xuat ra bao cao markdown + du lieu JSON.
"""
import glob, json, re, sys, unicodedata
from collections import defaultdict

def clean(t):
    t = re.sub(r'\[Chú thích:[^\]]*\]', ' ', t)
    t = re.sub(r'<!--.*?-->', ' ', t)
    t = re.sub(r'[#*_`>\[\]|]', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip().lower()
    return t

def load(n):
    d = glob.glob('%02d-*/' % n)[0]
    f = glob.glob(d + 'Kinh-*.md')[0]
    txt = open(f, encoding='utf-8').read()
    segs = re.split(r'^<!-- seg: (dn\d+:[^ ]+) -->$', txt, flags=re.M)
    out = []
    for i in range(1, len(segs), 2):
        key, body = segs[i], segs[i+1]
        out.append((key, clean(body)))
    return out

def main():
    books = {}
    for n in range(1, 35):
        books[n] = load(n)
    # n-gram index: 8-gram -> set of (book, seg)
    N = 8
    idx = defaultdict(list)
    grams = {}
    for n, segs in books.items():
        for key, body in segs:
            w = body.split()
            if len(w) < N: continue
            gs = set(' '.join(w[i:i+N]) for i in range(len(w)-N+1))
            grams[key] = gs
            for g in gs: idx[g].append(key)
    pair = defaultdict(lambda: [0, set(), set()])
    for g, keys in idx.items():
        bs = set(int(k[2:].split(':')[0]) for k in keys)
        if len(bs) < 2: continue
        for b1 in bs:
            for b2 in bs:
                if b1 < b2:
                    pair[(b1, b2)][1].add(g)
    # per-sutta totals for normalisation
    ng = {n: sum(len(g) for k, g in grams.items() if int(k[2:].split(':')[0]) == n) for n in books}
    rows = []
    for (b1, b2), (_, shared, _) in sorted(pair.items()):
        tot = len(shared)
        if tot < 20: continue
        a = tot / max(ng[b1], 1); b = tot / max(ng[b2], 1)
        rows.append(dict(a=b1, b=b2, grams=tot, pct_a=round(100*a, 1), pct_b=round(100*b, 1)))
    rows.sort(key=lambda r: -(r['pct_a'] + r['pct_b']))
    json.dump(rows, open('so-tay/du-lieu-lien-ket.json', 'w'), ensure_ascii=False, indent=1)
    print('%d cap bai co trung lap >= 20 cum 8 tu' % len(rows))
    for r in rows[:25]:
        print('DN%-2d <-> DN%-2d  %6d cum   %5.1f%% cua DN%d   %5.1f%% cua DN%d' %
              (r['a'], r['b'], r['grams'], r['pct_a'], r['a'], r['pct_b'], r['b']))

if __name__ == '__main__':
    main()
