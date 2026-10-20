#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_dn13.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn13.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (tên file, nhãn, key đầu, key cuối)
FILES = [
    ('00-title'                                , 'Nhan de'                                                     , 'dn13:0.1', 'dn13:0.2'),
    ('00b-mo-dau'                              , 'Mo dau'                                                      , 'dn13:1.1', 'dn13:7.7'),
    ('02-what-is-the-path-and-what-is-n'       , 'Muc 8 — What is the Path and What is Not the Path'           , 'dn13:8.0', 'dn13:10.4'),
    ('03-questioning-vasettha'                 , 'Muc 11 — Questioning Vāseṭṭha'                               , 'dn13:11.0', 'dn13:18.14'),
    ('04-the-simile-of-the-finest-lady'        , 'Muc 19 — The Simile of the Finest Lady in the Land'          , 'dn13:19.0', 'dn13:20.9'),
    ('05-the-simile-of-the-ladder'             , 'Muc 21 — The Simile of the Ladder'                           , 'dn13:21.0', 'dn13:23.1'),
    ('06-the-simile-of-the-aciravati-ri'       , 'Muc 24 — The Simile of the Aciravatī River'                  , 'dn13:24.0', 'dn13:30.6'),
    ('07-converging'                           , 'Muc 31 — Converging'                                         , 'dn13:31.0', 'dn13:39.5'),
    ('08-teaching-the-path-to-the-divin'       , 'Muc 40-75 — Teaching the Path to the Divinity'               , 'dn13:40-75.0', 'dn13:82.7'),
    ('09-83'                                   , 'Muc 83 — 83'                                                 , 'dn13:83.0', 'dn13:83.5'),
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
