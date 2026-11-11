import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:babyhealth_guard_mobile/features/onboarding/presentation/screens/welcome_screen.dart';

void main() {
  testWidgets('Welcome screen renders properly smoke test',
      (WidgetTester tester) async {
    await tester.pumpWidget(const MaterialApp(home: WelcomeScreen()));

    // Verify Welcome title and Get Started button text exist
    expect(find.text('Welcome to\nBabyHealth Guard'), findsOneWidget);
    expect(find.text('Get Started'), findsOneWidget);
    expect(find.text('Secure care records'), findsOneWidget);
    expect(find.text('Already have an account? Sign in'), findsOneWidget);
  });
}
