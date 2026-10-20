import re, glob, collections
def read(p): return open(p, encoding='utf-8').read().strip()

ORDER = ['00-title','01-wanderers','02-ethics-intro','03-shorter-ethics','04-middle-ethics',
 '05-large-ethics','06-views-intro','07-past-intro','08-eternalism','09-partial-eternalism',
 '10-finite-infinite','11-flip-floppers','12-anomalous-origination','13-future-intro',
 '14-percipient','15-nonpercipient','16-neither','17-annihilationism','18-nibbana-here-now',
 '19-grounds-intro','20-anxiety','21-contact','22-not-possible','23-dependent-origination',
 '24-end-of-round']

# inline "### 2.x ..." -> numbered "## 2.x ..."
NUM = {
 '03-shorter-ethics': ('### 2.1. Phần giới hạnh ngắn', '## 2.1. Giới hạnh ngắn (Cūḷasīla)'),
 '04-middle-ethics':  ('### 2.2. Phần giới hạnh trung', '## 2.2. Giới hạnh trung (Majjhimasīla)'),
 '05-large-ethics':   ('### 2.3. Phần giới hạnh rộng lớn', '## 2.3. Giới hạnh rộng lớn (Mahāsīla)'),
}
WRAP = {
 '03-shorter-ethics': '## Giới hạnh ngắn (Cūḷasīla)',
 '04-middle-ethics':  '## Giới hạnh trung (Majjhimasīla)',
 '05-large-ethics':   '## Giới hạnh rộng lớn (Mahāsīla)',
}

parts = [read('ban-dich/00-gioi-thieu.md')]
for name in ORDER:
    t = read('ban-dich/%s.md' % name)
    if name in WRAP and t.startswith(WRAP[name]):
        t = t[len(WRAP[name]):].lstrip('\n')
    if name in NUM:
        t = t.replace(*NUM[name], 1)
    parts.append(t)
parts.append(read('ban-dich/bang-thuat-ngu.md'))
parts.append(read('ban-dich/nguon-tham-khao.md'))

def sep_for(acc):
    """Không chèn đường kẻ ngang ngay dưới một tiêu đề hoặc một mốc seg."""
    last = [l for l in acc.strip().split('\n') if l.strip()][-1].strip()
    if last.startswith('<!--') or last.startswith('#'):
        return '\n\n'
    return '\n\n---\n\n'

out = parts[0]
for p in parts[1:]:
    out += sep_for(out) + p
out += '\n'

# --- chuẩn hóa dấu ngoặc kép: dùng thẳng (" và ') cho toàn bộ văn bản ---
def normalize_quotes(s):
    return (s.replace('\u201c', '"').replace('\u201d', '"')
             .replace('\u2018', "'").replace('\u2019', "'"))

# chỉ chuẩn hóa phần thân kinh, giữ nguyên phần giới thiệu/bảng/nguồn
a = out.index('## Trường Bộ Kinh')
b = out.index('\n## Bảng thuật ngữ')
out = out[:a] + normalize_quotes(out[a:b]) + out[b:]
open('Kinh-Pham-Vong.md','w',encoding='utf-8').write(out)
