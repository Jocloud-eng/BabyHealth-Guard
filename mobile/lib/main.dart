import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'core/theme/app_theme.dart';
import 'features/auth/presentation/screens/mother_registration_screen.dart';
import 'features/dashboard/presentation/screens/mother_dashboard_screen.dart';
import 'features/onboarding/presentation/screens/welcome_screen.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();

  // Set system UI overlay style matching modern edge-to-edge mobile designs
  SystemChrome.setSystemUIOverlayStyle(
    const SystemUiOverlayStyle(
      statusBarColor: Colors.transparent,
      statusBarIconBrightness: Brightness.dark,
      systemNavigationBarColor: Colors.transparent,
      systemNavigationBarIconBrightness: Brightness.dark,
    ),
  );

  runApp(const BabyHealthGuardApp());
}

class BabyHealthGuardApp extends StatelessWidget {
  const BabyHealthGuardApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'BabyHealth Guard',
      debugShowCheckedModeBanner: false,
      theme: AppTheme.lightTheme,
      home: const WelcomeScreen(),
      routes: {
        '/welcome': (context) => const WelcomeScreen(),
        '/register': (context) => const MotherRegistrationScreen(),
        '/dashboard': (context) => const MotherDashboardScreen(),
      },
    );
  }
}
