with open('frontend/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(3165, 3195):
    if i < len(lines):
        print(f"{i}: {lines[i].rstrip()}")

