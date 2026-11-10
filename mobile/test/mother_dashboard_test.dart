import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:babyhealth_guard_mobile/features/dashboard/presentation/screens/mother_dashboard_screen.dart';

void main() {
  testWidgets('MotherDashboardScreen renders profile, midwife and health checks',
      (WidgetTester tester) async {
    tester.view.physicalSize = const Size(1080, 2400);
    tester.view.devicePixelRatio = 1.0;
    addTearDown(tester.view.resetPhysicalSize);

    await tester.pumpWidget(
      const MaterialApp(
        home: MotherDashboardScreen(
          motherName: 'Amina Brenda',
          village: 'Kagando',
        ),
      ),
    );

    // Profile & Header checks
    expect(find.text('Amina Brenda'), findsOneWidget);
    expect(find.text('Kagando'), findsOneWidget);
    expect(find.text('Free USSD *920# Active'), findsOneWidget);

    // Midwife & ANC checks
    expect(find.text('Sr. Sarah Omondi'), findsOneWidget);
    expect(find.text('Bwera Health Centre III'), findsWidgets);

    // Health cards
    expect(find.text('10 kicks'), findsOneWidget);
    expect(find.text('118 / 76'), findsOneWidget);
    expect(find.text('Iron & Folic'), findsOneWidget);

    // Interactive Kick Counter: tap "+ Log Kick"
    await tester.tap(find.text('+ Log Kick'));
    await tester.pump();
    expect(find.text('11 kicks'), findsOneWidget);

    // Emergency action CTA
    expect(find.text('Emergency Call (Toll-Free 24/7)'), findsOneWidget);

    // Switch to "My Health" tab
    await tester.tap(find.text('My Health'));
    await tester.pumpAndSettle();

    // Verify "My Health" view elements
    expect(find.text("Today's Vitals"), findsOneWidget);
    expect(find.text('Blood Pressure'), findsOneWidget);
    expect(find.text('Baby Kicks'), findsOneWidget);
    expect(find.text('Care & Medication'), findsOneWidget);
    expect(find.text('Iron & Folic Acid'), findsOneWidget);
    expect(find.text("Next Clinic Visit"), findsOneWidget);
    expect(find.text("+ Record Today's Vitals"), findsOneWidget);

    // Switch to "Warning Signs" tab
    await tester.tap(find.text('Warning Signs'));
    await tester.pumpAndSettle();

    // Verify Danger Signs view elements
    expect(find.text('Danger Signs'), findsOneWidget);
    expect(find.text('Tap if you feel any of these'), findsOneWidget);
    expect(find.text('Bleeding'), findsOneWidget);
    expect(find.text('Severe Headache'), findsOneWidget);
    expect(find.text('Baby Not Moving'), findsOneWidget);
    expect(find.text('High Fever'), findsOneWidget);
    expect(find.text('Call Midwife Now (Free)'), findsOneWidget);
  });
}
