with open('frontend/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("=== VIEW MATERNAL CARE (lines 401-460) ===")
for i in range(401, min(470, len(lines))):
    print(f"{i}: {lines[i].rstrip()}")

