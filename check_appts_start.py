with open('frontend/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'id="view-appointments"' in l:
        print(f"Around line {i}:")
        for j in range(max(0, i-10), min(len(lines), i+15)):
            print(f"{j}: {lines[j].rstrip()}")

