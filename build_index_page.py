import json
import os

print("Writing clean, uncrowded, modern landing page with side AI assistant...")

# The same rich 10 Ugandan languages database
LANGUAGES_JSON = """{
  "luganda": {
    "name": "Luganda (Central)",
    "greeting": "Oli otya Maama! Nze MaamaCare AI, omuyambi wo ku by'obulamu bwo n'obw'omwana wo. Ndi wano okukuyamba ku bintu byonna ebikwata ku lubuto, okugenda mu ddwaliro, n'obulamu bw'omwana.",
    "placeholder": "Buuza ekibuuzo ku lubuto oba omwana...",
    "listenText": "Wuliriza eddoboozi",
    "quickChips": [
      "🚨 Obubonero obw'obulabe",
      "👶 Omwana akuba atya?",
      "🥗 Eby'okulya n'eddagala lya ayoni",
      "🏥 Eddwaliro n'okubala emyezi"
    ],
    "intents": {
      "danger": {
        "keywords": ["obulabe", "omusaayi", "omutwe", "amaaso", "omusujja", "kuzimba", "okulumwa", "ebire", "bleeding", "headache", "fever", "pain"],
        "response": "⚠️ OBULABE OBW'AMANGU! Singa ofuna okuvaamu omusaayi, omutwe omunene ogutawona ng'olina ebire mu maaso, omusujja omungi, oba amagulu n'obwenyi okuzimba ennyo, genda mu ddwaliro eriri okumpi amangu ddala! Osobola n'okukuba essimu ku 112 oba 0800 100 200 ku bwereere, oba kubira omusawo wo ku +256 778 501 066."
      },
      "kicks": {
        "keywords": ["kuba", "okukuba", "tazannya", "omwana", "kicks", "movement", "move"],
        "response": "👶 OKUKUBA KW'OMWANA: Okuva ku wiiki 24–28, omwana wo aba asuubirwa okukuba. Funa ekifo eky'eddembe, olyeko ekintu, owoomuleko wansi ku lubiriizi olwa kkono. Omwana asaanidde akube emirundi egitakka wansi wa 10 mu ssaawa bbiri (2). Bw'owulira nti takubye oba nti akendeezezza ennyo, genda mu ddwaliro omusawo akebe omutima gwe."
      },
      "nutrition": {
        "keywords": ["lya", "okulya", "enva", "ayoni", "omusaayi", "doodo", "nakati", "eddagala", "iron", "food", "eat"],
        "response": "🥗 EBY'OKULYA N'OBULAMU: Lya emmere ezimba omubiri n'ereeta omusaayi: enva endiirwa (doodo, nakati, bbugga), ebijanjaalo, amagi, ebinyebwa, n'ebibala nga emicungwa. Mira buli lunaku obutole bwa Ayoni ne Folic Acid (eddagala ery'omusaayi) lye baakuwa mu ddwaliro. Nwa amazzi amayonjo amalungi buli lunaku."
      },
      "visits": {
        "keywords": ["ddwaliro", "anc", "okugenda", "eddwaaliro", "omusawo", "appointment", "clinic", "hospital"],
        "response": "🏥 OKUGENDA MU DDWALIRO (ANC): Buli maama alina okugenda mu ddwaliro emirundi egitakka wansi wa 4 mu lubuto lwe olwonna. Bwe tuba tukozesa BabyHealth Guard, ofuna obubaka bwa SMS obukujjukiza olunaku lw'eddwaliro. Bw'oba tolina ssimu ya smartphone, koona *920# okumanya olunaku lwo."
      },
      "labor": {
        "keywords": ["okuzaala", "ebisa", "okulumwa", "amazzi", "labor", "delivery", "birth"],
        "response": "🤱 OBUBONERO OBW'OKUZAALA: Bw'otandika okulumwa ebisa ebijja buli luvannyuma lw'eddakiika 5-10 nga byeyongera, oba ng'amazzi g'omwana gasaze, tambula amangu ogende mu ddwaliro erina abasawo abazaalisa. Tuteekateeka ebyetaago by'omwana byonna."
      }
    },
    "default": "Weebale maama! Ekyo ekibuuzo kikulu nnyo ku bulamu bwo n'obw'omwana. Osobola okumbuuza ku bubonero obw'obulabe, okukuba kw'omwana, eby'okulya, oba okukuba essimu eri omusawo wo ku +256 778 501 066."
  },
  "runyankore": {
    "name": "Runyankore (Western)",
    "greeting": "Agandi Maama! Ndi MaamaCare AI, omuyambi waawe w'eby'amagara gaanyu n'omwana waawe ori munda. Ndi wano kukuyamba aha buri kintu eki orikwenda kumanya.",
    "placeholder": "Buuza ekibuuzo aha nda nari omwana...",
    "listenText": "Huuriza eiraka",
    "quickChips": [
      "🚨 Obumanyiso bw'akabi",
      "👶 Omwana arikutera ata?",
      "🥗 Eby'okurya n'obujuma bw'omusaayi",
      "🏥 Okwija omu ddwaliro"
    ],
    "intents": {
      "danger": {
        "keywords": ["akabi", "omusaayi", "omutwe", "amaisho", "omuswi", "okuzimba", "bleeding", "headache"],
        "response": "⚠️ AKABI K'AMAANI! Waareeba omusaayi kuruga omuriiwe, omutwe gukurema munonga oine ebihuubwa omu maisho, omusujja gw'amaani, nari amaguru n'amaisho bikazimba, yiruka aha ddwaliro ahonaaho! Nari teera essimu ya bwerere 112 / 0800 100 200, nari omidwife waawe aha +256 778 501 066."
      },
      "kicks": {
        "keywords": ["kutera", "omwana", "kicks", "gutera", "movement"],
        "response": "👶 OKUTERA KW'OMWANA: Kuruga aha wiiki 24–28, omwana ashemereire kutera. Za omu mwanya murungi, ohuumure aha rubaju rwa bumosho. Ashemereire kutera emirundi ikumi (10) omu shaaha ibiri (2). Yaaba atari kutera nari akakendeeza, yiruka aha ddwaliro amanguka."
      },
      "nutrition": {
        "keywords": ["kurya", "ebyokurya", "omusaayi", "ebihimba", "doodo", "iron", "food"],
        "response": "🥗 EBY'OKURYA: Rya emboga ziragrikirwe (doodo, ebitakuri), ebihimba, ebinyobwa, amagi n'amata. Mira buri eizooba obujuma bwa Iron & Folic Acid ebi bakuha aha ddwaliro kwongyera omusaayi. Nywa amaizi masya marungi."
      },
      "visits": {
        "keywords": ["eddwaliro", "irwariro", "anc", "omusawo", "clinic", "hospital"],
        "response": "🏥 OKWIZA OMU DDWALIRO (ANC): Oine kugyenda aha ddwaliro emirundi ekitari hansi y'ena (4) omu nda yaawe yoona. Bw'oba oine ekitabo kya BabyHealth Guard, tukwoherereza SMS y'okukwijusya. Aha simu ya butoosa, teera *920# kumanya ebiro byaawe."
      }
    },
    "default": "Webare maama! Ekyo n'ekibuuzo kirungi munonga. Ndi wano kukuyamba omu rugyendo rwawe rw'enda. Noobaasa kumbuuza aha kutera kw'omwana, eby'okurya, obumanyiso bw'akabi, nari waateera essimu aha +256 778 501 066."
  },
  "rukiga": {
    "name": "Rukiga (Kigezi)",
    "greeting": "Oraire ota Maama! Ndi MaamaCare AI, omukuru w'amagara gaanyu n'omwana ori munda omu Kigezi. Nkwase ki leero aha by'enda yaawe?",
    "placeholder": "Buuza aha nda n'omwana wo...",
    "listenText": "Huuriza eiraka",
    "quickChips": [
      "🚨 Obumanyiso bw'akabi k'amaani",
      "👶 Omwana arikutera ata?",
      "🥗 Eby'okurya by'omusaayi",
      "🏥 Okugyenda aha ddwaliro"
    ],
    "intents": {
      "danger": {
        "keywords": ["akabi", "omusaayi", "omutwe", "amaisho", "bleeding", "headache", "fever"],
        "response": "⚠️ AKABI K'AMAANI! Waaza omu musaayi kuruga omu nda, omutwe gukurema gwine ebihoho omu maisho, nari omusujja gw'amaani, yiruka aha ddwaliro erikukira haihi ahonaaho! Teera essimu 112 nari waza aha Bwera/Kabale HC ahonaaho."
      },
      "kicks": {
        "keywords": ["kutera", "omwana", "kicks", "movement"],
        "response": "👶 OKUTERA KW'OMWANA: Reeba yaaba omwana arikutera emirundi 10 omu shaaha ibiri waaba orikuhuumura. Omwana yaareka kutera, genda obwire obwo obwo aha ddwaliro bakebere omutima gw'omwana."
      },
      "nutrition": {
        "keywords": ["kurya", "ebyokurya", "iron", "omusaayi", "ebijuma"],
        "response": "🥗 EBY'OKURYA: Rya emboga zirikutukura, ebihimba, amagi, n'amata ga kaanywisa. Mira obujuma bwa ferusi (iron) bwa buri eizooba kureebeka ngu oine omusaayi gw'okukuza omwana gwawe."
      },
      "visits": {
        "keywords": ["eddwaliro", "anc", "irwariro", "omusawo"],
        "response": "🏥 OKUGYENDA AHA DDWALIRO: Genda aha ddwaliro emirundi 4. Teera *920# aha simu yawe yoona kureeba obwire bwawe obw'okubonana n'omusawo."
      }
    },
    "default": "Webare kwebuuza maama! Amagara gaawe n'omwana nigo g'omugasho munonga. Kumbuuza aha by'okurya, okutera kw'omwana, obumanyiso bw'akabi, nari kutuura oteire essimu aha +256 778 501 066."
  },
  "lusoga": {
    "name": "Lusoga (Busoga)",
    "greeting": "Kodheyo Maama! Nze MaamaCare AI ow'omulala gwo ku by'obulamu bwo n'obw'omwana ori mu nda. Kiki kye nsobola okukuyamba nakyo leero?",
    "placeholder": "Buuza ekibuuzo kyo ku nda n'omwana...",
    "listenText": "Wuliriza eddoboozi",
    "quickChips": [
      "🚨 Obubonero obubi",
      "👶 Omwana akuba atya?",
      "🥗 Eby'okulya n'amata",
      "🏥 Okubala enaku dh'eddwaliro"
    ],
    "intents": {
      "danger": {
        "keywords": ["obulabe", "omusaayi", "omutwe", "amaaso", "omusujja", "bleeding", "headache"],
        "response": "⚠️ AKABANGA AKABI! Singa obona omusaayi gukuvaamu, omutwe ogukutemye ng'obona obuziyaziyo mu maaso, oba amagulu okuzimba ennyo, fuba ogende mu ddwaliro lw'amangu ddala! Kuba ku 112 oba 0800 100 200 kw'ebwereere."
      },
      "kicks": {
        "keywords": ["kuba", "okukuba", "omwana", "kicks", "move"],
        "response": "👶 OKUKUBA KW'OMWANA: Omwana wo asaanidde akube emirundi egitakka wansi wa 10 mu ssaawa ibiri nga oli mukusiriikirira n'okuwummula. Bw'aleka okukuba, yanguwa ogende mu ddwaliro balamule omwana."
      },
      "nutrition": {
        "keywords": ["lya", "okulya", "doodo", "amata", "ayoni", "food"],
        "response": "🥗 EBY'OKULYA: Lya ebinyebwa, enva endiirwa nga doodo ne sukuma, ebijanjaalo, amagi, n'amata. Mira buli lunaku ebinini by'omusaayi (iron and folic acid) byebakuwa mu ddwaliro."
      },
      "visits": {
        "keywords": ["eddwaliro", "anc", "omusawo", "clinic"],
        "response": "🏥 OKUGENDA MU DDWALIRO: Buli maama agende mu ddwaliro emirundi 4 mu lubuto. Kozesa *920# ku ssimu ey'amapeesa okufuna enaku dho."
      }
    },
    "default": "Webale kwogera nange maama! Obulamu bwo n'obw'omwana bwe bukulu obusooka. Buuza ku buli kintu ky'oyagala oba kubira abasawo baffe ku +256 778 501 066."
  },
  "acholi": {
    "name": "Acholi (Northern / Luo)",
    "greeting": "Kop ango Maama! An aye MaamaCare AI me konyi i kom yotkom meri ki pa litino ma itye kwede i ici. Tye gin mo ma imito penyo tin?",
    "placeholder": "Peny lapiny i kom ic ki litino...",
    "listenText": "Winye dwon",
    "quickChips": [
      "🚨 Pwony me gemo",
      "👶 Gayo pa litino",
      "🥗 Cam me yotkom ki yat me remo",
      "🏥 Cito i ot yat (ANC)"
    ],
    "intents": {
      "danger": {
        "keywords": ["gemo", "remo", "wic", "wang", "lyeto", "bleeding", "headache", "fever"],
        "response": "⚠️ PWONY ME GEMO MADIT! Ka ineno remo cwer ki i dyere, wic abara madit marac atika, wangi bedo col, onyo lyeto me kom madit, citi i ot yat ma cok loyo oyotoyot! Go cim me nono 112 onyo 0800 100 200, onyo go cim pa daktari i +256 778 501 066."
      },
      "kicks": {
        "keywords": ["gayo", "litino", "kicks", "pe gayo", "movement"],
        "response": "👶 GAYO PA LITINO: Cakke ki i dwe me abic nyo abicel, litino myero ogoy cwinyi tyen apar (10) i cawa aryo ka itye ka yweyo maber. Ka litino ogik gayo onyo gayo manok atika, citi i ot yat oyotoyot me pimo cwinye."
      },
      "nutrition": {
        "keywords": ["cam", "dek", "alode", "remo", "yat", "food", "eat"],
        "response": "🥗 CAM ME YOTKOM: Cam alode, boo, lakotkot, lapena, odii, ki cam dwe dwe. Mony yat me remo (iron and folic acid) ma kimiyi i ot yat nino ducu wek remo bed ma opong i komi."
      },
      "visits": {
        "keywords": ["ot yat", "anc", "daktari", "cito", "hospital"],
        "response": "🏥 CITO I OT YAT (ANC): Citi i ot yat tyen angwen (4) i ic ma itye kwede. Go cim *920# me nongo nino me cito i ot yat meri."
      }
    },
    "default": "Apwoyo tutwal maama! Yotkom meri ki pa litino tye gin madit adada. Itye ki twero me penyo lapiny mo keken i kom gayo pa litino, cam maber, nyo cito i ot yat. Go cim i +256 778 501 066."
  },
  "lango": {
    "name": "Lango (Northern)",
    "greeting": "Kop ango Maama! Atye kany me konyi i yotkom me ic meri kede me litino ame itye kede. Imito apenya i kom ngo tin?",
    "placeholder": "Peny lapiny i yotkom me ic...",
    "listenText": "Winye dwon",
    "quickChips": [
      "🚨 Obanga gema",
      "👶 Kwano gayo pa litino",
      "🥗 Cam me kelo remo",
      "🏥 Nino me cito i ot yat"
    ],
    "intents": {
      "danger": {
        "keywords": ["gema", "remo", "wiye", "wang", "lyeto", "bleeding", "headache"],
        "response": "⚠️ OBANGA GEMA MALELE! Ka icwec remo, wiye obaro atek tutwal kede ceto col me wang, onyo komi olyet atek, wot i ot yat atotot! Pe igal bino cawa mo. Go cim me nono 112 onyo 0800 100 200."
      },
      "kicks": {
        "keywords": ["gayo", "litino", "kwano", "kicks", "move"],
        "response": "👶 GAYO PA LITINO: Litino myero ogoy ic tyen apar (10) i kine me cawa aryo ka iweyo. Ka pe tye ka gayo, nyo ogik gayo woko, citi i ot yat wek daktari opim yotkom pa litino."
      },
      "nutrition": {
        "keywords": ["cam", "dek", "alode", "cak", "remo", "food"],
        "response": "🥗 CAM ME KONYO REMO: Cam dek cwaa, dek ngor, odii, alode, kede cak. Mwony yat me remo (iron/folic) ame amiyi i ot yat nino ducu wek remo pe dok piny."
      },
      "visits": {
        "keywords": ["ot yat", "anc", "nino", "daktari"],
        "response": "🏥 NINO ME CITO I OT YAT: Citi i ot yat tyen angwen (4) i ic ducu. Teere cim i *920# me ngeyo cawa me ot yat."
      }
    },
    "default": "Apwoyo matek maama! Yotkom meri aye gin ma pigere tek tutwal. Peny lapiny i kom yotkom me ic, nino me ot yat, onyo go cim i +256 778 501 066 me lok kede midwife."
  },
  "ateso": {
    "name": "Ateso (Eastern / Teso)",
    "greeting": "Yoga noi Maama! Eong nesi MaamaCare AI ikepakoni kede aijar kon kede naka ikoku kotoma aberu. Anyoika bo inyikokit jo aisiom lolo?",
    "placeholder": "Ingit aingiset nako aijar naka ikoku...",
    "listenText": "Koko eporoto",
    "quickChips": [
      "🚨 Agogon naka akalany",
      "👶 Aikeun naka ikoku",
      "🥗 Inyamat ka edeka loka aokot",
      "🏥 Airot ore loka eipone"
    ],
    "intents": {
      "danger": {
        "keywords": ["akalany", "aokot", "akou", "akwap", "bleeding", "headache"],
        "response": "⚠️ AGOGON NAKA AKALANY! Arai ituru aokot, aipot akou kakwapi kede aitiyo na amoni, arai ekukuni akou noi kede amuranat, kotor ore loka eipone (hospital) atipet! Epedori jo aiyalam simu 112 arai 0800 100 200."
      },
      "kicks": {
        "keywords": ["ikoku", "aikeun", "kicks", "movement"],
        "response": "👶 AIKEUN NAKA IKOKU: Isubit ikoku aikeun akon akou irwan itomon (10) kotoma isaawan iarei ka iweiti. Arai mam ikoku ekukuni, kotor ore loka eipone atipet aanyun daktari."
      },
      "nutrition": {
        "keywords": ["inyamat", "edeka", "aokot", "ebwolo", "food"],
        "response": "🥗 INYAMAT LUKAJOKAK: Inyam emorot, ebwolo, imare, kede ikiyai. Inyam edeka loka aokot (Iron and Folic Acid) loka apukot nesi ijaikitai ore loka eipone kinyam ka aponi aokot kanu ikoku."
      },
      "visits": {
        "keywords": ["eipone", "ore", "anc", "daktari"],
        "response": "🏥 AIROT ORE LOKA EIPONE (ANC): Kolot ore loka eipone irwan iwon (4) kotoma aberu kere. Kooma *920# aanyun apaaran kon nako airot."
      }
    },
    "default": "Eyalama noi maama! Aijar kon kede naka ikoku nesi epol noi. Ingit aingiset kere nako aikeun naka ikoku, inyamat, arai koom simu mama ejaasi ikepakok wok ko +256 778 501 066."
  },
  "lugbara": {
    "name": "Lugbara (West Nile)",
    "greeting": "Mi ngoni Maama! Ma mini MaamaCare AI, aza koza mini kpere mva mini dria vule. E'yo azi mini ndazu ngo leero?",
    "placeholder": "Zi e'yo mva kede ali vule...",
    "listenText": "Eri o'du",
    "quickChips": [
      "🚨 E'yo ndri ka",
      "👶 Mva saza (Kicks)",
      "🥗 Enya kede aya ari nzeza",
      "🏥 Muza osipitali sia"
    ],
    "intents": {
      "danger": {
        "keywords": ["ndri", "ari", "dri", "aza", "bleeding", "headache", "fever"],
        "response": "⚠️ E'YO NDRI KA! Ari ka le'e mi ti vule, dri ka sa nyari-nyari kede mi ma amveza, ko mva ka mu pe ku, mu osipitali sia azo amvu! Zaza simu 112 ko 0800 100 200 awu be ku, ko zaza midwife mini i +256 778 501 066."
      },
      "kicks": {
        "keywords": ["mva", "saza", "pe", "kicks", "movement"],
        "response": "👶 MVA SAZA: Mva leke mu sa mudri (10) sawa iri (2) alu ma alea mi ka iwe. Mva ka pe ku ko ka pe mudri ku, mu osipitali sia daktari ma ne mva ma o'du mve."
      },
      "nutrition": {
        "keywords": ["enya", "aya", "ari", "nya", "food"],
        "response": "🥗 ENYA NYIRIKO: Nya enya nyiriko be (alode, enva endiirwa), anyapa nya, ebinyebe nya, kede aya ari nzeza (iron and folic acid) mini feza osipitali sia nya o'du dria."
      },
      "visits": {
        "keywords": ["osipitali", "anc", "muza", "daktari"],
        "response": "🏥 MUZA OSIPITALI SIA (ANC): Mi mu osipitali sia o'du su (4) ali mini dria. Zaza *920# simu si o'du mini nizu."
      }
    },
    "default": "Awa'difo maama! Yotkom mini be mva mini be nesi e'yo eripi a'dusi. Zi e'yo azi mini lezuri dria, ko zaza daktari mini simu si i +256 778 501 066."
  },
  "runyoro": {
    "name": "Runyoro-Rutooro (Western)",
    "greeting": "Oraire ota Maama! Ninyowe MaamaCare AI, omuyambi waawe ow'eby'obwomeezi bwawe n'obw'omwana ori munda. Oine kibuuzo ki ekiro kya leero?",
    "placeholder": "Buuza ekibuuzo kyona...",
    "listenText": "Huuriza iraka",
    "quickChips": [
      "🚨 Obulumuna bw'amaani",
      "👶 Omwana arikutera ata?",
      "🥗 Eby'okulya eby'omusaayi",
      "🏥 Ebiro by'okugenda ha ddwaliro"
    ],
    "intents": {
      "danger": {
        "keywords": ["obulumuna", "omusaayi", "omutwe", "amaisho", "bleeding", "headache"],
        "response": "⚠️ OBULUMUNA BW'AMAANI! Obworaaba oine omusaayi ogurukukwija, omutwe ogurukukulema oine ebihoho omu maisho, nari omusujja gw'amaani, genda ha ddwaliro erikukira haihi ahonaaho! Nari oteere essimu 112 / 0800 100 200 ey'obwereere."
      },
      "kicks": {
        "keywords": ["kutera", "omwana", "kicks", "movement"],
        "response": "👶 OKUTERA KW'OMWANA: Omwana asemerire kutera emirundi ikumi (10) omu saaha ibiri obworaaba orukuhuumura. Obw'araareka kutera, iruka ha ddwaliro abasawo bakebere omutima gwe."
      },
      "nutrition": {
        "keywords": ["kulya", "ebyokulya", "iron", "omusaayi", "food"],
        "response": "🥗 EBY'OKULYA: Lya emboga z'ebitakuri, doodo, ebihimba, n'amata. Mira obutole bwa ayoni na ffoliki obw'omusaayi obubakuhaire ha ddwaliro buli kiro."
      },
      "visits": {
        "keywords": ["ddwaliro", "anc", "omusawo", "ebiro"],
        "response": "🏥 EBIRO BY'OKUGENDA HA DDWALIRO: Oine kugenda ha ddwaliro emirundi ena (4) omu nda yoona. Teera *920# aha simu yawe kumanya ebiro byawe."
      }
    },
    "default": "Webale muno maama! Obwomeezi bwawe n'obw'omwana nigo b'omugaso gw'amaani. Kumbuuza ekiro kyona nari oteere essimu aha +256 778 501 066."
  },
  "lumasaba": {
    "name": "Lumasaba (Bugisu)",
    "greeting": "Mulembe Maama! Inze MaamaCare AI, omuyambi wo khulwe bulamu bwoosi n'obwo mwana ori munda. Wangatsile kwi leero khulwe nda yiyo?",
    "placeholder": "Buuza khulwe bulamu bwoosi...",
    "listenText": "Wulila lilaka",
    "quickChips": [
      "🚨 Kamatsai n'obulabe",
      "👶 Okhukuba khwo mwana",
      "🥗 By'okhulia n'eddagala",
      "🏥 Tsikhabado tsyo mu dwalilo"
    ],
    "intents": {
      "danger": {
        "keywords": ["kamatsai", "lilulu", "kamoni", "kamabeka", "bleeding", "headache"],
        "response": "⚠️ LUBANGA LULULU! Wakhabona kamatsai kakhuvaamu, omutwe ogukulumina ng'obona kamoni kanyirirala, khenda mu dwalilo mangu mangu! Khuba lisiimu ku 112 naye 0800 100 200 y'obwereere."
      },
      "kicks": {
        "keywords": ["khukuba", "mwana", "kicks", "movement"],
        "response": "👶 OKHUKUBA KHWO MWANA: Pima okhukuba khwo mwana. Akube kamasiira likumi (10) mu ssaawa tsibili ng'owumulile. Namaleka okhukuba, khenda mu dwalilo omusawo apime omwoyo gwo mwana."
      },
      "nutrition": {
        "keywords": ["lia", "khulia", "doodo", "kamatsai", "food"],
        "response": "🥗 EBY'OKHULIA: Lya lidodo, kamasindwa, biyanjaalo, kamagi, ne matsai. Manya okhunywa kimatwoli kye kamatsai (iron) kye bakhuwelesye mu dwalilo tsikhafu tsyoosi."
      },
      "visits": {
        "keywords": ["dwalilo", "anc", "omusawo", "tsikhabado"],
        "response": "🏥 TSIKHABADO TSYO MU DWALILO: Khenda mu dwalilo kamasiira kane (4) mu nda yiyo yoosi. Teera *920# khulwe tsikhabado tsyo."
      }
    },
    "default": "Wanyala naabi maama! Obulamu bwo n'obwo mwana bwebufuna imbeli. Buuza khuri kyosi ky'oyenda kuteera lisiimu ku +256 778 501 066."
  },
  "english": {
    "name": "English (Official)",
    "greeting": "Hello Mama! I am MaamaCare AI, your maternal and newborn health assistant. How can I help you today with pregnancy signs, fetal kicks, or clinic visits?",
    "placeholder": "Ask any maternal or baby question...",
    "listenText": "Listen to Voice",
    "quickChips": [
      "🚨 Danger signs in pregnancy",
      "👶 How to count baby kicks",
      "🥗 Nutrition & Iron pills",
      "🏥 Next clinic visit date"
    ],
    "intents": {
      "danger": {
        "keywords": ["danger", "bleeding", "headache", "vision", "fever", "swelling", "pain"],
        "response": "⚠️ CRITICAL EMERGENCY: If you experience vaginal bleeding, severe unyielding headache with blurred vision, or high fever, go to the nearest health centre immediately! Dial toll-free 112 or 0800 100 200, or call +256 778 501 066."
      },
      "kicks": {
        "keywords": ["kicks", "kick", "movement", "move"],
        "response": "👶 BABY KICKS: Rest on your left side after a meal. You should feel at least 10 distinct movements within 2 hours. If movement decreases noticeably, visit your midwife right away."
      },
      "nutrition": {
        "keywords": ["food", "nutrition", "eat", "iron", "greens"],
        "response": "🥗 NUTRITION: Eat green vegetables (doodo, nakati), beans, eggs, and take your daily Iron & Folic Acid supplements to build strong maternal blood and support baby development."
      },
      "visits": {
        "keywords": ["visit", "anc", "clinic", "hospital", "appointment"],
        "response": "🏥 CLINIC VISITS: The Ministry of Health recommends at least 4 ANC visits. BabyHealth Guard automatically sends SMS reminders, or dial *920# on any phone to check your dates."
      }
    },
    "default": "Thank you Mama! Your health and baby's care are our priority. Ask me about danger signs, counting kicks, or reach our midwife team at +256 778 501 066."
  },
  "swahili": {
    "name": "Kiswahili (East Africa)",
    "greeting": "Jambo Mama! Mimi ni MaamaCare AI, msaidizi wako wa afya ya uzazi na mtoto. Una swali lolote kuhusu ujauzito au mtoto leo?",
    "placeholder": "Uliza swali kuhusu ujauzito au mtoto...",
    "listenText": "Sikiliza sauti",
    "quickChips": [
      "🚨 Dalili za hatari",
      "👶 Mateke ya mtoto",
      "🥗 Lishe na vidonge vya damu",
      "🏥 Tarehe ya kliniki"
    ],
    "intents": {
      "danger": {
        "keywords": ["hatari", "damu", "kichwa", "macho", "homa", "bleeding"],
        "response": "⚠️ TAHADHARI YA HATARI! Ukiona damu inatoka, maumivu makali ya kichwa na kutoona vizuri, fika hospitalini haraka! Piga simu ya bure 112 au 0800 100 200, au piga +256 778 501 066."
      },
      "kicks": {
        "keywords": ["mateke", "kucheza", "mtoto", "kicks"],
        "response": "👶 MWENENDO WA MTOTO: Mtoto anapaswa kucheza angalau mara 10 ndani ya masaa mawili unapopumzika kwa ubavu wa kushoto."
      },
      "nutrition": {
        "keywords": ["chakula", "lishe", "mboga", "chuma", "food"],
        "response": "🥗 LISHE BORA: Kula mboga za kijani kibichi (dodo, mchicha), maharagwe, mayai, na unywe vidonge vya Iron kila siku."
      },
      "visits": {
        "keywords": ["kliniki", "hospitali", "anc"],
        "response": "🏥 KLINIKI (ANC): Hudhuria kliniki angalau mara 4. Piga *920# bure kupata tarehe yako."
      }
    },
    "default": "Asante sana mama! Afya yako ndiyo kipaumbele chetu. Uliza kuhusu dalili za hatari, mateke ya mtoto, au piga simu kwa +256 778 501 066."
  }
}"""

# New Clean, Breathable, Uncrowded HTML Template
clean_html = f'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>BabyHealth Guard — Digital Maternal & Newborn Care</title>
  <meta name="description" content="Simple, offline-first maternal health monitoring for Uganda. 10 local languages, 2G USSD (*920#), and clinical triage.">
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
            body: ['"Inter"', 'sans-serif'],
          }},
          colors: {{
            brand: {{
              50: '#ecfeff',
              100: '#cffafe',
              600: '#0891b2',
              700: '#0e7490',
              800: '#155e75',
              900: '#164e63',
              dark: '#08232c',
            }}
          }}
        }}
      }}
    }}
  </script>
  <style>
    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
    }}
    .material-symbols-outlined {{
      vertical-align: middle;
      font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
    }}
  </style>
</head>
<body class="bg-slate-50/50 text-slate-800 antialiased selection:bg-cyan-100 selection:text-cyan-900 flex flex-col min-h-screen">

  <!-- ========================================================================= -->
  <!-- 1. SLIM TOP EMERGENCY STRIP                                               -->
  <!-- ========================================================================= -->
  <div class="bg-[#08232c] text-white text-[11px] py-2 px-4 border-b border-cyan-900/50">
    <div class="max-w-6xl mx-auto flex flex-wrap items-center justify-between gap-2">
      <div class="flex items-center gap-2">
        <span class="w-2 h-2 rounded-full bg-rose-500 animate-pulse"></span>
        <span>24/7 Maternal Helpline: <a href="tel:112" class="font-bold underline text-rose-300">112</a> &amp; <a href="tel:0800100200" class="font-bold underline text-amber-300">0800 100 200</a></span>
        <span class="text-slate-400 hidden sm:inline">•</span>
        <span class="text-cyan-200 hidden sm:inline">Zero-Data USSD: <strong>*920#</strong></span>
      </div>
      <div class="flex items-center gap-4 text-xs font-semibold">
        <a href="https://wa.me/256778501066" target="_blank" class="text-emerald-400 hover:text-white transition-colors flex items-center gap-1">
          <span>WhatsApp: +256 778 501 066</span>
        </a>
        <a href="mailto:infor@babyguard.org" class="text-slate-300 hover:text-white hidden md:inline">infor@babyguard.org</a>
      </div>
    </div>
  </div>

  <!-- ========================================================================= -->
  <!-- 2. MINIMALIST CLEAN NAVBAR                                                -->
  <!-- ========================================================================= -->
  <header class="sticky top-0 z-40 bg-white/90 backdrop-blur-md border-b border-slate-200/80">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 h-18 flex items-center justify-between gap-4">
      
      <!-- Brand -->
      <a href="/" class="flex items-center gap-3 group">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-[#08232c] to-[#0e7490] text-white flex items-center justify-center shadow-md">
          <span class="material-symbols-outlined text-[22px]">health_and_safety</span>
        </div>
        <div class="flex flex-col">
          <span class="font-extrabold text-base sm:text-lg tracking-tight text-slate-900 leading-tight">
            BabyHealth Guard
          </span>
          <span class="text-[10px] font-bold text-[#0e7490] tracking-wider uppercase">
            Maternal Care • Uganda
          </span>
        </div>
      </a>

      <!-- Simple Nav -->
      <nav class="hidden md:flex items-center gap-6 text-xs font-semibold text-slate-600">
        <a href="#features" class="hover:text-[#0e7490] transition-colors">How It Works</a>
        <a href="#ussd" class="hover:text-[#0e7490] transition-colors">USSD *920#</a>
        <a href="#device-suite" class="hover:text-[#0e7490] transition-colors">Device Modes</a>
        <a href="#contact" class="hover:text-[#0e7490] transition-colors">Contact</a>
      </nav>

      <!-- Action Buttons -->
      <div class="flex items-center gap-2.5">
        <!-- AI Assistant Drawer Trigger Button -->
        <button onclick="openAiSideDrawer()" class="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-cyan-50 hover:bg-cyan-100 text-[#0e7490] font-bold text-xs border border-cyan-200 shadow-xs transition-all active:scale-95">
          <span class="material-symbols-outlined text-[16px]">auto_awesome</span>
          <span>Ask AI (10 Dialects)</span>
        </button>

        <!-- Dashboard -->
        <a href="/frontend/index.html" class="inline-flex items-center gap-1.5 px-4 py-2 rounded-xl bg-[#0e7490] hover:bg-[#08232c] text-white font-bold text-xs shadow-xs transition-all active:scale-95">
          <span class="material-symbols-outlined text-[16px]">monitor_heart</span>
          <span class="hidden sm:inline">Midwife</span> Dashboard
        </a>
      </div>

    </div>
  </header>

  <!-- ========================================================================= -->
  <!-- 3. CALM, SERENE HERO (BREATHABLE & FOCUSED)                                -->
  <!-- ========================================================================= -->
  <section class="py-12 sm:py-20 bg-gradient-to-b from-white via-slate-50 to-white border-b border-slate-200/60">
    <div class="max-w-6xl mx-auto px-4 sm:px-6">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
        
        <!-- Left Text: Clear, Concise, Not Wordy -->
        <div class="lg:col-span-6 flex flex-col items-start text-left">
          
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-cyan-50 border border-cyan-200 text-[#0e7490] font-bold text-xs mb-4">
            <span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
            <span>Digital Maternal Health Platform</span>
          </div>

          <h1 class="text-3xl sm:text-5xl font-extrabold text-slate-900 tracking-tight leading-[1.18] mb-4">
            Safe Motherhood, <br><span class="text-[#0e7490]">Every Step of the Way.</span>
          </h1>

          <p class="text-slate-600 text-sm sm:text-base leading-relaxed mb-7 max-w-lg">
            Empowering rural mothers and community midwives across Uganda with offline health tracking, instant emergency danger alerts, and zero-internet access via <strong class="text-slate-900 bg-slate-100 px-1.5 py-0.5 rounded font-bold">*920#</strong>.
          </p>

          <!-- 2 Action Buttons -->
          <div class="flex flex-wrap items-center gap-3 w-full sm:w-auto mb-8">
            <a href="/frontend/index.html" class="inline-flex items-center justify-center gap-2 px-5 py-3 rounded-xl bg-[#0e7490] hover:bg-[#0c627a] text-white font-bold text-xs sm:text-sm shadow-md shadow-cyan-900/15 transition-all active:scale-95">
              <span class="material-symbols-outlined text-[18px]">stethoscope</span>
              <span>Open Staff Dashboard</span>
            </a>
            
            <button onclick="openAiSideDrawer()" class="inline-flex items-center justify-center gap-2 px-5 py-3 rounded-xl bg-white hover:bg-slate-50 text-slate-800 font-bold text-xs sm:text-sm border border-slate-200 shadow-xs transition-all active:scale-95">
              <span class="material-symbols-outlined text-[18px] text-[#0e7490]">auto_awesome</span>
              <span>Open MaamaCare AI (Side Panel)</span>
            </button>
          </div>

          <!-- 4 Clean Key Metrics -->
          <div class="grid grid-cols-4 gap-4 w-full pt-4 border-t border-slate-200">
            <div>
              <span class="text-lg sm:text-xl font-extrabold text-slate-900 block">100%</span>
              <span class="text-[11px] text-slate-500">Offline App</span>
            </div>
            <div>
              <span class="text-lg sm:text-xl font-extrabold text-[#0e7490] block">10</span>
              <span class="text-[11px] text-slate-500">Ugandan Dialects</span>
            </div>
            <div>
              <span class="text-lg sm:text-xl font-extrabold text-slate-900 block">*920#</span>
              <span class="text-[11px] text-slate-500">Free 2G USSD</span>
            </div>
            <div>
              <span class="text-lg sm:text-xl font-extrabold text-emerald-600 block">4 ANC</span>
              <span class="text-[11px] text-slate-500">Visits Ensured</span>
            </div>
          </div>

        </div>

        <!-- Right: Single, Clean, Authentic Photo Card (No Chaos) -->
        <div class="lg:col-span-6 flex justify-center">
          <div class="relative w-full max-w-md rounded-3xl overflow-hidden shadow-xl border-4 border-white bg-slate-900 aspect-[4/3] group">
            <img src="https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?auto=format&fit=crop&w=800&q=80" 
                 onerror="this.onerror=null; this.src='/assets/images/mother_baby_hero.svg';" 
                 alt="Mother and Child" 
                 class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500">
            <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-transparent to-transparent"></div>
            
            <!-- Minimal, Clean Floating Overlay Tag -->
            <div class="absolute bottom-4 left-4 right-4 bg-white/95 backdrop-blur-md rounded-2xl p-3.5 shadow-md flex items-center justify-between text-slate-900">
              <div class="flex items-center gap-3">
                <div class="w-9 h-9 rounded-xl bg-emerald-50 text-emerald-700 flex items-center justify-center font-bold text-sm">
                  ✓
                </div>
                <div>
                  <h4 class="font-bold text-xs">Healthy Maternal Progress</h4>
                  <p class="text-[11px] text-slate-500">BP 118/76 • 11 Baby Kicks Logged</p>
                </div>
              </div>
              <span class="text-[10px] font-bold text-[#0e7490] bg-cyan-50 px-2 py-1 rounded-lg">
                Week 32
              </span>
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 4. 3 SIMPLE PILLARS (HOW IT WORKS — CRISP & UNCLUTTERED)                  -->
  <!-- ========================================================================= -->
  <section id="features" class="py-16 bg-white border-b border-slate-200/60">
    <div class="max-w-6xl mx-auto px-4 sm:px-6">
      
      <div class="text-center max-w-xl mx-auto mb-12">
        <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 tracking-tight mb-2">
          How BabyHealth Guard Works
        </h2>
        <p class="text-slate-600 text-xs sm:text-sm">
          A seamless digital ecosystem connecting rural homes to health centers.
        </p>
      </div>

      <!-- 3 Clean Feature Cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        
        <!-- Pillar 1 -->
        <div class="p-6 rounded-2xl bg-slate-50 border border-slate-200/80 hover:border-cyan-400 transition-all">
          <div class="w-10 h-10 rounded-xl bg-[#0e7490] text-white flex items-center justify-center mb-4">
            <span class="material-symbols-outlined text-[22px]">pregnant_woman</span>
          </div>
          <h3 class="font-bold text-base text-slate-900 mb-2">1. Offline Mobile Tracking</h3>
          <p class="text-xs text-slate-600 leading-relaxed mb-4">
            Mothers and village health workers record blood pressure, fetal kicks, and weight even when completely offline. Data syncs automatically once in connectivity.
          </p>
          <a href="/mobile/dashboard_preview.html" class="text-xs font-bold text-[#0e7490] hover:underline flex items-center gap-1">
            Preview Mother App →
          </a>
        </div>

        <!-- Pillar 2 -->
        <div class="p-6 rounded-2xl bg-slate-50 border border-slate-200/80 hover:border-rose-400 transition-all">
          <div class="w-10 h-10 rounded-xl bg-rose-600 text-white flex items-center justify-center mb-4">
            <span class="material-symbols-outlined text-[22px]">emergency</span>
          </div>
          <h3 class="font-bold text-base text-slate-900 mb-2">2. Emergency Danger Alerts</h3>
          <p class="text-xs text-slate-600 leading-relaxed mb-4">
            Immediate symptom triage flags complications like vaginal bleeding or severe preeclampsia headaches with direct 112 hotlines and WhatsApp midwife response.
          </p>
          <a href="/mobile/danger_signs_preview.html" class="text-xs font-bold text-rose-600 hover:underline flex items-center gap-1">
            Danger Signs Guide →
          </a>
        </div>

        <!-- Pillar 3 -->
        <div class="p-6 rounded-2xl bg-slate-50 border border-slate-200/80 hover:border-emerald-400 transition-all">
          <div class="w-10 h-10 rounded-xl bg-emerald-600 text-white flex items-center justify-center mb-4">
            <span class="material-symbols-outlined text-[22px]">dialpad</span>
          </div>
          <h3 class="font-bold text-base text-slate-900 mb-2">3. Zero-Data USSD (*920#)</h3>
          <p class="text-xs text-slate-600 leading-relaxed mb-4">
            Inclusive access on 2G button phones (MTN &amp; Airtel). Mothers receive clinic visit reminders and check in without needing internet or smartphones.
          </p>
          <a href="#ussd" class="text-xs font-bold text-emerald-700 hover:underline flex items-center gap-1">
            USSD Dial Guide →
          </a>
        </div>

      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 5. STREAMLINED USSD STRIP (*920#)                                         -->
  <!-- ========================================================================= -->
  <section id="ussd" class="py-12 bg-gradient-to-r from-[#08232c] via-[#0c404f] to-[#0e7490] text-white">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 flex flex-col md:flex-row items-center justify-between gap-6">
      <div>
        <span class="px-2.5 py-1 rounded-full bg-white/10 text-cyan-200 text-[10px] font-bold uppercase tracking-wider mb-2 inline-block">
          Rural Telecom Access
        </span>
        <h3 class="text-xl sm:text-2xl font-extrabold mb-1">
          Dial <span class="text-amber-300 font-mono">*920#</span> from Any Phone
        </h3>
        <p class="text-xs sm:text-sm text-cyan-100 max-w-xl">
          Free remote pregnancy registration, next ANC appointment date, and emergency midwife dispatch across Uganda. Zero mobile data needed.
        </p>
      </div>
      <div class="flex items-center gap-3">
        <a href="https://wa.me/256778501066?text=Hello%20BabyHealth%20Guard%2C%20inquiry%20about%20USSD%20service." target="_blank" class="px-4 py-2.5 rounded-xl bg-white text-slate-900 font-bold text-xs hover:bg-cyan-50 transition-colors shadow-sm">
          Contact USSD Team
        </a>
      </div>
    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 6. CLEAN MULTI-DEVICE SHORTCUTS BAR                                       -->
  <!-- ========================================================================= -->
  <section id="device-suite" class="py-14 bg-slate-50 border-b border-slate-200/80">
    <div class="max-w-6xl mx-auto px-4 sm:px-6">
      
      <div class="flex flex-col md:flex-row items-center justify-between gap-6 pb-6 border-b border-slate-200">
        <div>
          <h3 class="text-lg font-bold text-slate-900">Responsive Across All Screens</h3>
          <p class="text-xs text-slate-500">Adapts automatically to Android Studio emulators, tablets, and wide laptop browsers.</p>
        </div>
        <div class="flex flex-wrap items-center gap-2">
          <a href="/frontend/index.html" class="px-3.5 py-2 rounded-xl bg-white hover:bg-slate-100 text-slate-800 text-xs font-bold border border-slate-200 transition-colors">
            💻 Laptop (Clinical Dashboard)
          </a>
          <a href="/mobile/dashboard_preview.html" class="px-3.5 py-2 rounded-xl bg-white hover:bg-slate-100 text-slate-800 text-xs font-bold border border-slate-200 transition-colors">
            📱 Tablet / Mobile (Mother Flow)
          </a>
          <a href="/mobile/welcome_preview.html" class="px-3.5 py-2 rounded-xl bg-white hover:bg-slate-100 text-slate-800 text-xs font-bold border border-slate-200 transition-colors">
            ✨ Onboarding Screen
          </a>
        </div>
      </div>

    </div>
  </section>

  <!-- ========================================================================= -->
  <!-- 7. INSTITUTIONAL FOOTER WITH VERIFIED CONTACTS                            -->
  <!-- ========================================================================= -->
  <footer id="contact" class="bg-[#08232c] text-white pt-12 pb-10 border-t border-cyan-900/40">
    <div class="max-w-6xl mx-auto px-4 sm:px-6">
      
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8 pb-10 border-b border-slate-800 text-xs">
        
        <!-- Col 1: Brand -->
        <div class="space-y-3">
          <div class="flex items-center gap-2.5">
            <div class="w-8 h-8 rounded-lg bg-[#0e7490] text-white flex items-center justify-center font-bold">
              <span class="material-symbols-outlined text-[18px]">health_and_safety</span>
            </div>
            <span class="font-extrabold text-sm text-white">BabyHealth Guard</span>
          </div>
          <p class="text-slate-400 leading-relaxed">
            Digital Maternal &amp; Newborn Healthcare Platform. Uganda Ministry of Health Guidelines Compliant.
          </p>
          <div class="text-[11px] text-slate-400 flex items-center gap-1.5">
            <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
            <span>Platform Status: <strong>Operational</strong></span>
          </div>
        </div>

        <!-- Col 2: Navigation -->
        <div>
          <h4 class="font-bold text-cyan-300 uppercase tracking-wider text-[11px] mb-3">System Access</h4>
          <ul class="space-y-2 text-slate-300">
            <li><a href="/frontend/index.html" class="hover:text-cyan-200">Midwife Web Dashboard</a></li>
            <li><a href="/mobile/dashboard_preview.html" class="hover:text-cyan-200">Mother Care Dashboard</a></li>
            <li><a href="/mobile/danger_signs_preview.html" class="hover:text-cyan-200">Danger Signs Checklist</a></li>
            <li><a href="#ussd" class="hover:text-cyan-200">USSD *920# Gateway</a></li>
          </ul>
        </div>

        <!-- Col 3: Emergency -->
        <div>
          <h4 class="font-bold text-rose-300 uppercase tracking-wider text-[11px] mb-3">Emergency Hotlines</h4>
          <ul class="space-y-2 text-slate-300">
            <li><a href="tel:112" class="text-rose-400 font-bold hover:underline">Police &amp; Ambulance: 112</a></li>
            <li><a href="tel:0800100200" class="text-amber-300 font-bold hover:underline">Toll-Free Helpline: 0800 100 200</a></li>
            <li><a href="https://wa.me/256778501066" target="_blank" class="text-emerald-400 font-bold hover:underline">WhatsApp Direct Support</a></li>
          </ul>
        </div>

        <!-- Col 4: Contacts & Socials -->
        <div>
          <h4 class="font-bold text-cyan-300 uppercase tracking-wider text-[11px] mb-3">Contact Us</h4>
          <div class="space-y-2 text-slate-300 mb-4">
            <div>
              <span class="text-slate-400 block text-[10px]">Direct Phone:</span>
              <a href="tel:+256778501066" class="text-white font-bold hover:underline">+256 778 501 066</a>
            </div>
            <div>
              <span class="text-slate-400 block text-[10px]">Official Email:</span>
              <a href="mailto:infor@babyguard.org" class="text-cyan-200 font-semibold hover:underline">infor@babyguard.org</a>
            </div>
          </div>
          
          <!-- Social Icons -->
          <div class="flex items-center gap-2 pt-1">
            <a href="https://wa.me/256778501066" target="_blank" title="WhatsApp" class="w-7 h-7 rounded-lg bg-emerald-600/30 hover:bg-emerald-500 text-emerald-300 hover:text-white flex items-center justify-center transition-colors">
              <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.598 2.664-.698c.969.585 1.961.949 2.796.949 3.181 0 5.767-2.586 5.768-5.766.001-3.18-2.585-5.736-5.768-5.736zm0-1.872c4.225 0 7.639 3.414 7.639 7.638 0 4.225-3.414 7.639-7.639 7.639-.995 0-1.95-.194-2.825-.548l-4.706 1.233 1.258-4.597c-.439-.958-.667-2.008-.667-3.727 0-4.224 3.414-7.638 7.639-7.638zm0 0"/></svg>
            </a>
            <a href="https://www.tiktok.com/@babyhealthguard" target="_blank" title="TikTok" class="w-7 h-7 rounded-lg bg-white/10 hover:bg-[#ff0050] text-slate-200 hover:text-white flex items-center justify-center transition-colors">
              <svg class="w-3.5 h-3.5 fill-current" viewBox="0 0 24 24"><path d="M19.589 6.686a4.793 4.793 0 0 1-3.77-4.245V2h-3.445v13.672a2.896 2.896 0 0 1-2.901 2.89 2.896 2.896 0 0 1-2.892-2.89 2.896 2.896 0 0 1 2.892-2.891c.334 0 .653.055.952.153V9.45a6.34 6.34 0 0 0-.952-.072 6.335 6.335 0 0 0-6.336 6.336 6.335 6.335 0 0 0 6.336 6.336 6.335 6.335 0 0 0 6.336-6.336V8.653a8.163 8.163 0 0 0 4.78 1.528V6.735a4.797 4.797 0 0 1-1-.049z"/></svg>
            </a>
            <a href="https://x.com/babyhealthguard" target="_blank" title="X (Twitter)" class="w-7 h-7 rounded-lg bg-white/10 hover:bg-black text-slate-200 hover:text-white flex items-center justify-center transition-colors">
              <svg class="w-3 h-3 fill-current" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
            </a>
          </div>
        </div>

      </div>

      <div class="pt-6 flex flex-col sm:flex-row items-center justify-between gap-3 text-[11px] text-slate-400">
        <p>© 2026 BabyHealth Guard. All rights reserved.</p>
        <p>Medical Decision Support System • Ministry of Health Compliant</p>
      </div>

    </div>
  </footer>

  <!-- ========================================================================= -->
  <!-- 8. PERMANENT SIDE FLOATING TRIGGER BUTTON (AT THE SIDE)                   -->
  <!-- ========================================================================= -->
  <button onclick="openAiSideDrawer()" aria-label="Open MaamaCare AI Assistant" class="fixed top-1/2 right-0 -translate-y-1/2 z-40 bg-[#0e7490] hover:bg-[#08232c] text-white py-3 px-3 rounded-l-2xl shadow-2xl flex flex-col items-center gap-1.5 transition-all hover:pr-4 group active:scale-95 border-l-2 border-y-2 border-cyan-400/30">
    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
    <span class="material-symbols-outlined text-[20px]">auto_awesome</span>
    <span class="text-[10px] font-extrabold uppercase tracking-widest [writing-mode:vertical-rl] rotate-180">
      MaamaCare AI
    </span>
  </button>

  <!-- Bottom Floating Chat Pill Shortcut -->
  <div class="fixed bottom-6 right-6 z-40 flex items-center gap-2">
    <button onclick="openAiSideDrawer()" class="flex items-center gap-2 px-4 py-3 rounded-full bg-[#0e7490] hover:bg-[#08232c] text-white font-bold text-xs sm:text-sm shadow-xl shadow-cyan-900/25 transition-all active:scale-95">
      <span class="material-symbols-outlined text-[18px]">auto_awesome</span>
      <span>MaamaCare AI (10 Dialects)</span>
    </button>
    <a href="https://wa.me/256778501066?text=Hello%20BabyHealth%20Guard%2C%20I%20need%20assistance." target="_blank" class="w-11 h-11 rounded-full bg-emerald-500 hover:bg-emerald-600 text-white flex items-center justify-center shadow-lg transition-transform active:scale-95">
      <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.598 2.664-.698c.969.585 1.961.949 2.796.949 3.181 0 5.767-2.586 5.768-5.766.001-3.18-2.585-5.736-5.768-5.736zm0-1.872c4.225 0 7.639 3.414 7.639 7.638 0 4.225-3.414 7.639-7.639 7.639-.995 0-1.95-.194-2.825-.548l-4.706 1.233 1.258-4.597c-.439-.958-.667-2.008-.667-3.727 0-4.224 3.414-7.638 7.639-7.638zm0 0"/></svg>
    </a>
  </div>

  <!-- ========================================================================= -->
  <!-- 9. AI ASSISTANT SLIDE-OVER DRAWER (AT THE SIDE)                           -->
  <!-- ========================================================================= -->
  <!-- Backdrop Overlay -->
  <div id="aiSideDrawerBackdrop" onclick="closeAiSideDrawer()" class="fixed inset-0 bg-slate-900/50 backdrop-blur-xs z-50 hidden transition-opacity duration-300"></div>

  <!-- Side Drawer Container -->
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
      <button onclick="closeAiSideDrawer()" class="w-8 h-8 rounded-lg bg-white/10 hover:bg-white/20 flex items-center justify-center text-white transition-colors">
        <span class="material-symbols-outlined text-[20px]">close</span>
      </button>
    </div>

    <!-- Language Selector Dropdown in Drawer -->
    <div class="p-3 bg-slate-50 border-b border-slate-200 flex items-center justify-between text-xs shrink-0">
      <span class="font-bold text-slate-700">Choose Language:</span>
      <select onchange="switchLanguage(this.value)" id="drawerLangSelect" class="bg-white text-slate-900 font-bold text-xs rounded-xl px-2.5 py-1.5 border border-slate-300 focus:outline-hidden focus:ring-2 focus:ring-[#0e7490]">
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
      <!-- Bubbles populated by JS -->
    </div>

    <!-- Quick Question Chips -->
    <div id="drawerQuickChips" class="px-3.5 py-2.5 bg-white border-t border-slate-100 flex flex-wrap gap-1.5 shrink-0">
      <!-- Chips populated by JS -->
    </div>

    <!-- Input Bar -->
    <div class="p-3 bg-white border-t border-slate-200 shrink-0">
      <form onsubmit="handleDrawerChatSubmit(event)" class="flex items-center gap-2">
        <button type="button" onclick="startVoiceInput()" id="drawerMicBtn" title="Speak via microphone" class="w-9 h-9 rounded-xl bg-slate-100 hover:bg-cyan-50 text-slate-700 hover:text-[#0e7490] border border-slate-200 flex items-center justify-center shrink-0 transition-colors">
          <span class="material-symbols-outlined text-[18px]">mic</span>
        </button>
        <input type="text" id="drawerChatInput" placeholder="Buuza ekibuuzo..." class="flex-1 bg-slate-50 text-xs px-3.5 py-2 rounded-xl border border-slate-200 focus:outline-hidden focus:ring-1 focus:ring-[#0e7490]">
        <button type="submit" class="px-3.5 py-2 rounded-xl bg-[#0e7490] hover:bg-[#08232c] text-white font-bold text-xs flex items-center justify-center shrink-0 transition-colors">
          <span class="material-symbols-outlined text-[16px]">send</span>
        </button>
      </form>
      <div class="mt-2 flex items-center justify-between text-[10px] text-slate-400 px-1">
        <span>🔊 Tap "Listen" to hear spoken pronunciation</span>
        <a href="https://wa.me/256778501066" target="_blank" class="text-emerald-600 font-bold hover:underline">WhatsApp Help</a>
      </div>
    </div>

  </aside>

  <!-- ========================================================================= -->
  <!-- 10. JAVASCRIPT CORE LOGIC                                                 -->
  <!-- ========================================================================= -->
  <script>
    const LANGUAGES = {LANGUAGES_JSON};
    let currentLang = 'luganda';

    document.addEventListener('DOMContentLoaded', () => {{
      initDrawerChat();
    }});

    // Drawer Open/Close Logic
    function openAiSideDrawer() {{
      const drawer = document.getElementById('aiSideDrawer');
      const backdrop = document.getElementById('aiSideDrawerBackdrop');
      backdrop.classList.remove('hidden');
      setTimeout(() => drawer.classList.remove('translate-x-full'), 10);
    }}

    function closeAiSideDrawer() {{
      const drawer = document.getElementById('aiSideDrawer');
      const backdrop = document.getElementById('aiSideDrawerBackdrop');
      drawer.classList.add('translate-x-full');
      setTimeout(() => backdrop.classList.add('hidden'), 300);
      if ('speechSynthesis' in window) window.speechSynthesis.cancel();
    }}

    function switchLanguage(langKey) {{
      if (!LANGUAGES[langKey]) return;
      currentLang = langKey;
      
      const langData = LANGUAGES[langKey];
      document.getElementById('drawerDialectBadge').textContent = `${{langData.name}} Active • Audio Spoken`;
      document.getElementById('drawerChatInput').placeholder = langData.placeholder;
      document.getElementById('drawerLangSelect').value = langKey;

      initDrawerChat();
    }}

    function initDrawerChat() {{
      const langData = LANGUAGES[currentLang];
      const container = document.getElementById('drawerChatMessages');
      
      const greetingHtml = `
        <div class="flex items-start gap-2.5">
          <div class="w-7 h-7 rounded-lg bg-gradient-to-tr from-cyan-600 to-teal-500 text-white flex items-center justify-center text-xs shrink-0 shadow-xs">
            🤱
          </div>
          <div class="bg-white rounded-2xl rounded-tl-none p-3 shadow-xs border border-slate-200 text-xs text-slate-800 leading-relaxed max-w-[85%]">
            <span class="font-bold text-[#0e7490] block mb-1">${{langData.name}}</span>
            <p>${{langData.greeting}}</p>
            <div class="mt-2.5 pt-1.5 border-t border-slate-100 flex items-center justify-between text-[11px]">
              <button type="button" onclick="speakCurrentText('${{escapeQuotes(langData.greeting)}}', '${{currentLang}}')" class="inline-flex items-center gap-1 font-bold text-[#0e7490] hover:text-cyan-800">
                <span class="material-symbols-outlined text-[15px]">volume_up</span>
                <span>${{langData.listenText}}</span>
              </button>
            </div>
          </div>
        </div>
      `;
      container.innerHTML = greetingHtml;

      // Populate Quick Chips
      const chipsBox = document.getElementById('drawerQuickChips');
      chipsBox.innerHTML = '';
      langData.quickChips.forEach(chip => {{
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'px-2.5 py-1 rounded-full bg-slate-100 hover:bg-cyan-50 hover:text-[#0e7490] text-slate-700 text-[11px] font-medium border border-slate-200 transition-colors';
        btn.textContent = chip;
        btn.onclick = () => {{
          document.getElementById('drawerChatInput').value = chip;
          processDrawerMessage(chip);
        }};
        chipsBox.appendChild(btn);
      }});
    }}

    function handleDrawerChatSubmit(e) {{
      e.preventDefault();
      const input = document.getElementById('drawerChatInput');
      const text = input.value.trim();
      if (!text) return;
      processDrawerMessage(text);
      input.value = '';
    }}

    function processDrawerMessage(text) {{
      const container = document.getElementById('drawerChatMessages');
      
      // User Bubble
      const userBubble = `
        <div class="flex items-start justify-end gap-2">
          <div class="bg-[#0e7490] text-white rounded-2xl rounded-tr-none p-3 shadow-xs text-xs leading-relaxed max-w-[85%]">
            <p>${{text}}</p>
          </div>
          <div class="w-7 h-7 rounded-lg bg-slate-800 text-white flex items-center justify-center text-xs shrink-0">
            👤
          </div>
        </div>
      `;
      container.insertAdjacentHTML('beforeend', userBubble);
      container.scrollTop = container.scrollHeight;

      // AI Response
      setTimeout(() => {{
        const responseText = matchMedicalResponse(text, currentLang);
        const langData = LANGUAGES[currentLang];
        
        const aiBubble = `
          <div class="flex items-start gap-2.5">
            <div class="w-7 h-7 rounded-lg bg-gradient-to-tr from-cyan-600 to-teal-500 text-white flex items-center justify-center text-xs shrink-0 shadow-xs">
              🤱
            </div>
            <div class="bg-white rounded-2xl rounded-tl-none p-3 shadow-xs border border-slate-200 text-xs text-slate-800 leading-relaxed max-w-[85%]">
              <span class="font-bold text-[#0e7490] block mb-1">${{langData.name}}</span>
              <p>${{responseText}}</p>
              <div class="mt-2.5 pt-1.5 border-t border-slate-100 flex items-center justify-between text-[11px]">
                <button type="button" onclick="speakCurrentText('${{escapeQuotes(responseText)}}', '${{currentLang}}')" class="inline-flex items-center gap-1 font-bold text-[#0e7490] hover:text-cyan-800">
                  <span class="material-symbols-outlined text-[15px]">volume_up</span>
                  <span>${{langData.listenText}}</span>
                </button>
                <a href="https://wa.me/256778501066?text=${{encodeURIComponent('MaamaCare AI consultation: ' + text)}}" target="_blank" class="text-[10px] font-bold text-emerald-600 hover:underline">
                  Midwife WhatsApp →
                </a>
              </div>
            </div>
          </div>
        `;
        container.insertAdjacentHTML('beforeend', aiBubble);
        container.scrollTop = container.scrollHeight;

        speakCurrentText(responseText, currentLang);
      }}, 350);
    }}

    function matchMedicalResponse(query, langKey) {{
      const langConfig = LANGUAGES[langKey] || LANGUAGES['luganda'];
      const q = query.toLowerCase();
      
      if (langConfig.intents) {{
        for (const [intentKey, intentData] of Object.entries(langConfig.intents)) {{
          if (intentData.keywords.some(k => q.includes(k.toLowerCase()))) {{
            return intentData.response;
          }}
        }}
      }}
      return langConfig.default;
    }}

    function speakCurrentText(text, langKey) {{
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
    }}

    function startVoiceInput() {{
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
      if (!SpeechRecognition) {{
        alert("Voice speech recognition is not supported in this browser. Please type your question.");
        return;
      }}
      const micBtn = document.getElementById('drawerMicBtn');
      micBtn.classList.add('bg-rose-100', 'text-rose-600', 'animate-pulse');
      
      const recognition = new SpeechRecognition();
      recognition.lang = 'en-UG';
      recognition.continuous = false;
      recognition.interimResults = false;

      recognition.onresult = function(event) {{
        const transcript = event.results[0][0].transcript;
        document.getElementById('drawerChatInput').value = transcript;
        processDrawerMessage(transcript);
      }};

      recognition.onerror = function() {{
        micBtn.classList.remove('bg-rose-100', 'text-rose-600', 'animate-pulse');
      }};

      recognition.onend = function() {{
        micBtn.classList.remove('bg-rose-100', 'text-rose-600', 'animate-pulse');
      }};

      recognition.start();
    }}

    function escapeQuotes(str) {{
      return str.replace(/'/g, "\\\\'").replace(/"/g, '&quot;').replace(/\\n/g, ' ');
    }}
  </script>

</body>
</html>
'''

output_path = r"C:\Users\Admin\BabyHealth-Guard\index.html"
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(clean_html)

print(f"Generated clean uncrowded landing page with side drawer at: {output_path}")
