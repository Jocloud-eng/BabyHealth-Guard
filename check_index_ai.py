with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [line for line in text.splitlines() if 'maamacare' in line.lower() or 'assistant' in line.lower()]
print(f"Total matching lines in index.html: {len(matches)}")
for l in matches[:15]:
    print(" -", l.strip()[:100])

