# BabyHealth Guard

Digital maternal and newborn health monitoring system (MVP).

## Backend (Java / Spring Boot)
- Java 21, Spring Boot 3.3, H2 (dev), JPA, JWT (HMAC), clean architecture + DDD.
- Run: `cd backend && mvn spring-boot:run` (offline: `mvn -o spring-boot:run`)
- API: http://localhost:8080  | H2 console: /h2-console
- Default admin: admin@babyhealth.local / admin123

## Frontend (Web dashboard)
- Served by backend at http://localhost:8080 (vanilla JS).
- Source: frontend/index.html

## Mobile
- Flutter app not scaffolded here (no SDK in environment). Planned: offline-first SQLite + sync to /api.

## Architecture
Modular monolith with domain/application/infrastructure/presentation layers. See proposal doc.
