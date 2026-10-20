#!/usr/bin/env python3
"""Ghép ban-dich/*.md thành Kinh-Sa-Mon-Qua.md"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
def read(p): return open(os.path.join(BASE, p), encoding='utf-8').read().strip()

ORDER = [
 '00-title', '01-ministers', '02-jivaka', '03-question',
 '04-purana', '05-makkhali', '06-ajita', '07-pakudha', '08-nigantha', '09-sanjaya',
 '10-first-fruit', '11-second-fruit', '12-finer-intro',
 '13-shorter-ethics', '14-middle-ethics', '15-long-ethics',
 '16-sense-restraint', '17-mindfulness', '18-contentment', '19-hindrances',
 '20-first-jhana', '21-second-jhana', '22-third-jhana', '23-fourth-jhana',
 '24-knowledge-vision', '25-mind-made-body', '26-psychic-powers', '27-clairaudience',
 '28-minds-of-others', '29-past-lives', '30-clairvoyance', '31-defilements',
 '32-conclusion',
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
open(os.path.join(BASE, 'Kinh-Sa-Mon-Qua.md'), 'w', encoding='utf-8').write(out)
print('da ghep %d phan -> Kinh-Sa-Mon-Qua.md (%d ky tu)' % (len(parts), len(out)))
