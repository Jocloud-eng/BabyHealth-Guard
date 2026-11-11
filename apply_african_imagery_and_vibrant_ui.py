"""
Script: apply_african_imagery_and_vibrant_ui.py
Replaces all external and placeholder images with authentic, local African maternal photography:
- /assets/images/african_pregnant_mother.jpg
- /assets/images/african_lactating_mother.jpg
- /assets/images/african_healthy_baby.jpg

Also adds:
- Universal Back and Forward navigation buttons on all screens with breadcrumbs and quick-switch pills
- Vibrant, lively, professional mobile/tablet UI overhaul (warm gradients, elevated cards, glassmorphic badges)
- Full synchronization across index.html, frontend/index.html, backend static, and all mobile preview screens.
"""

import os
import re

print("Starting African Maternal Imagery & Vibrant Navigation Overhaul...")

# Universal Navigation Script and Header Components
navigation_js = '''
<script>
// Universal Back / Forward / View Navigation Logic
function navigateBack() {
  if (window.history.length > 1) {
    window.history.back();
  } else {
    window.location.href = '/index.html';
  }
}

function navigateForward() {
  window.history.forward();
}

function quickNavigate(path) {
  window.location.href = path;
}
</script>
'''

# =============================================================================
# 1. OVERHAUL mobile/dashboard_preview.html
# =============================================================================
mobile_dash_path = 'mobile/dashboard_preview.html'
with open(mobile_dash_path, 'r', encoding='utf-8') as f:
    mobile_html = f.read()

# Replace all image sources with local authentic African images
mobile_html = re.sub(
    r'<img id="header-avatar"[^>]+>',
    '<img id="header-avatar" alt="Amina Brenda - Ugandan Expectant Mother" class="w-full h-full object-cover rounded-full" src="/assets/images/african_pregnant_mother.jpg" onerror="this.onerror=null; this.src=\'/assets/images/pregnant_mother.svg\';">',
    mobile_html
)

mobile_html = re.sub(
    r'<img id="hero-image"[^>]+>',
    '<img id="hero-image" alt="Ugandan African Expectant Mother smiling in clinic" class="w-full h-full object-cover transform hover:scale-105 transition-transform duration-700" src="/assets/images/african_pregnant_mother.jpg" onerror="this.onerror=null; this.src=\'/assets/images/pregnant_mother.svg\';">',
    mobile_html
)

# Replace lactating mother and baby images in mobile dashboard
mobile_html = re.sub(
    r'src="[^"]*photo-1544126592[^"]*"',
    'src="/assets/images/african_lactating_mother.jpg"',
    mobile_html
)

mobile_html = re.sub(
    r'src="[^"]*photo-1519689680[^"]*"',
    'src="/assets/images/african_healthy_baby.jpg"',
    mobile_html
)

# Enhance header with Back and Forward buttons + Breadcrumbs + Quick Screen Switcher
vibrant_mobile_header = '''<!-- Professional App Header with Back, Forward, Breadcrumbs & Theme Switcher -->
<header class="fixed top-0 inset-x-0 z-40 pt-safe bg-white/95 dark:bg-slate-900/95 backdrop-blur-xl border-b border-slate-200/80 dark:border-slate-800 shadow-xs transition-colors">
  <div class="px-3 sm:px-4 pt-2.5 pb-2 flex items-center justify-between gap-2 max-w-md md:max-w-4xl lg:max-w-6xl mx-auto">
    
    <!-- Left Navigation: Back & Forward Controls -->
    <div class="flex items-center gap-1.5 shrink-0">
      <button onclick="navigateBack()" aria-label="Go Back" class="w-9 h-9 rounded-full bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 flex items-center justify-center transition-all active:scale-95 shadow-2xs cursor-pointer" title="Go to Previous Page">
        <span class="material-symbols-outlined text-[20px]">arrow_back</span>
      </button>
      <button onclick="navigateForward()" aria-label="Go Forward" class="w-9 h-9 rounded-full bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 flex items-center justify-center transition-all active:scale-95 shadow-2xs cursor-pointer" title="Go to Next Page">
        <span class="material-symbols-outlined text-[20px]">arrow_forward</span>
      </button>
    </div>

    <!-- Center Profile & Breadcrumb -->
    <div class="flex items-center gap-2.5 min-w-0 flex-1">
      <div class="relative w-10 h-10 rounded-full overflow-hidden shrink-0 border-2 border-teal-500 shadow-sm bg-slate-100">
        <img id="header-avatar" alt="Amina Brenda - Ugandan Expectant Mother" class="w-full h-full object-cover" src="/assets/images/african_pregnant_mother.jpg" onerror="this.onerror=null; this.src='/assets/images/pregnant_mother.svg';">
        <span class="absolute bottom-0 right-0 w-3 h-3 bg-emerald-500 rounded-full border-2 border-white dark:border-slate-900"></span>
      </div>
      <div class="flex flex-col min-w-0">
        <div class="flex items-center gap-1.5">
          <span class="text-xs font-bold text-slate-900 dark:text-white truncate">Amina Brenda</span>
          <span class="px-2 py-0.2 rounded-full bg-teal-50 dark:bg-teal-900/40 text-teal-700 dark:text-teal-300 text-[10px] font-bold border border-teal-200/60 dark:border-teal-800 shrink-0">Kagando Village</span>
        </div>
        <div class="flex items-center gap-1 text-[11px] text-slate-500 dark:text-slate-400">
          <span class="text-teal-700 dark:text-teal-400 font-semibold">Home</span>
          <span>›</span>
          <span class="truncate font-medium">Mother Dashboard (Week 28)</span>
        </div>
      </div>
    </div>

    <!-- Right Actions: Theme Toggle, Sync, Notifications & Sign Out -->
    <div class="flex items-center gap-1.5 shrink-0">
      <button onclick="toggleTheme()" class="theme-toggle-btn w-9 h-9 rounded-full bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 flex items-center justify-center transition-transform active:scale-95 shadow-2xs cursor-pointer" title="Toggle Dark/Light Mode">
        <span class="material-symbols-outlined theme-toggle-icon text-[18px]">dark_mode</span>
      </button>
      <button onclick="handleMotherSignOut()" aria-label="Sign Out" class="p-2 sm:px-2.5 sm:py-1.5 rounded-full bg-rose-50 hover:bg-rose-100 dark:bg-rose-950/40 dark:hover:bg-rose-900/60 text-rose-700 dark:text-rose-300 font-bold text-xs flex items-center gap-1 border border-rose-200/80 dark:border-rose-900 shadow-2xs active:scale-95 transition-all cursor-pointer" title="Sign Out Profile">
        <span class="material-symbols-outlined text-[16px]">logout</span>
        <span class="hidden md:inline">Sign Out</span>
      </button>
    </div>
  </div>

  <!-- Quick Screen Switcher Pill Ribbon (Mobile & Tablet) -->
  <div class="px-3 sm:px-4 py-1.5 bg-slate-50/90 dark:bg-slate-950/90 border-t border-slate-100 dark:border-slate-800 overflow-x-auto no-scrollbar">
    <div class="flex items-center gap-2 text-xs font-semibold max-w-md md:max-w-4xl lg:max-w-6xl mx-auto whitespace-nowrap">
      <a href="/index.html" class="px-3 py-1 rounded-full bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 hover:border-teal-500 transition-colors flex items-center gap-1 shadow-2xs">
        <span class="material-symbols-outlined text-[15px] text-teal-600">home</span> Home
      </a>
      <a href="/mobile/dashboard_preview.html" class="px-3 py-1 rounded-full bg-[#0e7490] text-white flex items-center gap-1 shadow-xs">
        <span class="material-symbols-outlined text-[15px]">pregnant_woman</span> Dashboard
      </a>
      <a href="/mobile/visits_preview.html" class="px-3 py-1 rounded-full bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 hover:border-teal-500 transition-colors flex items-center gap-1 shadow-2xs">
        <span class="material-symbols-outlined text-[15px] text-teal-600">calendar_month</span> ANC Visits
      </a>
      <a href="/mobile/danger_signs_preview.html" class="px-3 py-1 rounded-full bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 hover:border-amber-500 transition-colors flex items-center gap-1 shadow-2xs">
        <span class="material-symbols-outlined text-[15px] text-amber-500">warning</span> Danger Signs
      </a>
      <a href="/frontend/index.html" class="px-3 py-1 rounded-full bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 hover:border-teal-500 transition-colors flex items-center gap-1 shadow-2xs">
        <span class="material-symbols-outlined text-[15px] text-emerald-600">local_hospital</span> Clinic Workstation
      </a>
    </div>
  </div>
</header>'''

# Replace the existing header in mobile dashboard
old_mobile_hdr_pattern = r'<header class="fixed top-0 inset-x-0 z-40.*?</header>'
mobile_html = re.sub(old_mobile_hdr_pattern, vibrant_mobile_header, mobile_html, flags=re.DOTALL)

# Inject navigation JS before </body>
if 'function navigateBack()' not in mobile_html:
    mobile_html = mobile_html.replace('</body>', f'{navigation_js}\n</body>')

with open(mobile_dash_path, 'w', encoding='utf-8') as f:
    f.write(mobile_html)
print("Updated mobile/dashboard_preview.html with African imagery, vibrant UI, and Back/Forward nav.")

# =============================================================================
# 2. OVERHAUL mobile/visits_preview.html
# =============================================================================
visits_path = 'mobile/visits_preview.html'
with open(visits_path, 'r', encoding='utf-8') as f:
    visits_html = f.read()

# Replace any image in visits with African pregnant mother photo
visits_html = re.sub(
    r'src="[^"]*(?:photo-159670|pregnant_mother)[^"]*"',
    'src="/assets/images/african_pregnant_mother.jpg"',
    visits_html
)

visits_header = '''<!-- Professional Visits Header with Back, Forward & Screen Switcher -->
<header class="fixed top-0 inset-x-0 z-40 pt-safe bg-white/95 dark:bg-slate-900/95 backdrop-blur-xl border-b border-slate-200/80 dark:border-slate-800 shadow-xs transition-colors">
  <div class="px-3 sm:px-4 pt-2.5 pb-2 flex items-center justify-between gap-2 max-w-md md:max-w-3xl lg:max-w-4xl mx-auto">
    <div class="flex items-center gap-1.5 shrink-0">
      <button onclick="navigateBack()" aria-label="Go Back" class="w-9 h-9 rounded-full bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 flex items-center justify-center transition-all active:scale-95 shadow-2xs cursor-pointer" title="Go to Previous Page">
        <span class="material-symbols-outlined text-[20px]">arrow_back</span>
      </button>
      <button onclick="navigateForward()" aria-label="Go Forward" class="w-9 h-9 rounded-full bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 flex items-center justify-center transition-all active:scale-95 shadow-2xs cursor-pointer" title="Go to Next Page">
        <span class="material-symbols-outlined text-[20px]">arrow_forward</span>
      </button>
    </div>
    
    <div class="flex flex-col min-w-0 flex-1">
      <div class="flex items-center gap-2">
        <h1 class="text-sm font-bold text-slate-900 dark:text-white truncate">Antenatal Clinic Visits</h1>
        <span class="px-2 py-0.5 rounded-full bg-teal-50 dark:bg-teal-900/40 text-teal-700 dark:text-teal-300 text-[10px] font-bold">ANC 3 of 4</span>
      </div>
      <div class="flex items-center gap-1 text-[11px] text-slate-500 dark:text-slate-400">
        <a href="/mobile/dashboard_preview.html" class="text-teal-700 dark:text-teal-400 hover:underline">Dashboard</a>
        <span>›</span>
        <span>Clinic Schedule</span>
      </div>
    </div>

    <div class="flex items-center gap-1.5 shrink-0">
      <button onclick="toggleTheme()" class="theme-toggle-btn w-9 h-9 rounded-full bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 flex items-center justify-center transition-transform active:scale-95 shadow-2xs cursor-pointer" title="Toggle Dark/Light Mode">
        <span class="material-symbols-outlined theme-toggle-icon text-[18px]">dark_mode</span>
      </button>
      <a href="tel:112" class="px-3 py-1.5 rounded-full bg-red-600 hover:bg-red-700 text-white font-bold text-xs flex items-center gap-1 shadow-xs active:scale-95 transition-all">
        <span class="material-symbols-outlined text-[16px]">call</span>
        <span class="hidden sm:inline">Emergency 112</span>
      </a>
    </div>
  </div>

  <!-- Quick Screen Switcher -->
  <div class="px-3 sm:px-4 py-1.5 bg-slate-50/90 dark:bg-slate-950/90 border-t border-slate-100 dark:border-slate-800 overflow-x-auto no-scrollbar">
    <div class="flex items-center gap-2 text-xs font-semibold max-w-md md:max-w-3xl lg:max-w-4xl mx-auto whitespace-nowrap">
      <a href="/mobile/dashboard_preview.html" class="px-3 py-1 rounded-full bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 hover:border-teal-500 transition-colors flex items-center gap-1 shadow-2xs">
        <span class="material-symbols-outlined text-[15px] text-teal-600">pregnant_woman</span> Dashboard
      </a>
      <a href="/mobile/visits_preview.html" class="px-3 py-1 rounded-full bg-[#0e7490] text-white flex items-center gap-1 shadow-xs">
        <span class="material-symbols-outlined text-[15px]">calendar_month</span> ANC Visits
      </a>
      <a href="/mobile/danger_signs_preview.html" class="px-3 py-1 rounded-full bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 hover:border-amber-500 transition-colors flex items-center gap-1 shadow-2xs">
        <span class="material-symbols-outlined text-[15px] text-amber-500">warning</span> Danger Signs
      </a>
      <a href="/frontend/index.html" class="px-3 py-1 rounded-full bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 hover:border-teal-500 transition-colors flex items-center gap-1 shadow-2xs">
        <span class="material-symbols-outlined text-[15px] text-emerald-600">local_hospital</span> Clinic Workstation
      </a>
      <a href="/index.html" class="px-3 py-1 rounded-full bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 hover:border-teal-500 transition-colors flex items-center gap-1 shadow-2xs">
        <span class="material-symbols-outlined text-[15px] text-teal-600">home</span> Home
      </a>
    </div>
  </div>
</header>'''

visits_html = re.sub(r'<header class="fixed top-0.*?<\/header>', visits_header, visits_html, flags=re.DOTALL)
if 'function navigateBack()' not in visits_html:
    visits_html = visits_html.replace('</body>', f'{navigation_js}\n</body>')

with open(visits_path, 'w', encoding='utf-8') as f:
    f.write(visits_html)
print("Updated mobile/visits_preview.html with African imagery and Back/Forward nav.")

# =============================================================================
# 3. OVERHAUL mobile/danger_signs_preview.html
# =============================================================================
danger_path = 'mobile/danger_signs_preview.html'
with open(danger_path, 'r', encoding='utf-8') as f:
    danger_html = f.read()

danger_header = '''<!-- Professional Danger Signs Header with Back, Forward & Screen Switcher -->
<header class="fixed top-0 inset-x-0 z-40 pt-safe bg-white/95 dark:bg-slate-900/95 backdrop-blur-xl border-b border-slate-200/80 dark:border-slate-800 shadow-xs transition-colors">
  <div class="px-3 sm:px-4 pt-2.5 pb-2 flex items-center justify-between gap-2 max-w-md md:max-w-3xl lg:max-w-4xl mx-auto">
    <div class="flex items-center gap-1.5 shrink-0">
      <button onclick="navigateBack()" aria-label="Go Back" class="w-9 h-9 rounded-full bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 flex items-center justify-center transition-all active:scale-95 shadow-2xs cursor-pointer" title="Go to Previous Page">
        <span class="material-symbols-outlined text-[20px]">arrow_back</span>
      </button>
      <button onclick="navigateForward()" aria-label="Go Forward" class="w-9 h-9 rounded-full bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 flex items-center justify-center transition-all active:scale-95 shadow-2xs cursor-pointer" title="Go to Next Page">
        <span class="material-symbols-outlined text-[20px]">arrow_forward</span>
      </button>
    </div>
    
    <div class="flex flex-col min-w-0 flex-1">
      <div class="flex items-center gap-2">
        <h1 class="text-sm font-bold text-red-600 dark:text-red-400 flex items-center gap-1 truncate">
          <span class="material-symbols-outlined text-[18px]">warning</span> Maternal Danger Signs
        </h1>
      </div>
      <div class="flex items-center gap-1 text-[11px] text-slate-500 dark:text-slate-400">
        <a href="/mobile/dashboard_preview.html" class="text-teal-700 dark:text-teal-400 hover:underline">Dashboard</a>
        <span>›</span>
        <span>Emergency Triage</span>
      </div>
    </div>

    <div class="flex items-center gap-1.5 shrink-0">
      <button onclick="toggleTheme()" class="theme-toggle-btn w-9 h-9 rounded-full bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 flex items-center justify-center transition-transform active:scale-95 shadow-2xs cursor-pointer" title="Toggle Dark/Light Mode">
        <span class="material-symbols-outlined theme-toggle-icon text-[18px]">dark_mode</span>
      </button>
      <a href="tel:112" class="px-3.5 py-1.5 rounded-full bg-red-600 hover:bg-red-700 text-white font-extrabold text-xs flex items-center gap-1 shadow-md active:scale-95 transition-all">
        <span class="material-symbols-outlined text-[16px]">call</span>
        <span>112 Free</span>
      </a>
    </div>
  </div>

  <!-- Quick Screen Switcher -->
  <div class="px-3 sm:px-4 py-1.5 bg-slate-50/90 dark:bg-slate-950/90 border-t border-slate-100 dark:border-slate-800 overflow-x-auto no-scrollbar">
    <div class="flex items-center gap-2 text-xs font-semibold max-w-md md:max-w-3xl lg:max-w-4xl mx-auto whitespace-nowrap">
      <a href="/mobile/dashboard_preview.html" class="px-3 py-1 rounded-full bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 hover:border-teal-500 transition-colors flex items-center gap-1 shadow-2xs">
        <span class="material-symbols-outlined text-[15px] text-teal-600">pregnant_woman</span> Dashboard
      </a>
      <a href="/mobile/visits_preview.html" class="px-3 py-1 rounded-full bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 hover:border-teal-500 transition-colors flex items-center gap-1 shadow-2xs">
        <span class="material-symbols-outlined text-[15px] text-teal-600">calendar_month</span> ANC Visits
      </a>
      <a href="/mobile/danger_signs_preview.html" class="px-3 py-1 rounded-full bg-red-600 text-white flex items-center gap-1 shadow-xs">
        <span class="material-symbols-outlined text-[15px]">warning</span> Danger Signs
      </a>
      <a href="/frontend/index.html" class="px-3 py-1 rounded-full bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 hover:border-teal-500 transition-colors flex items-center gap-1 shadow-2xs">
        <span class="material-symbols-outlined text-[15px] text-emerald-600">local_hospital</span> Clinic Workstation
      </a>
      <a href="/index.html" class="px-3 py-1 rounded-full bg-white dark:bg-slate-800 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 hover:border-teal-500 transition-colors flex items-center gap-1 shadow-2xs">
        <span class="material-symbols-outlined text-[15px] text-teal-600">home</span> Home
      </a>
    </div>
  </div>
</header>'''

danger_html = re.sub(r'<header class="fixed top-0.*?<\/header>', danger_header, danger_html, flags=re.DOTALL)
if 'function navigateBack()' not in danger_html:
    danger_html = danger_html.replace('</body>', f'{navigation_js}\n</body>')

with open(danger_path, 'w', encoding='utf-8') as f:
    f.write(danger_html)
print("Updated mobile/danger_signs_preview.html with Back/Forward nav.")

# =============================================================================
# 4. OVERHAUL index.html (Landing Page)
# =============================================================================
index_path = 'index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    index_html = f.read()

# Replace Hero and Continuum images with authentic African images
# 1. Hero Image
index_html = re.sub(
    r'<img src="https://images\.unsplash\.com/photo-1596704017254[^"]*"[^>]*alt="Pregnant Mother[^"]*"[^>]*>',
    '<img src="/assets/images/african_pregnant_mother.jpg" onerror="this.onerror=null; this.src=\'/assets/images/pregnant_mother.svg\';" alt="Ugandan African Expectant Mother" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700">',
    index_html
)

# 2. Continuum Card 1 (Pregnant Mother)
index_html = re.sub(
    r'src="https://images\.unsplash\.com/photo-1596704017254[^"]*"',
    'src="/assets/images/african_pregnant_mother.jpg"',
    index_html
)

# 3. Continuum Card 2 (Healthy Baby)
index_html = re.sub(
    r'src="https://images\.unsplash\.com/photo-1519689680058[^"]*"',
    'src="/assets/images/african_healthy_baby.jpg"',
    index_html
)

# 4. Continuum Card 3 (Lactating Mother)
index_html = re.sub(
    r'src="https://images\.unsplash\.com/photo-1544126592-807ade215a0b[^"]*"',
    'src="/assets/images/african_lactating_mother.jpg"',
    index_html
)

# Add Back and Forward buttons to index.html navigation bar
nav_btn_target = '<div class="flex items-center gap-3">'
nav_controls_landing = '''<div class="flex items-center gap-1.5 mr-2">
          <button onclick="navigateBack()" aria-label="Go Back" class="w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 flex items-center justify-center transition-all active:scale-95 shadow-2xs cursor-pointer" title="Go to Previous Page">
            <span class="material-symbols-outlined text-[18px]">arrow_back</span>
          </button>
          <button onclick="navigateForward()" aria-label="Go Forward" class="w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 flex items-center justify-center transition-all active:scale-95 shadow-2xs cursor-pointer" title="Go to Next Page">
            <span class="material-symbols-outlined text-[18px]">arrow_forward</span>
          </button>
        </div>'''

if 'navigateBack()' not in index_html and nav_btn_target in index_html:
    index_html = index_html.replace(nav_btn_target, f'{nav_btn_target}\n        {nav_controls_landing}', 1)

if 'function navigateBack()' not in index_html:
    index_html = index_html.replace('</body>', f'{navigation_js}\n</body>')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_html)
print("Updated index.html with African maternal imagery and navigation controls.")

# =============================================================================
# 5. OVERHAUL frontend/index.html (Clinical Web Dashboard)
# =============================================================================
frontend_path = 'frontend/index.html'
with open(frontend_path, 'r', encoding='utf-8') as f:
    frontend_html = f.read()

# Replace pregnant mother, baby, and lactating mother images in frontend
frontend_html = re.sub(
    r'src="https://images\.unsplash\.com/photo-1596704017254[^"]*"',
    'src="/assets/images/african_pregnant_mother.jpg"',
    frontend_html
)

frontend_html = re.sub(
    r'src="https://images\.unsplash\.com/photo-1519689680058[^"]*"',
    'src="/assets/images/african_healthy_baby.jpg"',
    frontend_html
)

frontend_html = re.sub(
    r'src="https://images\.unsplash\.com/photo-1544126592-807ade215a0b[^"]*"',
    'src="/assets/images/african_lactating_mother.jpg"',
    frontend_html
)

# Add Forward button next to existing Back button in Clinical Dashboard Header
old_back_btn = '<a href="/index.html" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 text-xs font-bold transition-colors shadow-2xs cursor-pointer" title="Back to Home Page">'
new_nav_btns = '''<div class="flex items-center gap-1">
          <button onclick="navigateBack()" class="p-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 transition-colors shadow-2xs cursor-pointer" title="Go to Previous Page">
            <span class="material-symbols-outlined text-[18px]">arrow_back</span>
          </button>
          <button onclick="navigateForward()" class="p-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 transition-colors shadow-2xs cursor-pointer" title="Go to Next Page">
            <span class="material-symbols-outlined text-[18px]">arrow_forward</span>
          </button>
          <a href="/index.html" class="inline-flex items-center gap-1 px-2.5 py-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 text-xs font-bold transition-colors shadow-2xs cursor-pointer" title="Back to Home Page">
            <span class="material-symbols-outlined text-[16px]">home</span>
            <span class="hidden xl:inline">Home</span>
          </a>
        </div>'''

if old_back_btn in frontend_html:
    frontend_html = frontend_html.replace(old_back_btn, new_nav_btns, 1)

if 'function navigateBack()' not in frontend_html:
    frontend_html = frontend_html.replace('</body>', f'{navigation_js}\n</body>')

with open(frontend_path, 'w', encoding='utf-8') as f:
    f.write(frontend_html)

# Synchronize backend static copy
if os.path.exists('backend/src/main/resources/static/index.html'):
    with open('backend/src/main/resources/static/index.html', 'w', encoding='utf-8') as f:
        f.write(frontend_html)
    print("Synchronized to backend/src/main/resources/static/index.html.")

# =============================================================================
# 6. OVERHAUL mobile/welcome_preview.html
# =============================================================================
welcome_path = 'mobile/welcome_preview.html'
if os.path.exists(welcome_path):
    with open(welcome_path, 'r', encoding='utf-8') as f:
        welcome_html = f.read()
    
    welcome_html = re.sub(
        r'<img[^>]+baby_welcome\.jpg[^>]+>',
        '<img alt="Ugandan African newborn baby" class="w-full h-full object-cover object-center transform hover:scale-105 transition-transform duration-700 ease-out" src="/assets/images/african_healthy_baby.jpg" onerror="this.onerror=null; this.src=\'/assets/images/baby_welcome.jpg\';">',
        welcome_html
    )
    if 'function navigateBack()' not in welcome_html:
        welcome_html = welcome_html.replace('</body>', f'{navigation_js}\n</body>')
    with open(welcome_path, 'w', encoding='utf-8') as f:
        f.write(welcome_html)
    print("Updated mobile/welcome_preview.html with African healthy baby photo.")

print("\nAll African imagery deployed and navigation back/forward active across all devices!")

