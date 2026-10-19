#!/usr/bin/env python3
"""Ghep ban-dich/*.md thanh Kinh-Khoi-The-Nhan-Bon.md"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
def read(p): return open(os.path.join(BASE, p), encoding='utf-8').read().strip()

ORDER = [
 '00-title',
 '00b-mo-dau',
 '02-purification-in-the-four-class',
 '03-the-earths-nectar-appears',
 '04-the-moon-and-sun-appear',
 '05-ground-fungus',
 '06-bursting-pods',
 '07-ripe-untilled-rice',
 '08-sex-appears',
 '09-sexual-intercourse',
 '10-dividing-the-rice',
 '11-the-elected-king',
 '12-the-circle-of-brahmins',
 '13-the-circle-of-peasants',
 '14-the-circle-of-menials',
 '15-on-bad-conduct',
 '16-the-qualities-on-the-side-of-a',
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
    # ban-dich/*.md dung duong dan tuong doi ../ ; o ban ghep (goc thu muc) phai bo ../
    for a, b in (('](../HUONG-DAN-DICH.md)', '](HUONG-DAN-DICH.md)'),
                 ('](../nguon/)', '](nguon/)'),
                 ):
        s = s.replace(a, b)
    return s

a = out.find('\n## ')
if a < 0: a = 0
out = out[:a] + fix_links(normalize_quotes(out[a:]))
open(os.path.join(BASE, 'Kinh-Khoi-The-Nhan-Bon.md'), 'w', encoding='utf-8').write(out)
print('da ghep %d phan -> Kinh-Khoi-The-Nhan-Bon.md (%d ky tu)' % (len(parts), len(out)))
