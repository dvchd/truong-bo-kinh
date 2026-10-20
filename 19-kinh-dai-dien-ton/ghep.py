#!/usr/bin/env python3
"""Ghép ban-dich/*.md thành Kinh-Dai-Dien-Ton.md"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
def read(p): return open(os.path.join(BASE, p), encoding='utf-8').read().strip()

ORDER = [
 '00-title',
 '00b-mo-dau',
 '02-the-council-of-the-gods',
 '03-eight-genuine-praises',
 '04-on-sanankumara',
 '05-eight-genuine-praises',
 '06-the-story-of-the-steward',
 '07-the-story-of-the-great-steward',
 '08-dividing-the-realm',
 '09-a-good-reputation',
 '10-a-discussion-with-the-divinity',
 '11-informing-king-renu',
 '12-informing-the-six-aristocrats',
 '13-informing-the-brahmins',
 '14-informing-the-wives',
 '15-the-great-steward-goes-forth',
]
OPTIONAL_HEAD = ['00-gioi-thieu']
OPTIONAL_TAIL = ['bang-thuat-ngu', 'nguon-tham-khao']

def has(name): return os.path.exists(os.path.join(BASE, 'ban-dich', name + '.md'))

parts = []
for n in OPTIONAL_HEAD:
    if has(n): parts.append(read('ban-dich/%s.md' % n))
for name in ORDER:
    if not has(name):
        print('  (chua co: %s)' % name); continue
    parts.append(read('ban-dich/%s.md' % name))
for n in OPTIONAL_TAIL:
    if has(n): parts.append(read('ban-dich/%s.md' % n))

def sep_for(acc):
    last = [l for l in acc.strip().split('\n') if l.strip()][-1].strip()
    if last.startswith('<!--') or last.startswith('#'):
        return '\n\n'
    return '\n\n---\n\n'

if not parts:
    print("chua co tep nao"); raise SystemExit(1)
out = parts[0]
for p in parts[1:]:
    out += sep_for(out) + p
out += '\n'

def normalize_quotes(s):
    return (s.replace('\u201c', '"').replace('\u201d', '"')
             .replace('\u2018', "'").replace('\u2019', "'"))

def fix_links(s):
    # ban-dich/*.md dùng đường dẫn tương đối ../ ; ở bản ghép (gốc thư mục) phải bỏ ../
    for a, b in (('](../HUONG-DAN-DICH.md)', '](HUONG-DAN-DICH.md)'),
                 ('](../nguon/)', '](nguon/)'),
                 ):
        s = s.replace(a, b)
    return s

a = out.find('\n## ')
if a < 0: a = 0
out = out[:a] + fix_links(normalize_quotes(out[a:]))
open(os.path.join(BASE, 'Kinh-Dai-Dien-Ton.md'), 'w', encoding='utf-8').write(out)
print('da ghep %d phan -> Kinh-Dai-Dien-Ton.md (%d ky tu)' % (len(parts), len(out)))
