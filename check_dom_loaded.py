with open('frontend/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [l for l in text.splitlines() if 'DOMContentLoaded' in l or 'switchNavView' in l]
for m in matches:
    print(m)

