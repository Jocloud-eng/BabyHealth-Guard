import re
import urllib.request
import os

print("=== COMPREHENSIVE VERIFICATION SUITE ===")

# Test 1: HTTP Accessibility of Local Assets on server
assets = [
    '/assets/images/pregnant_mother.svg',
    '/assets/images/lactating_mother.svg',
    '/assets/images/healthy_baby.svg',
    '/assets/images/baby_welcome.jpg',
    '/',
    '/frontend/index.html',
    '/mobile/dashboard_preview.html',
    '/mobile/visits_preview.html',
    '/mobile/danger_signs_preview.html',
    '/mobile/welcome_preview.html'
]

print("\n--- 1. Testing HTTP Server (Port 8080) Endpoints ---")
for asset in assets:
    url = f"http://localhost:8080{asset}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=3) as resp:
            content_type = resp.headers.get('Content-Type', '')
            content_length = len(resp.read())
            print(f"  [OK] 200 {asset} ({content_length} bytes, {content_type})")
    except Exception as e:
        print(f"  [FAIL] {asset} -> {e}")

# Test 2: AI Button Count (Strictly 1 AI button per page)
print("\n--- 2. Verifying STRICT Single AI Assistant Button Rule ---")
pages = [
    ('Landing Page', 'index.html'),
    ('Clinical Dashboard', 'frontend/index.html'),
    ('Mother Dashboard', 'mobile/dashboard_preview.html'),
    ('Visits Preview', 'mobile/visits_preview.html'),
    ('Danger Signs Preview', 'mobile/danger_signs_preview.html')
]

for name, fpath in pages:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Find all button triggers that open the AI drawer
    matches = re.findall(r'<button[^>]*onclick="openAiSideDrawer\(\)"[^>]*>', content)
    status = "PASS" if len(matches) == 1 else "FAIL"
    print(f"  [{status}] {name} ({fpath}): Exactly {len(matches)} AI trigger button(s) found.")

# Test 3: Check Presence of Pregnant Mother, Baby, and Lactating Mother Images
print("\n--- 3. Verifying Maternal & Infant Imagery ---")
for name, fpath in pages:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    has_pregnant = 'pregnant_mother' in content
    has_baby = 'healthy_baby' in content or 'baby_welcome' in content
    has_lactating = 'lactating_mother' in content
    print(f"  {name} ({fpath}):")
    print(f"    - Pregnant Mother Image: {'FOUND' if has_pregnant else 'Not in this view'}")
    print(f"    - Healthy Baby Image:   {'FOUND' if has_baby else 'Not in this view'}")
    print(f"    - Lactating Mother Image:{'FOUND' if has_lactating else 'Not in this view'}")

# Test 4: Navigation & Sign Out Verification
print("\n--- 4. Verifying Back & Sign Out Navigation ---")
for name, fpath in pages:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    has_back = 'Back' in content or 'arrow_back' in content or 'chevron_left' in content
    has_signout = 'handleSignOut()' in content or 'Sign Out' in content or 'logout' in content
    print(f"  {name}: Back Navigation: {'YES' if has_back else 'N/A (Root)'} | Sign Out / Exit: {'YES' if has_signout else 'N/A'}")

# Test 5: Institutional Contacts in Footers
print("\n--- 5. Verifying Institutional Contacts (+256 778 501 066, infor@babyguard.org, WhatsApp) ---")
for name, fpath in pages:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    has_phone = '256778501066' in content
    has_email = 'infor@babyguard.org' in content
    has_wa = 'wa.me/256778501066' in content
    print(f"  {name}: Phone: {'YES' if has_phone else 'NO'} | Email: {'YES' if has_email else 'NO'} | WhatsApp: {'YES' if has_wa else 'NO'}")

print("\nVerification Completed!")

