with open('frontend/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
print("Searching for maternal patients data array:")
m = re.search(r'const\s+patients\s*=\s*\[.*?\];', text, re.S)
if m:
    print(m.group(0)[:400])

print("\nSearching for baby data array:")
m2 = re.search(r'const\s+(?:babies|babyList|babyData)\s*=\s*\[.*?\];', text, re.S)
if m2:
    print(m2.group(0)[:400])
else:
    # Look for selectBaby or filterBabyTable
    m3 = re.search(r'function\s+selectBaby\(.*?\)\s*\{.*?\}', text, re.S)
    if m3:
        print("selectBaby function:", m3.group(0)[:400])

