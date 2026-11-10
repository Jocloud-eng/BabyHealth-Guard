# BabyHealth Guard — Mobile App (Mother's Interface)

This Flutter mobile application is designed for **BabyHealth Guard** to support pregnant women and new mothers—especially in rural and low-connectivity environments. It features an offline-first architecture, clean UI with warm pastel gradients, quick health monitoring, clinic appointment tracking, and fallback USSD (`*920#`) access.

---

## 📱 Welcome & Onboarding Screen (Screen 1)

The first screen welcomes the mother into the care ecosystem with:

- **Ambient Background**: Soft vertical pastel gradient (`#FAF8FF` → `#F2F3FF` → `#EAEDFF`) accented with top-right and mid-left blurred pastel glow orbs.
- **Header & Typography**: Clean, high-contrast headline using *Plus Jakarta Sans* (`Welcome to BabyHealth Guard`) with warm subtext explaining simple monitoring and midwife care.
- **Hero Visual Card**: Soft rounded portrait (`borderRadius: 36`) with an 80% opacity white border, organic warm shadow (`#D7B28E`), and gentle bottom gradient blending. Includes an artistic offline-ready fallback when running without internet.
- **Interactive "Get Started" Pill Button**:
  - Signature Teal (`#0E7490`) circular indicator with an arrow icon.
  - Centered bold label (`Get Started`).
  - Animated trailing triple chevron shimmer (`>>>`) with smooth slide transitions.
  - Scale bounce animation on touch feedback.
- **Rural Accessibility Indicator**:
  - Pulsing emerald green dot (`Works offline`).
  - Free USSD shortcut tag (`Free *920# access`).
  - Native iOS/Android home bar indicator.

---

## 📁 Project Architecture

```
mobile/
├── pubspec.yaml                     # Dependencies (google_fonts, cupertino_icons)
├── analysis_options.yaml            # Linting and best practices
├── welcome_preview.html             # Standalone web preview of the Welcome screen
├── assets/
│   └── images/                      # App icons and imagery
└── lib/
    ├── main.dart                    # Entry point & edge-to-edge system UI styling
    ├── core/
    │   └── theme/
    │       ├── app_colors.dart      # Color tokens (Teal, Stone, Sand, Pastel glows)
    │       └── app_theme.dart       # Material3 typography & theme configuration
    └── features/
        ├── onboarding/
        │   └── presentation/
        │       ├── screens/
        │       │   └── welcome_screen.dart           # The first screen
        │       └── widgets/
        │           ├── ambient_background.dart       # Backdrop glow & gradient
        │           ├── hero_image_card.dart          # Rounded hero card & fallback
        │           ├── get_started_button.dart       # Interactive pill button & chevrons
        │           └── offline_indicator_bar.dart    # USSD & offline status widget
        └── auth/
            └── presentation/
                └── screens/
                    └── mother_registration_screen.dart # Registration & profile setup
        └── dashboard/
            └── presentation/
                └── screens/
                    └── mother_dashboard_screen.dart    # Mother's care dashboard (Screen 3)
```

---

## 📱 Mother's Flow & Screens

1. **Welcome Screen** ([`welcome_screen.dart`](file:///home/joanitah/BabyHealth%20Guard/BabyHealth-Guard/mobile/lib/features/onboarding/presentation/screens/welcome_screen.dart) / [`welcome_preview.html`](file:///home/joanitah/BabyHealth%20Guard/BabyHealth-Guard/mobile/welcome_preview.html)):
   - Pastel ambient backdrop, hero card, interactive "Get Started" slider, rural offline/USSD indicators.
2. **Registration Screen** ([`mother_registration_screen.dart`](file:///home/joanitah/BabyHealth%20Guard/BabyHealth-Guard/mobile/lib/features/auth/presentation/screens/mother_registration_screen.dart) / [`registration_preview.html`](file:///home/joanitah/BabyHealth%20Guard/BabyHealth-Guard/mobile/registration_preview.html)):
   - Photo picker, name, age, village, phone, language preference, trimester/stage, conditions.
3. **Mother Dashboard Screen** ([`mother_dashboard_screen.dart`](file:///home/joanitah/BabyHealth%20Guard/BabyHealth-Guard/mobile/lib/features/dashboard/presentation/screens/mother_dashboard_screen.dart) / [`dashboard_preview.html`](file:///home/joanitah/BabyHealth%20Guard/BabyHealth-Guard/mobile/dashboard_preview.html)):
   - **Hero Countdown Card**: Trimester badge, countdown due window, mother & baby photo.
   - **Assigned Care Midwife**: Direct call (`0800100200`) and SMS shortcuts to Sr. Sarah Omondi.
   - **Daily Health Checks**: Interactive Kick Counter (+ Log Kick), Blood Pressure monitor, and Iron & Folic daily toggle.
   - **Next ANC Visit**: Calendar countdown, facility details, and SMS confirmation status.
   - **Danger Signs & Emergency Dispatch**: Interactive danger signs checklist & toll-free `112` speed dial.
   - **Floating Bottom Navigation**: Quick switching between Home, Health, Warnings, and Visits.

4. **My Health Screen** ([`my_health_preview.html`](file:///home/joanitah/BabyHealth%20Guard/BabyHealth-Guard/mobile/my_health_preview.html)):
   - Today's vitals (Blood pressure `118/76`, interactive baby kick logger).
   - Care & Medication (Iron & Folic Acid toggle, Next clinic visit tracker).
   - Interactive `+ Record Today's Vitals` modal sheet.
5. **Danger Signs / Warnings Screen** ([`danger_signs_preview.html`](file:///home/joanitah/BabyHealth%20Guard/BabyHealth-Guard/mobile/danger_signs_preview.html)):
   - 24/7 Priority emergency header with pulsing indicator.
   - 4 large visual danger sign cards: Bleeding, Severe Headache, Baby Not Moving, and High Fever.
   - One-tap "Call Midwife Now (Free)" (`0800100200`) and fallback USSD (`*920#`) shortcut.

---

## 🚀 Running the App

### 1. Flutter Run (Mobile / Desktop / Web)
```bash
cd mobile
flutter pub get
flutter run
```

### 2. Immediate Web Previews (Interactive Flow)
Open any of the preview files in your browser:
- `mobile/welcome_preview.html` ➔ Click **Get Started** ➔
- `mobile/registration_preview.html` ➔ Complete profile & Click **Save & Continue** ➔
- `mobile/dashboard_preview.html` ➔ Switch between **Home**, **My Health**, and **Warning Signs** tabs!
- `mobile/my_health_preview.html` (Dedicated My Health view)
- `mobile/danger_signs_preview.html` (Dedicated Warning Signs view)
