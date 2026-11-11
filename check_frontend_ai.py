with open('frontend/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'openAiSideDrawer' in l or 'MaamaCare' in l:
        print(f"Line {i}: {l.strip()[:100]}")

