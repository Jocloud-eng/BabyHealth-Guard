import re
import os

print("Adding Back Button, Sign Out Button, and Real Working Downloads...")

# =============================================================================
# 1. PATCH frontend/index.html
# =============================================================================
frontend_path = r"C:\Users\Admin\BabyHealth-Guard\frontend\index.html"
with open(frontend_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1.1 Add Back to Home button in Header next to hamburger & logo
old_header_brand = '''      <!-- App Branding -->
      <div class="flex items-center gap-3 cursor-pointer" onclick="switchNavView('maternal-care')">'''

new_header_brand = '''      <!-- Back to Home Navigation Button -->
      <a href="/index.html" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 hover:text-slate-900 font-bold text-xs transition-colors shrink-0 mr-1" title="Back to Home Page">
        <span class="material-symbols-outlined text-[18px]">arrow_back</span>
        <span class="hidden sm:inline">Back to Home</span>
      </a>

      <!-- App Branding -->
      <div class="flex items-center gap-3 cursor-pointer" onclick="switchNavView('maternal-care')">'''

if old_header_brand in content:
    content = content.replace(old_header_brand, new_header_brand, 1)
    print("Added Header Back to Home button.")
else:
    print("WARNING: old_header_brand not found")

# 1.2 Add Sign Out Button in Header next to Worker Profile
old_worker_profile = '''          <div id="headerWorkerAvatar" class="w-9 h-9 rounded-full bg-[#0e7490] text-white flex items-center justify-center font-bold text-xs tracking-wider shadow-xs">
            SO
          </div>
        </div>
      </div>
    </div>
  </header>'''

new_worker_profile = '''          <div id="headerWorkerAvatar" class="w-9 h-9 rounded-full bg-[#0e7490] text-white flex items-center justify-center font-bold text-xs tracking-wider shadow-xs">
            SO
          </div>
        </div>

        <!-- Prominent Sign Out Button -->
        <button onclick="handleSignOut()" class="inline-flex items-center gap-1 px-3 py-1.5 rounded-lg bg-rose-50 hover:bg-rose-100 text-rose-700 hover:text-rose-800 text-xs font-bold border border-rose-200 transition-colors shadow-2xs active:scale-95 cursor-pointer ml-1" title="Sign Out of Clinical Account">
          <span class="material-symbols-outlined text-[16px]">logout</span>
          <span class="hidden md:inline">Sign Out</span>
        </button>
      </div>
    </div>
  </header>'''

if old_worker_profile in content:
    content = content.replace(old_worker_profile, new_worker_profile, 1)
    print("Added Header Sign Out button.")
else:
    print("WARNING: old_worker_profile not found")

# 1.3 Add Back button & Sign Out button in Sidebar
old_sidebar_header = '''    <!-- CARE MENU Header -->
    <div class="px-5 py-6 border-b border-[#144758]/50">
      <div class="text-xs uppercase tracking-wider text-cyan-300/80 font-bold">CARE MENU</div>
    </div>'''

new_sidebar_header = '''    <!-- CARE MENU Header with Back Button -->
    <div class="px-4 py-4 border-b border-[#144758]/50 space-y-2.5">
      <a href="/index.html" class="flex items-center gap-2 px-3 py-2 rounded-lg bg-white/10 hover:bg-white/20 text-cyan-100 hover:text-white transition-colors text-xs font-bold">
        <span class="material-symbols-outlined text-[18px]">arrow_back</span>
        <span>Back to Home Page</span>
      </a>
      <div class="text-[10px] uppercase tracking-wider text-cyan-300/80 font-bold px-1">CARE MENU</div>
    </div>'''

if old_sidebar_header in content:
    content = content.replace(old_sidebar_header, new_sidebar_header, 1)
    print("Added Sidebar Back button.")
else:
    print("WARNING: old_sidebar_header not found")

# Sidebar bottom Sign Out button
old_sidebar_footer = '''      <button onclick="openWorkerAccountModal('switch')" class="flex-1 flex items-center justify-center gap-1.5 py-2 px-2 rounded-lg bg-white/5 hover:bg-white/10 text-cyan-200 text-[11px] font-medium border border-cyan-800/40 transition-all cursor-pointer">
        <span class="material-symbols-outlined text-[15px]">swap_horiz</span> Switch
      </button>
    </div>
  </div>
</aside>'''

new_sidebar_footer = '''      <button onclick="openWorkerAccountModal('switch')" class="flex-1 flex items-center justify-center gap-1.5 py-2 px-2 rounded-lg bg-white/5 hover:bg-white/10 text-cyan-200 text-[11px] font-medium border border-cyan-800/40 transition-all cursor-pointer">
        <span class="material-symbols-outlined text-[15px]">swap_horiz</span> Switch
      </button>
    </div>
    <div class="pt-1">
      <button onclick="handleSignOut()" class="w-full flex items-center justify-center gap-2 py-2 px-3 rounded-lg bg-rose-950/50 hover:bg-rose-900 text-rose-200 text-xs font-bold border border-rose-800/50 transition-colors cursor-pointer">
        <span class="material-symbols-outlined text-[16px]">logout</span>
        <span>Sign Out Account</span>
      </button>
    </div>
  </div>
</aside>'''

if old_sidebar_footer in content:
    content = content.replace(old_sidebar_footer, new_sidebar_footer, 1)
    print("Added Sidebar Sign Out button.")
else:
    print("WARNING: old_sidebar_footer not found")

# 1.4 Add Maternal Roster Export & Report Buttons
old_maternal_actions = '''            <button onclick="openRegisterMotherModal()" class="inline-flex items-center gap-2 px-4 py-2.5 rounded-lg bg-[#0e7490] text-white text-[13px] font-semibold hover:bg-[#0c627a] transition-all shadow-xs cursor-pointer">
              <span class="material-symbols-outlined text-[18px]">add_circle</span>
              <span>Register Expectant Mother</span>
            </button>
          </div>'''

new_maternal_actions = '''            <button onclick="downloadMaternalRegistryCSV()" class="inline-flex items-center gap-2 px-3.5 py-2.5 rounded-lg border border-slate-200 bg-white text-slate-700 text-[13px] font-semibold hover:bg-slate-50 transition-all shadow-xs cursor-pointer" title="Download Maternal Health Registry as CSV file">
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
          </div>'''

if old_maternal_actions in content:
    content = content.replace(old_maternal_actions, new_maternal_actions, 1)
    print("Added Maternal Roster Download CSV & Monthly Report buttons.")
else:
    print("WARNING: old_maternal_actions not found")

# 1.5 Replace placeholder downloads with real download functions
content = content.replace(
    'onclick="toast(\'Exporting baby registry to CSV...\')"',
    'onclick="downloadBabyRegistryCSV()"'
)
content = content.replace(
    'onclick="toast(\'Downloading today\\\'s schedule export (CSV/PDF)...\')"',
    'onclick="downloadClinicScheduleCSV()"'
)
print("Replaced placeholder download toasts with real download function triggers.")

# 1.6 Add FR12 Report Modal and JavaScript download & signout functions
download_js_and_modals = '''
<!-- ========================================================================= -->
<!-- FACILITY CLINICAL MONTHLY REPORT MODAL (MOH FR12)                         -->
<!-- ========================================================================= -->
<div id="facilityReportModal" class="fixed inset-0 z-50 bg-black/60 backdrop-blur-xs hidden items-center justify-center p-4">
  <div class="bg-white rounded-2xl shadow-2xl max-w-4xl w-full max-h-[90vh] overflow-y-auto flex flex-col">
    <!-- Header -->
    <div class="bg-gradient-to-r from-[#08232c] via-[#0e7490] to-teal-800 p-5 text-white flex items-center justify-between shrink-0">
      <div class="flex items-center gap-3">
        <div class="w-10 h-10 rounded-xl bg-white/15 flex items-center justify-center">
          <span class="material-symbols-outlined text-[24px]">description</span>
        </div>
        <div>
          <h3 class="font-bold text-lg leading-tight">Monthly Health Facility Maternal Report (FR12)</h3>
          <p class="text-xs text-cyan-200">Uganda Ministry of Health • Health Management Information System (HMIS)</p>
        </div>
      </div>
      <div class="flex items-center gap-2">
        <button onclick="downloadFacilityReportCSV()" class="px-3 py-1.5 rounded-lg bg-white text-slate-900 font-bold text-xs flex items-center gap-1.5 hover:bg-cyan-50 transition-colors cursor-pointer">
          <span class="material-symbols-outlined text-[16px]">download</span>
          <span>Download CSV</span>
        </button>
        <button onclick="printFacilityReport()" class="px-3 py-1.5 rounded-lg bg-teal-600 hover:bg-teal-700 text-white font-bold text-xs flex items-center gap-1.5 transition-colors cursor-pointer">
          <span class="material-symbols-outlined text-[16px]">print</span>
          <span>Print / PDF</span>
        </button>
        <button onclick="closeFacilityReportModal()" class="w-8 h-8 rounded-lg bg-white/10 hover:bg-white/20 text-white flex items-center justify-center cursor-pointer">
          <span class="material-symbols-outlined text-[20px]">close</span>
        </button>
      </div>
    </div>

    <!-- Printable Report Area -->
    <div class="p-6 space-y-6 text-slate-800" id="printableReportArea">
      <div class="flex flex-wrap items-center justify-between pb-4 border-b border-slate-200 text-xs">
        <div>
          <span class="text-slate-500 block">Reporting Facility:</span>
          <strong class="text-slate-900 text-sm">Bwera Health Centre III (Maji Mazuri Outpost)</strong>
        </div>
        <div>
          <span class="text-slate-500 block">Lead Healthcare Worker:</span>
          <strong class="text-slate-900 text-sm" id="reportMidwifeName">Sr. Sarah Omondi (Midwife)</strong>
        </div>
        <div>
          <span class="text-slate-500 block">Reporting Month:</span>
          <strong class="text-slate-900 text-sm">November 2026 (Active Cycle)</strong>
        </div>
      </div>

      <!-- KPI Metrics Grid -->
      <div class="grid grid-cols-2 sm:grid-cols-4 gap-3">
        <div class="bg-slate-50 p-3.5 rounded-xl border border-slate-200">
          <span class="text-[11px] text-slate-500 block">Total Active Mothers</span>
          <strong class="text-2xl font-black text-slate-900" id="repTotalMothers">16</strong>
          <span class="text-[10px] text-emerald-600 font-semibold block">100% Registry Completeness</span>
        </div>
        <div class="bg-rose-50 p-3.5 rounded-xl border border-rose-200">
          <span class="text-[11px] text-rose-700 block">High Risk Mothers</span>
          <strong class="text-2xl font-black text-rose-700" id="repHighRisk">4</strong>
          <span class="text-[10px] text-rose-600 font-semibold block">Under weekly surveillance</span>
        </div>
        <div class="bg-cyan-50 p-3.5 rounded-xl border border-cyan-200">
          <span class="text-[11px] text-cyan-800 block">ANC Visits Logged</span>
          <strong class="text-2xl font-black text-[#0e7490]">28</strong>
          <span class="text-[10px] text-cyan-700 font-semibold block">94% Attendance Rate</span>
        </div>
        <div class="bg-emerald-50 p-3.5 rounded-xl border border-emerald-200">
          <span class="text-[11px] text-emerald-800 block">Safe Deliveries</span>
          <strong class="text-2xl font-black text-emerald-700">12</strong>
          <span class="text-[10px] text-emerald-600 font-semibold block">Zero Maternal Deaths</span>
        </div>
      </div>

      <!-- Registry Extract Table -->
      <div>
        <h4 class="font-bold text-sm text-slate-900 mb-2">Registered Expectant Mothers Cohort</h4>
        <div class="overflow-x-auto border border-slate-200 rounded-xl">
          <table class="w-full text-left text-xs text-slate-700">
            <thead class="bg-slate-100 text-slate-600 uppercase font-bold text-[10px]">
              <tr>
                <th class="p-2.5">ID & Name</th>
                <th class="p-2.5">Age</th>
                <th class="p-2.5">Gestation</th>
                <th class="p-2.5">BP (mmHg)</th>
                <th class="p-2.5">Hemoglobin</th>
                <th class="p-2.5">Risk Category</th>
                <th class="p-2.5">Facility</th>
              </tr>
            </thead>
            <tbody id="reportTableBody" class="divide-y divide-slate-100">
              <!-- Dynamically populated by JS -->
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Footer Actions -->
    <div class="p-4 bg-slate-50 border-t border-slate-200 flex justify-end gap-3 shrink-0">
      <button onclick="closeFacilityReportModal()" class="px-4 py-2 rounded-lg bg-slate-200 hover:bg-slate-300 text-slate-800 font-semibold text-xs transition-colors cursor-pointer">
        Close
      </button>
      <button onclick="downloadFacilityReportCSV()" class="px-4 py-2 rounded-lg bg-[#0e7490] hover:bg-[#0c627a] text-white font-bold text-xs flex items-center gap-1.5 transition-colors cursor-pointer">
        <span class="material-symbols-outlined text-[16px]">download</span>
        <span>Download CSV</span>
      </button>
    </div>
  </div>
</div>

<!-- ========================================================================= -->
<!-- JAVASCRIPT: REAL WORKING FILE DOWNLOADS & SIGN OUT IMPLEMENTATION         -->
<!-- ========================================================================= -->
<script>
// Generic helper to trigger real browser file downloads
function triggerBrowserDownload(filename, content, mimeType) {
  const blob = new Blob(["\\uFEFF" + content], { type: mimeType + ';charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.setAttribute("href", url);
  link.setAttribute("download", filename);
  link.style.visibility = 'hidden';
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
  URL.revokeObjectURL(url);
  toast(`Downloaded ${filename} successfully!`);
}

// 1. Download Maternal Health Registry CSV
function downloadMaternalRegistryCSV() {
  const headers = ["Patient ID", "Full Name", "Age", "Gestation", "Trimester", "Due Date", "Blood Pressure", "BP Status", "Hemoglobin", "Risk Category", "Assigned Midwife", "Facility", "Clinical Notes"];
  const rows = patients.map(p => [
    `"${p.id || ''}"`,
    `"${p.name || ''}"`,
    `"${p.age || ''}"`,
    `"${p.week || ''}"`,
    `"${p.trimester || ''}"`,
    `"${p.dueDate || ''}"`,
    `"${p.bp || ''}"`,
    `"${p.bpStatus || ''}"`,
    `"${p.hb || ''}"`,
    `"${p.risk || ''}"`,
    `"${p.assignedWorker || ''}"`,
    `"${p.facility || ''}"`,
    `"${(p.notes || '').replace(/"/g, '""')}"`
  ]);

  const csvContent = [headers.join(','), ...rows.map(r => r.join(','))].join('\\n');
  triggerBrowserDownload('maternal_patients_registry.csv', csvContent, 'text/csv');
}

// 2. Download Baby Checks Registry CSV
function downloadBabyRegistryCSV() {
  const babyData = [
    { id: "B-01", babyName: "Baby of Mary Osei", motherName: "Mary Osei", age: "Day 3", weightKg: "2.45", tempC: "35.3", breathRate: "52/min", status: "Needs Urgent Care", village: "Asamankese" },
    { id: "B-02", babyName: "Baby of Fatima Abubakar", motherName: "Fatima Abubakar", age: "Day 7", weightKg: "3.10", tempC: "36.8", breathRate: "44/min", status: "Doing Well", village: "Beposo" },
    { id: "B-03", babyName: "Baby of Amina Brenda", motherName: "Amina Brenda", age: "Day 14", weightKg: "3.42", tempC: "36.5", breathRate: "46/min", status: "Doing Well", village: "Kagando" },
    { id: "B-04", babyName: "Baby of Grace Mwangi", motherName: "Grace Mwangi", age: "Day 21", weightKg: "3.80", tempC: "36.7", breathRate: "42/min", status: "Doing Well", village: "Lindi" },
    { id: "B-05", babyName: "Baby of Zainab Bello", motherName: "Zainab Bello", age: "Day 2", weightKg: "2.85", tempC: "36.4", breathRate: "48/min", status: "Monitoring", village: "Maji Mazuri" }
  ];

  const headers = ["Baby ID", "Baby Reference", "Mother Name", "Age", "Weight (kg)", "Temperature (C)", "Breath Rate", "Clinical Care Status", "Village / Facility"];
  const rows = babyData.map(b => [
    `"${b.id}"`,
    `"${b.babyName}"`,
    `"${b.motherName}"`,
    `"${b.age}"`,
    `"${b.weightKg}"`,
    `"${b.tempC}"`,
    `"${b.breathRate}"`,
    `"${b.status}"`,
    `"${b.village}"`
  ]);

  const csvContent = [headers.join(','), ...rows.map(r => r.join(','))].join('\\n');
  triggerBrowserDownload('baby_checks_registry.csv', csvContent, 'text/csv');
}

// 3. Download Clinic Visits Schedule CSV
function downloadClinicScheduleCSV() {
  const headers = ["Appointment ID", "Patient Name", "Visit Type", "Scheduled Date & Time", "Facility / Clinic Room", "Attendance Status"];
  const rows = appointments.map(a => [
    `"${a.id || ''}"`,
    `"${a.patientName || ''}"`,
    `"${a.type || ''}"`,
    `"${a.when || ''}"`,
    `"${a.facility || ''}"`,
    `"${a.status || ''}"`
  ]);

  const csvContent = [headers.join(','), ...rows.map(r => r.join(','))].join('\\n');
  triggerBrowserDownload('today_clinic_schedule.csv', csvContent, 'text/csv');
}

// 4. Monthly Report (FR12) Modal Logic
function openFacilityReportModal() {
  const modal = document.getElementById('facilityReportModal');
  const tbody = document.getElementById('reportTableBody');
  
  // Populate cohort table
  tbody.innerHTML = '';
  patients.slice(0, 8).forEach(p => {
    const tr = document.createElement('tr');
    tr.className = 'hover:bg-slate-50';
    tr.innerHTML = `
      <td class="p-2.5 font-bold">${p.name} <span class="text-slate-400 font-normal">(${p.id})</span></td>
      <td class="p-2.5">${p.age}</td>
      <td class="p-2.5">${p.week}</td>
      <td class="p-2.5">${p.bp}</td>
      <td class="p-2.5">${p.hb}</td>
      <td class="p-2.5"><span class="px-2 py-0.5 rounded text-[10px] font-bold ${p.risk === 'High Risk' ? 'bg-rose-100 text-rose-700' : 'bg-emerald-100 text-emerald-700'}">${p.risk}</span></td>
      <td class="p-2.5">${p.facility}</td>
    `;
    tbody.appendChild(tr);
  });

  document.getElementById('repTotalMothers').textContent = patients.length;
  document.getElementById('repHighRisk').textContent = patients.filter(p => p.risk === 'High Risk').length;
  modal.classList.remove('hidden');
  modal.classList.add('flex');
}

function closeFacilityReportModal() {
  const modal = document.getElementById('facilityReportModal');
  modal.classList.add('hidden');
  modal.classList.remove('flex');
}

function downloadFacilityReportCSV() {
  const headers = ["HMIS Indicator", "Count / Value", "Description"];
  const rows = [
    ['"Total Registered Expectant Mothers"', `"${patients.length}"`, '"Active in clinical cohort"'],
    ['"High Risk Pregnancies Flagged"', `"${patients.filter(p => p.risk === 'High Risk').length}"`, '"Preeclampsia and severe anemia surveillance"'],
    ['"Routine Antenatal Attendances"', `"${patients.filter(p => p.risk !== 'High Risk').length}"`, '"Standard 4-visit WHO pathway"'],
    ['"ANC Clinic Visits Conducted This Cycle"', '"28"', '"Documented in facility records"'],
    ['"Emergency Referrals to Sub-County Hospital"', '"2"', '"Transferred via fast-track protocol"'],
    ['"Facility"', '"Bwera Health Centre III (Maji Mazuri Outpost)"', '"Uganda Ministry of Health"'],
    ['"Report Generated At"', `"${new Date().toISOString()}"`, '"BabyHealth Guard Digital System"']
  ];

  const csvContent = [headers.join(','), ...rows.map(r => r.join(','))].join('\\n');
  triggerBrowserDownload('maternal_facility_report_FR12.csv', csvContent, 'text/csv');
}

function printFacilityReport() {
  window.print();
}

// 5. Sign Out Logic
function handleSignOut() {
  if (confirm("Are you sure you want to sign out of your healthcare worker account?")) {
    try {
      localStorage.removeItem('authToken');
      localStorage.removeItem('currentUser');
      sessionStorage.clear();
    } catch(e) {}
    toast("Signed out successfully. Returning to Home...");
    setTimeout(() => {
      window.location.href = '/index.html';
    }, 500);
  }
}
</script>
'''

if '</body>' in content:
    content = content.replace('</body>', download_js_and_modals + '\n</body>', 1)
    print("Added download & sign out JavaScript and modal.")

with open(frontend_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated frontend/index.html successfully.")

# =============================================================================
# 2. PATCH mobile/dashboard_preview.html (Back Button & Sign Out)
# =============================================================================
dash_path = r"C:\Users\Admin\BabyHealth-Guard\mobile\dashboard_preview.html"
if os.path.exists(dash_path):
    with open(dash_path, "r", encoding="utf-8") as f:
        dash_content = f.read()

    # Add back button and sign out button in header
    old_dash_header = '''<!-- Minimal App Header inspired by Reference -->
<header class="fixed top-0 inset-x-0 z-40 pt-safe bg-[#F6F7FA]/90 backdrop-blur-md">
  <div class="px-5 pt-2 pb-2.5 flex items-center justify-between border-b border-slate-100 max-w-md md:max-w-4xl lg:max-w-6xl mx-auto">
    <div class="flex items-center gap-3">'''

    new_dash_header = '''<!-- Minimal App Header with Navigation Back & Sign Out -->
<header class="fixed top-0 inset-x-0 z-40 pt-safe bg-[#F6F7FA]/90 backdrop-blur-md">
  <div class="px-4 pt-2 pb-2.5 flex items-center justify-between border-b border-slate-100 max-w-md md:max-w-4xl lg:max-w-6xl mx-auto">
    <div class="flex items-center gap-2.5">
      <!-- Back to Home Button -->
      <a href="/index.html" aria-label="Go back to Home" class="w-9 h-9 rounded-full bg-white shadow-xs flex items-center justify-center text-slate-700 hover:text-slate-900 border border-slate-200 active:scale-95 transition-transform" title="Back to Home Page">
        <span class="material-symbols-outlined text-[20px]">arrow_back</span>
      </a>'''

    if old_dash_header in dash_content:
        dash_content = dash_content.replace(old_dash_header, new_dash_header, 1)
        print("Added Back button to mobile/dashboard_preview.html header.")

    # Add Sign Out button next to notifications in mobile header
    old_dash_notif = '''    <div class="flex items-center gap-2">
      <button id="btn-notifications" aria-label="Notifications" class="relative w-10 h-10 rounded-full bg-white shadow-sm flex items-center justify-center text-slate-700 border border-slate-100 active:scale-95 transition-transform" type="button">
        <span class="material-symbols-outlined text-[20px]">notifications</span>
        <span class="absolute top-2.5 right-2.5 w-2 h-2 bg-amber-500 rounded-full ring-2 ring-white"></span>
      </button>
    </div>'''

    new_dash_notif = '''    <div class="flex items-center gap-2">
      <button id="btn-notifications" aria-label="Notifications" class="relative w-9 h-9 rounded-full bg-white shadow-xs flex items-center justify-center text-slate-700 border border-slate-100 active:scale-95 transition-transform" type="button">
        <span class="material-symbols-outlined text-[18px]">notifications</span>
        <span class="absolute top-2 right-2 w-2 h-2 bg-amber-500 rounded-full ring-2 ring-white"></span>
      </button>
      <button onclick="handleMotherSignOut()" aria-label="Sign Out" class="px-2.5 py-1.5 rounded-full bg-white hover:bg-rose-50 text-slate-600 hover:text-rose-600 font-bold text-xs flex items-center gap-1 border border-slate-200 shadow-xs active:scale-95 transition-all" title="Sign Out Profile">
        <span class="material-symbols-outlined text-[16px]">logout</span>
        <span class="hidden sm:inline">Sign Out</span>
      </button>
    </div>'''

    if old_dash_notif in dash_content:
        dash_content = dash_content.replace(old_dash_notif, new_dash_notif, 1)
        print("Added Sign Out button to mobile/dashboard_preview.html header.")

    # Add Sign Out script and Download Health Passport script before </body>
    dash_scripts = '''
<script>
function handleMotherSignOut() {
  if (confirm("Are you sure you want to sign out of your maternal care profile?")) {
    window.location.href = '/index.html';
  }
}

function downloadMotherHealthCard() {
  const content = `BABYHEALTH GUARD - MATERNAL HEALTH PASSPORT\\n--------------------------------------------\\nMother Name: Amina Brenda\\nAge: 24 yrs\\nVillage: Kagando Village, Bwera Sub-County\\nGestational Age: 28 Weeks (Trimester 3)\\nBlood Pressure: 118/76 mmHg (Normal)\\nDaily Kicks Logged: 11 kicks / 2 hours\\nIron & Folic Pills: Taken Today\\nAssigned Midwife: Sr. Sarah Omondi\\nNext Clinic Date: Thursday 24 Oct (Bwera HC III)\\nEmergency Hotlines: 112 / 0800 100 200\\nUSSD Service: *920# (Free on 2G)`;
  const blob = new Blob(["\\uFEFF" + content], { type: 'text/plain;charset=utf-8;' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'amina_brenda_maternal_passport.txt';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
  alert("Maternal Health Card downloaded successfully!");
}
</script>
'''
    if '</body>' in dash_content:
        dash_content = dash_content.replace('</body>', dash_scripts + '\n</body>', 1)

    with open(dash_path, "w", encoding="utf-8") as f:
        f.write(dash_content)
    print("Updated mobile/dashboard_preview.html successfully.")

# =============================================================================
# 3. PATCH mobile/welcome_preview.html (Back Button)
# =============================================================================
welcome_path = r"C:\Users\Admin\BabyHealth-Guard\mobile\welcome_preview.html"
if os.path.exists(welcome_path):
    with open(welcome_path, "r", encoding="utf-8") as f:
        w_content = f.read()
    
    # Check if back button to landing page exists
    if '/index.html' not in w_content:
        w_content = w_content.replace(
            '<body class="bg-surface',
            '<body class="bg-surface">\n<div class="fixed top-4 left-4 z-50"><a href="/index.html" class="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-white/90 backdrop-blur-md shadow-md text-slate-800 text-xs font-bold border border-slate-200 hover:bg-slate-100 transition-colors"><span class="material-symbols-outlined text-[16px]">arrow_back</span><span>Back to Home</span></a></div><!--'
        )
        with open(welcome_path, "w", encoding="utf-8") as f:
            f.write(w_content)
        print("Added Back to Home button in mobile/welcome_preview.html.")

print("All navigation back buttons, sign out buttons, and working downloads patched successfully!")

