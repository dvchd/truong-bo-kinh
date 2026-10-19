#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_dn5.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn5.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (ten file, nhan, key dau, key cuoi)
FILES = [
    ('00-title'                                , 'Nhan de'                                                     , 'dn5:0.1', 'dn5:0.2'),
    ('01-khanumata'                            , 'Muc 1 — The Brahmins and Householders of Khāṇumata'          , 'dn5:1.0', 'dn5:4.13'),
    ('02-kutadanta'                            , 'Muc 5 — The Qualities of Kūṭadanta'                          , 'dn5:5.0', 'dn5:6.21'),
    ('03-buddha'                               , 'Muc 7 — The Qualities of the Buddha'                         , 'dn5:7.0', 'dn5:7.47'),
    ('04-sacrifice'                            , 'Muc 8 — The Story of King Mahāvijita’s Sacrifice'            , 'dn5:8.0', 'dn5:11.23'),
    ('05-four-accessories'                     , 'Muc 12 — The Four Accessories'                               , 'dn5:12.0', 'dn5:12.9'),
    ('06-eight-accessories'                    , 'Muc 13 — The Eight Accessories'                              , 'dn5:13.0', 'dn5:13.11'),
    ('07-four-more'                            , 'Muc 14 — Four More Accessories'                              , 'dn5:14.0', 'dn5:14.7'),
    ('08-three-modes'                          , 'Muc 15 — The Three Modes'                                    , 'dn5:15.0', 'dn5:15.8'),
    ('09-ten-respects'                         , 'Muc 16 — The Ten Respects'                                   , 'dn5:16.0', 'dn5:16.16'),
    ('10-sixteen-respects'                     , 'Muc 17 — The Sixteen Respects'                               , 'dn5:17.0', 'dn5:21.16'),
    ('11-regular-gift'                         , 'Muc 22 — A Regular Gift as a Propitious Sacrifice.'          , 'dn5:22.0', 'dn5:27.16'),
    ('12-lay-follower'                         , 'Muc 28 — Kūṭadanta Declares Himself a Lay Follower'          , 'dn5:28.0', 'dn5:28.6'),
    ('13-stream-entry'                         , 'Muc 29 — The Realization of the Fruit of Stream-Entry'       , 'dn5:29.0', 'dn5:30.11'),
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
