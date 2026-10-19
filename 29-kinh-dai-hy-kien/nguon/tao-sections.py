#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_dn29.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn29.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (ten file, nhan, key dau, key cuoi)
FILES = [
    ('00-title'                                , 'Nhan de'                                                     , 'dn29:0.1', 'dn29:0.2'),
    ('00b-mo-dau'                              , 'Mo dau'                                                      , 'dn29:1.1', 'dn29:3.3'),
    ('02-the-teaching-of-the-unawakened'       , 'Muc 4 — The Teaching of the Unawakened'                      , 'dn29:4.0', 'dn29:5.11'),
    ('03-the-teaching-of-the-awakened'         , 'Muc 6 — The Teaching of the Awakened'                        , 'dn29:6.0', 'dn29:7.12'),
    ('04-when-disciples-have-regrets'          , 'Muc 8 — When Disciples Have Regrets'                         , 'dn29:8.0', 'dn29:8.8'),
    ('05-when-disciples-have-no-regrets'       , 'Muc 9 — When Disciples Have No Regrets'                      , 'dn29:9.0', 'dn29:9.10'),
    ('06-on-the-incomplete-spiritual-pa'       , 'Muc 10 — On the Incomplete Spiritual Path, Etc.'             , 'dn29:10.0', 'dn29:16.28'),
    ('07-teachings-should-be-recited-in'       , 'Muc 17 — Teachings Should be Recited in Concert'             , 'dn29:17.0', 'dn29:17.5'),
    ('08-reaching-agreement'                   , 'Muc 18 — Reaching Agreement'                                 , 'dn29:18.0', 'dn29:21.7'),
    ('09-the-reasons-for-allowing-requi'       , 'Muc 22 — The Reasons for Allowing Requisites'                , 'dn29:22.0', 'dn29:22.12'),
    ('10-indulgence-in-pleasure'               , 'Muc 23 — Indulgence in Pleasure'                             , 'dn29:23.0', 'dn29:24.19'),
    ('11-the-benefits-of-indulgence-in'        , 'Muc 25 — The Benefits of Indulgence in Pleasure'             , 'dn29:25.0', 'dn29:25.14'),
    ('12-things-impossible-for-the-perf'       , 'Muc 26 — Things Impossible for the Perfected'                , 'dn29:26.0', 'dn29:26.9'),
    ('13-questions-and-answers'                , 'Muc 27 — Questions and Answers'                              , 'dn29:27.0', 'dn29:29.7'),
    ('14-the-undeclared-points'                , 'Muc 30 — The Undeclared Points'                              , 'dn29:30.0', 'dn29:31.4'),
    ('15-the-declared-points'                  , 'Muc 32 — The Declared Points'                                , 'dn29:32.0', 'dn29:33.4'),
    ('16-views-of-the-first-beginning'         , 'Muc 34 — Views of the First Beginning'                       , 'dn29:34.0', 'dn29:36.28'),
    ('17-views-of-the-final-end'               , 'Muc 37 — Views of the Final End'                             , 'dn29:37.0', 'dn29:41.9'),
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
