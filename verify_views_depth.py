with open('frontend/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

views = ['maternal-care', 'newborn-care', 'appointments', 'referrals']
view_lines = {}
for i, l in enumerate(lines):
    for v in views:
        if f'id="view-{v}"' in l:
            view_lines[v] = i

print("View line starts:", view_lines)

# Check depth between each view
main_start = None
for i, l in enumerate(lines):
    if '<main' in l:
        main_start = i
        break

print(f"Main starts at line {main_start}")

# Trace depth from main_start to end of main
depth = 0
for i in range(main_start, len(lines)):
    l = lines[i]
    opens = l.count('<div')
    closes = l.count('</div')
    depth += (opens - closes)
    for v, line_idx in view_lines.items():
        if i == line_idx:
            print(f"-> View '{v}' starts at line {i} (div depth={depth - (opens - closes)})")
    if '</main>' in l:
        print(f"Main ends at line {i} (div depth={depth})")
        break

