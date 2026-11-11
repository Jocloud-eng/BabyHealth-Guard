import json
import os

print("Applying single AI Assistant button across all dashboards...")

# Common AI Drawer HTML
AI_DRAWER_HTML = '''
<!-- ========================================================================= -->
<!-- MAAMACARE AI ASSISTANT SIDE DRAWER (10 UGANDAN LOCAL LANGUAGES)           -->
<!-- ========================================================================= -->
<div id="aiSideDrawerBackdrop" onclick="closeAiSideDrawer()" class="fixed inset-0 bg-slate-900/50 backdrop-blur-xs z-50 hidden transition-opacity duration-300"></div>

<aside id="aiSideDrawer" class="fixed top-0 right-0 h-full w-full sm:w-[420px] bg-white shadow-2xl z-50 flex flex-col transform translate-x-full transition-transform duration-300 ease-in-out border-l border-slate-200">
  
  <!-- Drawer Header -->
  <div class="bg-gradient-to-r from-[#08232c] to-[#0e7490] p-4 text-white flex items-center justify-between shrink-0 shadow-sm">
    <div class="flex items-center gap-3">
      <div class="w-10 h-10 rounded-xl bg-white/15 flex items-center justify-center text-xl">🤱</div>
      <div>
        <h3 class="font-extrabold text-sm sm:text-base leading-tight">MaamaCare AI Assistant</h3>
        <p class="text-[11px] text-cyan-200" id="drawerDialectBadge">Luganda Active • Audio Spoken</p>
      </div>
    </div>
    <button onclick="closeAiSideDrawer()" class="w-8 h-8 rounded-lg bg-white/10 hover:bg-white/20 flex items-center justify-center text-white transition-colors cursor-pointer" title="Close AI Assistant">
      <span class="material-symbols-outlined text-[20px]">close</span>
    </button>
  </div>

  <!-- Language Selector Dropdown in Drawer -->
  <div class="p-3 bg-slate-50 border-b border-slate-200 flex items-center justify-between text-xs shrink-0">
    <span class="font-bold text-slate-700">Choose Language:</span>
    <select onchange="switchLanguage(this.value)" id="drawerLangSelect" class="bg-white text-slate-900 font-bold text-xs rounded-xl px-2.5 py-1.5 border border-slate-300 focus:outline-hidden focus:ring-2 focus:ring-[#0e7490] cursor-pointer">
      <option value="luganda">🇺🇬 Luganda (Central)</option>
      <option value="runyankore">🇺🇬 Runyankore (Western)</option>
      <option value="rukiga">🇺🇬 Rukiga (Kigezi)</option>
      <option value="lusoga">🇺🇬 Lusoga (Busoga)</option>
      <option value="acholi">🇺🇬 Acholi (Northern / Luo)</option>
      <option value="lango">🇺🇬 Lango (Northern)</option>
      <option value="ateso">🇺🇬 Ateso (Eastern / Teso)</option>
      <option value="lugbara">🇺🇬 Lugbara (West Nile)</option>
      <option value="runyoro">🇺🇬 Runyoro-Rutooro (Western)</option>
      <option value="lumasaba">🇺🇬 Lumasaba (Bugisu)</option>
      <option value="english">🌐 English (Official)</option>
      <option value="swahili">🇹🇿 Kiswahili (East Africa)</option>
    </select>
  </div>

  <!-- Chat Messages Window -->
  <div id="drawerChatMessages" class="flex-1 p-4 overflow-y-auto space-y-3.5 bg-slate-50/70 text-xs">
    <!-- Messages populated by JS -->
  </div>

  <!-- Quick Question Chips -->
  <div id="drawerQuickChips" class="px-3.5 py-2.5 bg-white border-t border-slate-100 flex flex-wrap gap-1.5 shrink-0">
    <!-- Chips populated by JS -->
  </div>

  <!-- Input Bar -->
  <div class="p-3 bg-white border-t border-slate-200 shrink-0">
    <form onsubmit="handleDrawerChatSubmit(event)" class="flex items-center gap-2">
      <button type="button" onclick="startVoiceInput()" id="drawerMicBtn" title="Speak via microphone" class="w-9 h-9 rounded-xl bg-slate-100 hover:bg-cyan-50 text-slate-700 hover:text-[#0e7490] border border-slate-200 flex items-center justify-center shrink-0 transition-colors cursor-pointer">
        <span class="material-symbols-outlined text-[18px]">mic</span>
      </button>
      <input type="text" id="drawerChatInput" placeholder="Buuza ekibuuzo..." class="flex-1 bg-slate-50 text-xs px-3.5 py-2 rounded-xl border border-slate-200 focus:outline-hidden focus:ring-1 focus:ring-[#0e7490]">
      <button type="submit" class="px-3.5 py-2 rounded-xl bg-[#0e7490] hover:bg-[#08232c] text-white font-bold text-xs flex items-center justify-center shrink-0 transition-colors cursor-pointer">
        <span class="material-symbols-outlined text-[16px]">send</span>
      </button>
    </form>
    <div class="mt-2 flex items-center justify-between text-[10px] text-slate-400 px-1">
      <span>🔊 Tap "Listen" to hear spoken pronunciation</span>
      <a href="https://wa.me/256778501066" target="_blank" class="text-emerald-600 font-bold hover:underline">WhatsApp Help</a>
    </div>
  </div>

</aside>
'''

# Common JS logic for AI Drawer
AI_DRAWER_JS = '''
<script>
// MaamaCare AI Multilingual Knowledge Engine (10 Ugandan Languages)
const MAAMA_LANGUAGES = {
  "luganda": {
    "name": "Luganda (Central)",
    "greeting": "Oli otya Maama! Nze MaamaCare AI, omuyambi wo ku by'obulamu bwo n'obw'omwana wo. Ndi wano okukuyamba ku bintu byonna ebikwata ku lubuto, okugenda mu ddwaliro, n'obulamu bw'omwana.",
    "placeholder": "Buuza ekibuuzo ku lubuto oba omwana...",
    "listenText": "Wuliriza eddoboozi",
    "quickChips": ["🚨 Obubonero obw'obulabe", "👶 Omwana akuba atya?", "🥗 Eby'okulya n'eddagala lya ayoni", "🏥 Eddwaliro n'okubala emyezi"],
    "intents": {
      "danger": { "keywords": ["obulabe", "omusaayi", "omutwe", "amaaso", "omusujja", "kuzimba", "okulumwa", "bleeding", "headache"], "response": "⚠️ OBULABE OBW'AMANGU! Singa ofuna okuvaamu omusaayi, omutwe ogutawona ng'olina ebire mu maaso, omusujja omungi, oba okuzimba ennyo, genda mu ddwaliro amangu ddala! Kuba essimu ku 112 oba 0800 100 200 ku bwereere, oba omusawo wo ku +256 778 501 066." },
      "kicks": { "keywords": ["kuba", "okukuba", "omwana", "kicks", "move"], "response": "👶 OKUKUBA KW'OMWANA: Omwana asaanidde akube emirundi egitakka wansi wa 10 mu ssaawa bbiri (2) ng'oli mu kuwummula ku lubiriizi olwa kkono. Bw'aleka okukuba, yanguwa ogende mu ddwaliro bakebe omutima gwe." },
      "nutrition": { "keywords": ["lya", "okulya", "enva", "ayoni", "doodo", "food"], "response": "🥗 EBY'OKULYA: Lya emmere ezimba omusaayi: doodo, nakati, bbugga, ebijanjaalo, amagi, n'amata. Mira buli lunaku ebinini bya Ayoni ne Folic Acid eby'omusaayi." },
      "visits": { "keywords": ["ddwaliro", "anc", "omusawo", "appointment"], "response": "🏥 OKUGENDA MU DDWALIRO (ANC): Buli maama agende mu ddwaliro emirundi egitakka wansi wa 4. Koona *920# ku ssimu yo okumanya olunaku lwo." }
    },
    "default": "Weebale maama! Ekyo ekibuuzo kikulu nnyo. Osobola okumbuuza ku bubonero obw'obulabe, okukuba kw'omwana, eby'okulya, oba okukuba essimu eri omusawo ku +256 778 501 066."
  },
  "runyankore": {
    "name": "Runyankore (Western)",
    "greeting": "Agandi Maama! Ndi MaamaCare AI, omuyambi waawe w'eby'amagara gaanyu n'omwana waawe ori munda.",
    "placeholder": "Buuza ekibuuzo aha nda nari omwana...",
    "listenText": "Huuriza eiraka",
    "quickChips": ["🚨 Obumanyiso bw'akabi", "👶 Omwana arikutera ata?", "🥗 Eby'okurya n'obujuma", "🏥 Okwija omu ddwaliro"],
    "intents": {
      "danger": { "keywords": ["akabi", "omusaayi", "omutwe", "amaisho", "bleeding"], "response": "⚠️ AKABI K'AMAANI! Waareeba omusaayi kuruga omuriiwe, omutwe gw'amaani, nari omusujja, yiruka aha ddwaliro ahonaaho! Nari teera 112 / 0800 100 200, nari midwife aha +256 778 501 066." },
      "kicks": { "keywords": ["kutera", "omwana", "kicks"], "response": "👶 OKUTERA KW'OMWANA: Omwana ashemereire kutera emirundi ikumi (10) omu shaaha ibiri ohuumwire aha rubaju rwa bumosho. Yaaba atari kutera, yiruka aha ddwaliro." },
      "nutrition": { "keywords": ["kurya", "ebyokurya", "doodo", "iron"], "response": "🥗 EBY'OKURYA: Rya emboga ziragrikirwe (doodo, ebitakuri), ebihimba, amagi n'amata. Mira obujuma bwa Iron & Folic Acid buri eizooba." }
    },
    "default": "Webare maama! Ndi wano kukuyamba. Noobaasa kumbuuza aha kutera kw'omwana, eby'okurya, obumanyiso bw'akabi, nari waateera essimu aha +256 778 501 066."
  },
  "rukiga": {
    "name": "Rukiga (Kigezi)",
    "greeting": "Oraire ota Maama! Ndi MaamaCare AI, omukuru w'amagara gaanyu n'omwana ori munda omu Kigezi.",
    "placeholder": "Buuza aha nda n'omwana wo...",
    "listenText": "Huuriza eiraka",
    "quickChips": ["🚨 Obumanyiso bw'akabi", "👶 Omwana arikutera ata?", "🥗 Eby'okurya by'omusaayi", "🏥 Okugyenda aha ddwaliro"],
    "intents": {
      "danger": { "keywords": ["akabi", "omusaayi", "omutwe", "bleeding"], "response": "⚠️ AKABI K'AMAANI! Waaza omu musaayi kuruga omu nda, omutwe gukurema gwine ebihoho omu maisho, yiruka aha ddwaliro erikukira haihi ahonaaho!" }
    },
    "default": "Webare kwebuuza maama! Amagara gaawe n'omwana nigo g'omugasho. Kumbuuza aha by'okurya, okutera kw'omwana, obumanyiso bw'akabi, nari +256 778 501 066."
  },
  "lusoga": {
    "name": "Lusoga (Busoga)",
    "greeting": "Kodheyo Maama! Nze MaamaCare AI ow'omulala gwo ku by'obulamu bwo n'obw'omwana ori mu nda.",
    "placeholder": "Buuza ekibuuzo kyo ku nda...",
    "listenText": "Wuliriza eddoboozi",
    "quickChips": ["🚨 Obubonero obubi", "👶 Omwana akuba atya?", "🥗 Eby'okulya n'amata", "🏥 Enaku dh'eddwaliro"],
    "intents": {
      "danger": { "keywords": ["obulabe", "omusaayi", "omutwe", "bleeding"], "response": "⚠️ AKABANGA AKABI! Singa obona omusaayi gukuvaamu oba omutwe ogukutemye, yanguwa ogende mu ddwaliro lw'amangu ddala! Kuba ku 112 oba 0800 100 200." }
    },
    "default": "Webale kwogera nange maama! Buuza ku buli kintu ky'oyagala oba kubira abasawo baffe ku +256 778 501 066."
  },
  "acholi": {
    "name": "Acholi (Northern / Luo)",
    "greeting": "Kop ango Maama! An aye MaamaCare AI me konyi i kom yotkom meri ki pa litino ma itye kwede i ici.",
    "placeholder": "Peny lapiny i kom ic...",
    "listenText": "Winye dwon",
    "quickChips": ["🚨 Pwony me gemo", "👶 Gayo pa litino", "🥗 Cam me yotkom", "🏥 Cito i ot yat"],
    "intents": {
      "danger": { "keywords": ["gemo", "remo", "wic", "bleeding"], "response": "⚠️ PWONY ME GEMO MADIT! Ka ineno remo cwer ki i dyere onyo wic abara madit marac, citi i ot yat ma cok loyo oyotoyot! Go cim 112 onyo 0800 100 200." }
    },
    "default": "Apwoyo tutwal maama! Yotkom meri ki pa litino tye gin madit. Peny lapiny mo keken nyo go cim i +256 778 501 066."
  },
  "lango": {
    "name": "Lango (Northern)",
    "greeting": "Kop ango Maama! Atye kany me konyi i yotkom me ic meri kede me litino ame itye kede.",
    "placeholder": "Peny lapiny i yotkom...",
    "listenText": "Winye dwon",
    "quickChips": ["🚨 Obanga gema", "👶 Kwano gayo pa litino", "🥗 Cam me remo", "🏥 Nino me ot yat"],
    "intents": {
      "danger": { "keywords": ["gema", "remo", "wiye", "bleeding"], "response": "⚠️ OBANGA GEMA MALELE! Ka icwec remo onyo wiye obaro atek tutwal, wot i ot yat atotot! Go cim me nono 112 onyo 0800 100 200." }
    },
    "default": "Apwoyo matek maama! Peny lapiny i kom yotkom me ic, nino me ot yat, onyo go cim i +256 778 501 066."
  },
  "ateso": {
    "name": "Ateso (Eastern / Teso)",
    "greeting": "Yoga noi Maama! Eong nesi MaamaCare AI ikepakoni kede aijar kon kede naka ikoku kotoma aberu.",
    "placeholder": "Ingit aingiset nako ikoku...",
    "listenText": "Koko eporoto",
    "quickChips": ["🚨 Agogon naka akalany", "👶 Aikeun naka ikoku", "🥗 Inyamat ka aokot", "🏥 Airot ore eipone"],
    "intents": {
      "danger": { "keywords": ["akalany", "aokot", "akou", "bleeding"], "response": "⚠️ AGOGON NAKA AKALANY! Arai ituru aokot arai ekukuni akou noi, kotor ore loka eipone (hospital) atipet! Epedori jo aiyalam simu 112 arai 0800 100 200." }
    },
    "default": "Eyalama noi maama! Ingit aingiset kere nako aikeun naka ikoku, inyamat, arai koom simu mama +256 778 501 066."
  },
  "lugbara": {
    "name": "Lugbara (West Nile)",
    "greeting": "Mi ngoni Maama! Ma mini MaamaCare AI, aza koza mini kpere mva mini dria vule.",
    "placeholder": "Zi e'yo mva kede ali vule...",
    "listenText": "Eri o'du",
    "quickChips": ["🚨 E'yo ndri ka", "👶 Mva saza (Kicks)", "🥗 Enya kede aya ari", "🏥 Muza osipitali sia"],
    "intents": {
      "danger": { "keywords": ["ndri", "ari", "dri", "bleeding"], "response": "⚠️ E'YO NDRI KA! Ari ka le'e mi ti vule, dri ka sa nyari-nyari, mu osipitali sia azo amvu! Zaza simu 112 ko 0800 100 200 awu be ku." }
    },
    "default": "Awa'difo maama! Yotkom mini be mva mini be nesi e'yo eripi. Zi e'yo azi mini lezuri dria, ko zaza midwife mini i +256 778 501 066."
  },
  "runyoro": {
    "name": "Runyoro-Rutooro (Western)",
    "greeting": "Oraire ota Maama! Ninyowe MaamaCare AI, omuyambi waawe ow'eby'obwomeezi bwawe n'obw'omwana ori munda.",
    "placeholder": "Buuza ekibuuzo kyona...",
    "listenText": "Huuriza iraka",
    "quickChips": ["🚨 Obulumuna bw'amaani", "👶 Omwana arikutera ata?", "🥗 Eby'okulya eby'omusaayi", "🏥 Ebiro by'okugenda"],
    "intents": {
      "danger": { "keywords": ["obulumuna", "omusaayi", "omutwe", "bleeding"], "response": "⚠️ OBULUMUNA BW'AMAANI! Obworaaba oine omusaayi ogurukukwija nari omutwe ogurukukulema, genda ha ddwaliro erikukira haihi ahonaaho!" }
    },
    "default": "Webale muno maama! Obwomeezi bwawe n'obw'omwana nigo b'omugaso. Kumbuuza ekiro kyona nari oteere essimu aha +256 778 501 066."
  },
  "lumasaba": {
    "name": "Lumasaba (Bugisu)",
    "greeting": "Mulembe Maama! Inze MaamaCare AI, omuyambi wo khulwe bulamu bwoosi n'obwo mwana ori munda.",
    "placeholder": "Buuza khulwe bulamu...",
    "listenText": "Wulila lilaka",
    "quickChips": ["🚨 Kamatsai n'obulabe", "👶 Okhukuba khwo mwana", "🥗 By'okhulia n'eddagala", "🏥 Tsikhabado tsyo mu dwalilo"],
    "intents": {
      "danger": { "keywords": ["kamatsai", "lilulu", "omutwe", "bleeding"], "response": "⚠️ LUBANGA LULULU! Wakhabona kamatsai kakhuvaamu, omutwe ogukulumina, khenda mu dwalilo mangu mangu! Khuba lisiimu ku 112 naye 0800 100 200." }
    },
    "default": "Wanyala naabi maama! Obulamu bwo n'obwo mwana bwebufuna imbeli. Buuza khuri kyosi ky'oyenda kuteera lisiimu ku +256 778 501 066."
  },
  "english": {
    "name": "English (Official)",
    "greeting": "Hello Mama! I am MaamaCare AI, your maternal and newborn health assistant. How can I help you today with pregnancy signs, fetal kicks, or clinic visits?",
    "placeholder": "Ask any maternal or baby question...",
    "listenText": "Listen to Voice",
    "quickChips": ["🚨 Danger signs in pregnancy", "👶 How to count baby kicks", "🥗 Nutrition & Iron pills", "🏥 Next clinic visit date"],
    "intents": {
      "danger": { "keywords": ["danger", "bleeding", "headache", "vision", "fever", "pain"], "response": "⚠️ CRITICAL EMERGENCY: If you experience vaginal bleeding, severe unyielding headache with blurred vision, or high fever, proceed to the nearest health facility immediately! Dial toll-free 112 or 0800 100 200, or call +256 778 501 066." },
      "kicks": { "keywords": ["kicks", "kick", "movement", "move"], "response": "👶 BABY KICKS: Rest on your left side after a meal. You should feel at least 10 distinct movements within 2 hours. If movement decreases noticeably, visit your clinic right away." },
      "nutrition": { "keywords": ["food", "nutrition", "eat", "iron", "greens"], "response": "🥗 NUTRITION: Eat green vegetables (doodo, nakati), beans, eggs, and take your daily Iron & Folic Acid supplements to build strong maternal blood and support baby development." },
      "visits": { "keywords": ["visit", "anc", "clinic", "hospital", "appointment"], "response": "🏥 CLINIC VISITS: The Ministry of Health recommends at least 4 ANC visits. BabyHealth Guard automatically sends SMS reminders, or dial *920# on any phone to check your dates." }
    },
    "default": "Thank you Mama! Your health and baby's care are our priority. Ask me about danger signs, counting kicks, or reach our midwife team at +256 778 501 066."
  },
  "swahili": {
    "name": "Kiswahili (East Africa)",
    "greeting": "Jambo Mama! Mimi ni MaamaCare AI, msaidizi wako wa afya ya uzazi na mtoto. Una swali lolote kuhusu ujauzito au mtoto leo?",
    "placeholder": "Uliza swali kuhusu ujauzito au mtoto...",
    "listenText": "Sikiliza sauti",
    "quickChips": ["🚨 Dalili za hatari", "👶 Mateke ya mtoto", "🥗 Lishe na vidonge vya damu", "🏥 Tarehe ya kliniki"],
    "intents": {
      "danger": { "keywords": ["hatari", "damu", "kichwa", "macho", "homa", "bleeding"], "response": "⚠️ TAHADHARI YA HATARI! Ukiona damu inatoka, maumivu makali ya kichwa na kutoona vizuri, fika hospitalini haraka! Piga simu ya bure 112 au 0800 100 200, au piga +256 778 501 066." }
    },
    "default": "Asante sana mama! Afya yako ndiyo kipaumbele chetu. Uliza kuhusu dalili za hatari, mateke ya mtoto, au piga simu kwa +256 778 501 066."
  }
};

let currentMaamaLang = 'luganda';

function openAiSideDrawer() {
  const drawer = document.getElementById('aiSideDrawer');
  const backdrop = document.getElementById('aiSideDrawerBackdrop');
  if (!drawer || !backdrop) return;
  initMaamaDrawerChat();
  backdrop.classList.remove('hidden');
  setTimeout(() => drawer.classList.remove('translate-x-full'), 10);
}

function closeAiSideDrawer() {
  const drawer = document.getElementById('aiSideDrawer');
  const backdrop = document.getElementById('aiSideDrawerBackdrop');
  if (!drawer || !backdrop) return;
  drawer.classList.add('translate-x-full');
  setTimeout(() => backdrop.classList.add('hidden'), 300);
  if ('speechSynthesis' in window) window.speechSynthesis.cancel();
}

function switchLanguage(langKey) {
  if (!MAAMA_LANGUAGES[langKey]) return;
  currentMaamaLang = langKey;
  
  const langData = MAAMA_LANGUAGES[langKey];
  const badge = document.getElementById('drawerDialectBadge');
  const input = document.getElementById('drawerChatInput');
  const select = document.getElementById('drawerLangSelect');
  
  if (badge) badge.textContent = `${langData.name} Active • Audio Spoken`;
  if (input) input.placeholder = langData.placeholder;
  if (select) select.value = langKey;

  initMaamaDrawerChat();
}

function initMaamaDrawerChat() {
  const langData = MAAMA_LANGUAGES[currentMaamaLang];
  const container = document.getElementById('drawerChatMessages');
  if (!container) return;
  
  container.innerHTML = `
    <div class="flex items-start gap-2.5">
      <div class="w-7 h-7 rounded-lg bg-gradient-to-tr from-cyan-600 to-teal-500 text-white flex items-center justify-center text-xs shrink-0 shadow-xs">
        🤱
      </div>
      <div class="bg-white rounded-2xl rounded-tl-none p-3 shadow-xs border border-slate-200 text-xs text-slate-800 leading-relaxed max-w-[85%]">
        <span class="font-bold text-[#0e7490] block mb-1">${langData.name}</span>
        <p>${langData.greeting}</p>
        <div class="mt-2.5 pt-1.5 border-t border-slate-100 flex items-center justify-between text-[11px]">
          <button type="button" onclick="speakMaamaText('${escapeMaamaQuotes(langData.greeting)}', '${currentMaamaLang}')" class="inline-flex items-center gap-1 font-bold text-[#0e7490] hover:text-cyan-800 cursor-pointer">
            <span class="material-symbols-outlined text-[15px]">volume_up</span>
            <span>${langData.listenText}</span>
          </button>
        </div>
      </div>
    </div>
  `;

  const chipsBox = document.getElementById('drawerQuickChips');
  if (chipsBox) {
    chipsBox.innerHTML = '';
    langData.quickChips.forEach(chip => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'px-2.5 py-1 rounded-full bg-slate-100 hover:bg-cyan-50 hover:text-[#0e7490] text-slate-700 text-[11px] font-medium border border-slate-200 transition-colors cursor-pointer';
      btn.textContent = chip;
      btn.onclick = () => {
        const inp = document.getElementById('drawerChatInput');
        if (inp) inp.value = chip;
        processMaamaDrawerMessage(chip);
      };
      chipsBox.appendChild(btn);
    });
  }
}

function handleDrawerChatSubmit(e) {
  e.preventDefault();
  const input = document.getElementById('drawerChatInput');
  if (!input) return;
  const text = input.value.trim();
  if (!text) return;
  processMaamaDrawerMessage(text);
  input.value = '';
}

function processMaamaDrawerMessage(text) {
  const container = document.getElementById('drawerChatMessages');
  if (!container) return;
  
  // User bubble
  container.insertAdjacentHTML('beforeend', `
    <div class="flex items-start justify-end gap-2">
      <div class="bg-[#0e7490] text-white rounded-2xl rounded-tr-none p-3 shadow-xs text-xs leading-relaxed max-w-[85%]">
        <p>${text}</p>
      </div>
      <div class="w-7 h-7 rounded-lg bg-slate-800 text-white flex items-center justify-center text-xs shrink-0">
        👤
      </div>
    </div>
  `);
  container.scrollTop = container.scrollHeight;

  // AI Response
  setTimeout(() => {
    const langData = MAAMA_LANGUAGES[currentMaamaLang];
    let responseText = langData.default;
    const q = text.toLowerCase();
    if (langData.intents) {
      for (const [key, val] of Object.entries(langData.intents)) {
        if (val.keywords.some(k => q.includes(k.toLowerCase()))) {
          responseText = val.response;
          break;
        }
      }
    }
    
    container.insertAdjacentHTML('beforeend', `
      <div class="flex items-start gap-2.5">
        <div class="w-7 h-7 rounded-lg bg-gradient-to-tr from-cyan-600 to-teal-500 text-white flex items-center justify-center text-xs shrink-0 shadow-xs">
          🤱
        </div>
        <div class="bg-white rounded-2xl rounded-tl-none p-3 shadow-xs border border-slate-200 text-xs text-slate-800 leading-relaxed max-w-[85%]">
          <span class="font-bold text-[#0e7490] block mb-1">${langData.name}</span>
          <p>${responseText}</p>
          <div class="mt-2.5 pt-1.5 border-t border-slate-100 flex items-center justify-between text-[11px]">
            <button type="button" onclick="speakMaamaText('${escapeMaamaQuotes(responseText)}', '${currentMaamaLang}')" class="inline-flex items-center gap-1 font-bold text-[#0e7490] hover:text-cyan-800 cursor-pointer">
              <span class="material-symbols-outlined text-[15px]">volume_up</span>
              <span>${langData.listenText}</span>
            </button>
            <a href="https://wa.me/256778501066?text=${encodeURIComponent('MaamaCare AI: ' + text)}" target="_blank" class="text-[10px] font-bold text-emerald-600 hover:underline">
              Midwife WhatsApp →
            </a>
          </div>
        </div>
      </div>
    `);
    container.scrollTop = container.scrollHeight;

    speakMaamaText(responseText, currentMaamaLang);
  }, 350);
}

function speakMaamaText(text, langKey) {
  if (!('speechSynthesis' in window)) return;
  window.speechSynthesis.cancel();
  
  const cleanText = text.replace(/⚠️|👶|🥗|🏥|🤱|●|🚨/g, '').trim();
  const utterance = new SpeechSynthesisUtterance(cleanText);
  
  const voices = window.speechSynthesis.getVoices();
  const preferred = voices.find(v => v.lang.startsWith('sw') || v.lang.includes('ZA') || v.lang.includes('KE') || v.lang.includes('NG')) 
                 || voices.find(v => v.lang.startsWith('en')) 
                 || voices[0];
  if (preferred) utterance.voice = preferred;
  utterance.rate = 0.93;
  utterance.pitch = 1.04;
  window.speechSynthesis.speak(utterance);
}

function startVoiceInput() {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (!SpeechRecognition) {
    alert("Voice speech recognition is not supported in this browser. Please type your question.");
    return;
  }
  const micBtn = document.getElementById('drawerMicBtn');
  if (micBtn) micBtn.classList.add('bg-rose-100', 'text-rose-600', 'animate-pulse');
  
  const recognition = new SpeechRecognition();
  recognition.lang = 'en-UG';
  recognition.continuous = false;
  recognition.interimResults = false;

  recognition.onresult = function(event) {
    const transcript = event.results[0][0].transcript;
    const inp = document.getElementById('drawerChatInput');
    if (inp) inp.value = transcript;
    processMaamaDrawerMessage(transcript);
  };

  recognition.onerror = function() {
    if (micBtn) micBtn.classList.remove('bg-rose-100', 'text-rose-600', 'animate-pulse');
  };

  recognition.onend = function() {
    if (micBtn) micBtn.classList.remove('bg-rose-100', 'text-rose-600', 'animate-pulse');
  };

  recognition.start();
}

function escapeMaamaQuotes(str) {
  return str.replace(/'/g, "\\\\'").replace(/"/g, '&quot;').replace(/\\n/g, ' ');
}
</script>
'''

# Single Floating Button for desktop / web dashboards
SINGLE_DESKTOP_AI_BUTTON = '''
<!-- STRICTLY ONE FLOATING AI ASSISTANT BUTTON -->
<div class="fixed bottom-6 right-6 z-40">
  <button onclick="openAiSideDrawer()" aria-label="Open MaamaCare AI Assistant" class="flex items-center gap-2 px-4 py-3 rounded-full bg-[#0e7490] hover:bg-[#08232c] text-white font-bold text-xs sm:text-sm shadow-xl shadow-cyan-950/20 active:scale-95 transition-all border border-cyan-400/30 cursor-pointer" title="Open 10 Ugandan Languages Maternal AI Assistant">
    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
    <span class="material-symbols-outlined text-[19px]">auto_awesome</span>
    <span>MaamaCare AI (10 Dialects)</span>
  </button>
</div>
'''

# Single Floating Button for Mobile screens (above bottom nav)
SINGLE_MOBILE_AI_BUTTON = '''
<!-- STRICTLY ONE FLOATING AI ASSISTANT BUTTON (MOBILE) -->
<div class="fixed bottom-20 right-4 z-40">
  <button onclick="openAiSideDrawer()" aria-label="Open MaamaCare AI Assistant" class="flex items-center gap-2 px-3.5 py-2.5 rounded-full bg-[#0e7490] hover:bg-[#08232c] text-white font-bold text-xs shadow-xl active:scale-95 transition-all border border-white/20 cursor-pointer" title="Open 10 Ugandan Languages Maternal AI Assistant">
    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
    <span class="material-symbols-outlined text-[18px]">auto_awesome</span>
    <span>MaamaCare AI</span>
  </button>
</div>
'''

# =============================================================================
# 1. CLEAN UP index.html TO STRICTLY ONE BUTTON
# =============================================================================
index_path = r"C:\Users\Admin\BabyHealth-Guard\index.html"
with open(index_path, "r", encoding="utf-8") as f:
    idx_content = f.read()

# 1.1 Remove Header AI button if present
old_nav_ai = '''        <!-- AI Assistant Drawer Trigger Button -->
        <button onclick="openAiSideDrawer()" class="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-cyan-50 hover:bg-cyan-100 text-[#0e7490] font-bold text-xs border border-cyan-200 shadow-xs transition-all active:scale-95">
          <span class="material-symbols-outlined text-[16px]">auto_awesome</span>
          <span>Ask AI (10 Dialects)</span>
        </button>'''
if old_nav_ai in idx_content:
    idx_content = idx_content.replace(old_nav_ai, '')
    print("Removed duplicate AI button from index.html Header.")

# 1.2 Remove Hero AI button if present
old_hero_ai = '''            <button onclick="openAiSideDrawer()" class="inline-flex items-center justify-center gap-2 px-5 py-3 rounded-xl bg-white hover:bg-slate-50 text-slate-800 font-bold text-xs sm:text-sm border border-slate-200 shadow-xs transition-all active:scale-95">
              <span class="material-symbols-outlined text-[18px] text-[#0e7490]">auto_awesome</span>
              <span>Open MaamaCare AI (Side Panel)</span>
            </button>'''
new_hero_link = '''            <a href="/mobile/dashboard_preview.html" class="inline-flex items-center justify-center gap-2 px-5 py-3 rounded-xl bg-white hover:bg-slate-50 text-slate-800 font-bold text-xs sm:text-sm border border-slate-200 shadow-xs transition-all active:scale-95">
              <span class="material-symbols-outlined text-[18px]">smartphone</span>
              <span>Preview Mother App</span>
            </a>'''
if old_hero_ai in idx_content:
    idx_content = idx_content.replace(old_hero_ai, new_hero_link)
    print("Removed duplicate AI button from index.html Hero.")

# 1.3 Remove docked vertical button on right edge if present
old_docked_tab = '''  <!-- ========================================================================= -->
  <!-- 8. PERMANENT SIDE FLOATING TRIGGER BUTTON (AT THE SIDE)                   -->
  <!-- ========================================================================= -->
  <button onclick="openAiSideDrawer()" aria-label="Open MaamaCare AI Assistant" class="fixed top-1/2 right-0 -translate-y-1/2 z-40 bg-[#0e7490] hover:bg-[#08232c] text-white py-3 px-3 rounded-l-2xl shadow-2xl flex flex-col items-center gap-1.5 transition-all hover:pr-4 group active:scale-95 border-l-2 border-y-2 border-cyan-400/30">
    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
    <span class="material-symbols-outlined text-[20px]">auto_awesome</span>
    <span class="text-[10px] font-extrabold uppercase tracking-widest [writing-mode:vertical-rl] rotate-180">
      MaamaCare AI
    </span>
  </button>'''
if old_docked_tab in idx_content:
    idx_content = idx_content.replace(old_docked_tab, '')
    print("Removed duplicate vertical docked AI tab from index.html.")

# Also clean up any loose vertical tab button
old_vertical_btn = '''<button onclick="openAiSideDrawer()" aria-label="Open MaamaCare AI Assistant" class="fixed top-1/2 right-0 -translate-y-1/2 z-40 bg-[#0e7490] hover:bg-[#08232c] text-white py-3 px-3 rounded-l-2xl shadow-2xl flex flex-col items-center gap-1.5 transition-all hover:pr-4 group active:scale-95 border-l-2 border-y-2 border-cyan-400/30">
    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
    <span class="material-symbols-outlined text-[20px]">auto_awesome</span>
    <span class="text-[10px] font-extrabold uppercase tracking-widest [writing-mode:vertical-rl] rotate-180">
      MaamaCare AI
    </span>
  </button>'''
if old_vertical_btn in idx_content:
    idx_content = idx_content.replace(old_vertical_btn, '')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(idx_content)
print("Updated index.html: Now has strictly ONE AI button at bottom-right.")

# =============================================================================
# 2. INJECT AI ASSISTANT WITH STRICTLY ONE BUTTON INTO frontend/index.html
# =============================================================================
fe_path = r"C:\Users\Admin\BabyHealth-Guard\frontend\index.html"
with open(fe_path, "r", encoding="utf-8") as f:
    fe_content = f.read()

# Remove any old drawer if already added
if 'id="aiSideDrawer"' not in fe_content:
    # Insert AI Drawer & Single Button & JS before </body>
    insertion = SINGLE_DESKTOP_AI_BUTTON + '\n' + AI_DRAWER_HTML + '\n' + AI_DRAWER_JS + '\n'
    fe_content = fe_content.replace('</body>', insertion + '</body>')
    with open(fe_path, "w", encoding="utf-8") as f:
        f.write(fe_content)
    print("Injected AI Assistant with strictly ONE button into frontend/index.html.")
else:
    print("AI Assistant already in frontend/index.html.")

# Copy to backend static as well
be_static = r"C:\Users\Admin\BabyHealth-Guard\backend\src\main\resources\static\index.html"
with open(be_static, "w", encoding="utf-8") as f:
    f.write(fe_content)
print("Synchronized to backend/src/main/resources/static/index.html.")

# =============================================================================
# 3. INJECT AI ASSISTANT WITH STRICTLY ONE BUTTON INTO mobile/dashboard_preview.html
# =============================================================================
mob_dash_path = r"C:\Users\Admin\BabyHealth-Guard\mobile\dashboard_preview.html"
with open(mob_dash_path, "r", encoding="utf-8") as f:
    mob_content = f.read()

if 'id="aiSideDrawer"' not in mob_content:
    insertion = SINGLE_MOBILE_AI_BUTTON + '\n' + AI_DRAWER_HTML + '\n' + AI_DRAWER_JS + '\n'
    mob_content = mob_content.replace('</body>', insertion + '</body>')
    with open(mob_dash_path, "w", encoding="utf-8") as f:
        f.write(mob_content)
    print("Injected AI Assistant with strictly ONE button into mobile/dashboard_preview.html.")
else:
    print("AI Assistant already in mobile/dashboard_preview.html.")

# =============================================================================
# 4. INJECT AI ASSISTANT WITH STRICTLY ONE BUTTON INTO mobile/visits_preview.html
# =============================================================================
mob_visits_path = r"C:\Users\Admin\BabyHealth-Guard\mobile\visits_preview.html"
if os.path.exists(mob_visits_path):
    with open(mob_visits_path, "r", encoding="utf-8") as f:
        v_content = f.read()
    if 'id="aiSideDrawer"' not in v_content:
        insertion = SINGLE_MOBILE_AI_BUTTON + '\n' + AI_DRAWER_HTML + '\n' + AI_DRAWER_JS + '\n'
        v_content = v_content.replace('</body>', insertion + '</body>')
        with open(mob_visits_path, "w", encoding="utf-8") as f:
            f.write(v_content)
        print("Injected AI Assistant with strictly ONE button into mobile/visits_preview.html.")

# =============================================================================
# 5. INJECT AI ASSISTANT WITH STRICTLY ONE BUTTON INTO mobile/danger_signs_preview.html
# =============================================================================
mob_danger_path = r"C:\Users\Admin\BabyHealth-Guard\mobile\danger_signs_preview.html"
if os.path.exists(mob_danger_path):
    with open(mob_danger_path, "r", encoding="utf-8") as f:
        d_content = f.read()
    if 'id="aiSideDrawer"' not in d_content:
        insertion = SINGLE_MOBILE_AI_BUTTON + '\n' + AI_DRAWER_HTML + '\n' + AI_DRAWER_JS + '\n'
        d_content = d_content.replace('</body>', insertion + '</body>')
        with open(mob_danger_path, "w", encoding="utf-8") as f:
            f.write(d_content)
        print("Injected AI Assistant with strictly ONE button into mobile/danger_signs_preview.html.")

print("All dashboards successfully updated: strictly ONE AI Assistant button on each screen!")
