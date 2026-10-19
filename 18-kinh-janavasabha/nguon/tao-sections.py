#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_dn18.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn18.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (ten file, nhan, key dau, key cuoi)
FILES = [
    ('00-title'                                , 'Nhan de'                                                     , 'dn18:0.1', 'dn18:0.2'),
    ('01-declaring-the-rebirths-of-peop'       , 'Muc 1 — Declaring the Rebirths of People From Ñātika and Elsewhere', 'dn18:1.0', 'dn18:3.7'),
    ('02-anandas-suggestion'                   , 'Muc 4 — Ānanda’s Suggestion'                                 , 'dn18:4.0', 'dn18:9.3'),
    ('03-janavasabha-the-spirit'               , 'Muc 9.4 — Janavasabha the Spirit'                            , 'dn18:9.4.0', 'dn18:11.9'),
    ('04-the-council-of-the-gods'              , 'Muc 12 — The Council of the Gods'                            , 'dn18:12.0', 'dn18:15.7'),
    ('05-on-sanankumara'                       , 'Muc 16 — On Sanaṅkumāra'                                     , 'dn18:16.0', 'dn18:22.1'),
    ('06-developing-the-bases-of-psychi'       , 'Muc 22.2 — Developing the Bases of Psychic Power'            , 'dn18:22.2.0', 'dn18:23.2'),
    ('07-the-three-openings'                   , 'Muc 23.3 — The Three Openings'                               , 'dn18:23.3.0', 'dn18:26.2'),
    ('08-mindfulness-meditation'               , 'Muc 26.3 — Mindfulness Meditation'                           , 'dn18:26.3.0', 'dn18:27.2'),
    ('09-seven-prerequisites-of-immersi'       , 'Muc 27.3 — Seven Prerequisites of Immersion'                 , 'dn18:27.3.0', 'dn18:29.5'),
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
