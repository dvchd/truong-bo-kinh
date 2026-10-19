#!/usr/bin/env python3
"""Ghep ban-dich/*.md thanh Kinh-Dai-Hy-Kien.md"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
def read(p): return open(os.path.join(BASE, p), encoding='utf-8').read().strip()

ORDER = [
 '00-title',
 '00b-mo-dau',
 '02-the-teaching-of-the-unawakened',
 '03-the-teaching-of-the-awakened',
 '04-when-disciples-have-regrets',
 '05-when-disciples-have-no-regrets',
 '06-on-the-incomplete-spiritual-pa',
 '07-teachings-should-be-recited-in',
 '08-reaching-agreement',
 '09-the-reasons-for-allowing-requi',
 '10-indulgence-in-pleasure',
 '11-the-benefits-of-indulgence-in',
 '12-things-impossible-for-the-perf',
 '13-questions-and-answers',
 '14-the-undeclared-points',
 '15-the-declared-points',
 '16-views-of-the-first-beginning',
 '17-views-of-the-final-end',
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
open(os.path.join(BASE, 'Kinh-Dai-Hy-Kien.md'), 'w', encoding='utf-8').write(out)
print('da ghep %d phan -> Kinh-Dai-Hy-Kien.md (%d ky tu)' % (len(parts), len(out)))
