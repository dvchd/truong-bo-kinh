#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_dn16.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn16.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (tên file, nhãn, key đầu, key cuối)
FILES = [
    ('00-title'                                , 'Nhan de'                                                     , 'dn16:0.1', 'dn16:0.2'),
    ('00b-mo-dau'                              , 'Mo dau'                                                      , 'dn16:1.1.1', 'dn16:1.2.9'),
    ('02-the-brahmin-vassakara'                , 'Muc 1.3 — The Brahmin Vassakāra'                             , 'dn16:1.3.0', 'dn16:1.3.7'),
    ('03-principles-that-prevent-declin'       , 'Muc 1.4 — Principles That Prevent Decline'                   , 'dn16:1.4.0', 'dn16:1.5.11'),
    ('04-principles-that-prevent-declin'       , 'Muc 1.6 — Principles That Prevent Decline Among the Mendicants', 'dn16:1.6.0', 'dn16:1.15.5'),
    ('05-sariputtas-lions-roar'                , 'Muc 1.16 — Sāriputta’s Lion’s Roar'                          , 'dn16:1.16.0', 'dn16:1.18.6'),
    ('06-the-drawbacks-of-unethical-con'       , 'Muc 1.19 — The Drawbacks of Unethical Conduct'               , 'dn16:1.19.0', 'dn16:1.23.14'),
    ('07-the-benefits-of-ethical-conduc'       , 'Muc 1.24 — The Benefits of Ethical Conduct'                  , 'dn16:1.24.0', 'dn16:1.25.4'),
    ('08-building-a-citadel'                   , 'Muc 1.26 — Building a Citadel'                               , 'dn16:1.26.0', 'dn16:1.34.7'),
    ('09-talk-on-the-noble-truths'             , 'Muc 2.1 — Talk on the Noble Truths'                          , 'dn16:2.1.0', 'dn16:2.4.6'),
    ('10-the-deaths-in-natika'                 , 'Muc 2.5 — The Deaths in Ñātika'                              , 'dn16:2.5.0', 'dn16:2.7.15'),
    ('11-the-mirror-of-the-teaching'           , 'Muc 2.8 — The Mirror of the Teaching'                        , 'dn16:2.8.0', 'dn16:2.13.5'),
    ('12-ambapali-the-courtesan'               , 'Muc 2.14 — Ambapālī the Courtesan'                           , 'dn16:2.14.0', 'dn16:2.20.6'),
    ('13-commencing-the-rains-at-beluva'       , 'Muc 2.21 — Commencing the Rains at Beluva'                   , 'dn16:2.21.0', 'dn16:2.26.9'),
    ('14-an-obvious-hint'                      , 'Muc 3.1 — An Obvious Hint'                                   , 'dn16:3.1.0', 'dn16:3.6.4'),
    ('15-the-appeal-of-mara'                   , 'Muc 3.7 — The Appeal of Māra'                                , 'dn16:3.7.0', 'dn16:3.9.3'),
    ('16-surrendering-the-life-force'          , 'Muc 3.10 — Surrendering the Life Force'                      , 'dn16:3.10.0', 'dn16:3.10.7'),
    ('17-the-causes-of-earthquakes'            , 'Muc 3.11 — The Causes of Earthquakes'                        , 'dn16:3.11.0', 'dn16:3.20.3'),
    ('18-eight-assemblies'                     , 'Muc 3.21 — Eight Assemblies'                                 , 'dn16:3.21.0', 'dn16:3.23.17'),
    ('19-eight-dimensions-of-mastery'          , 'Muc 3.24 — Eight Dimensions of Mastery'                      , 'dn16:3.24.0', 'dn16:3.32.6'),
    ('20-the-eight-liberations'                , 'Muc 3.33 — The Eight Liberations'                            , 'dn16:3.33.0', 'dn16:3.37.4'),
    ('21-the-appeal-of-ananda'                 , 'Muc 3.38 — The Appeal of Ānanda'                             , 'dn16:3.38.0', 'dn16:3.51.21'),
    ('22-the-elephant-look'                    , 'Muc 4.1 — The Elephant Look'                                 , 'dn16:4.1.0', 'dn16:4.4.6'),
    ('23-the-four-great-references'            , 'Muc 4.5 — The Four Great References'                         , 'dn16:4.5.0', 'dn16:4.12.6'),
    ('24-on-cunda-the-smith'                   , 'Muc 4.13 — On Cunda the Smith'                               , 'dn16:4.13.0', 'dn16:4.20.13'),
    ('25-bringing-a-drink'                     , 'Muc 4.21 — Bringing a Drink'                                 , 'dn16:4.21.0', 'dn16:4.25.8'),
    ('26-on-pukkusa-the-malla'                 , 'Muc 4.26 — On Pukkusa the Malla'                             , 'dn16:4.26.0', 'dn16:4.43.6'),
    ('27-the-pair-of-sal-trees'                , 'Muc 5.1 — The Pair of Sal Trees'                             , 'dn16:5.1.0', 'dn16:5.3.11'),
    ('28-the-monk-upavana'                     , 'Muc 5.4 — The Monk Upavāṇa'                                  , 'dn16:5.4.0', 'dn16:5.6.7'),
    ('29-the-four-inspiring-places'            , 'Muc 5.7 — The Four Inspiring Places'                         , 'dn16:5.7.0', 'dn16:5.8.10'),
    ('30-anandas-questions'                    , 'Muc 5.9 — Ānanda’s Questions'                                , 'dn16:5.9.0', 'dn16:5.11.10'),
    ('31-individuals-worthy-of-a-monume'       , 'Muc 5.12 — Individuals Worthy of a Monument'                 , 'dn16:5.12.0', 'dn16:5.12.20'),
    ('32-anandas-incredible-qualities'         , 'Muc 5.13 — Ānanda’s Incredible Qualities'                    , 'dn16:5.13.0', 'dn16:5.16.37'),
    ('33-teaching-the-discourse-on-maha'       , 'Muc 5.17 — Teaching the Discourse on Mahāsudassana'          , 'dn16:5.17.0', 'dn16:5.19.6'),
    ('34-the-mallas-pay-homage'                , 'Muc 5.20 — The Mallas Pay Homage'                            , 'dn16:5.20.0', 'dn16:5.22.7'),
    ('35-on-subhadda-the-wanderer'             , 'Muc 5.23 — On Subhadda the Wanderer'                         , 'dn16:5.23.0', 'dn16:5.30.9'),
    ('36-the-buddhas-last-words'               , 'Muc 6.1 — The Buddha’s Last Words'                           , 'dn16:6.1.0', 'dn16:6.7.4'),
    ('37-fully-quenched'                       , 'Muc 6.8 — Fully Quenched'                                    , 'dn16:6.8.0', 'dn16:6.12.11'),
    ('38-the-rites-of-venerating-the-bu'       , 'Muc 6.13 — The Rites of Venerating the Buddha’s Corpse'      , 'dn16:6.13.0', 'dn16:6.18.4'),
    ('39-mahakassapas-arrival'                 , 'Muc 6.19 — Mahākassapa’s Arrival'                            , 'dn16:6.19.0', 'dn16:6.23.10'),
    ('40-distributing-the-relics'              , 'Muc 6.24 — Distributing the Relics'                          , 'dn16:6.24.0', 'dn16:6.26.7'),
    ('41-venerating-the-relics'                , 'Muc 6.27 — Venerating the Relics'                            , 'dn16:6.27.0', 'dn16:6.28.21'),
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
