#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_dn9.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn9.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (ten file, nhan, key dau, key cuoi)
FILES = [
    ('00-title'                                , 'Nhan de'                                                     , 'dn9:0.1', 'dn9:0.2'),
    ('01-on-the-wanderer-potthapada'           , 'Muc 1 — On the Wanderer Poṭṭhapāda'                          , 'dn9:1.0', 'dn9:5.10'),
    ('02-on-the-cessation-of-perception'       , 'Muc 6 — On the Cessation of Perception'                      , 'dn9:6.0', 'dn9:6.35'),
    ('03-perception-arises-with-a-cause'       , 'Muc 7 — Perception Arises With a Cause'                      , 'dn9:7.0', 'dn9:20.6'),
    ('04-perception-and-the-self'              , 'Muc 21 — Perception and the Self'                            , 'dn9:21.0', 'dn9:31.11'),
    ('05-on-citta-hatthisariputta'             , 'Muc 32 — On Citta Hatthisāriputta'                           , 'dn9:32.0', 'dn9:33.18'),
    ('06-teachings-that-are-categorical'       , 'Muc 33.19 — Teachings That Are Categorical'                  , 'dn9:33.19.0', 'dn9:38.22'),
    ('07-three-kinds-of-incarnation'           , 'Muc 39 — Three Kinds of Incarnation'                         , 'dn9:39.0', 'dn9:54.5'),
    ('08-the-ordination-of-citta-hatthi'       , 'Muc 55 — The Ordination of Citta Hatthisāriputta'            , 'dn9:55.0', 'dn9:56.5'),
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
