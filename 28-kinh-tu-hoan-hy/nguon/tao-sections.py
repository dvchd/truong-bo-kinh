#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_dn28.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn28.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (ten file, nhan, key dau, key cuoi)
FILES = [
    ('00-title'                                , 'Nhan de'                                                     , 'dn28:0.1', 'dn28:0.2'),
    ('01-sariputtas-lions-roar'                , 'Muc 1 — Sāriputta’s Lion’s Roar'                             , 'dn28:1.0', 'dn28:2.15'),
    ('02-teaching-skillful-qualities'          , 'Muc 3 — Teaching Skillful Qualities'                         , 'dn28:3.0', 'dn28:3.6'),
    ('03-describing-the-sense-fields'          , 'Muc 4 — Describing the Sense Fields'                         , 'dn28:4.0', 'dn28:4.5'),
    ('04-the-conception-of-the-embryo'         , 'Muc 5 — The Conception of the Embryo'                        , 'dn28:5.0', 'dn28:5.7'),
    ('05-ways-of-revealing'                    , 'Muc 6 — Ways of Revealing'                                   , 'dn28:6.0', 'dn28:6.19'),
    ('06-attainments-of-vision'                , 'Muc 7 — Attainments of Vision'                               , 'dn28:7.0', 'dn28:7.20'),
    ('07-description-of-individuals'           , 'Muc 8 — Description of Individuals'                          , 'dn28:8.0', 'dn28:8.4'),
    ('08-kinds-of-striving'                    , 'Muc 9 — Kinds of Striving'                                   , 'dn28:9.0', 'dn28:9.3'),
    ('09-ways-of-practice'                     , 'Muc 10 — Ways of Practice'                                   , 'dn28:10.0', 'dn28:10.10'),
    ('10-behavior-in-speech'                   , 'Muc 11 — Behavior in Speech'                                 , 'dn28:11.0', 'dn28:12.3'),
    ('11-responsiveness-to-instruction'        , 'Muc 13 — Responsiveness to Instruction'                      , 'dn28:13.0', 'dn28:13.11'),
    ('12-the-knowledge-and-freedom-of-o'       , 'Muc 14 — The Knowledge and Freedom of Others'                , 'dn28:14.0', 'dn28:14.10'),
    ('13-eternalism'                           , 'Muc 15 — Eternalism'                                         , 'dn28:15.0', 'dn28:15.26'),
    ('14-recollecting-past-lives'              , 'Muc 16 — Recollecting Past Lives'                            , 'dn28:16.0', 'dn28:16.8'),
    ('15-death-and-rebirth'                    , 'Muc 17 — Death and Rebirth'                                  , 'dn28:17.0', 'dn28:17.4'),
    ('16-psychic-powers'                       , 'Muc 18 — Psychic Powers'                                     , 'dn28:18.0', 'dn28:18.17'),
    ('17-the-four-absorptions'                 , 'Muc 19 — The Four Absorptions'                               , 'dn28:19.0', 'dn28:19.3'),
    ('18-on-being-questioned'                  , 'Muc 19.4 — On Being Questioned'                              , 'dn28:19.4.0', 'dn28:19.22'),
    ('19-incredible-and-amazing'               , 'Muc 20 — Incredible and Amazing'                             , 'dn28:20.0', 'dn28:21.6'),
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
