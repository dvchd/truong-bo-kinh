#!/usr/bin/env python3
"""Ghep ban-dich/*.md thanh Kinh-Tuong-Lakkhana.md"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
def read(p): return open(os.path.join(BASE, p), encoding='utf-8').read().strip()

ORDER = [
 '00-title',
 '00b-mo-dau',
 '02-well-planted-feet',
 '03-wheels-on-the-feet',
 '04-5-stretched-heels-etc',
 '05-seven-bulging-places',
 '06-8-tender-and-serried-hands',
 '07-10-arched-feet-and-upright-hai',
 '08-antelope-calves',
 '09-delicate-skin',
 '10-golden-skin',
 '11-privates-in-foreskin',
 '12-16-equal-proportions-and-touch',
 '13-19-a-lions-chest-etc',
 '14-ridged-taste-buds',
 '15-22-indigo-eyes',
 '16-crown-like-a-turban',
 '17-25-one-hair-per-pore-and-a-tuf',
 '18-27-forty-gapless-teeth',
 '19-29-a-large-tongue-and-the-voic',
 '20-a-lion-like-jaw',
 '21-32-even-and-white-teeth',
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
open(os.path.join(BASE, 'Kinh-Tuong-Lakkhana.md'), 'w', encoding='utf-8').write(out)
print('da ghep %d phan -> Kinh-Tuong-Lakkhana.md (%d ky tu)' % (len(parts), len(out)))
