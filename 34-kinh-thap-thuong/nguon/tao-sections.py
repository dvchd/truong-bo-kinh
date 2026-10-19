#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_dn34.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn34.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (ten file, nhan, key dau, key cuoi)
FILES = [
    ('00-title'                                , 'Nhan de'                                                     , 'dn34:0.1', 'dn34:0.2'),
    ('00b-mo-dau'                              , 'Mo dau'                                                      , 'dn34:1.1.1', 'dn34:1.1.10'),
    ('02-groups-of-one'                        , 'Muc 1.2 — Groups of One'                                     , 'dn34:1.2.0', 'dn34:1.2.32'),
    ('03-groups-of-two'                        , 'Muc 1.3 — Groups of Two'                                     , 'dn34:1.3.0', 'dn34:1.3.34'),
    ('04-groups-of-three'                      , 'Muc 1.4 — Groups of Three'                                   , 'dn34:1.4.0', 'dn34:1.4.41'),
    ('05-groups-of-four'                       , 'Muc 1.5 — Groups of Four'                                    , 'dn34:1.5.0', 'dn34:1.5.45'),
    ('06-groups-of-five'                       , 'Muc 1.6 — Groups of Five'                                    , 'dn34:1.6.0', 'dn34:1.6.105'),
    ('07-groups-of-six'                        , 'Muc 1.7 — Groups of Six'                                     , 'dn34:1.7.0', 'dn34:1.7.94'),
    ('08-groups-of-seven'                      , 'Muc 1.8 — Groups of Seven'                                   , 'dn34:1.8.0', 'dn34:1.8.76'),
    ('09-groups-of-eight'                      , 'Muc 2.1 — Groups of Eight'                                   , 'dn34:2.1.0', 'dn34:2.1.209'),
    ('10-groups-of-nine'                       , 'Muc 2.2 — Groups of Nine'                                    , 'dn34:2.2.0', 'dn34:2.2.90'),
    ('11-groups-of-ten'                        , 'Muc 2.3 — Groups of Ten'                                     , 'dn34:2.3.0', 'dn34:2.3.134'),
    ('12-2-4'                                  , 'Muc 2.4 — 2.4'                                               , 'dn34:2.4.0', 'dn34:2.4.11'),
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
