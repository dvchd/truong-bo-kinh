#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_dn27.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn27.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (ten file, nhan, key dau, key cuoi)
FILES = [
    ('00-title'                                , 'Nhan de'                                                     , 'dn27:0.1', 'dn27:0.2'),
    ('00b-mo-dau'                              , 'Mo dau'                                                      , 'dn27:1.1', 'dn27:4.12'),
    ('02-purification-in-the-four-class'       , 'Muc 5 — Purification in the Four Classes'                    , 'dn27:5.0', 'dn27:10.6'),
    ('03-the-earths-nectar-appears'            , 'Muc 11 — The Earth’s Nectar Appears'                         , 'dn27:11.0', 'dn27:11.13'),
    ('04-the-moon-and-sun-appear'              , 'Muc 12 — The Moon and Sun Appear'                            , 'dn27:12.0', 'dn27:13.12'),
    ('05-ground-fungus'                        , 'Muc 14 — Ground-Fungus'                                      , 'dn27:14.0', 'dn27:14.11'),
    ('06-bursting-pods'                        , 'Muc 14.12 — Bursting Pods'                                   , 'dn27:14.12.0', 'dn27:15.12'),
    ('07-ripe-untilled-rice'                   , 'Muc 16 — Ripe Untilled Rice'                                 , 'dn27:16.0', 'dn27:16.5'),
    ('08-sex-appears'                          , 'Muc 16.6 — Sex Appears'                                      , 'dn27:16.6.0', 'dn27:16.15'),
    ('09-sexual-intercourse'                   , 'Muc 17 — Sexual Intercourse'                                 , 'dn27:17.0', 'dn27:17.23'),
    ('10-dividing-the-rice'                    , 'Muc 18 — Dividing the Rice'                                  , 'dn27:18.0', 'dn27:19.12'),
    ('11-the-elected-king'                     , 'Muc 20 — The Elected King'                                   , 'dn27:20.0', 'dn27:21.5'),
    ('12-the-circle-of-brahmins'               , 'Muc 22 — The Circle of Brahmins'                             , 'dn27:22.0', 'dn27:23.7'),
    ('13-the-circle-of-peasants'               , 'Muc 24 — The Circle of Peasants'                             , 'dn27:24.0', 'dn27:24.4'),
    ('14-the-circle-of-menials'                , 'Muc 25 — The Circle of Menials'                              , 'dn27:25.0', 'dn27:26.8'),
    ('15-on-bad-conduct'                       , 'Muc 27 — On Bad Conduct'                                     , 'dn27:27.0', 'dn27:29.5'),
    ('16-the-qualities-on-the-side-of-a'       , 'Muc 30 — The Qualities on the Side of Awakening'             , 'dn27:30.0', 'dn27:32.14'),
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
