#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_dn6.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn6.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (ten file, nhan, key dau, key cuoi)
FILES = [
    ('00-title'                                , 'Nhan de'                                                     , 'dn6:0.1', 'dn6:0.2'),
    ('01-on-the-brahmin-emissaries'            , 'Muc 1 — On the Brahmin Emissaries'                           , 'dn6:1.0', 'dn6:2.8'),
    ('02-on-otthaddha-the-licchavi'            , 'Muc 3 — On Oṭṭhaddha the Licchavi'                           , 'dn6:3.0', 'dn6:5.5'),
    ('03-one-sided-immersion'                  , 'Muc 5.6 — One-Sided Immersion'                               , 'dn6:5.6.0', 'dn6:12.3'),
    ('04-the-four-noble-fruits'                , 'Muc 13 — The Four Noble Fruits'                              , 'dn6:13.0', 'dn6:13.10'),
    ('05-the-noble-eightfold-path'             , 'Muc 14 — The Noble Eightfold Path'                           , 'dn6:14.0', 'dn6:14.6'),
    ('06-on-the-two-renunciates'               , 'Muc 15 — On the Two Renunciates'                             , 'dn6:15.0', 'dn6:19.11'),
]

# Doan PLI khong co EN: Sujato gop cau. Neu PLI trung khop tuyet doi voi mot
# doan phia truoc thi muon lai EN cua doan do.
exact = {}
for x in k:
    if norm(r.get(x)):
        exact.setdefault(norm(p.get(x)), x)

def en_for(x):
    v = norm(r.get(x))
    if v: return v, None
    t = exact.get(norm(p.get(x)))
    if t and POS[t] < POS[x]: return norm(r.get(t)), t
    return '', None

seen = set(); stats = {'copied': 0, 'empty': 0}
for name, label, k0, k1 in FILES:
    ks = [x for x in k[POS[k0]:POS[k1] + 1] if x not in seen]
    seen |= set(ks)
    out = ['# %s  (%d đoạn)' % (label, len(ks)), '']
    for x in ks:
        line = '## ' + x
        rf = (ref.get(x) or '').strip()
        if rf: line += '  `%s`' % rf
        out.append(line)
        pl = norm(p.get(x))
        if pl: out.append('- **PLI**: ' + pl)
        en, src = en_for(x)
        if en:
            tag = '- **EN**: ' + en
            if src: tag += '  (= %s)' % src
            out.append(tag)
            if src: stats['copied'] += 1
        elif pl:
            out.append('- **EN**: (Sujato gộp đoạn này vào câu trước — dịch trực tiếp từ PLI)')
            stats['empty'] += 1
        cm = norm(c.get(x))
        if cm: out.append('- **NOTE**: ' + cm)
        out.append('')
    open(os.path.join(HERE, 'sections', name + '.md'), 'w', encoding='utf-8').write('\n'.join(out))

print('xong:', len(FILES), 'file |', len(seen), 'đoạn | EN mượn lại:', stats['copied'], '| EN trống:', stats['empty'])
