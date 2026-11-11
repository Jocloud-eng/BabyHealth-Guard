for fpath in ['mobile/dashboard_preview.html', 'mobile/visits_preview.html', 'mobile/danger_signs_preview.html']:
    with open(fpath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    print(f"\n=== {fpath} ===")
    for i, l in enumerate(lines):
        if 'openAiSideDrawer' in l or 'MaamaCare' in l:
            if 'greeting' not in l:
                print(f"Line {i}: {l.strip()[:100]}")

