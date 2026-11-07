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
```

---

## 🚀 Running the App

### 1. Flutter Run (Mobile / Desktop / Web)
```bash
cd mobile
flutter pub get
flutter run
```

### 2. Immediate Web Preview
You can also open `mobile/welcome_preview.html` directly in any web browser to view and test the interactive design layout immediately.
