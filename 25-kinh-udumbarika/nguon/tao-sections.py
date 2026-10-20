#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_dn25.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn25.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (tên file, nhãn, key đầu, key cuối)
FILES = [
    ('00-title'                                , 'Nhan de'                                                     , 'dn25:0.1', 'dn25:0.2'),
    ('01-the-story-of-the-wanderer-nigr'       , 'Muc 1 — The Story of the Wanderer Nigrodha'                  , 'dn25:1.0', 'dn25:6.10'),
    ('02-mortification-in-disgust-of-si'       , 'Muc 7 — Mortification in Disgust of Sin'                     , 'dn25:7.0', 'dn25:8.25'),
    ('03-defects'                              , 'Muc 9 — Defects'                                             , 'dn25:9.0', 'dn25:12.19'),
    ('04-on-reaching-the-shoots'               , 'Muc 13 — On Reaching the Shoots'                             , 'dn25:13.0', 'dn25:15.18'),
    ('05-on-reaching-the-bark'                 , 'Muc 16 — On Reaching the Bark'                               , 'dn25:16.0', 'dn25:17.10'),
    ('06-on-reaching-the-softwood'             , 'Muc 18 — On Reaching the Softwood'                           , 'dn25:18.0', 'dn25:18.18'),
    ('07-on-reaching-the-heartwood'            , 'Muc 19 — On Reaching the Heartwood'                          , 'dn25:19.0', 'dn25:19.21'),
    ('08-nigrodha-feels-depressed'             , 'Muc 20 — Nigrodha Feels Depressed'                           , 'dn25:20.0', 'dn25:21.16'),
    ('09-the-culmination-of-the-spiritu'       , 'Muc 22 — The Culmination of the Spiritual Path'              , 'dn25:22.0', 'dn25:22.31'),
    ('10-the-wanderers-feel-depressed'         , 'Muc 23 — The Wanderers Feel Depressed'                       , 'dn25:23.0', 'dn25:24.8'),
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
