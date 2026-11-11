import os
import re

files = [
    ('Landing Page', 'index.html'),
    ('Clinical Dashboard', 'frontend/index.html'),
    ('Mother Dashboard', 'mobile/dashboard_preview.html'),
    ('Visits Screen', 'mobile/visits_preview.html'),
    ('Danger Signs Screen', 'mobile/danger_signs_preview.html'),
    ('Welcome Screen', 'mobile/welcome_preview.html')
]

print("=== FINAL SYSTEM VERIFICATION: AFRICAN IMAGES & NAVIGATION ===")

# 1. Local Image Files Verification
print("\n--- 1. Checking African Image Assets on Disk ---")
african_assets = [
    'assets/images/african_pregnant_mother.jpg',
    'assets/images/african_lactating_mother.jpg',
    'assets/images/african_healthy_baby.jpg',
    'mobile/assets/images/african_pregnant_mother.jpg',
    'mobile/assets/images/african_lactating_mother.jpg',
    'mobile/assets/images/african_healthy_baby.jpg'
]

for p in african_assets:
    if os.path.exists(p):
        print(f"  [EXISTS] {p} ({os.path.getsize(p):,} bytes)")
    else:
        print(f"  [MISSING] {p}")

# 2. Image References in HTML Files
print("\n--- 2. Checking HTML Image References ---")
for name, fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    has_af_preg = '/assets/images/african_pregnant_mother.jpg' in content
    has_af_lact = '/assets/images/african_lactating_mother.jpg' in content
    has_af_baby = '/assets/images/african_healthy_baby.jpg' in content
    print(f"  {name} ({fpath}):")
    print(f"    - African Pregnant Mother: {'YES' if has_af_preg else 'N/A'}")
    print(f"    - African Lactating Mother: {'YES' if has_af_lact else 'N/A'}")
    print(f"    - African Healthy Baby:     {'YES' if has_af_baby else 'N/A'}")

# 3. Navigation Controls (Back & Forward)
print("\n--- 3. Checking Proper Navigation (Back & Forward) ---")
for name, fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    has_back = 'navigateBack()' in content or 'history.back()' in content
    has_fwd = 'navigateForward()' in content or 'history.forward()' in content
    has_switcher = 'Quick Screen Switcher' in content or 'quickNavigate' in content
    print(f"  {name}: Back Button: {'YES' if has_back else 'NO'} | Forward Button: {'YES' if has_fwd else 'NO'} | Quick Switcher: {'YES' if has_switcher else 'NO'}")

# 4. Strictly 1 AI Assistant Button
print("\n--- 4. Checking Strictly 1 AI Assistant Button ---")
for name, fpath in files[:5]: # exclude welcome screen
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    btns = re.findall(r'<button[^>]*onclick="openAiSideDrawer\(\)"[^>]*>', content)
    status = "PASS" if len(btns) == 1 else f"FAIL ({len(btns)})"
    print(f"  [{status}] {name}: {len(btns)} AI launcher button found.")

print("\nVerification Complete!")

