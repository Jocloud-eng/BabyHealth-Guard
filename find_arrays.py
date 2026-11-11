with open('frontend/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(?:const|let|var)\s+([a-zA-Z0-9_]+)\s*=\s*\[', text)
print("Arrays found:", matches)

# Check around babyData
idx = text.find('babyData')
if idx != -1:
    print("\n--- Around babyData ---")
    print(text[idx-50:idx+800])

