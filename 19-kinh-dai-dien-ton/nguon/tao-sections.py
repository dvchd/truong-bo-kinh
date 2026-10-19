#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_dn19.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn19.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (ten file, nhan, key dau, key cuoi)
FILES = [
    ('00-title'                                , 'Nhan de'                                                     , 'dn19:0.1', 'dn19:0.2'),
    ('00b-mo-dau'                              , 'Mo dau'                                                      , 'dn19:1.1', 'dn19:1.5'),
    ('02-the-council-of-the-gods'              , 'Muc 2 — The Council of the Gods'                             , 'dn19:2.0', 'dn19:3.22'),
    ('03-eight-genuine-praises'                , 'Muc 4 — Eight Genuine Praises'                               , 'dn19:4.0', 'dn19:15.8'),
    ('04-on-sanankumara'                       , 'Muc 16 — On Sanaṅkumāra'                                     , 'dn19:16.0', 'dn19:19.4'),
    ('05-eight-genuine-praises'                , 'Muc 19.5 — Eight Genuine Praises'                            , 'dn19:19.5.0', 'dn19:28.6'),
    ('06-the-story-of-the-steward'             , 'Muc 28.7 — The Story of the Steward'                         , 'dn19:28.7.0', 'dn19:29.14'),
    ('07-the-story-of-the-great-steward'       , 'Muc 30 — The Story of the Great Steward'                     , 'dn19:30.0', 'dn19:31.6'),
    ('08-dividing-the-realm'                   , 'Muc 32 — Dividing the Realm'                                 , 'dn19:32.0', 'dn19:36.17'),
    ('09-a-good-reputation'                    , 'Muc 37 — A Good Reputation'                                  , 'dn19:37.0', 'dn19:43.6'),
    ('10-a-discussion-with-the-divinity'       , 'Muc 44 — A Discussion With the Divinity'                     , 'dn19:44.0', 'dn19:46.23'),
    ('11-informing-king-renu'                  , 'Muc 47 — Informing King Reṇu'                                , 'dn19:47.0', 'dn19:47.43'),
    ('12-informing-the-six-aristocrats'        , 'Muc 48 — Informing the Six Aristocrats'                      , 'dn19:48.0', 'dn19:55.7'),
    ('13-informing-the-brahmins'               , 'Muc 56 — Informing the Brahmins'                             , 'dn19:56.0', 'dn19:56.15'),
    ('14-informing-the-wives'                  , 'Muc 57 — Informing the Wives'                                , 'dn19:57.0', 'dn19:57.7'),
    ('15-the-great-steward-goes-forth'         , 'Muc 58 — The Great Steward Goes Forth'                       , 'dn19:58.0', 'dn19:62.8'),
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
