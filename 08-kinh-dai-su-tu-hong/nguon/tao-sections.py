#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_dn8.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn8.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (ten file, nhan, key dau, key cuoi)
FILES = [
    ('00-title'                                , 'Nhan de'                                                     , 'dn8:0.1', 'dn8:0.2'),
    ('00b-mo-dau'                              , 'Mo dau'                                                      , 'dn8:1.1', 'dn8:4.10'),
    ('02-examination'                          , 'Muc 5 — Examination'                                         , 'dn8:5.0', 'dn8:12.4'),
    ('03-the-noble-eightfold-path'             , 'Muc 13 — The Noble Eightfold Path'                           , 'dn8:13.0', 'dn8:13.7'),
    ('04-the-courses-of-fervent-mortifi'       , 'Muc 14 — The Courses of Fervent Mortification'               , 'dn8:14.0', 'dn8:14.23'),
    ('05-the-uselessness-of-fervent-mor'       , 'Muc 15 — The Uselessness of Fervent Mortification'           , 'dn8:15.0', 'dn8:17.30'),
    ('06-the-accomplishment-of-ethics-m'       , 'Muc 18 — The Accomplishment of Ethics, Mind, and Wisdom'     , 'dn8:18.0', 'dn8:20.7'),
    ('07-the-lions-roar'                       , 'Muc 21 — The Lion’s Roar'                                    , 'dn8:21.0', 'dn8:22.19'),
    ('08-the-probation-for-one-previous'       , 'Muc 23 — The Probation For One Previously Ordained'          , 'dn8:23.0', 'dn8:24.8'),
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
