# BabyHealth Guard Mobile

Flutter app for maternal and newborn care. Screens are native Flutter widgets; the HTML previews have been removed. The mobile app uses Firebase Authentication and Cloud Firestore. Firestore local persistence is disabled, so an internet connection is required to sign in and view or save care records.

## Project layout

```text
mobile/
├── firestore.rules
├── pubspec.yaml
└── lib/
    ├── main.dart
    ├── firebase_options.dart
    ├── core/
    │   ├── constants/       # Colors and collection names
    │   ├── theme/           # Material 3 theme
    │   └── utils/           # Form validators
    └── features/
        ├── onboarding/presentation/
        ├── auth/
        │   ├── data/        # Firebase Authentication repository
        │   └── presentation/screens/
        ├── dashboard/
        │   ├── data/        # Firestore care-record repository
        │   ├── domain/      # Profile, vital, appointment, and log models
        │   └── presentation/screens/
        ├── health_tracking/presentation/screens/
        └── danger_signs/presentation/screens/
```

## Firebase setup

1. Configure the Android app in Firebase and provide its generated Android and Dart configuration files.
2. Enable Email/Password in Firebase Authentication and create the Cloud Firestore database.
3. From `mobile/`, deploy `firestore.rules` to the Firebase project before testing with real accounts.
4. Run `flutter pub get` and `flutter run`.

The app does not seed demo profiles, vitals, health logs, or appointments. Registration creates an auth account and a patient profile. Appointment documents are read-only to the mobile client and must be created by an authorized service or care-team workflow.

## Firestore data layout

- `users/{uid}`: patient profile fields such as name, age, village, phone, preferred language, maternal status, pregnancy stage, and conditions.
- `users/{uid}/dailyVitals/{yyyy-MM-dd}`: that day's blood pressure, kick count, and iron/folic status.
- `users/{uid}/healthLogs/{logId}`: append-only events for vital updates, kick counts, medication status, and reported danger signs.
- `users/{uid}/appointments/{appointmentId}`: scheduled clinic visits. The app reads these but cannot create or change them.

Firestore rules limit profile and health data access to the authenticated owner. Health records should be used only with correctly deployed Firebase rules; client-side checks are not a substitute for backend security.

## Run checks

```sh
flutter analyze
flutter test
```
