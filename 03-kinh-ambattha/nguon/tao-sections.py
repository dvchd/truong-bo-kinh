#!/usr/bin/env python3
"""Sinh nguon/sections/*.md từ api_dn3.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn3.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']
POS = {x: i for i, x in enumerate(k)}

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

# (tên file, nhãn, key đầu, key cuối)
FILES = [
 ('00-title',              'Nhan đề',                                             'dn3:0.1',    'dn3:0.2'),
 ('01-opening',            'Mở đầu — Bà-la-môn Pokkharasāti ở Ukkaṭṭhā',          'dn3:1.1.1',  'dn3:1.2.8'),
 ('02-ambattha',           '2 — Thanh niên Ambaṭṭha',                              'dn3:1.3.0',  'dn3:1.9.5'),
 ('03-primitives-1',       '2.1 — Lần thứ nhất dùng chữ “tiện dân”',               'dn3:1.10.0', 'dn3:1.12.9'),
 ('04-primitives-2-3',     '2.2–2.3 — Lần thứ hai và thứ ba',                      'dn3:1.13.0', 'dn3:1.14.9'),
 ('05-slavegirl',          '2.4 — Chữ “con của người nữ tỳ”',                      'dn3:1.15.0', 'dn3:1.21.11'),
 ('06-heritage',           '2.5 — Bàn luận về dòng dõi Ambaṭṭha',                  'dn3:1.22.0', 'dn3:1.23.22'),
 ('07-aristocrats',        '3 — Giai cấp sát-đế-lợi là cao quý nhất',                   'dn3:1.24.0', 'dn3:1.28.12'),
 ('08-knowledge-conduct',  '4 — Trí tuệ và hạnh tu',                              'dn3:2.1.0',  'dn3:2.2.23'),
 ('09-four-causes',        '5 — Bốn lý do từ bỏ',                                  'dn3:2.3.0',  'dn3:2.5.5'),
 ('10-seers',              '6 — Giống các ẩn sĩ thời xưa',                         'dn3:2.6.0',  'dn3:2.10.14'),
 ('11-two-marks',          '7 — Thấy hai tướng',                                   'dn3:2.11.0', 'dn3:2.15.5'),
 ('12-pokkarasati-visits', '8 — Pokkharasāti đến gặp Đức Thế Tôn',                 'dn3:2.16.0', 'dn3:2.21.7'),
 ('13-conclusion',         '9 — Pokkharasāti xin quy y',                           'dn3:2.22.0', 'dn3:2.22.9'),
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
