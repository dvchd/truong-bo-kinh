#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_dn24.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn24.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (ten file, nhan, key dau, key cuoi)
FILES = [
    ('00-title'                                , 'Nhan de'                                                     , 'dn24:0.1', 'dn24:0.2'),
    ('01-the-story-of-sunakkhatta'             , 'Muc 1 — The Story of Sunakkhatta'                            , 'dn24:1.0', 'dn24:1.6.13'),
    ('02-on-the-aristocrat-of-kuru'            , 'Muc 1.7 — On the Aristocrat of Kuru'                         , 'dn24:1.7.0', 'dn24:1.10.11'),
    ('03-on-the-naked-ascetic-kalaramat'       , 'Muc 1.11 — On the Naked Ascetic Kaḷāramaṭṭaka'               , 'dn24:1.11.0', 'dn24:1.14.13'),
    ('04-on-the-naked-ascetic-patikaput'       , 'Muc 1.15 — On the Naked Ascetic Pāṭikaputta'                 , 'dn24:1.15.0', 'dn24:1.18.39'),
    ('05-on-demonstrations-of-psychic-p'       , 'Muc 1.19 — On Demonstrations of Psychic Power'               , 'dn24:1.19.0', 'dn24:2.13.12'),
    ('06-on-describing-the-origin-of-th'       , 'Muc 2.14 — On Describing the Origin of the World'            , 'dn24:2.14.0', 'dn24:2.21.17'),
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
