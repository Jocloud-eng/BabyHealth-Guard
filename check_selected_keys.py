with open('frontend/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [l for l in text.splitlines() if 'selectedBabyKey' in l or 'selectedPatientId' in l]
for m in matches:
    print(m)

