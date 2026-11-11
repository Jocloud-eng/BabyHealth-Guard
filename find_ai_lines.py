with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'openAiSideDrawer()' in l:
        print(f"Line {i}: {l.strip()[:100]}")

