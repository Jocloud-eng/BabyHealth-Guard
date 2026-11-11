with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for j in range(365, 380):
    if j < len(lines):
        print(f"{j}: {lines[j].rstrip()}")

