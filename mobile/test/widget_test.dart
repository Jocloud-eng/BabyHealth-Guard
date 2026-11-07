import 'package:flutter_test/flutter_test.dart';
import 'package:babyhealth_guard_mobile/main.dart';

void main() {
  testWidgets('Welcome screen renders properly smoke test', (WidgetTester tester) async {
    // Build BabyHealth Guard app and trigger a frame.
    await tester.pumpWidget(const BabyHealthGuardApp());

    // Verify Welcome title and Get Started button text exist
    expect(find.text('Welcome to\nBabyHealth Guard'), findsOneWidget);
    expect(find.text('Get Started'), findsOneWidget);
    expect(find.text('Works offline'), findsOneWidget);
  });
}
