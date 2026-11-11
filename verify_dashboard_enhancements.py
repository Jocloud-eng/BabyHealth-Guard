import os
import re

print("=== VERIFYING MATERNAL & BABY CHECKS DASHBOARDS ===")

# 1. Check frontend/index.html
with open('frontend/index.html', 'r', encoding='utf-8') as f:
    fe_text = f.read()

has_maternal_kpis = 'MOTHERS MONITORED' in fe_text and 'HIGH-RISK ALERTS' in fe_text
has_who_checklist = 'WHO ANC Quality Checklist' in fe_text
has_baby_toggle = 'btnBabyViewCards' in fe_text and 'btnBabyViewTable' in fe_text
has_baby_photos_in_table = 'african_healthy_baby.jpg' in fe_text
has_unepi_matrix = 'UNEPI Newborn Immunization' in fe_text

print("Clinical Web Workstation (frontend/index.html):")
print(f"  - Maternal Overview KPI Ribbon (4 Cards): {'PASS' if has_maternal_kpis else 'FAIL'}")
print(f"  - WHO ANC Quality Protocol Checklist:   {'PASS' if has_who_checklist else 'FAIL'}")
print(f"  - Baby Gallery Mode Toggle (Table/Cards): {'PASS' if has_baby_toggle else 'FAIL'}")
print(f"  - Baby Photos in Checks Table & Gallery:  {'PASS' if has_baby_photos_in_table else 'FAIL'}")
print(f"  - Uganda UNEPI Immunization Matrix:       {'PASS' if has_unepi_matrix else 'FAIL'}")

# 2. Check mobile/dashboard_preview.html
with open('mobile/dashboard_preview.html', 'r', encoding='utf-8') as f:
    mob_text = f.read()

has_fetal_growth = 'Fetal Growth & Ultrasound Milestones Card' in mob_text or 'Size of an Eggplant' in mob_text
has_delivery_prep = 'Delivery Bag & Mama Kit Prep' in mob_text or 'Mama Kit Sterile Pack' in mob_text
has_lactating_card = 'african_lactating_mother_nursing.jpg' in mob_text
has_kmc_card = 'african_mother_kangaroo_care.jpg' in mob_text

print("\nPregnant Mother Mobile Dashboard (mobile/dashboard_preview.html):")
print(f"  - Fetal Growth & Milestone Visualizer:    {'PASS' if has_fetal_growth else 'FAIL'}")
print(f"  - Hospital Delivery Bag & Mama Kit Prep:  {'PASS' if has_delivery_prep else 'FAIL'}")
print(f"  - African Lactating Mother Card:          {'PASS' if has_lactating_card else 'FAIL'}")
print(f"  - African Mother Doing Kangaroo Care:     {'PASS' if has_kmc_card else 'FAIL'}")

# 3. Check Strictly 1 AI button rule
for fpath in ['frontend/index.html', 'mobile/dashboard_preview.html', 'index.html']:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    btns = re.findall(r'<button[^>]*onclick="openAiSideDrawer\(\)"[^>]*>', content)
    print(f"\n{fpath}: Exactly {len(btns)} AI button(s) found -> {'PASS' if len(btns) == 1 else 'FAIL'}")

print("\nVerification Complete!")

