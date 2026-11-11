# BabyHealth Guard

Digital maternal and newborn health monitoring system (MVP).

## Backend (Java / Spring Boot)
- Java 21, Spring Boot 3.3, H2 (dev), JPA, JWT (HMAC), clean architecture + DDD.
- Run: `cd backend && mvn spring-boot:run` (offline: `mvn -o spring-boot:run`)
- API: http://localhost:8080  | H2 console: /h2-console
- Local demo seed only: admin@babyhealth.local / admin123. Do not use demo credentials in production.

## Frontend (Web dashboard)
- Served by backend at http://localhost:8080 (vanilla JS).
- Source: frontend/index.html

## Mobile (Flutter)
- Native Flutter application for mothers located in `mobile/`, using Firebase Authentication and Cloud Firestore.
- Firestore offline persistence is disabled; internet access is required for account and health-record operations.
- See [`mobile/README.md`](mobile/README.md) for Firebase setup, data structure, and run instructions.
- Run: `cd mobile && flutter pub get && flutter run`.

## Architecture
Modular monolith with domain/application/infrastructure/presentation layers. See the project proposal and Software Requirements Specification in `documentation/`.
