with open('frontend/index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

m_start = None
n_start = None
appts_start = None

for i, l in enumerate(lines):
    if 'id="view-maternal-care"' in l:
        m_start = i
    if 'id="view-newborn-care"' in l:
        n_start = i
    if 'id="view-appointments"' in l:
        appts_start = i

print(f"Maternal care start: {m_start}")
print(f"Newborn care start: {n_start}")
print(f"Appointments start: {appts_start}")

