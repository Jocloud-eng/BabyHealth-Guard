with open('frontend/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("=== VIEW NEWBORN CARE (lines 622-750) ===")
for i in range(622, min(760, len(lines))):
    print(f"{i}: {lines[i].rstrip()[:110]}")

