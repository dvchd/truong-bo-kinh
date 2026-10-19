#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_dn26.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn26.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (ten file, nhan, key dau, key cuoi)
FILES = [
    ('00-title'                                , 'Nhan de'                                                     , 'dn26:0.1', 'dn26:0.2'),
    ('01-taking-refuge-in-oneself'             , 'Muc 1 — Taking Refuge in Oneself'                            , 'dn26:1.0', 'dn26:1.16'),
    ('02-king-dalhanemi'                       , 'Muc 2 — King Daḷhanemi'                                      , 'dn26:2.0', 'dn26:4.9'),
    ('03-the-noble-duty-of-a-wheel-turn'       , 'Muc 5 — The Noble Duty of a Wheel-Turning Monarch'           , 'dn26:5.0', 'dn26:5.8'),
    ('04-the-wheel-treasure-appears'           , 'Muc 5.9 — The Wheel-Treasure Appears'                        , 'dn26:5.9.0', 'dn26:7.16'),
    ('05-on-subsequent-wheel-turning-mo'       , 'Muc 8 — On Subsequent Wheel-Turning Monarchs'                , 'dn26:8.0', 'dn26:9.11'),
    ('06-on-the-period-of-decline'             , 'Muc 10 — On the Period of Decline'                           , 'dn26:10.0', 'dn26:18.14'),
    ('07-when-people-live-for-ten-years'       , 'Muc 19 — When People Live for Ten Years'                     , 'dn26:19.0', 'dn26:21.9'),
    ('08-the-period-of-growth'                 , 'Muc 21.10 — The Period of Growth'                            , 'dn26:21.10.0', 'dn26:23.3'),
    ('09-the-time-of-king-sankha'              , 'Muc 23.4 — The Time of King Saṅkha'                          , 'dn26:23.4.0', 'dn26:24.5'),
    ('10-the-arising-of-the-buddha-mett'       , 'Muc 25 — The Arising of the Buddha Metteyya'                 , 'dn26:25.0', 'dn26:27.7'),
    ('11-on-long-life-and-beauty-for-me'       , 'Muc 28 — On Long Life and Beauty for Mendicants'             , 'dn26:28.0', 'dn26:28.32'),
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
