#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_dn22.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn22.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (ten file, nhan, key dau, key cuoi)
FILES = [
    ('00-title'                                , 'Nhan de'                                                     , 'dn22:0.1', 'dn22:0.2'),
    ('00b-mo-dau'                              , 'Mo dau'                                                      , 'dn22:1.1', 'dn22:2.15'),
    ('02-the-postures'                         , 'Muc 3 — The Postures'                                        , 'dn22:3.0', 'dn22:3.7'),
    ('03-situational-awareness'                , 'Muc 4 — Situational Awareness'                               , 'dn22:4.0', 'dn22:4.4'),
    ('04-focusing-on-the-repulsive'            , 'Muc 5 — Focusing on the Repulsive'                           , 'dn22:5.0', 'dn22:5.8'),
    ('05-focusing-on-the-elements'             , 'Muc 6 — Focusing on the Elements'                            , 'dn22:6.0', 'dn22:6.8'),
    ('06-the-charnel-ground-contemplati'       , 'Muc 7 — The Charnel Ground Contemplations'                   , 'dn22:7.0', 'dn22:10.11'),
    ('07-observing-the-feelings'               , 'Muc 11 — Observing the Feelings'                             , 'dn22:11.0', 'dn22:11.15'),
    ('08-observing-the-mind'                   , 'Muc 12 — Observing the Mind'                                 , 'dn22:12.0', 'dn22:13.13'),
    ('09-the-aggregates'                       , 'Muc 14 — The Aggregates'                                     , 'dn22:14.0', 'dn22:14.13'),
    ('10-the-sense-fields'                     , 'Muc 15 — The Sense Fields'                                   , 'dn22:15.0', 'dn22:15.13'),
    ('11-the-awakening-factors'                , 'Muc 16 — The Awakening Factors'                              , 'dn22:16.0', 'dn22:16.14'),
    ('12-the-truths'                           , 'Muc 17 — The Truths'                                         , 'dn22:17.0', 'dn22:17.4'),
    ('13-the-truth-of-suffering'               , 'Muc 18 — The Truth of Suffering'                             , 'dn22:18.0', 'dn22:18.51'),
    ('14-the-origin-of-suffering'              , 'Muc 19 — The Origin of Suffering'                            , 'dn22:19.0', 'dn22:19.67'),
    ('15-the-cessation-of-suffering'           , 'Muc 20 — The Cessation of Suffering'                         , 'dn22:20.0', 'dn22:20.66'),
    ('16-the-path'                             , 'Muc 21 — The Path'                                           , 'dn22:21.0', 'dn22:22.28'),
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
