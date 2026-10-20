#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_dn30.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn30.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (tên file, nhãn, key đầu, key cuối)
FILES = [
    ('00-title'                                , 'Nhan de'                                                     , 'dn30:0.1', 'dn30:0.2'),
    ('00b-mo-dau'                              , 'Mo dau'                                                      , 'dn30:1.1.1', 'dn30:1.3.5'),
    ('02-well-planted-feet'                    , 'Muc 1.4 — Well-Planted Feet'                                 , 'dn30:1.4.0', 'dn30:1.6.21'),
    ('03-wheels-on-the-feet'                   , 'Muc 1.7 — Wheels on the Feet'                                , 'dn30:1.7.0', 'dn30:1.9.24'),
    ('04-5-stretched-heels-etc'                , 'Muc 1.10 — –5. Stretched Heels, Etc.'                        , 'dn30:1.10.0', 'dn30:1.12.17'),
    ('05-seven-bulging-places'                 , 'Muc 1.13 — Seven Bulging Places'                             , 'dn30:1.13.0', 'dn30:1.15.13'),
    ('06-8-tender-and-serried-hands'           , 'Muc 1.16 — –8. Tender and Serried Hands'                     , 'dn30:1.16.0', 'dn30:1.18.17'),
    ('07-10-arched-feet-and-upright-hai'       , 'Muc 1.19 — –10. Arched Feet and Upright Hair'                , 'dn30:1.19.0', 'dn30:1.21.21'),
    ('08-antelope-calves'                      , 'Muc 1.22 — Antelope Calves'                                  , 'dn30:1.22.0', 'dn30:1.24.17'),
    ('09-delicate-skin'                        , 'Muc 1.25 — Delicate Skin'                                    , 'dn30:1.25.0', 'dn30:1.27.17'),
    ('10-golden-skin'                          , 'Muc 1.28 — Golden Skin'                                      , 'dn30:1.28.0', 'dn30:1.30.17'),
    ('11-privates-in-foreskin'                 , 'Muc 1.31 — Privates in Foreskin'                             , 'dn30:1.31.0', 'dn30:1.33.18'),
    ('12-16-equal-proportions-and-touch'       , 'Muc 2.1 — –16. Equal Proportions and Touching the Knees'     , 'dn30:2.1.0', 'dn30:2.3.17'),
    ('13-19-a-lions-chest-etc'                 , 'Muc 2.4 — –19. A Lion’s Chest, Etc.'                         , 'dn30:2.4.0', 'dn30:2.6.17'),
    ('14-ridged-taste-buds'                    , 'Muc 2.7 — Ridged Taste Buds'                                 , 'dn30:2.7.0', 'dn30:2.9.13'),
    ('15-22-indigo-eyes'                       , 'Muc 2.10 — –22. Indigo Eyes'                                 , 'dn30:2.10.0', 'dn30:2.12.17'),
    ('16-crown-like-a-turban'                  , 'Muc 2.13 — Crown Like a Turban'                              , 'dn30:2.13.0', 'dn30:2.15.17'),
    ('17-25-one-hair-per-pore-and-a-tuf'       , 'Muc 2.16 — –25. One Hair Per Pore, and a Tuft'               , 'dn30:2.16.0', 'dn30:2.18.17'),
    ('18-27-forty-gapless-teeth'               , 'Muc 2.19 — –27. Forty Gapless Teeth'                         , 'dn30:2.19.0', 'dn30:2.21.17'),
    ('19-29-a-large-tongue-and-the-voic'       , 'Muc 2.22 — –29. A Large Tongue and the Voice of the Divinity', 'dn30:2.22.0', 'dn30:2.24.17'),
    ('20-a-lion-like-jaw'                      , 'Muc 2.25 — A Lion-Like Jaw'                                  , 'dn30:2.25.0', 'dn30:2.27.17'),
    ('21-32-even-and-white-teeth'              , 'Muc 2.28 — –32. Even and White Teeth'                        , 'dn30:2.28.0', 'dn30:2.31.32'),
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
