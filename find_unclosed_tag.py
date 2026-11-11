with open('frontend/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

m_start = text.find('id="view-maternal-care"')
n_start = text.find('id="view-newborn-care"')
m_chunk = text[m_start:n_start]

# Parse tags in m_chunk
import re
tags = re.findall(r'<(/?[a-zA-Z0-9]+)[^>]*>', m_chunk)
stack = []
for idx, t in enumerate(tags):
    name = t.lower()
    if name in ['img', 'input', 'br', 'hr', 'meta', 'link']:
        continue
    if not name.startswith('/'):
        stack.append((name, idx))
    else:
        close_name = name[1:]
        if stack and stack[-1][0] == close_name:
            stack.pop()
        else:
            print(f"Mismatch: found </{close_name}>, expected </{stack[-1][0] if stack else 'EMPTY'}> at tag {idx}")

print(f"Remaining unclosed tags: {len(stack)}")
for s, idx in stack:
    print(" -", s, "at tag index", idx)

