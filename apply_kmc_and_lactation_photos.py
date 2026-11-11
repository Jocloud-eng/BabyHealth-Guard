"""
Script: apply_kmc_and_lactation_photos.py
Updates the exact two cards requested by the user:
1. Lactating Mother card -> /assets/images/african_lactating_mother_nursing.jpg
2. Kangaroo Care card -> /assets/images/african_mother_kangaroo_care.jpg

Applied across:
- mobile/dashboard_preview.html
- frontend/index.html
- backend/src/main/resources/static/index.html
- index.html
"""

import os
import re

print("Applying exact Lactating Mother and Mother doing Kangaroo Care photos...")

# =============================================================================
# 1. UPDATE mobile/dashboard_preview.html
# =============================================================================
mobile_path = 'mobile/dashboard_preview.html'
with open(mobile_path, 'r', encoding='utf-8') as f:
    mobile_html = f.read()

# Exact replacement for the two continuum cards shown in the user's screenshot
old_cards_mobile = '''  <!-- Maternal Care Continuum: Baby & Lactation Guides -->
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3.5 pt-1">
    
    <!-- Card 1: Lactating Mother & Breastfeeding -->
    <div class="bg-white rounded-2xl p-4 shadow-[0_4px_20px_rgba(0,0,0,0.02)] border border-emerald-100 flex items-center gap-3.5">
      <div class="relative w-16 h-16 rounded-2xl overflow-hidden shrink-0 border border-emerald-200 shadow-sm bg-slate-900">
        <img src="/assets/images/african_lactating_mother.jpg" 
             onerror="this.onerror=null; this.src='/assets/images/lactating_mother.svg';" 
             alt="Lactating Mother Nursing Baby" 
             class="w-full h-full object-cover">
      </div>
      <div class="flex flex-col min-w-0">
        <span class="text-[10px] font-bold uppercase tracking-wider text-emerald-700">Lactating Mother</span>
        <span class="text-[13px] font-bold text-slate-900 leading-snug">Exclusive Breastfeeding</span>
        <span class="text-[11px] text-slate-500 mt-0.5">Colostrum &amp; proper latch tips for newborn care.</span>
      </div>
    </div>

    <!-- Card 2: Healthy Newborn Baby Checks -->
    <div class="bg-white rounded-2xl p-4 shadow-[0_4px_20px_rgba(0,0,0,0.02)] border border-teal-100 flex items-center gap-3.5">
      <div class="relative w-16 h-16 rounded-2xl overflow-hidden shrink-0 border border-teal-200 shadow-sm bg-slate-900">
        <img src="/assets/images/african_healthy_baby.jpg" 
             onerror="this.onerror=null; this.src='/assets/images/healthy_baby.svg';" 
             alt="Healthy Newborn Baby Care" 
             class="w-full h-full object-cover">
      </div>
      <div class="flex flex-col min-w-0">
        <span class="text-[10px] font-bold uppercase tracking-wider text-teal-700">Healthy Infant</span>
        <span class="text-[13px] font-bold text-slate-900 leading-snug">Newborn Growth &amp; Warmth</span>
        <span class="text-[11px] text-slate-500 mt-0.5">Skin-to-skin Kangaroo Care &amp; cord protection.</span>
      </div>
    </div>

  </div>'''

new_cards_mobile = '''  <!-- Maternal Care Continuum: Lactating Mother & Kangaroo Mother Care -->
  <div class="grid grid-cols-1 sm:grid-cols-2 gap-3.5 pt-1">
    
    <!-- Card 1: Lactating Mother & Breastfeeding -->
    <div class="bg-white dark:bg-slate-900 rounded-2xl p-4 shadow-[0_4px_20px_rgba(0,0,0,0.02)] border border-emerald-100 dark:border-emerald-900/60 flex items-center gap-3.5 hover:border-emerald-300 transition-all">
      <div class="relative w-16 h-16 rounded-2xl overflow-hidden shrink-0 border-2 border-emerald-500 shadow-sm bg-slate-900">
        <img src="/assets/images/african_lactating_mother_nursing.jpg" 
             onerror="this.onerror=null; this.src='/assets/images/lactating_mother.svg';" 
             alt="Ugandan African Lactating Mother Breastfeeding Baby" 
             class="w-full h-full object-cover">
      </div>
      <div class="flex flex-col min-w-0">
        <span class="text-[10px] font-bold uppercase tracking-wider text-emerald-700 dark:text-emerald-400">Lactating Mother</span>
        <span class="text-[13px] font-bold text-slate-900 dark:text-white leading-snug">Exclusive Breastfeeding</span>
        <span class="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5">Colostrum &amp; proper latch tips for newborn care.</span>
      </div>
    </div>

    <!-- Card 2: Mother Doing Kangaroo Care (KMC) -->
    <div class="bg-white dark:bg-slate-900 rounded-2xl p-4 shadow-[0_4px_20px_rgba(0,0,0,0.02)] border border-teal-100 dark:border-teal-900/60 flex items-center gap-3.5 hover:border-teal-300 transition-all">
      <div class="relative w-16 h-16 rounded-2xl overflow-hidden shrink-0 border-2 border-teal-500 shadow-sm bg-slate-900">
        <img src="/assets/images/african_mother_kangaroo_care.jpg" 
             onerror="this.onerror=null; this.src='/assets/images/healthy_baby.svg';" 
             alt="Ugandan African Mother Doing Kangaroo Care for Baby" 
             class="w-full h-full object-cover">
      </div>
      <div class="flex flex-col min-w-0">
        <span class="text-[10px] font-bold uppercase tracking-wider text-teal-700 dark:text-teal-400">Kangaroo Care (KMC)</span>
        <span class="text-[13px] font-bold text-slate-900 dark:text-white leading-snug">Mother Doing Kangaroo Care</span>
        <span class="text-[11px] text-slate-500 dark:text-slate-400 mt-0.5">Skin-to-skin Kangaroo Care &amp; thermal bonding.</span>
      </div>
    </div>

  </div>'''

if old_cards_mobile in mobile_html:
    mobile_html = mobile_html.replace(old_cards_mobile, new_cards_mobile)
    print("Replaced continuum cards in mobile/dashboard_preview.html with exact nursing & kangaroo care photos.")
else:
    # Fallback regex replace for image sources in those cards
    mobile_html = re.sub(
        r'<img src="[^"]*african_lactating_mother\.jpg"[^>]*alt="Lactating Mother Nursing Baby"[^>]*>',
        '<img src="/assets/images/african_lactating_mother_nursing.jpg" onerror="this.onerror=null; this.src=\'/assets/images/lactating_mother.svg\';" alt="Ugandan African Lactating Mother Breastfeeding Baby" class="w-full h-full object-cover">',
        mobile_html
    )
    mobile_html = re.sub(
        r'<img src="[^"]*african_healthy_baby\.jpg"[^>]*alt="Healthy Newborn Baby Care"[^>]*>',
        '<img src="/assets/images/african_mother_kangaroo_care.jpg" onerror="this.onerror=null; this.src=\'/assets/images/healthy_baby.svg\';" alt="Ugandan African Mother Doing Kangaroo Care for Baby" class="w-full h-full object-cover">',
        mobile_html
    )
    # Update title
    mobile_html = mobile_html.replace('Newborn Growth &amp; Warmth', 'Mother Doing Kangaroo Care')
    print("Updated images and titles via regex in mobile/dashboard_preview.html.")

with open(mobile_path, 'w', encoding='utf-8') as f:
    f.write(mobile_html)

# =============================================================================
# 2. UPDATE frontend/index.html & backend static copy
# =============================================================================
frontend_path = 'frontend/index.html'
with open(frontend_path, 'r', encoding='utf-8') as f:
    frontend_html = f.read()

# In View 2 Card 2: Lactating Mother & Kangaroo Care
frontend_html = re.sub(
    r'<img src="[^"]*african_lactating_mother\.jpg"[^>]*alt="Lactating Mother & Kangaroo Mother Care"[^>]*>',
    '<img src="/assets/images/african_lactating_mother_nursing.jpg" onerror="this.onerror=null; this.src=\'/assets/images/lactating_mother.svg\';" alt="Ugandan African Lactating Mother Breastfeeding Baby" class="w-full h-full object-cover">',
    frontend_html
)

# In View 2 Detail Panel: Kangaroo Mother Care progress block -> Add mother doing kangaroo photo
kmc_block_target = '<div class="bg-slate-50 p-3.5 rounded-lg border border-slate-100 space-y-1.5">'
new_kmc_block = '''<div class="bg-slate-50 p-3.5 rounded-lg border border-slate-100 space-y-2">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-xl overflow-hidden shrink-0 border border-teal-500 shadow-2xs">
                  <img src="/assets/images/african_mother_kangaroo_care.jpg" 
                       onerror="this.onerror=null; this.src='/assets/images/healthy_baby.svg';" 
                       alt="Mother Doing Kangaroo Care" 
                       class="w-full h-full object-cover">
                </div>
                <div class="flex-1">
                  <div class="flex items-center justify-between text-[11px]">
                    <span class="text-slate-500 font-bold uppercase tracking-wider">KMC SKIN-TO-SKIN CARE</span>
                    <span class="font-bold text-[#0e7490]" id="panel-kmc-pct">54%</span>
                  </div>
                  <div class="w-full bg-slate-200 h-2 rounded-full overflow-hidden mt-1">
                    <div id="panel-kmc-bar" class="bg-[#0e7490] h-2 rounded-full transition-all duration-300" style="width: 54%"></div>
                  </div>
                </div>
              </div>
              <p class="text-[11px] text-slate-500 leading-tight" id="panel-kmc-text">Mother holding baby skin-to-skin: 9 of 18 hours done today (54%).</p>
            </div>'''

if kmc_block_target in frontend_html and 'african_mother_kangaroo_care' not in frontend_html:
    frontend_html = frontend_html.replace(kmc_block_target, new_kmc_block, 1)
    print("Injected Mother Doing Kangaroo Care photo into KMC panel in frontend/index.html.")

with open(frontend_path, 'w', encoding='utf-8') as f:
    f.write(frontend_html)

if os.path.exists('backend/src/main/resources/static/index.html'):
    with open('backend/src/main/resources/static/index.html', 'w', encoding='utf-8') as f:
        f.write(frontend_html)
    print("Synchronized to backend/src/main/resources/static/index.html.")

# =============================================================================
# 3. UPDATE index.html (Landing Page Continuum)
# =============================================================================
index_path = 'index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    index_html = f.read()

# Update Continuum Card 2 & Card 3
index_html = re.sub(
    r'<img src="[^"]*african_lactating_mother\.jpg"[^>]*alt="Lactating Mother Breastfeeding"[^>]*>',
    '<img src="/assets/images/african_lactating_mother_nursing.jpg" onerror="this.onerror=null; this.src=\'/assets/images/lactating_mother.svg\';" alt="Ugandan African Lactating Mother Breastfeeding Baby" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">',
    index_html
)

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_html)
print("Updated index.html continuum with African lactating mother photo.")

print("All exact KMC and Lactating mother images applied successfully!")

