#!/usr/bin/env python3
"""Sinh nguon/sections/*.md tu api_dn2.json (SuttaCentral bilara)."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, 'api_dn2.json'), encoding='utf-8'))
r, p, c, ref = d['translation_text'], d['root_text'], d['comment_text'], d.get('reference_text', {})
k = d['keys_order']

def norm(s): return re.sub(r'\s+', ' ', (s or '')).strip()

FILES = [
 ('00-title','Nhan đề',[0]),
 ('01-ministers','Mục 1 — Cuộc bàn luận với các quan đại thần',range(1,8)),
 ('02-jivaka','Mục 2 — Cuộc bàn luận với Jīvaka Komārabhacca',range(8,11)),
 ('03-question','Mục 3 — Câu hỏi về quả của đời sống sa-môn',range(11,16)),
 ('04-purana','3.1 — Giáo thuyết của Pūraṇa Kassapa',range(16,19)),
 ('05-makkhali','3.2 — Giáo thuyết của du sĩ trường trượng Gosāla',range(19,22)),
 ('06-ajita','3.3 — Giáo thuyết của Ajita Kesakambala',range(22,25)),
 ('07-pakudha','3.4 — Giáo thuyết của Pakudha Kaccāyana',range(25,28)),
 ('08-nigantha','3.5 — Giáo thuyết của Ni-kiền-tử Nātaputta',range(28,31)),
 ('09-sanjaya','3.6 — Giáo thuyết của Sañjaya Belaṭṭhiputta',range(31,34)),
 ('10-first-fruit','4.1 — Quả thứ nhất của đời sống sa-môn',range(34,37)),
 ('11-second-fruit','4.2 — Quả thứ hai của đời sống sa-môn',range(37,39)),
 ('12-finer-intro','4.3 — Những quả vi tế hơn',range(39,43)),
 ('13-shorter-ethics','4.3.1.1 — Phần giới hạnh ngắn',range(43,46)),
 ('14-middle-ethics','4.3.1.2 — Phần giới hạnh trung',range(46,56)),
 ('15-long-ethics','4.3.1.3 — Phần giới hạnh rộng lớn',range(56,64)),
 ('16-sense-restraint','4.3.2.1 — Hộ trì các giác quan',range(64,65)),
 ('17-mindfulness','4.3.2.2 — Chánh niệm và tỉnh giác',range(65,66)),
 ('18-contentment','4.3.2.3 — Biết đủ',range(66,67)),
 ('19-hindrances','4.3.2.4 — Từ bỏ năm triền cái',range(67,75)),
 ('20-first-jhana','4.3.2.5 — Sơ thiền',range(75,77)),
 ('21-second-jhana','4.3.2.6 — Nhị thiền',range(77,79)),
 ('22-third-jhana','4.3.2.7 — Tam thiền',range(79,81)),
 ('23-fourth-jhana','4.3.2.8 — Tứ thiền',range(81,83)),
 ('24-knowledge-vision','4.3.3.1 — Tri kiến',range(83,85)),
 ('25-mind-made-body','4.3.3.2 — Thân do tâm tạo',range(85,87)),
 ('26-psychic-powers','4.3.3.3 — Các thần thông',range(87,89)),
 ('27-clairaudience','4.3.3.4 — Thiên nhĩ',range(89,91)),
 ('28-minds-of-others','4.3.3.5 — Biết tâm người khác',range(91,93)),
 ('29-past-lives','4.3.3.6 — Nhớ lại các đời trước',range(93,95)),
 ('30-clairvoyance','4.3.3.7 — Thiên nhãn',range(95,97)),
 ('31-defilements','4.3.3.8 — Đoạn tận các lậu hoặc',range(97,99)),
 ('32-conclusion','Mục 5 — Ajātasattu xin quy y',range(99,103)),
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
    if t and k.index(t) < k.index(x): return norm(r.get(t)), t
    return '', None

seen = set(); stats = {'copied': 0, 'empty': 0}
for name, label, secs in FILES:
    secs = set(secs)
    ks = [x for x in k if x.split(':')[1].split('.')[0].isdigit()
          and int(x.split(':')[1].split('.')[0]) in secs and x not in seen]
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
            if src: tag += '  ⟨= %s⟩' % src
            out.append(tag)
            if src: stats['copied'] += 1
        elif pl:
            out.append('- **EN**: (Sujato gộp đoạn này vào câu trước — dịch trực tiếp từ PLI)')
            stats['empty'] += 1
        cm = norm(c.get(x))
        if cm: out.append('- **NOTE**: ' + cm)
        out.append('')
    open(os.path.join(HERE, 'sections', name + '.md'), 'w', encoding='utf-8').write('\n'.join(out))

print('xong:', len(FILES), 'file |', len(seen), 'doan | EN muon lai:', stats['copied'], '| EN trong:', stats['empty'])
