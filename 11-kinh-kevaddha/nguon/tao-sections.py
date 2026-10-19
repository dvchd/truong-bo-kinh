#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_dn11.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn11.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (ten file, nhan, key dau, key cuoi)
FILES = [
    ('00-title'                                , 'Nhan de'                                                     , 'dn11:0.1', 'dn11:0.2'),
    ('00b-mo-dau'                              , 'Mo dau'                                                      , 'dn11:1.1', 'dn11:3.6'),
    ('02-the-demonstration-of-psychic-p'       , 'Muc 3.7 — The Demonstration of Psychic Power'                , 'dn11:3.7.0', 'dn11:5.7'),
    ('03-the-demonstration-of-revealing'       , 'Muc 6 — The Demonstration of Revealing'                      , 'dn11:6.0', 'dn11:7.8'),
    ('04-the-demonstration-of-instructi'       , 'Muc 8 — The Demonstration of Instruction'                    , 'dn11:8.0', 'dn11:67.1'),
    ('05-on-the-mendicant-in-search-of'        , 'Muc 67.2 — On the Mendicant in Search of the Cessation of Being', 'dn11:67.2.0', 'dn11:84.3'),
    ('06-the-simile-of-the-land-spottin'       , 'Muc 85 — The Simile of the Land-Spotting Bird'               , 'dn11:85.0', 'dn11:85.30'),
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
