import re
import os

files = [
    'index.html',
    'frontend/index.html',
    'backend/src/main/resources/static/index.html',
    'mobile/dashboard_preview.html',
    'mobile/visits_preview.html',
    'mobile/danger_signs_preview.html'
]

print("=== AUDIT OF AI ASSISTANT BUTTONS & TRIGGERS ===")
for path in files:
    if not os.path.exists(path):
        print(f"File not found: {path}")
        continue
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for MaamaCare trigger buttons
    matches = re.findall(r'<button[^>]*onclick="[^"]*(?:toggleMaamaCare|openMaamaCare|toggleChat|openChat|MaamaCare)[^"]*"[^>]*>', content, re.I)
    # Also check id="btn-maamacare..." or floating AI buttons
    ai_buttons = re.findall(r'<button[^>]*(?:id="maamaCareFab"|id="btn-ai-assistant"|id="openMaamaCare"|id="aiDrawerBtn"|floating-ai)[^>]*>', content, re.I)
    
    print(f"\nFile: {path}")
    print(f"  AI Launcher Buttons found: {len(matches) + len(ai_buttons)}")
    for m in (matches + ai_buttons):
        print("   ->", m[:100])

