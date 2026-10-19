#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_dn23.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn23.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (ten file, nhan, key dau, key cuoi)
FILES = [
    ('00-title'                                , 'Nhan de'                                                     , 'dn23:0.1', 'dn23:0.2'),
    ('00b-mo-dau'                              , 'Mo dau'                                                      , 'dn23:1.1', 'dn23:1.4'),
    ('02-on-payasi'                            , 'Muc 2 — On Pāyāsi'                                           , 'dn23:2.0', 'dn23:4.7'),
    ('03-nihilism'                             , 'Muc 5 — Nihilism'                                            , 'dn23:5.0', 'dn23:5.6'),
    ('04-the-simile-of-the-moon-and-sun'       , 'Muc 5.7 — The Simile of the Moon and Sun'                    , 'dn23:5.7.0', 'dn23:6.21'),
    ('05-the-simile-of-the-bandit'             , 'Muc 7 — The Simile of the Bandit'                            , 'dn23:7.0', 'dn23:8.21'),
    ('06-the-simile-of-the-sewer'              , 'Muc 9 — The Simile of the Sewer'                             , 'dn23:9.0', 'dn23:10.19'),
    ('07-the-simile-of-the-gods-of-the'        , 'Muc 11 — The Simile of the gods of the thirty-three'         , 'dn23:11.0', 'dn23:11.14'),
    ('08-blind-from-birth'                     , 'Muc 11.15 — Blind From Birth'                                , 'dn23:11.15.0', 'dn23:12.14'),
    ('09-the-simile-of-the-pregnant-wom'       , 'Muc 13 — The Simile of the Pregnant Woman'                   , 'dn23:13.0', 'dn23:14.16'),
    ('10-the-simile-of-the-dream'              , 'Muc 15 — The Simile of the Dream'                            , 'dn23:15.0', 'dn23:16.15'),
    ('11-the-simile-of-the-hot-iron-bal'       , 'Muc 17 — The Simile of the Hot Iron Ball'                    , 'dn23:17.0', 'dn23:18.35'),
    ('12-the-simile-of-the-horn-blower'        , 'Muc 19 — The Simile of the Horn Blower'                      , 'dn23:19.0', 'dn23:20.17'),
    ('13-the-simile-of-the-fire-worship'       , 'Muc 21 — The Simile of the Fire-Worshiping Matted-Hair Ascetic', 'dn23:21.0', 'dn23:22.7'),
    ('14-the-simile-of-the-two-caravan'        , 'Muc 23 — The Simile of the Two Caravan Leaders'              , 'dn23:23.0', 'dn23:24.6'),
    ('15-the-simile-of-the-dung-carrier'       , 'Muc 25 — The Simile of the Dung-Carrier'                     , 'dn23:25.0', 'dn23:26.7'),
    ('16-the-simile-of-the-gamblers'           , 'Muc 27 — The Simile of the Gamblers'                         , 'dn23:27.0', 'dn23:28.7'),
    ('17-the-simile-of-the-man-who-carr'       , 'Muc 29 — The Simile of the Man Who Carried Hemp'             , 'dn23:29.0', 'dn23:29.43'),
    ('18-going-for-refuge'                     , 'Muc 30 — Going for Refuge'                                   , 'dn23:30.0', 'dn23:30.7'),
    ('19-on-sacrifice'                         , 'Muc 31 — On Sacrifice'                                       , 'dn23:31.0', 'dn23:31.14'),
    ('20-on-the-student-uttara'                , 'Muc 32 — On the Student Uttara'                              , 'dn23:32.0', 'dn23:32.23'),
    ('21-the-godling-payasi'                   , 'Muc 33 — The Godling Pāyāsi'                                 , 'dn23:33.0', 'dn23:34.6'),
    ('22-35'                                   , 'Muc 35 — 35'                                                 , 'dn23:35.0', 'dn23:35.7'),
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
