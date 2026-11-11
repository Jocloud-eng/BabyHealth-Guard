with open('frontend/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("=== SIDEBAR NAVIGATION (around line 270-320) ===")
for i in range(270, 330):
    if i < len(lines):
        print(f"{i}: {lines[i].rstrip()}")

print("\n=== SEARCHING FOR switchNavView FUNCTION ===")
for i, l in enumerate(lines):
    if 'function switchNavView' in l:
        print(f"Around line {i}:")
        for j in range(max(0, i-5), min(len(lines), i+45)):
            print(f"{j}: {lines[j].rstrip()}")

