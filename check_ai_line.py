with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'MaamaCare AI (10 Dialects)' in l:
        print(f"Around line {i}:")
        for j in range(max(0, i-5), min(len(lines), i+15)):
            print(f"{j}: {lines[j].rstrip()}")

