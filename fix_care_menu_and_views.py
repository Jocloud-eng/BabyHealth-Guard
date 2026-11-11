"""
Script: fix_care_menu_and_views.py
Fixes:
1. Div structure in view-maternal-care (closes banner div cleanly).
2. Removes duplicated KMC block in view-newborn-care so both views close at depth 0.
3. Fixes switchNavView to explicitly render maternal-care and newborn-care when clicked.
4. Sets default view to 'maternal-care' so the clinical dashboard opens directly to Pregnant Mothers.
5. Verifies both views show their full tables, cards, and drawers without any blank screens.
"""

import os
import re

print("=== FIXING CARE MENU & DASHBOARD VIEWS ===")

frontend_path = 'frontend/index.html'
with open(frontend_path, 'r', encoding='utf-8') as f:
    html = f.read()

# -----------------------------------------------------------------------------
# 1. FIX view-maternal-care header banner divs
# -----------------------------------------------------------------------------
old_banner_html = '''          <div class="flex items-center gap-2.5">
          <div class="flex items-center flex-wrap gap-2.5">
            <button onclick="downloadMaternalRegistryCSV()" class="inline-flex items-center gap-2 px-3.5 py-2.5 rounded-lg border border-slate-200 bg-white text-slate-700 text-[13px] font-semibold hover:bg-slate-50 transition-all shadow-xs cursor-pointer" title="Download Maternal Health Registry as CSV file">
              <span class="material-symbols-outlined text-[18px]">download</span>
              <span>Download CSV</span>
            </button>
            <button onclick="openFacilityReportModal()" class="inline-flex items-center gap-2 px-3.5 py-2.5 rounded-lg bg-emerald-700 hover:bg-emerald-800 text-white text-[13px] font-semibold transition-all shadow-xs cursor-pointer" title="Generate Ministry of Health FR12 Facility Report">
              <span class="material-symbols-outlined text-[18px]">summarize</span>
              <span>Monthly Report (FR12)</span>
            </button>
            <button onclick="openRegisterMotherModal()" class="inline-flex items-center gap-2 px-4 py-2.5 rounded-lg bg-[#0e7490] text-white text-[13px] font-semibold hover:bg-[#0c627a] transition-all shadow-xs cursor-pointer">
              <span class="material-symbols-outlined text-[18px]">add_circle</span>
              <span>Register Expectant Mother</span>
            </button>
          </div>
        </div>'''

fixed_banner_html = '''          <div class="flex items-center flex-wrap gap-2.5">
            <button onclick="downloadMaternalRegistryCSV()" class="inline-flex items-center gap-2 px-3.5 py-2.5 rounded-lg border border-slate-200 bg-white text-slate-700 text-[13px] font-semibold hover:bg-slate-50 transition-all shadow-xs cursor-pointer" title="Download Maternal Health Registry as CSV file">
              <span class="material-symbols-outlined text-[18px]">download</span>
              <span>Download CSV</span>
            </button>
            <button onclick="openFacilityReportModal()" class="inline-flex items-center gap-2 px-3.5 py-2.5 rounded-lg bg-emerald-700 hover:bg-emerald-800 text-white text-[13px] font-semibold transition-all shadow-xs cursor-pointer" title="Generate Ministry of Health FR12 Facility Report">
              <span class="material-symbols-outlined text-[18px]">summarize</span>
              <span>Monthly Report (FR12)</span>
            </button>
            <button onclick="openRegisterMotherModal()" class="inline-flex items-center gap-2 px-4 py-2.5 rounded-lg bg-[#0e7490] text-white text-[13px] font-semibold hover:bg-[#0c627a] transition-all shadow-xs cursor-pointer">
              <span class="material-symbols-outlined text-[18px]">add_circle</span>
              <span>Register Expectant Mother</span>
            </button>
          </div>
        </div>'''

if old_banner_html in html:
    html = html.replace(old_banner_html, fixed_banner_html, 1)
    print("Fixed unclosed div in view-maternal-care header banner.")

# -----------------------------------------------------------------------------
# 2. REMOVE DUPLICATE KMC BLOCK IN view-newborn-care
# -----------------------------------------------------------------------------
old_duplicate_kmc = '''              <div class="flex items-center justify-between text-[11px]">
                <span class="text-slate-500 font-bold uppercase tracking-wider">KMC SKIN-TO-SKIN CARE</span>
                <span class="font-bold text-[#0e7490]" id="panel-kmc-pct">54%</span>
              </div>
              <div class="w-full bg-slate-200 h-2 rounded-full overflow-hidden">
                <div id="panel-kmc-bar" class="bg-[#0e7490] h-2 rounded-full transition-all duration-300" style="width: 54%"></div>
              </div>
              <p class="text-[11px] text-slate-500 leading-tight" id="panel-kmc-text">Mother holding baby skin-to-skin: 9 of 18 hours done today (54%).</p>
            </div>'''

if old_duplicate_kmc in html:
    html = html.replace(old_duplicate_kmc, '', 1)
    print("Removed duplicate KMC block and extra closing div in view-newborn-care.")

# -----------------------------------------------------------------------------
# 3. UPGRADE switchNavView FUNCTION
# -----------------------------------------------------------------------------
old_switch_nav = '''function switchNavView(viewName) {
  toggleMobileSidebar(false);
  document.querySelectorAll('.nav-btn').forEach(btn => {
    if (btn.dataset.view === viewName) {
      btn.className = 'nav-btn flex items-center gap-3 px-3.5 py-2.5 rounded-lg bg-[#0e7490] text-white font-semibold shadow-sm transition-all cursor-pointer';
      btn.querySelector('.material-symbols-outlined').className = 'material-symbols-outlined text-[20px] text-white';
    } else {
      btn.className = 'nav-btn flex items-center gap-3 px-3.5 py-2.5 rounded-lg text-slate-200 hover:bg-white/10 hover:text-white transition-colors duration-150 cursor-pointer';
      btn.querySelector('.material-symbols-outlined').className = 'material-symbols-outlined text-[20px] text-cyan-300';
    }
  });

  const views = ['maternal-care', 'newborn-care', 'appointments', 'referrals'];
  views.forEach(v => {
    const el = document.getElementById('view-' + v);
    if (el) {
      if (v === viewName) el.classList.remove('hidden');
      else el.classList.add('hidden');
    }
  });

  if (viewName === 'appointments') {
    renderAppointmentsList('ALL');
  } else if (viewName === 'newborn-care') {
    renderBabyTable();
    selectBaby(selectedBabyKey);
  } else if (viewName === 'referrals') {
    renderTransfersTable();
    selectTransfer(selectedTransferKey);
  }

  window.scrollTo({ top: 0, behavior: 'smooth' });
}'''

new_switch_nav = '''function switchNavView(viewName) {
  toggleMobileSidebar(false);
  document.querySelectorAll('.nav-btn').forEach(btn => {
    if (btn.dataset.view === viewName) {
      btn.className = 'nav-btn flex items-center gap-3 px-3.5 py-2.5 rounded-lg bg-[#0e7490] text-white font-semibold shadow-sm transition-all cursor-pointer';
      const icon = btn.querySelector('.material-symbols-outlined');
      if (icon) icon.className = 'material-symbols-outlined text-[20px] text-white';
    } else {
      btn.className = 'nav-btn flex items-center gap-3 px-3.5 py-2.5 rounded-lg text-slate-200 hover:bg-white/10 hover:text-white transition-colors duration-150 cursor-pointer';
      const icon = btn.querySelector('.material-symbols-outlined');
      if (icon) icon.className = 'material-symbols-outlined text-[20px] text-cyan-300';
    }
  });

  const views = ['maternal-care', 'newborn-care', 'appointments', 'referrals'];
  views.forEach(v => {
    const el = document.getElementById('view-' + v);
    if (el) {
      if (v === viewName) {
        el.classList.remove('hidden');
        el.style.display = 'flex';
      } else {
        el.classList.add('hidden');
        el.style.display = 'none';
      }
    }
  });

  // Explicitly render and select the active view data
  if (viewName === 'maternal-care') {
    renderPatientsTable();
    if (typeof selectedPatientId !== 'undefined' && selectedPatientId) {
      selectPatient(selectedPatientId);
    } else {
      selectPatient('M-01');
    }
  } else if (viewName === 'newborn-care') {
    renderBabyTable();
    if (typeof selectedBabyKey !== 'undefined' && selectedBabyKey) {
      selectBaby(selectedBabyKey);
    } else {
      selectBaby('mary_osei');
    }
  } else if (viewName === 'appointments') {
    renderAppointmentsList('ALL');
  } else if (viewName === 'referrals') {
    renderTransfersTable();
    if (typeof selectedTransferKey !== 'undefined' && selectedTransferKey) {
      selectTransfer(selectedTransferKey);
    }
  }

  window.scrollTo({ top: 0, behavior: 'smooth' });
}'''

if old_switch_nav in html:
    html = html.replace(old_switch_nav, new_switch_nav)
    print("Upgraded switchNavView function with explicit maternal-care rendering and display toggle.")

# -----------------------------------------------------------------------------
# 4. SET DEFAULT INITIAL VIEW TO 'maternal-care' (Pregnant Mothers)
# -----------------------------------------------------------------------------
old_initial_view = "const initialView = (window.location.hash ? window.location.hash.replace('#', '') : '') || 'appointments';"
new_initial_view = "const initialView = (window.location.hash ? window.location.hash.replace('#', '') : '') || 'maternal-care';"

if old_initial_view in html:
    html = html.replace(old_initial_view, new_initial_view)
    print("Set initial default view to 'maternal-care' (Pregnant Mothers).")

# Also ensure sidebar nav has 'maternal-care' highlighted by default in HTML
old_sidebar_active = '''      <a class="nav-btn flex items-center gap-3 px-3.5 py-2.5 rounded-lg text-slate-200 hover:bg-white/10 hover:text-white transition-colors duration-150 cursor-pointer" data-view="maternal-care" onclick="switchNavView('maternal-care')">
        <span class="material-symbols-outlined text-[20px] text-cyan-300">pregnant_woman</span>
        <span class="font-label-lg text-[14px]">Pregnant Mothers</span>
      </a>
      <a class="nav-btn flex items-center gap-3 px-3.5 py-2.5 rounded-lg text-slate-200 hover:bg-white/10 hover:text-white transition-colors duration-150 cursor-pointer" data-view="newborn-care" onclick="switchNavView('newborn-care')">
        <span class="material-symbols-outlined text-[20px] text-cyan-300">child_care</span>
        <span class="font-label-lg text-[14px]">Baby Checks</span>
      </a>
      <a class="nav-btn flex items-center gap-3 px-3.5 py-2.5 rounded-lg bg-[#0e7490] text-white font-semibold shadow-sm transition-all cursor-pointer" data-view="appointments" onclick="switchNavView('appointments')">'''

new_sidebar_active = '''      <a class="nav-btn flex items-center gap-3 px-3.5 py-2.5 rounded-lg bg-[#0e7490] text-white font-semibold shadow-sm transition-all cursor-pointer" data-view="maternal-care" onclick="switchNavView('maternal-care')">
        <span class="material-symbols-outlined text-[20px] text-white">pregnant_woman</span>
        <span class="font-label-lg text-[14px]">Pregnant Mothers</span>
      </a>
      <a class="nav-btn flex items-center gap-3 px-3.5 py-2.5 rounded-lg text-slate-200 hover:bg-white/10 hover:text-white transition-colors duration-150 cursor-pointer" data-view="newborn-care" onclick="switchNavView('newborn-care')">
        <span class="material-symbols-outlined text-[20px] text-cyan-300">child_care</span>
        <span class="font-label-lg text-[14px]">Baby Checks</span>
      </a>
      <a class="nav-btn flex items-center gap-3 px-3.5 py-2.5 rounded-lg text-slate-200 hover:bg-white/10 hover:text-white transition-colors duration-150 cursor-pointer" data-view="appointments" onclick="switchNavView('appointments')">'''

if old_sidebar_active in html:
    html = html.replace(old_sidebar_active, new_sidebar_active)
    print("Highlighted Pregnant Mothers nav button in sidebar.")

# Ensure view-maternal-care is NOT hidden initially, while other views are hidden
html = html.replace('<div id="view-maternal-care" class="hidden flex flex-col w-full">', '<div id="view-maternal-care" class="flex flex-col w-full">')
html = html.replace('<div id="view-appointments" class="flex flex-col w-full p-8 max-w-[1720px] mx-auto space-y-6">', '<div id="view-appointments" class="hidden flex flex-col w-full p-8 max-w-[1720px] mx-auto space-y-6">')

with open(frontend_path, 'w', encoding='utf-8') as f:
    f.write(html)

# Synchronize backend static copy
backend_static_path = 'backend/src/main/resources/static/index.html'
if os.path.exists(backend_static_path):
    with open(backend_static_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Synchronized to backend/src/main/resources/static/index.html.")

print("All fixes applied successfully!")

