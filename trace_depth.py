with open('frontend/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

m_start = None
n_start = None
for i, l in enumerate(lines):
    if 'id="view-maternal-care"' in l:
        m_start = i
    if 'id="view-newborn-care"' in l:
        n_start = i

depth = 0
for i in range(m_start, n_start):
    l = lines[i]
    opens = l.count('<div')
    closes = l.count('</div')
    depth += (opens - closes)
    if opens != closes:
        print(f"Line {i:4d}: open={opens} close={closes} => depth={depth} | {l.strip()[:60]}")

print(f"\nFinal depth at start of view-newborn-care: {depth}")

