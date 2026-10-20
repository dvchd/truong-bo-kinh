#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_dn17.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn17.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (tên file, nhãn, key đầu, key cuối)
FILES = [
    ('00-title'                                , 'Nhan de'                                                     , 'dn17:0.1', 'dn17:0.2'),
    ('00b-mo-dau'                              , 'Mo dau'                                                      , 'dn17:1.1.1', 'dn17:1.3.2'),
    ('02-the-capital-city-of-kusavati'         , 'Muc 1.3.3 — The Capital City of Kusāvatī'                    , 'dn17:1.3.3.0', 'dn17:1.11.2'),
    ('03-the-elephant-treasure'                , 'Muc 1.12 — The Elephant-Treasure'                            , 'dn17:1.12.0', 'dn17:1.12.7'),
    ('04-the-horse-treasure'                   , 'Muc 1.13 — The Horse-Treasure'                               , 'dn17:1.13.0', 'dn17:1.13.7'),
    ('05-the-jewel-treasure'                   , 'Muc 1.14 — The Jewel-Treasure'                               , 'dn17:1.14.0', 'dn17:1.14.6'),
    ('06-the-woman-treasure'                   , 'Muc 1.15 — The Woman-Treasure'                               , 'dn17:1.15.0', 'dn17:1.15.8'),
    ('07-the-householder-treasure'             , 'Muc 1.16 — The Householder-Treasure'                         , 'dn17:1.16.0', 'dn17:1.16.13'),
    ('08-the-commander-treasure'               , 'Muc 1.17 — The Commander-Treasure'                           , 'dn17:1.17.0', 'dn17:1.18.6'),
    ('09-the-four-blessings'                   , 'Muc 1.18.7 — The Four Blessings'                             , 'dn17:1.18.7.0', 'dn17:1.21.13'),
    ('10-lotus-ponds-in-the-palace-of-p'       , 'Muc 1.22 — Lotus Ponds in the Palace of Principle'           , 'dn17:1.22.0', 'dn17:1.33.2'),
    ('11-attaining-absorption'                 , 'Muc 2.1 — Attaining Absorption'                              , 'dn17:2.1.0', 'dn17:2.4.5'),
    ('12-of-all-cities'                        , 'Muc 2.5 — Of All Cities'                                     , 'dn17:2.5.0', 'dn17:2.6.7'),
    ('13-the-visit-of-queen-subhadda'          , 'Muc 2.7 — The Visit of Queen Subhaddā'                       , 'dn17:2.7.0', 'dn17:2.12.31'),
    ('14-rebirth-in-the-realm-of-divini'       , 'Muc 2.13 — Rebirth in the Realm of Divinity'                 , 'dn17:2.13.0', 'dn17:2.17.9'),
]

# Đoạn PLI không có EN: Sujato gộp câu. Nếu PLI trùng khớp tuyệt đối với một
# đoạn phía trước thì mượn lại EN của đoạn đó.
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
