#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_dn31.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn31.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (ten file, nhan, key dau, key cuoi)
FILES = [
    ('00-title'                                , 'Nhan de'                                                     , 'dn31:0.1', 'dn31:0.2'),
    ('00b-mo-dau'                              , 'Mo dau'                                                      , 'dn31:1.1', 'dn31:2.10'),
    ('02-the-six-directions'                   , 'Muc 2.11 — The Six Directions'                               , 'dn31:2.11.0', 'dn31:3.3'),
    ('03-four-corrupt-deeds'                   , 'Muc 3.4 — Four Corrupt Deeds'                                , 'dn31:3.4.0', 'dn31:4.4'),
    ('04-four-grounds'                         , 'Muc 5 — Four Grounds'                                        , 'dn31:5.0', 'dn31:6.8'),
    ('05-six-drains-on-wealth'                 , 'Muc 7 — Six Drains on Wealth'                                , 'dn31:7.0', 'dn31:7.2'),
    ('06-six-drawbacks-of-drinking'            , 'Muc 8 — Six Drawbacks of Drinking'                           , 'dn31:8.0', 'dn31:8.3'),
    ('07-six-drawbacks-of-roaming-the-s'       , 'Muc 9 — Six Drawbacks of Roaming the Street Markets at Night', 'dn31:9.0', 'dn31:9.3'),
    ('08-six-drawbacks-of-festivals'           , 'Muc 10 — Six Drawbacks of Festivals'                         , 'dn31:10.0', 'dn31:10.3'),
    ('09-six-drawbacks-of-gambling'            , 'Muc 11 — Six Drawbacks of Gambling'                          , 'dn31:11.0', 'dn31:11.4'),
    ('10-six-drawbacks-of-bad-friends'         , 'Muc 12 — Six Drawbacks of Bad Friends'                       , 'dn31:12.0', 'dn31:12.3'),
    ('11-six-drawbacks-of-laziness'            , 'Muc 13 — Six Drawbacks of Laziness'                          , 'dn31:13.0', 'dn31:14.36'),
    ('12-fake-friends'                         , 'Muc 15 — Fake Friends'                                       , 'dn31:15.0', 'dn31:20.8'),
    ('13-good-hearted-friends'                 , 'Muc 21 — Good-Hearted Friends'                               , 'dn31:21.0', 'dn31:26.22'),
    ('14-covering-the-six-directions'          , 'Muc 27 — Covering the Six Directions'                        , 'dn31:27.0', 'dn31:35.6'),
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
