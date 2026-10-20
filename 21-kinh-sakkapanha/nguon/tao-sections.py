#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_dn21.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn21.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (tên file, nhãn, key đầu, key cuối)
FILES = [
    ('00-title'                                , 'Nhan de'                                                     , 'dn21:0.1', 'dn21:0.2'),
    ('00b-mo-dau'                              , 'Mo dau'                                                      , 'dn21:1.1.1', 'dn21:1.4.6'),
    ('02-pancasikhas-song'                     , 'Muc 1.4.7 — Pañcasikha’s Song'                               , 'dn21:1.4.7.0', 'dn21:1.7.14'),
    ('03-the-approach-of-sakka'                , 'Muc 1.8 — The Approach of Sakka'                             , 'dn21:1.8.0', 'dn21:1.11.3'),
    ('04-the-story-of-gopika'                  , 'Muc 1.11.4 — The Story of Gopikā'                            , 'dn21:1.11.4.0', 'dn21:2.3.1'),
    ('05-meditation-on-feelings'               , 'Muc 2.3.2 — Meditation on Feelings'                          , 'dn21:2.3.2.0', 'dn21:2.3.37'),
    ('06-restraint-in-the-monastic-code'       , 'Muc 2.4 — Restraint in the Monastic Code'                    , 'dn21:2.4.0', 'dn21:2.4.35'),
    ('07-sense-restraint'                      , 'Muc 2.5 — Sense Restraint'                                   , 'dn21:2.5.0', 'dn21:2.7.20'),
    ('08-on-feeling-happy'                     , 'Muc 2.7.21 — On Feeling Happy'                               , 'dn21:2.7.21.0', 'dn21:2.10.14'),
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
