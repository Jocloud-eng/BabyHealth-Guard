with open('frontend/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'id="view-newborn-care"' in l:
        print(f"Around line {i}:")
        for j in range(max(0, i-10), min(len(lines), i+25)):
            print(f"{j}: {lines[j].rstrip()}")

