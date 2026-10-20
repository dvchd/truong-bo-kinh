#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_dn14.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn14.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (tên file, nhãn, key đầu, key cuối)
FILES = [
    ('00-title'                                , 'Nhan de'                                                     , 'dn14:0.1', 'dn14:0.2'),
    ('01-on-past-lives'                        , 'Muc 1 — On Past Lives'                                       , 'dn14:1.0', 'dn14:1.16.13'),
    ('02-whats-normal-for-one-intent-on'       , 'Muc 1.17 — What’s Normal For One Intent on Awakening'        , 'dn14:1.17.0', 'dn14:1.30.5'),
    ('03-the-thirty-two-marks-of-a-grea'       , 'Muc 1.31 — The Thirty-Two Marks of a Great Man'              , 'dn14:1.31.0', 'dn14:1.33.7'),
    ('04-how-he-came-to-be-known-as-vip'       , 'Muc 1.33.8 — How He Came to be Known as Vipassī'             , 'dn14:1.33.8.0', 'dn14:1.38.4'),
    ('05-the-old-man'                          , 'Muc 2.1 — The Old Man'                                       , 'dn14:2.1.0', 'dn14:2.3.16'),
    ('06-the-sick-man'                         , 'Muc 2.4 — The Sick Man'                                      , 'dn14:2.4.0', 'dn14:2.7.16'),
    ('07-the-dead-man'                         , 'Muc 2.8 — The Dead Man'                                      , 'dn14:2.8.0', 'dn14:2.11.23'),
    ('08-the-renunciate'                       , 'Muc 2.12 — The Renunciate'                                   , 'dn14:2.12.0', 'dn14:2.14.17'),
    ('09-the-going-forth'                      , 'Muc 2.15 — The Going Forth'                                  , 'dn14:2.15.0', 'dn14:2.15.5'),
    ('10-a-great-crowd-goes-forth'             , 'Muc 2.16 — A Great Crowd Goes Forth'                         , 'dn14:2.16.0', 'dn14:2.17.3'),
    ('11-vipassis-reflections'                 , 'Muc 2.18 — Vipassī’s Reflections'                            , 'dn14:2.18.0', 'dn14:2.22.8'),
    ('12-the-appeal-of-the-divinity'           , 'Muc 3.1 — The Appeal of the Divinity'                        , 'dn14:3.1.0', 'dn14:3.7.17'),
    ('13-the-chief-disciples'                  , 'Muc 3.8 — The Chief Disciples'                               , 'dn14:3.8.0', 'dn14:3.13.4'),
    ('14-the-going-forth-of-the-large-c'       , 'Muc 3.14 — The Going Forth of the Large Crowd'               , 'dn14:3.14.0', 'dn14:3.17.4'),
    ('15-the-84-000-who-had-gone-forth'        , 'Muc 3.18 — The 84,000 Who Had Gone Forth Previously'         , 'dn14:3.18.0', 'dn14:3.21.4'),
    ('16-the-allowance-to-wander'              , 'Muc 3.22 — The Allowance to Wander'                          , 'dn14:3.22.0', 'dn14:3.28.15'),
    ('17-being-informed-by-deities'            , 'Muc 3.29 — Being Informed by Deities'                        , 'dn14:3.29.0', 'dn14:3.33.7'),
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
