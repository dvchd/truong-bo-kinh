#!/usr/bin/env python3
"""Ghep ban-dich/*.md thanh Kinh-Dai-Bat-Niet-Ban.md"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
def read(p): return open(os.path.join(BASE, p), encoding='utf-8').read().strip()

ORDER = [
 '00-title',
 '00b-mo-dau',
 '02-the-brahmin-vassakara',
 '03-principles-that-prevent-declin',
 '04-principles-that-prevent-declin',
 '05-sariputtas-lions-roar',
 '06-the-drawbacks-of-unethical-con',
 '07-the-benefits-of-ethical-conduc',
 '08-building-a-citadel',
 '09-talk-on-the-noble-truths',
 '10-the-deaths-in-natika',
 '11-the-mirror-of-the-teaching',
 '12-ambapali-the-courtesan',
 '13-commencing-the-rains-at-beluva',
 '14-an-obvious-hint',
 '15-the-appeal-of-mara',
 '16-surrendering-the-life-force',
 '17-the-causes-of-earthquakes',
 '18-eight-assemblies',
 '19-eight-dimensions-of-mastery',
 '20-the-eight-liberations',
 '21-the-appeal-of-ananda',
 '22-the-elephant-look',
 '23-the-four-great-references',
 '24-on-cunda-the-smith',
 '25-bringing-a-drink',
 '26-on-pukkusa-the-malla',
 '27-the-pair-of-sal-trees',
 '28-the-monk-upavana',
 '29-the-four-inspiring-places',
 '30-anandas-questions',
 '31-individuals-worthy-of-a-monume',
 '32-anandas-incredible-qualities',
 '33-teaching-the-discourse-on-maha',
 '34-the-mallas-pay-homage',
 '35-on-subhadda-the-wanderer',
 '36-the-buddhas-last-words',
 '37-fully-quenched',
 '38-the-rites-of-venerating-the-bu',
 '39-mahakassapas-arrival',
 '40-distributing-the-relics',
 '41-venerating-the-relics',
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
open(os.path.join(BASE, 'Kinh-Dai-Bat-Niet-Ban.md'), 'w', encoding='utf-8').write(out)
print('da ghep %d phan -> Kinh-Dai-Bat-Niet-Ban.md (%d ky tu)' % (len(parts), len(out)))
