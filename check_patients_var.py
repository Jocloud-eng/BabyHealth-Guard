with open('frontend/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [l for l in text.splitlines() if 'patients' in l.lower() and ('[' in l or '{' in l or 'let ' in l or 'var ' in l)]
for m in matches[:10]:
    print(m)

