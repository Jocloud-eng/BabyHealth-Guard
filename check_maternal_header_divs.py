with open('frontend/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(418, 442):
    print(f"{i}: {lines[i].rstrip()}")

