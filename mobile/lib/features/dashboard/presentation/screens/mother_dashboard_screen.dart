import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';

/// Mother Dashboard Screen
/// Faithful Flutter implementation of the BabyHealth Guard Mother Dashboard,
/// My Health, and Danger Signs views.
class MotherDashboardScreen extends StatefulWidget {
  final String motherName;
  final String village;
  final String phone;
  final Uint8List? profilePhotoBytes;
  final String maternalStatus;
  final String pregnancyStage;

  const MotherDashboardScreen({
    super.key,
    this.motherName = 'Amina Brenda',
    this.village = 'Kagando',
    this.phone = '+256 772 000 000',
    this.profilePhotoBytes,
    this.maternalStatus = 'expecting',
    this.pregnancyStage = '4 - 6 Mo',
  });

  @override
  State<MotherDashboardScreen> createState() => _MotherDashboardScreenState();
}

class _MotherDashboardScreenState extends State<MotherDashboardScreen> {
  int _currentTab = 0; // 0: Home, 1: My Health, 2: Warning Signs, 3: Visits
  int _kickCount = 10;
  bool _isIronFolicTaken = true;
  String _bpSystolic = '118';
  String _bpDiastolic = '76';

  // Design Token Colors matching Tailwind Config
  static const Color colorBackground = Color(0xFFFAF8FF);
  static const Color colorPrimary = Color(0xFF005A71);
  static const Color colorPrimaryContainer = Color(0xFF0E7490);
  static const Color colorSecondary = Color(0xFF00687A);
  static const Color colorOnPrimary = Color(0xFFFFFFFF);
  static const Color colorOnSurface = Color(0xFF131B2E);
  static const Color colorOnSurfaceVariant = Color(0xFF3F484C);
  static const Color colorSurfaceContainerLow = Color(0xFFF2F3FF);
  static const Color colorSurfaceContainerLowest = Color(0xFFFFFFFF);
  static const Color colorSecondaryFixed = Color(0xFFACEDFF);
  static const Color colorOnSecondaryFixed = Color(0xFF001F26);
  static const Color colorPrimaryFixed = Color(0xFFB9EAFF);

  Future<void> _makeCall(String phoneNumber) async {
    final uri = Uri.parse('tel:$phoneNumber');
    if (await canLaunchUrl(uri)) {
      await launchUrl(uri);
    } else {
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Dialing $phoneNumber...')),
      );
    }
  }

  Future<void> _sendSms(String phoneNumber) async {
    final uri = Uri.parse('sms:$phoneNumber');
    if (await canLaunchUrl(uri)) {
      await launchUrl(uri);
    } else {
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Opening SMS to $phoneNumber...')),
      );
    }
  }

  void _showRecordVitalsSheet() {
    final sysController = TextEditingController(text: _bpSystolic);
    final diaController = TextEditingController(text: _bpDiastolic);
    final kickController = TextEditingController(text: '$_kickCount');

    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.white,
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(28)),
      ),
      builder: (context) {
        return Padding(
          padding: EdgeInsets.fromLTRB(
            20,
            16,
            20,
            MediaQuery.of(context).viewInsets.bottom + 24,
          ),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Center(
                child: Container(
                  width: 40,
                  height: 4,
                  decoration: BoxDecoration(
                    color: Colors.grey.shade300,
                    borderRadius: BorderRadius.circular(2),
                  ),
                ),
              ),
              const SizedBox(height: 16),
              const Row(
                children: [
                  Icon(Icons.favorite_rounded, color: colorPrimary, size: 24),
                  SizedBox(width: 10),
                  Text(
                    "Record Today's Vitals",
                    style: TextStyle(
                      fontFamily: 'Inter',
                      fontSize: 17,
                      fontWeight: FontWeight.bold,
                      color: colorOnSurface,
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 16),
              const Text(
                'Blood Pressure (Systolic / Diastolic mmHg)',
                style: TextStyle(
                  fontFamily: 'Inter',
                  fontSize: 12.5,
                  fontWeight: FontWeight.w600,
                  color: colorOnSurface,
                ),
              ),
              const SizedBox(height: 6),
              Row(
                children: [
                  Expanded(
                    child: TextField(
                      controller: sysController,
                      keyboardType: TextInputType.number,
                      decoration: InputDecoration(
                        hintText: '118',
                        filled: true,
                        fillColor: colorSurfaceContainerLow,
                        border: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(12),
                          borderSide: BorderSide.none,
                        ),
                        contentPadding: const EdgeInsets.symmetric(
                            horizontal: 14, vertical: 12),
                      ),
                    ),
                  ),
                  const Padding(
                    padding: EdgeInsets.symmetric(horizontal: 10),
                    child: Text('/',
                        style: TextStyle(
                            fontSize: 20, fontWeight: FontWeight.bold)),
                  ),
                  Expanded(
                    child: TextField(
                      controller: diaController,
                      keyboardType: TextInputType.number,
                      decoration: InputDecoration(
                        hintText: '76',
                        filled: true,
                        fillColor: colorSurfaceContainerLow,
                        border: OutlineInputBorder(
                          borderRadius: BorderRadius.circular(12),
                          borderSide: BorderSide.none,
                        ),
                        contentPadding: const EdgeInsets.symmetric(
                            horizontal: 14, vertical: 12),
                      ),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 16),
              const Text(
                'Baby Kicks Counted Today',
                style: TextStyle(
                  fontFamily: 'Inter',
                  fontSize: 12.5,
                  fontWeight: FontWeight.w600,
                  color: colorOnSurface,
                ),
              ),
              const SizedBox(height: 6),
              TextField(
                controller: kickController,
                keyboardType: TextInputType.number,
                decoration: InputDecoration(
                  hintText: '10',
                  filled: true,
                  fillColor: colorSurfaceContainerLow,
                  border: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(12),
                    borderSide: BorderSide.none,
                  ),
                  contentPadding:
                      const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
                ),
              ),
              const SizedBox(height: 20),
              SizedBox(
                width: double.infinity,
                height: 50,
                child: ElevatedButton(
                  onPressed: () {
                    setState(() {
                      if (sysController.text.trim().isNotEmpty) {
                        _bpSystolic = sysController.text.trim();
                      }
                      if (diaController.text.trim().isNotEmpty) {
                        _bpDiastolic = diaController.text.trim();
                      }
                      final parsedKicks =
                          int.tryParse(kickController.text.trim());
                      if (parsedKicks != null) {
                        _kickCount = parsedKicks;
                      }
                    });
                    Navigator.pop(context);
                    ScaffoldMessenger.of(context).showSnackBar(
                      const SnackBar(
                        content: Text("Today's vitals saved successfully!"),
                        behavior: SnackBarBehavior.floating,
                      ),
                    );
                  },
                  style: ElevatedButton.styleFrom(
                    backgroundColor: colorPrimaryContainer,
                    foregroundColor: colorOnPrimary,
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(100),
                    ),
                    elevation: 0,
                  ),
                  child: const Text(
                    'Save Vitals',
                    style: TextStyle(
                      fontFamily: 'Inter',
                      fontSize: 15,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
              ),
            ],
          ),
        );
      },
    );
  }

  void _handleDangerCardTap(String signTitle, String signDescription) {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(24)),
        title: Row(
          children: [
            const Icon(Icons.warning_amber_rounded, color: Colors.red, size: 26),
            const SizedBox(width: 8),
            Expanded(
              child: Text(
                signTitle,
                style: const TextStyle(
                  fontFamily: 'Inter',
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                  color: colorOnSurface,
                ),
              ),
            ),
          ],
        ),
        content: Text(
          '$signDescription\n\nWould you like to call your midwife now for free support?',
          style: const TextStyle(
            fontFamily: 'Inter',
            fontSize: 13.5,
            color: colorOnSurfaceVariant,
            height: 1.4,
          ),
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('Cancel'),
          ),
          ElevatedButton.icon(
            onPressed: () {
              Navigator.pop(context);
              _makeCall('0800100200');
            },
            style: ElevatedButton.styleFrom(
              backgroundColor: colorPrimaryContainer,
              foregroundColor: Colors.white,
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(100),
              ),
            ),
            icon: const Icon(Icons.call, size: 16),
            label: const Text('Call Midwife'),
          ),
        ],
      ),
    );
  }

  void _showVisitDetails() {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
        title: const Text(
          'ANC Visit 3 of 4 Details',
          style: TextStyle(fontFamily: 'Inter', fontWeight: FontWeight.bold),
        ),
        content: const Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('• Date: Thursday, 24 Oct at 9:00 AM'),
            SizedBox(height: 6),
            Text('• Clinic: Bwera Health Centre III'),
            SizedBox(height: 6),
            Text('• Assigned Midwife: Sr. Sarah Omondi'),
            SizedBox(height: 6),
            Text(
                '• Agenda: Routine ultrasound, tetanus booster dose & blood pressure review.'),
            SizedBox(height: 10),
            Text(
              'SMS reminder has been dispatched to your registered phone number.',
              style: TextStyle(fontSize: 12, color: colorPrimaryContainer),
            ),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(context),
            child: const Text('Close'),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: colorBackground,
      body: SafeArea(
        bottom: false,
        child: Column(
          children: [
            // Header dynamically changes based on active tab
            if (_currentTab == 1)
              _buildMyHealthHeader()
            else if (_currentTab == 2)
              _buildDangerSignsHeader()
            else if (_currentTab == 3)
              _buildVisitsHeader()
            else
              _buildHomeHeader(),

            // Content changes based on active tab
            Expanded(
              child: _buildCurrentTabContent(),
            ),
          ],
        ),
      ),
      bottomNavigationBar: _buildBottomNav(),
    );
  }

  Widget _buildCurrentTabContent() {
    switch (_currentTab) {
      case 1:
        return _buildMyHealthContent();
      case 2:
        return _buildDangerSignsContent();
      case 3:
        return _buildVisitsContent();
      default:
        return _buildHomeContent();
    }
  }

  // --------------------------------------------------------------------------
  // TAB 2: DANGER SIGNS (WARNINGS) SECTION
  // --------------------------------------------------------------------------
  Widget _buildDangerSignsHeader() {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 10),
      decoration: BoxDecoration(
        color: colorBackground.withValues(alpha: 0.95),
        border: Border(
          bottom: BorderSide(color: Colors.grey.shade200, width: 0.8),
        ),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          InkWell(
            onTap: () => setState(() => _currentTab = 0),
            borderRadius: BorderRadius.circular(100),
            child: Container(
              width: 40,
              height: 40,
              decoration: const BoxDecoration(
                color: Color(0xFFEAEDFF),
                shape: BoxShape.circle,
              ),
              child: const Icon(Icons.arrow_back, size: 22, color: colorOnSurface),
            ),
          ),
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
            decoration: BoxDecoration(
              color: const Color(0xFFEAEDFF),
              borderRadius: BorderRadius.circular(100),
              border: Border.all(
                  color: const Color(0xFFBEC8CD).withValues(alpha: 0.4)),
            ),
            child: Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                Container(
                  width: 8,
                  height: 8,
                  decoration: const BoxDecoration(
                    color: colorPrimary,
                    shape: BoxShape.circle,
                  ),
                ),
                const SizedBox(width: 6),
                const Text(
                  '24/7 PRIORITY',
                  style: TextStyle(
                    fontFamily: 'Inter',
                    fontSize: 11,
                    fontWeight: FontWeight.bold,
                    letterSpacing: 0.5,
                    color: colorPrimary,
                  ),
                ),
              ],
            ),
          ),
          InkWell(
            onTap: () {
              ScaffoldMessenger.of(context).showSnackBar(
                const SnackBar(
                  content: Text('Priority emergency line is active.'),
                  duration: Duration(seconds: 2),
                ),
              );
            },
            borderRadius: BorderRadius.circular(100),
            child: Container(
              width: 40,
              height: 40,
              decoration: const BoxDecoration(
                color: Color(0xFFEAEDFF),
                shape: BoxShape.circle,
              ),
              child: const Icon(Icons.notifications_none_rounded,
                  size: 20, color: colorOnSurface),
            ),
          ),
        ],
      ),
    );
  }

  /// Header for the Visits tab (Tab 3)
  Widget _buildVisitsHeader() {
    final namePart = widget.motherName.split(' ').first;
    final stageLabel = widget.maternalStatus == 'baby'
        ? 'Newborn'
        : (widget.pregnancyStage.isNotEmpty
            ? widget.pregnancyStage
            : '28 Wks');

    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 10),
      decoration: BoxDecoration(
        color: colorBackground.withValues(alpha: 0.95),
        border: Border(
          bottom: BorderSide(color: Colors.grey.shade200, width: 0.8),
        ),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          // Left: pulsing dot + subtext + title
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisSize: MainAxisSize.min,
              children: [
                Row(
                  children: [
                    TweenAnimationBuilder<double>(
                      tween: Tween(begin: 0.4, end: 1.0),
                      duration: const Duration(milliseconds: 900),
                      curve: Curves.easeInOut,
                      builder: (context, value, child) => Opacity(
                        opacity: value,
                        child: child,
                      ),
                      child: Container(
                        width: 8,
                        height: 8,
                        decoration: const BoxDecoration(
                          color: colorPrimary,
                          shape: BoxShape.circle,
                        ),
                      ),
                    ),
                    const SizedBox(width: 6),
                    Text(
                      '$namePart • $stageLabel',
                      style: const TextStyle(
                        fontFamily: 'Inter',
                        fontSize: 11,
                        fontWeight: FontWeight.w600,
                        letterSpacing: 0.44,
                        color: Color(0xFF00687A),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 2),
                const Text(
                  'My Visits',
                  style: TextStyle(
                    fontFamily: 'Inter',
                    fontSize: 16,
                    fontWeight: FontWeight.w600,
                    color: colorOnSurface,
                  ),
                ),
              ],
            ),
          ),
          // Right: Emergency button + person icon
          Row(
            children: [
              InkWell(
                onTap: () {},
                borderRadius: BorderRadius.circular(12),
                child: Container(
                  padding:
                      const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
                  decoration: BoxDecoration(
                    color: colorPrimaryContainer,
                    borderRadius: BorderRadius.circular(12),
                  ),
                  child: const Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Icon(Icons.call_rounded,
                          size: 16, color: Colors.white),
                      SizedBox(width: 4),
                      Text(
                        'Emergency',
                        style: TextStyle(
                          fontFamily: 'Inter',
                          fontSize: 12,
                          fontWeight: FontWeight.w600,
                          color: Colors.white,
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              const SizedBox(width: 8),
              Container(
                width: 32,
                height: 32,
                decoration: const BoxDecoration(
                  color: colorPrimary,
                  shape: BoxShape.circle,
                ),
                child: const Icon(Icons.person_rounded,
                    size: 18, color: Colors.white),
              ),
            ],
          ),
        ],
      ),
    );
  }

  Widget _buildDangerSignsContent() {
    return Center(
      child: ConstrainedBox(
        constraints: const BoxConstraints(maxWidth: 860),
        child: SingleChildScrollView(
      physics: const BouncingScrollPhysics(),
      padding: const EdgeInsets.fromLTRB(20, 16, 20, 100),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Title Header
          const SizedBox(height: 4),
          const Text(
            'Danger Signs',
            style: TextStyle(
              fontFamily: 'Inter',
              fontSize: 24,
              fontWeight: FontWeight.bold,
              color: colorOnSurface,
              letterSpacing: -0.5,
            ),
          ),
          const SizedBox(height: 4),
          const Text(
            'Tap if you feel any of these',
            style: TextStyle(
              fontFamily: 'Inter',
              fontSize: 14,
              fontWeight: FontWeight.w500,
              color: colorOnSurfaceVariant,
            ),
          ),
          const SizedBox(height: 20),

          // 4 Clean Large Visual Cards Grid
          Row(
            children: [
              Expanded(
                child: _buildDangerCard(
                  icon: Icons.water_drop_rounded,
                  iconColor: colorPrimaryContainer,
                  title: 'Bleeding',
                  subtitle: 'Any blood',
                  onTap: () => _handleDangerCardTap(
                    'Bleeding',
                    'Vaginal bleeding during pregnancy requires immediate clinical review.',
                  ),
                ),
              ),
              const SizedBox(width: 14),
              Expanded(
                child: _buildDangerCard(
                  icon: Icons.visibility_off_rounded,
                  iconColor: colorPrimaryContainer,
                  title: 'Severe Headache',
                  subtitle: 'Blurry vision',
                  onTap: () => _handleDangerCardTap(
                    'Severe Headache',
                    'Severe headache with blurry vision may indicate elevated blood pressure.',
                  ),
                ),
              ),
            ],
          ),
          const SizedBox(height: 14),
          Row(
            children: [
              Expanded(
                child: _buildDangerCard(
                  icon: Icons.child_care_rounded,
                  iconColor: colorPrimary,
                  title: 'Baby Not Moving',
                  subtitle: 'Fewer kicks',
                  onTap: () => _handleDangerCardTap(
                    'Baby Not Moving',
                    'Noticeably reduced fetal kicks should be checked immediately by your midwife.',
                  ),
                ),
              ),
              const SizedBox(width: 14),
              Expanded(
                child: _buildDangerCard(
                  icon: Icons.thermostat_rounded,
                  iconColor: colorSecondary,
                  title: 'High Fever',
                  subtitle: 'Hot or chills',
                  onTap: () => _handleDangerCardTap(
                    'High Fever',
                    'High fever or severe chills could indicate maternal infection.',
                  ),
                ),
              ),
            ],
          ),

          const SizedBox(height: 32),

          // Emergency Help Card
          Container(
            padding: const EdgeInsets.all(20),
            decoration: BoxDecoration(
              color: colorSurfaceContainerLow,
              borderRadius: BorderRadius.circular(28),
              border: Border.all(
                color: const Color(0xFFBEC8CD).withValues(alpha: 0.3),
              ),
              boxShadow: [
                BoxShadow(
                  color: Colors.black.withValues(alpha: 0.02),
                  blurRadius: 10,
                ),
              ],
            ),
            child: Column(
              children: [
                SizedBox(
                  width: double.infinity,
                  height: 54,
                  child: ElevatedButton(
                    onPressed: () => _makeCall('0800100200'),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: colorPrimaryContainer,
                      foregroundColor: Colors.white,
                      elevation: 2,
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(16),
                      ),
                    ),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        Container(
                          width: 32,
                          height: 32,
                          decoration: BoxDecoration(
                            color: Colors.white.withValues(alpha: 0.2),
                            shape: BoxShape.circle,
                          ),
                          child: const Icon(Icons.call,
                              size: 18, color: Colors.white),
                        ),
                        const SizedBox(width: 12),
                        const Text(
                          'Call Midwife Now (Free)',
                          style: TextStyle(
                            fontFamily: 'Inter',
                            fontSize: 15,
                            fontWeight: FontWeight.w600,
                            letterSpacing: 0.2,
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
                const SizedBox(height: 14),
                const Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Icon(Icons.dialpad, size: 16, color: colorPrimaryContainer),
                    SizedBox(width: 6),
                    Text(
                      'Or dial *920# with no internet',
                      style: TextStyle(
                        fontFamily: 'Inter',
                        fontSize: 12.5,
                        fontWeight: FontWeight.w500,
                        color: colorOnSurfaceVariant,
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
        ],
      ),
    ),
  ),
);
  }

  Widget _buildDangerCard({
    required IconData icon,
    required Color iconColor,
    required String title,
    required String subtitle,
    required VoidCallback onTap,
  }) {
    return InkWell(
      onTap: onTap,
      borderRadius: BorderRadius.circular(24),
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 20),
        decoration: BoxDecoration(
          color: colorSurfaceContainerLow,
          borderRadius: BorderRadius.circular(24),
          border: Border.all(
            color: const Color(0xFFBEC8CD).withValues(alpha: 0.3),
          ),
          boxShadow: [
            BoxShadow(
              color: Colors.black.withValues(alpha: 0.02),
              blurRadius: 8,
              offset: const Offset(0, 2),
            ),
          ],
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              width: 64,
              height: 64,
              decoration: BoxDecoration(
                color: colorSurfaceContainerLowest,
                borderRadius: BorderRadius.circular(18),
                boxShadow: [
                  BoxShadow(
                    color: Colors.black.withValues(alpha: 0.03),
                    blurRadius: 6,
                  ),
                ],
              ),
              child: Icon(icon, size: 34, color: iconColor),
            ),
            const SizedBox(height: 14),
            Text(
              title,
              textAlign: TextAlign.center,
              style: const TextStyle(
                fontFamily: 'Inter',
                fontSize: 15.5,
                fontWeight: FontWeight.bold,
                color: colorOnSurface,
                height: 1.2,
              ),
            ),
            const SizedBox(height: 3),
            Text(
              subtitle,
              textAlign: TextAlign.center,
              style: const TextStyle(
                fontFamily: 'Inter',
                fontSize: 12,
                fontWeight: FontWeight.w500,
                color: colorOnSurfaceVariant,
              ),
            ),
          ],
        ),
      ),
    );
  }

  // --------------------------------------------------------------------------
  // TAB 1: MY HEALTH SECTION
  // --------------------------------------------------------------------------
  Widget _buildMyHealthHeader() {
    final firstName = widget.motherName.split(' ').first;
    final stageText = widget.maternalStatus == 'baby' ? 'Newborn' : '28 Wks';

    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
      decoration: BoxDecoration(
        color: colorBackground.withValues(alpha: 0.95),
        border: Border(
          bottom: BorderSide(color: Colors.grey.shade200, width: 0.8),
        ),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisSize: MainAxisSize.min,
            children: [
              const Text(
                'My Health',
                style: TextStyle(
                  fontFamily: 'Inter',
                  fontSize: 17,
                  fontWeight: FontWeight.bold,
                  color: colorOnSurface,
                ),
              ),
              const SizedBox(height: 2),
              Row(
                children: [
                  Container(
                    width: 7,
                    height: 7,
                    decoration: const BoxDecoration(
                      shape: BoxShape.circle,
                      color: Color(0xFF10B981),
                    ),
                  ),
                  const SizedBox(width: 6),
                  Text(
                    '$firstName • $stageText',
                    style: const TextStyle(
                      fontFamily: 'Inter',
                      fontSize: 11.5,
                      fontWeight: FontWeight.w600,
                      color: colorSecondary,
                    ),
                  ),
                ],
              ),
            ],
          ),
          InkWell(
            onTap: () => _makeCall('112'),
            borderRadius: BorderRadius.circular(12),
            child: Container(
              height: 40,
              padding: const EdgeInsets.symmetric(horizontal: 14),
              decoration: BoxDecoration(
                color: colorPrimaryContainer,
                borderRadius: BorderRadius.circular(12),
                boxShadow: [
                  BoxShadow(
                    color: colorPrimaryContainer.withValues(alpha: 0.25),
                    blurRadius: 6,
                    offset: const Offset(0, 2),
                  ),
                ],
              ),
              child: const Row(
                children: [
                  Icon(Icons.call, size: 16, color: colorOnPrimary),
                  SizedBox(width: 6),
                  Text(
                    'Emergency',
                    style: TextStyle(
                      fontFamily: 'Inter',
                      fontSize: 12.5,
                      fontWeight: FontWeight.bold,
                      color: colorOnPrimary,
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildMyHealthContent() {
    return Center(
      child: ConstrainedBox(
        constraints: const BoxConstraints(maxWidth: 880),
        child: SingleChildScrollView(
      physics: const BouncingScrollPhysics(),
      padding: const EdgeInsets.fromLTRB(20, 16, 20, 100),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Section: Today's Vitals
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              const Text(
                "Today's Vitals",
                style: TextStyle(
                  fontFamily: 'Inter',
                  fontSize: 16,
                  fontWeight: FontWeight.w600,
                  color: colorOnSurface,
                ),
              ),
              Text(
                'Oct 10',
                style: TextStyle(
                  fontFamily: 'Inter',
                  fontSize: 12,
                  color: colorOnSurfaceVariant.withValues(alpha: 0.8),
                ),
              ),
            ],
          ),
          const SizedBox(height: 10),

          // Grid: 2 Cards (Blood Pressure & Baby Kicks)
          Row(
            children: [
              // Blood Pressure Card
              Expanded(
                child: Container(
                  constraints: const BoxConstraints(minHeight: 130),
                  padding: const EdgeInsets.all(14),
                  decoration: BoxDecoration(
                    color: colorSurfaceContainerLowest,
                    borderRadius: BorderRadius.circular(16),
                    border: Border.all(
                      color: Colors.grey.shade200,
                      width: 0.8,
                    ),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.black.withValues(alpha: 0.02),
                        blurRadius: 8,
                      ),
                    ],
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      const Row(
                        children: [
                          Icon(Icons.favorite, size: 18, color: colorPrimary),
                          SizedBox(width: 6),
                          Text(
                            'Blood Pressure',
                            style: TextStyle(
                              fontFamily: 'Inter',
                              fontSize: 12,
                              fontWeight: FontWeight.w500,
                              color: colorOnSurfaceVariant,
                            ),
                          ),
                        ],
                      ),
                      Padding(
                        padding: const EdgeInsets.symmetric(vertical: 8),
                        child: RichText(
                          text: TextSpan(
                            children: [
                              TextSpan(
                                text: _bpSystolic,
                                style: const TextStyle(
                                  fontFamily: 'Inter',
                                  fontSize: 26,
                                  fontWeight: FontWeight.bold,
                                  color: colorOnSurface,
                                ),
                              ),
                              TextSpan(
                                text: '/$_bpDiastolic',
                                style: const TextStyle(
                                  fontFamily: 'Inter',
                                  fontSize: 15,
                                  fontWeight: FontWeight.normal,
                                  color: colorOnSurfaceVariant,
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                      const Text(
                        'Normal',
                        style: TextStyle(
                          fontFamily: 'Inter',
                          fontSize: 11.5,
                          fontWeight: FontWeight.w600,
                          color: colorSecondary,
                        ),
                      ),
                    ],
                  ),
                ),
              ),

              const SizedBox(width: 12),

              // Baby Kicks Card (Interactive)
              Expanded(
                child: InkWell(
                  onTap: () {
                    setState(() => _kickCount++);
                    ScaffoldMessenger.of(context).showSnackBar(
                      SnackBar(
                        content: Text('Baby kick logged! Total: $_kickCount'),
                        duration: const Duration(seconds: 1),
                        behavior: SnackBarBehavior.floating,
                      ),
                    );
                  },
                  borderRadius: BorderRadius.circular(16),
                  child: Container(
                    constraints: const BoxConstraints(minHeight: 130),
                    padding: const EdgeInsets.all(14),
                    decoration: BoxDecoration(
                      color: colorSurfaceContainerLowest,
                      borderRadius: BorderRadius.circular(16),
                      border: Border.all(
                        color: Colors.grey.shade200,
                        width: 0.8,
                      ),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.black.withValues(alpha: 0.02),
                          blurRadius: 8,
                        ),
                      ],
                    ),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        const Row(
                          children: [
                            Icon(Icons.child_care,
                                size: 18, color: colorPrimary),
                            SizedBox(width: 6),
                            Text(
                              'Baby Kicks',
                              style: TextStyle(
                                fontFamily: 'Inter',
                                fontSize: 12,
                                fontWeight: FontWeight.w500,
                                color: colorOnSurfaceVariant,
                              ),
                            ),
                          ],
                        ),
                        Padding(
                          padding: const EdgeInsets.symmetric(vertical: 8),
                          child: RichText(
                            text: TextSpan(
                              children: [
                                TextSpan(
                                  text: '$_kickCount ',
                                  style: const TextStyle(
                                    fontFamily: 'Inter',
                                    fontSize: 26,
                                    fontWeight: FontWeight.bold,
                                    color: colorPrimary,
                                  ),
                                ),
                                const TextSpan(
                                  text: 'kicks',
                                  style: TextStyle(
                                    fontFamily: 'Inter',
                                    fontSize: 14,
                                    fontWeight: FontWeight.normal,
                                    color: colorOnSurface,
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ),
                        const Text(
                          'Counted today ✓',
                          style: TextStyle(
                            fontFamily: 'Inter',
                            fontSize: 11.5,
                            fontWeight: FontWeight.w600,
                            color: colorSecondary,
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ),
            ],
          ),

          const SizedBox(height: 24),

          // Section: Care & Medication
          const Text(
            'Care & Medication',
            style: TextStyle(
              fontFamily: 'Inter',
              fontSize: 16,
              fontWeight: FontWeight.w600,
              color: colorOnSurface,
            ),
          ),
          const SizedBox(height: 10),

          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: colorSurfaceContainerLowest,
              borderRadius: BorderRadius.circular(18),
              border: Border.all(color: Colors.grey.shade200, width: 0.8),
              boxShadow: [
                BoxShadow(
                  color: Colors.black.withValues(alpha: 0.02),
                  blurRadius: 8,
                ),
              ],
            ),
            child: Column(
              children: [
                // Item 1: Iron & Folic Acid
                InkWell(
                  onTap: () {
                    setState(() => _isIronFolicTaken = !_isIronFolicTaken);
                  },
                  borderRadius: BorderRadius.circular(12),
                  child: Container(
                    padding: const EdgeInsets.all(10),
                    decoration: BoxDecoration(
                      color: colorSurfaceContainerLow,
                      borderRadius: BorderRadius.circular(12),
                    ),
                    child: Row(
                      children: [
                        Container(
                          width: 40,
                          height: 40,
                          decoration: const BoxDecoration(
                            color: colorSecondaryFixed,
                            shape: BoxShape.circle,
                          ),
                          child: const Icon(
                            Icons.medication_rounded,
                            size: 20,
                            color: colorOnSecondaryFixed,
                          ),
                        ),
                        const SizedBox(width: 12),
                        const Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                'Iron & Folic Acid',
                                style: TextStyle(
                                  fontFamily: 'Inter',
                                  fontSize: 14,
                                  fontWeight: FontWeight.w600,
                                  color: colorOnSurface,
                                ),
                              ),
                              SizedBox(height: 2),
                              Text(
                                '1 tablet daily',
                                style: TextStyle(
                                  fontFamily: 'Inter',
                                  fontSize: 11.5,
                                  color: colorOnSurfaceVariant,
                                ),
                              ),
                            ],
                          ),
                        ),
                        Container(
                          padding: const EdgeInsets.symmetric(
                              horizontal: 10, vertical: 4),
                          decoration: BoxDecoration(
                            color: _isIronFolicTaken
                                ? colorSecondaryFixed
                                : Colors.amber.shade100,
                            borderRadius: BorderRadius.circular(100),
                          ),
                          child: Row(
                            mainAxisSize: MainAxisSize.min,
                            children: [
                              Icon(
                                _isIronFolicTaken
                                    ? Icons.check
                                    : Icons.schedule,
                                size: 14,
                                color: _isIronFolicTaken
                                    ? colorOnSecondaryFixed
                                    : Colors.amber.shade900,
                              ),
                              const SizedBox(width: 4),
                              Text(
                                _isIronFolicTaken
                                    ? 'Taken today'
                                    : 'Pending',
                                style: TextStyle(
                                  fontFamily: 'Inter',
                                  fontSize: 11,
                                  fontWeight: FontWeight.w600,
                                  color: _isIronFolicTaken
                                      ? colorOnSecondaryFixed
                                      : Colors.amber.shade900,
                                ),
                              ),
                            ],
                          ),
                        ),
                      ],
                    ),
                  ),
                ),

                const SizedBox(height: 8),

                // Item 2: Next Clinic Visit
                InkWell(
                  onTap: _showVisitDetails,
                  borderRadius: BorderRadius.circular(12),
                  child: Container(
                    padding: const EdgeInsets.all(10),
                    decoration: BoxDecoration(
                      color: colorSurfaceContainerLow,
                      borderRadius: BorderRadius.circular(12),
                    ),
                    child: Row(
                      children: [
                        Container(
                          width: 40,
                          height: 40,
                          decoration: const BoxDecoration(
                            color: colorPrimaryFixed,
                            shape: BoxShape.circle,
                          ),
                          child: const Icon(
                            Icons.calendar_today_rounded,
                            size: 19,
                            color: colorPrimary,
                          ),
                        ),
                        const SizedBox(width: 12),
                        const Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                'Next Clinic Visit',
                                style: TextStyle(
                                  fontFamily: 'Inter',
                                  fontSize: 14,
                                  fontWeight: FontWeight.w600,
                                  color: colorOnSurface,
                                ),
                              ),
                              SizedBox(height: 2),
                              Text(
                                'Bwera Health Centre III',
                                style: TextStyle(
                                  fontFamily: 'Inter',
                                  fontSize: 11.5,
                                  color: colorOnSurfaceVariant,
                                ),
                              ),
                            ],
                          ),
                        ),
                        const Column(
                          crossAxisAlignment: CrossAxisAlignment.end,
                          children: [
                            Text(
                              'Thu 24 Oct',
                              style: TextStyle(
                                fontFamily: 'Inter',
                                fontSize: 13,
                                fontWeight: FontWeight.bold,
                                color: colorPrimary,
                              ),
                            ),
                            SizedBox(height: 1),
                            Text(
                              'Visit 3 of 4',
                              style: TextStyle(
                                fontFamily: 'Inter',
                                fontSize: 11,
                                color: colorOnSurfaceVariant,
                              ),
                            ),
                          ],
                        ),
                      ],
                    ),
                  ),
                ),
              ],
            ),
          ),

          const SizedBox(height: 20),

          // + Record Today's Vitals Button
          SizedBox(
            width: double.infinity,
            height: 52,
            child: ElevatedButton.icon(
              onPressed: _showRecordVitalsSheet,
              style: ElevatedButton.styleFrom(
                backgroundColor: colorPrimaryContainer,
                foregroundColor: colorOnPrimary,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(16),
                ),
                elevation: 0,
              ),
              icon: const Icon(Icons.add_circle_outline_rounded, size: 22),
              label: const Text(
                "+ Record Today's Vitals",
                style: TextStyle(
                  fontFamily: 'Inter',
                  fontSize: 14.5,
                  fontWeight: FontWeight.w600,
                ),
              ),
            ),
          ),
        ],
      ),
    ),
  ),
);
  }

  // --------------------------------------------------------------------------
  // TAB 3: VISITS SECTION
  // --------------------------------------------------------------------------
  Widget _buildVisitsContent() {
    return Center(
      child: ConstrainedBox(
        constraints: const BoxConstraints(maxWidth: 880),
        child: SingleChildScrollView(
      physics: const BouncingScrollPhysics(),
      padding: const EdgeInsets.fromLTRB(16, 16, 16, 100),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Title Section
          const Padding(
            padding: EdgeInsets.fromLTRB(4, 4, 4, 0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'Clinic Visits & Reminders',
                  style: TextStyle(
                    fontFamily: 'Inter',
                    fontSize: 24,
                    fontWeight: FontWeight.w700,
                    letterSpacing: -0.24,
                    color: colorOnSurface,
                  ),
                ),
                SizedBox(height: 4),
                Text(
                  'Regular checks protect both you and your baby\'s safe arrival.',
                  style: TextStyle(
                    fontFamily: 'Inter',
                    fontSize: 12,
                    fontWeight: FontWeight.w400,
                    color: colorOnSurfaceVariant,
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(height: 16),

          // Next ANC Visit Card
          Container(
            decoration: BoxDecoration(
              color: colorSurfaceContainerLowest,
              borderRadius: BorderRadius.circular(12),
              border: Border.all(
                color: const Color(0xFFBEC8CD).withValues(alpha: 0.3),
              ),
              boxShadow: [
                BoxShadow(
                  color: Colors.black.withValues(alpha: 0.08),
                  blurRadius: 12,
                  offset: const Offset(0, 2),
                ),
              ],
            ),
            clipBehavior: Clip.antiAlias,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                // Colored top bar
                Container(height: 6, color: colorPrimary),
                Padding(
                  padding: const EdgeInsets.all(16),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      // Badges row
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Container(
                            padding: const EdgeInsets.symmetric(
                                horizontal: 10, vertical: 5),
                            decoration: BoxDecoration(
                              color: colorPrimary.withValues(alpha: 0.1),
                              borderRadius: BorderRadius.circular(100),
                            ),
                            child: Row(
                              mainAxisSize: MainAxisSize.min,
                              children: [
                                Container(
                                  width: 8,
                                  height: 8,
                                  decoration: const BoxDecoration(
                                    color: colorPrimary,
                                    shape: BoxShape.circle,
                                  ),
                                ),
                                const SizedBox(width: 6),
                                const Text(
                                  'Next ANC Visit (3 of 4)',
                                  style: TextStyle(
                                    fontFamily: 'Inter',
                                    fontSize: 11,
                                    fontWeight: FontWeight.w700,
                                    letterSpacing: 0.44,
                                    color: colorPrimary,
                                  ),
                                ),
                              ],
                            ),
                          ),
                          Container(
                            padding: const EdgeInsets.symmetric(
                                horizontal: 8, vertical: 2),
                            decoration: BoxDecoration(
                              color: const Color(0xFFE2E7FF),
                              borderRadius: BorderRadius.circular(100),
                            ),
                            child: const Text(
                              'Confirmed',
                              style: TextStyle(
                                fontFamily: 'Inter',
                                fontSize: 11,
                                fontWeight: FontWeight.w700,
                                letterSpacing: 0.44,
                                color: Color(0xFF00687A),
                              ),
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 12),

                      // Date & Time
                      const Text(
                        'Thursday, 24 Oct',
                        style: TextStyle(
                          fontFamily: 'Inter',
                          fontSize: 24,
                          fontWeight: FontWeight.w600,
                          letterSpacing: -0.24,
                          color: colorOnSurface,
                        ),
                      ),
                      const SizedBox(height: 2),
                      const Text(
                        '9:00 AM • Morning slot',
                        style: TextStyle(
                          fontFamily: 'Inter',
                          fontSize: 16,
                          fontWeight: FontWeight.w500,
                          color: colorPrimary,
                        ),
                      ),
                      const SizedBox(height: 12),

                      // Clinic info row
                      Container(
                        padding: const EdgeInsets.all(10),
                        decoration: BoxDecoration(
                          color: const Color(0xFFF2F3FF),
                          borderRadius: BorderRadius.circular(12),
                        ),
                        child: Row(
                          children: [
                            Container(
                              width: 40,
                              height: 40,
                              decoration: BoxDecoration(
                                color: colorPrimary.withValues(alpha: 0.1),
                                borderRadius: BorderRadius.circular(10),
                              ),
                              child: const Icon(
                                Icons.local_hospital_rounded,
                                color: colorPrimary,
                                size: 22,
                              ),
                            ),
                            const SizedBox(width: 10),
                            const Expanded(
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Text(
                                    'Bwera Health Centre III',
                                    style: TextStyle(
                                      fontFamily: 'Inter',
                                      fontSize: 14,
                                      fontWeight: FontWeight.w600,
                                      color: colorOnSurface,
                                    ),
                                  ),
                                  Text(
                                    'Midwife Sr. Sarah • Room 4B',
                                    style: TextStyle(
                                      fontFamily: 'Inter',
                                      fontSize: 12,
                                      color: colorOnSurfaceVariant,
                                    ),
                                  ),
                                ],
                              ),
                            ),
                          ],
                        ),
                      ),
                      const SizedBox(height: 14),

                      // Call button
                      SizedBox(
                        width: double.infinity,
                        height: 46,
                        child: ElevatedButton.icon(
                          onPressed: () {},
                          style: ElevatedButton.styleFrom(
                            backgroundColor: colorPrimaryContainer,
                            foregroundColor: Colors.white,
                            shape: RoundedRectangleBorder(
                              borderRadius: BorderRadius.circular(12),
                            ),
                            elevation: 1,
                          ),
                          icon: const Icon(Icons.call_rounded, size: 20),
                          label: const Text(
                            'Call Clinic / Midwife',
                            style: TextStyle(
                              fontFamily: 'Inter',
                              fontSize: 14,
                              fontWeight: FontWeight.w600,
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(height: 16),

          // Remember Note Card
          Container(
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: colorSurfaceContainerLowest,
              borderRadius: BorderRadius.circular(12),
              border: Border.all(
                color: const Color(0xFFBEC8CD).withValues(alpha: 0.3),
              ),
              boxShadow: [
                BoxShadow(
                  color: Colors.black.withValues(alpha: 0.04),
                  blurRadius: 6,
                  offset: const Offset(0, 1),
                ),
              ],
            ),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Icon(
                  Icons.check_circle_rounded,
                  color: colorPrimary,
                  size: 20,
                ),
                const SizedBox(width: 10),
                Expanded(
                  child: RichText(
                    text: const TextSpan(
                      style: TextStyle(
                        fontFamily: 'Inter',
                        fontSize: 14,
                        color: colorOnSurface,
                      ),
                      children: [
                        TextSpan(
                          text: 'Remember: ',
                          style: TextStyle(
                            fontWeight: FontWeight.w700,
                            color: colorPrimary,
                          ),
                        ),
                        TextSpan(
                          text:
                              'Bring your Mother-Child Yellow Book and clean drinking water.',
                        ),
                      ],
                    ),
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(height: 16),

          // Past Visit Progress Card
          Container(
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: colorSurfaceContainerLowest,
              borderRadius: BorderRadius.circular(12),
              border: Border.all(
                color: const Color(0xFFBEC8CD).withValues(alpha: 0.3),
              ),
              boxShadow: [
                BoxShadow(
                  color: Colors.black.withValues(alpha: 0.04),
                  blurRadius: 6,
                  offset: const Offset(0, 1),
                ),
              ],
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    const Row(
                      children: [
                        Icon(
                          Icons.history_edu_rounded,
                          color: colorPrimary,
                          size: 20,
                        ),
                        SizedBox(width: 6),
                        Text(
                          'Past Visit Progress',
                          style: TextStyle(
                            fontFamily: 'Inter',
                            fontSize: 16,
                            fontWeight: FontWeight.w600,
                            color: colorOnSurface,
                          ),
                        ),
                      ],
                    ),
                    Container(
                      padding: const EdgeInsets.symmetric(
                          horizontal: 8, vertical: 2),
                      decoration: BoxDecoration(
                        color: colorPrimary.withValues(alpha: 0.1),
                        borderRadius: BorderRadius.circular(100),
                      ),
                      child: const Text(
                        '2 of 4 Done',
                        style: TextStyle(
                          fontFamily: 'Inter',
                          fontSize: 11,
                          fontWeight: FontWeight.w700,
                          letterSpacing: 0.44,
                          color: colorPrimary,
                        ),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 10),

                // Progress bar
                ClipRRect(
                  borderRadius: BorderRadius.circular(100),
                  child: const LinearProgressIndicator(
                    value: 0.5,
                    minHeight: 8,
                    backgroundColor: Color(0xFFE2E7FF),
                    valueColor:
                        AlwaysStoppedAnimation<Color>(colorPrimary),
                  ),
                ),
                const SizedBox(height: 6),
                const Text(
                  '2 of 4 visits completed • Next check-up is Visit 3',
                  style: TextStyle(
                    fontFamily: 'Inter',
                    fontSize: 12,
                    color: colorOnSurfaceVariant,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    ),
  ),
);
  }

  // --------------------------------------------------------------------------
  // TAB 0: HOME SECTION
  // --------------------------------------------------------------------------
  Widget _buildHomeHeader() {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 10),
      decoration: BoxDecoration(
        color: colorBackground.withValues(alpha: 0.95),
        border: Border(
          bottom: BorderSide(color: Colors.grey.shade200, width: 0.8),
        ),
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Row(
            children: [
              // Avatar
              Container(
                width: 44,
                height: 44,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: Colors.white,
                  border: Border.all(color: Colors.grey.shade200, width: 1.5),
                  boxShadow: [
                    BoxShadow(
                      color: Colors.black.withValues(alpha: 0.04),
                      blurRadius: 4,
                      offset: const Offset(0, 2),
                    ),
                  ],
                ),
                child: ClipOval(
                  child: widget.profilePhotoBytes != null
                      ? Image.memory(
                          widget.profilePhotoBytes!,
                          fit: BoxFit.cover,
                        )
                      : Image.network(
                          'https://lh3.googleusercontent.com/aida/ALJJyrB02uNzgSUFmyA16NdXCEdl86RHOVW_SV4uhcvcQVIo7BNtuvhGPopPUo0PpIzaDWxVmK3GOU_6UJ2Gt-HJXfp0Vn2pcetClnxxoNwiA4tRwlLoPWINdj5PQEJuc-R7CAS70KJxBYggnyirlfbSEPRl02scU-DsOyO8Muaz97pajK7fgWNuVlbvNOi2kZJMf_3mt6Z3U_MtH7VeZLSDAUMeJ21fSr4OpfU9mZwwfjv-Hw',
                          fit: BoxFit.cover,
                          errorBuilder: (context, error, stackTrace) =>
                              const Icon(Icons.person, color: colorPrimary),
                        ),
                ),
              ),
              const SizedBox(width: 12),
              // Name + Village Tag + USSD Active
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                mainAxisSize: MainAxisSize.min,
                children: [
                  Row(
                    children: [
                      Text(
                        widget.motherName,
                        style: const TextStyle(
                          fontFamily: 'Inter',
                          fontSize: 15,
                          fontWeight: FontWeight.bold,
                          color: colorOnSurface,
                        ),
                      ),
                      const SizedBox(width: 6),
                      Container(
                        padding: const EdgeInsets.symmetric(
                            horizontal: 8, vertical: 2),
                        decoration: BoxDecoration(
                          color: const Color(0xFFE6F4F1),
                          borderRadius: BorderRadius.circular(100),
                          border: Border.all(
                            color: const Color(0xFFCCE9E3),
                            width: 0.8,
                          ),
                        ),
                        child: Text(
                          widget.village,
                          style: const TextStyle(
                            fontFamily: 'Inter',
                            fontSize: 11,
                            fontWeight: FontWeight.w600,
                            color: Color(0xFF0F766E),
                          ),
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 2),
                  Row(
                    children: [
                      Container(
                        width: 7,
                        height: 7,
                        decoration: const BoxDecoration(
                          shape: BoxShape.circle,
                          color: Color(0xFF10B981),
                        ),
                      ),
                      const SizedBox(width: 6),
                      const Text(
                        'Free USSD *920# Active',
                        style: TextStyle(
                          fontFamily: 'Inter',
                          fontSize: 11,
                          fontWeight: FontWeight.w500,
                          color: colorOnSurfaceVariant,
                        ),
                      ),
                    ],
                  ),
                ],
              ),
            ],
          ),

          // Notifications
          InkWell(
            onTap: () {
              ScaffoldMessenger.of(context).showSnackBar(
                const SnackBar(
                  content: Text('No new urgent clinic alerts.'),
                  duration: Duration(seconds: 2),
                ),
              );
            },
            borderRadius: BorderRadius.circular(20),
            child: Container(
              width: 40,
              height: 40,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: Colors.white,
                border: Border.all(color: Colors.grey.shade200, width: 0.8),
                boxShadow: [
                  BoxShadow(
                    color: Colors.black.withValues(alpha: 0.03),
                    blurRadius: 4,
                  ),
                ],
              ),
              child: Stack(
                alignment: Alignment.center,
                children: [
                  const Icon(Icons.notifications_none_rounded,
                      size: 20, color: colorOnSurface),
                  Positioned(
                    top: 10,
                    right: 10,
                    child: Container(
                      width: 7,
                      height: 7,
                      decoration: BoxDecoration(
                        color: Colors.amber.shade600,
                        shape: BoxShape.circle,
                        border: Border.all(color: Colors.white, width: 1.5),
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildHomeContent() {
    return LayoutBuilder(
      builder: (context, constraints) {
        final isWide = constraints.maxWidth >= 768;

        if (isWide) {
          // Tablet & Laptop responsive layout: Balanced dual-column dashboard
          return Center(
            child: ConstrainedBox(
              constraints: const BoxConstraints(maxWidth: 1120),
              child: SingleChildScrollView(
                physics: const BouncingScrollPhysics(),
                padding: const EdgeInsets.fromLTRB(28, 20, 28, 100),
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    // Left Column (Hero Card + Assigned Midwife + Next Clinic Visit)
                    Expanded(
                      flex: 6,
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.stretch,
                        children: [
                          _buildHeroCard(),
                          const SizedBox(height: 18),
                          _buildMidwifeCard(),
                          const SizedBox(height: 18),
                          _buildAncVisitCard(),
                        ],
                      ),
                    ),
                    const SizedBox(width: 24),
                    // Right Column (Daily Health Metrics + Emergency Triage & Actions)
                    Expanded(
                      flex: 5,
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.stretch,
                        children: [
                          _buildQuickHealthChecks(),
                          const SizedBox(height: 18),
                          _buildEmergencyActions(),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ),
          );
        }

        // Phone standard layout (vertical stack)
        return SingleChildScrollView(
          physics: const BouncingScrollPhysics(),
          padding: const EdgeInsets.fromLTRB(20, 16, 20, 100),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              // Hero Visual Card
              _buildHeroCard(),

              const SizedBox(height: 16),

              // Midwife Card
              _buildMidwifeCard(),

              const SizedBox(height: 16),

              // 3 Health Metric Cards
              _buildQuickHealthChecks(),

              const SizedBox(height: 16),

              // Next ANC Visit Card
              _buildAncVisitCard(),

              const SizedBox(height: 16),

              // Danger signs banner & Emergency call
              _buildEmergencyActions(),
            ],
          ),
        );
      },
    );
  }

  // Hero Card with Image and Trimester Countdown
  Widget _buildHeroCard() {
    return Container(
      padding: const EdgeInsets.all(10),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(28),
        border: Border.all(color: Colors.grey.shade100),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withValues(alpha: 0.03),
            blurRadius: 20,
            offset: const Offset(0, 10),
          ),
        ],
      ),
      child: ClipRRect(
        borderRadius: BorderRadius.circular(20),
        child: AspectRatio(
          aspectRatio: 4 / 3,
          child: Stack(
            fit: StackFit.expand,
            children: [
              // Hero Photo
              widget.profilePhotoBytes != null
                  ? Image.memory(widget.profilePhotoBytes!, fit: BoxFit.cover)
                  : Image.network(
                      'https://lh3.googleusercontent.com/aida/ALJJyrB02uNzgSUFmyA16NdXCEdl86RHOVW_SV4uhcvcQVIo7BNtuvhGPopPUo0PpIzaDWxVmK3GOU_6UJ2Gt-HJXfp0Vn2pcetClnxxoNwiA4tRwlLoPWINdj5PQEJuc-R7CAS70KJxBYggnyirlfbSEPRl02scU-DsOyO8Muaz97pajK7fgWNuVlbvNOi2kZJMf_3mt6Z3U_MtH7VeZLSDAUMeJ21fSr4OpfU9mZwwfjv-Hw',
                      fit: BoxFit.cover,
                      errorBuilder: (context, error, stackTrace) => Container(
                        decoration: const BoxDecoration(
                          gradient: LinearGradient(
                            colors: [Color(0xFF0E7490), Color(0xFF005A71)],
                            begin: Alignment.topLeft,
                            end: Alignment.bottomRight,
                          ),
                        ),
                        child: const Center(
                          child: Icon(Icons.favorite_rounded,
                              size: 64, color: Colors.white70),
                        ),
                      ),
                    ),

              // Gradient Overlay at Bottom
              Positioned.fill(
                child: DecoratedBox(
                  decoration: BoxDecoration(
                    gradient: LinearGradient(
                      colors: [
                        Colors.transparent,
                        Colors.black.withValues(alpha: 0.25),
                        Colors.black.withValues(alpha: 0.75),
                      ],
                      begin: Alignment.topCenter,
                      end: Alignment.bottomCenter,
                      stops: const [0.5, 0.75, 1.0],
                    ),
                  ),
                ),
              ),

              // Top Badges
              Positioned(
                top: 12,
                left: 12,
                child: Container(
                  padding:
                      const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
                  decoration: BoxDecoration(
                    color: Colors.white.withValues(alpha: 0.95),
                    borderRadius: BorderRadius.circular(100),
                    border: Border.all(
                      color: Colors.white.withValues(alpha: 0.6),
                    ),
                  ),
                  child: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Container(
                        width: 7,
                        height: 7,
                        decoration: const BoxDecoration(
                          color: Color(0xFF10B981),
                          shape: BoxShape.circle,
                        ),
                      ),
                      const SizedBox(width: 6),
                      Text(
                        widget.maternalStatus == 'baby'
                            ? 'Newborn Baby Stage'
                            : 'Week 28 • Trimester 3',
                        style: const TextStyle(
                          fontFamily: 'Inter',
                          fontSize: 11.5,
                          fontWeight: FontWeight.w600,
                          color: colorOnSurface,
                        ),
                      ),
                    ],
                  ),
                ),
              ),

              Positioned(
                top: 12,
                right: 12,
                child: Container(
                  padding:
                      const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                  decoration: BoxDecoration(
                    color: Colors.white.withValues(alpha: 0.92),
                    borderRadius: BorderRadius.circular(100),
                  ),
                  child: const Text(
                    'Dec 2024',
                    style: TextStyle(
                      fontFamily: 'Inter',
                      fontSize: 11,
                      fontWeight: FontWeight.w600,
                      color: Color(0xFF0F766E),
                    ),
                  ),
                ),
              ),

              // Bottom Title & Due window
              Positioned(
                left: 16,
                right: 16,
                bottom: 14,
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Text(
                      '${widget.motherName} & ${widget.maternalStatus == 'baby' ? 'Newborn' : 'Baby'}',
                      style: const TextStyle(
                        fontFamily: 'Inter',
                        fontSize: 16,
                        fontWeight: FontWeight.bold,
                        color: Colors.white,
                        shadows: [
                          Shadow(
                            color: Colors.black45,
                            blurRadius: 4,
                            offset: Offset(0, 1),
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 2),
                    Text(
                      widget.maternalStatus == 'baby'
                          ? 'Postnatal checkup recommended at 6 weeks'
                          : 'Estimated due in ~10 weeks (40-day window)',
                      style: TextStyle(
                        fontFamily: 'Inter',
                        fontSize: 12,
                        color: Colors.white.withValues(alpha: 0.92),
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  // Assigned Midwife Card
  Widget _buildMidwifeCard() {
    return Container(
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(18),
        border: Border.all(color: const Color(0xFFCCE9E3), width: 0.8),
        gradient: LinearGradient(
          colors: [
            const Color(0xFFF0FDF4).withValues(alpha: 0.4),
            Colors.white,
          ],
          begin: Alignment.centerLeft,
          end: Alignment.centerRight,
        ),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withValues(alpha: 0.02),
            blurRadius: 15,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Row(
        children: [
          // Midwife icon
          Container(
            width: 44,
            height: 44,
            decoration: BoxDecoration(
              shape: BoxShape.circle,
              color: const Color(0xFFE6F4F1),
              border: Border.all(color: const Color(0xFFCCE9E3)),
            ),
            child: const Icon(
              Icons.support_agent_rounded,
              color: Color(0xFF0F766E),
              size: 22,
            ),
          ),
          const SizedBox(width: 12),
          // Details
          const Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'YOUR MIDWIFE',
                  style: TextStyle(
                    fontFamily: 'Inter',
                    fontSize: 10.5,
                    fontWeight: FontWeight.bold,
                    letterSpacing: 0.5,
                    color: Color(0xFF0F766E),
                  ),
                ),
                SizedBox(height: 1),
                Text(
                  'Sr. Sarah Omondi',
                  style: TextStyle(
                    fontFamily: 'Inter',
                    fontSize: 14,
                    fontWeight: FontWeight.bold,
                    color: colorOnSurface,
                  ),
                ),
                Text(
                  'Bwera Health Centre III',
                  style: TextStyle(
                    fontFamily: 'Inter',
                    fontSize: 11,
                    color: colorOnSurfaceVariant,
                  ),
                ),
              ],
            ),
          ),
          // Call & SMS buttons
          Row(
            children: [
              InkWell(
                onTap: () => _makeCall('0800100200'),
                borderRadius: BorderRadius.circular(100),
                child: Container(
                  width: 36,
                  height: 36,
                  decoration: const BoxDecoration(
                    shape: BoxShape.circle,
                    color: Color(0xFF0F766E),
                  ),
                  child: const Icon(Icons.call, color: Colors.white, size: 18),
                ),
              ),
              const SizedBox(width: 8),
              InkWell(
                onTap: () => _sendSms('0800100200'),
                borderRadius: BorderRadius.circular(100),
                child: Container(
                  width: 36,
                  height: 36,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    color: Colors.grey.shade100,
                  ),
                  child: const Icon(Icons.chat_bubble_outline_rounded,
                      color: colorOnSurface, size: 18),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }

  // 3 Quick Health Checks
  Widget _buildQuickHealthChecks() {
    return Row(
      children: [
        // Kicks Card (Interactive)
        Expanded(
          child: InkWell(
            onTap: () {
              setState(() => _kickCount++);
              ScaffoldMessenger.of(context).showSnackBar(
                SnackBar(
                  content: Text('Kick logged! Total: $_kickCount kicks today.'),
                  duration: const Duration(seconds: 1),
                  behavior: SnackBarBehavior.floating,
                ),
              );
            },
            borderRadius: BorderRadius.circular(18),
            child: Container(
              height: 116,
              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 10),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(18),
                border: Border.all(color: Colors.grey.shade100),
                boxShadow: [
                  BoxShadow(
                    color: Colors.black.withValues(alpha: 0.02),
                    blurRadius: 10,
                  ),
                ],
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Container(
                    width: 36,
                    height: 36,
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      color: Colors.amber.shade50,
                    ),
                    child: Icon(Icons.child_care_rounded,
                        color: Colors.amber.shade600, size: 18),
                  ),
                  Column(
                    children: [
                      Text(
                        '$_kickCount kicks',
                        style: const TextStyle(
                          fontFamily: 'Inter',
                          fontSize: 14,
                          fontWeight: FontWeight.bold,
                          color: colorOnSurface,
                        ),
                      ),
                      const Text(
                        'Count Today',
                        style: TextStyle(
                          fontFamily: 'Inter',
                          fontSize: 10.5,
                          color: colorOnSurfaceVariant,
                        ),
                      ),
                    ],
                  ),
                  const Text(
                    '+ Log Kick',
                    style: TextStyle(
                      fontFamily: 'Inter',
                      fontSize: 10.5,
                      fontWeight: FontWeight.w600,
                      color: Color(0xFF0F766E),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),

        const SizedBox(width: 10),

        // Blood Pressure Card
        Expanded(
          child: Container(
            height: 116,
            padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 10),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(18),
              border: Border.all(color: Colors.grey.shade100),
              boxShadow: [
                BoxShadow(
                  color: Colors.black.withValues(alpha: 0.02),
                  blurRadius: 10,
                ),
              ],
            ),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Container(
                  width: 36,
                  height: 36,
                  decoration: const BoxDecoration(
                    shape: BoxShape.circle,
                    color: Color(0xFFE6F4F1),
                  ),
                  child: const Icon(Icons.favorite_rounded,
                      color: Color(0xFF0F766E), size: 18),
                ),
                Column(
                  children: [
                    Text(
                      '$_bpSystolic / $_bpDiastolic',
                      style: const TextStyle(
                        fontFamily: 'Inter',
                        fontSize: 14,
                        fontWeight: FontWeight.bold,
                        color: colorOnSurface,
                      ),
                    ),
                    const Text(
                      'Normal BP',
                      style: TextStyle(
                        fontFamily: 'Inter',
                        fontSize: 10.5,
                        color: colorOnSurfaceVariant,
                      ),
                    ),
                  ],
                ),
                const Text(
                  'Healthy',
                  style: TextStyle(
                    fontFamily: 'Inter',
                    fontSize: 10.5,
                    fontWeight: FontWeight.w600,
                    color: Color(0xFF10B981),
                  ),
                ),
              ],
            ),
          ),
        ),

        const SizedBox(width: 10),

        // Iron & Folic (Interactive Toggle)
        Expanded(
          child: InkWell(
            onTap: () {
              setState(() => _isIronFolicTaken = !_isIronFolicTaken);
            },
            borderRadius: BorderRadius.circular(18),
            child: Container(
              height: 116,
              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 10),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(18),
                border: Border.all(color: Colors.grey.shade100),
                boxShadow: [
                  BoxShadow(
                    color: Colors.black.withValues(alpha: 0.02),
                    blurRadius: 10,
                  ),
                ],
              ),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Container(
                    width: 36,
                    height: 36,
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      color: Colors.indigo.shade50,
                    ),
                    child: Icon(Icons.medication_rounded,
                        color: Colors.indigo.shade600, size: 18),
                  ),
                  const Column(
                    children: [
                      Text(
                        'Iron & Folic',
                        style: TextStyle(
                          fontFamily: 'Inter',
                          fontSize: 13.5,
                          fontWeight: FontWeight.bold,
                          color: colorOnSurface,
                        ),
                      ),
                      Text(
                        '1 Pill Daily',
                        style: TextStyle(
                          fontFamily: 'Inter',
                          fontSize: 10.5,
                          color: colorOnSurfaceVariant,
                        ),
                      ),
                    ],
                  ),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Icon(
                        _isIronFolicTaken
                            ? Icons.check_circle_rounded
                            : Icons.schedule_rounded,
                        size: 13,
                        color: _isIronFolicTaken
                            ? const Color(0xFF10B981)
                            : Colors.amber.shade700,
                      ),
                      const SizedBox(width: 3),
                      Text(
                        _isIronFolicTaken ? 'Taken' : 'Pending',
                        style: TextStyle(
                          fontFamily: 'Inter',
                          fontSize: 10.5,
                          fontWeight: FontWeight.w600,
                          color: _isIronFolicTaken
                              ? const Color(0xFF10B981)
                              : Colors.amber.shade700,
                        ),
                      ),
                    ],
                  ),
                ],
              ),
            ),
          ),
        ),
      ],
    );
  }

  // Next ANC Visit Card
  Widget _buildAncVisitCard() {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: Colors.grey.shade100),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withValues(alpha: 0.02),
            blurRadius: 20,
            offset: const Offset(0, 6),
          ),
        ],
      ),
      child: Row(
        children: [
          Container(
            width: 44,
            height: 44,
            decoration: BoxDecoration(
              color: const Color(0xFFE6F4F1),
              borderRadius: BorderRadius.circular(12),
            ),
            child: const Icon(
              Icons.calendar_month_rounded,
              color: Color(0xFF0F766E),
              size: 22,
            ),
          ),
          const SizedBox(width: 12),
          const Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Text(
                      'ANC VISIT 3 OF 4',
                      style: TextStyle(
                        fontFamily: 'Inter',
                        fontSize: 11,
                        fontWeight: FontWeight.bold,
                        letterSpacing: 0.5,
                        color: Color(0xFF0F766E),
                      ),
                    ),
                    SizedBox(width: 6),
                    Text(
                      'SMS Sent',
                      style: TextStyle(
                        fontFamily: 'Inter',
                        fontSize: 10,
                        fontWeight: FontWeight.w500,
                        color: colorOnSurfaceVariant,
                      ),
                    ),
                  ],
                ),
                SizedBox(height: 2),
                Text(
                  'Thu, 24 Oct • 9:00 AM',
                  style: TextStyle(
                    fontFamily: 'Inter',
                    fontSize: 14,
                    fontWeight: FontWeight.w600,
                    color: colorOnSurface,
                  ),
                ),
                Text(
                  'Bwera Health Centre III',
                  style: TextStyle(
                    fontFamily: 'Inter',
                    fontSize: 11,
                    color: colorOnSurfaceVariant,
                  ),
                ),
              ],
            ),
          ),
          ElevatedButton(
            onPressed: _showVisitDetails,
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.grey.shade100,
              foregroundColor: colorOnSurface,
              elevation: 0,
              padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(100),
              ),
            ),
            child: const Text(
              'Details',
              style: TextStyle(
                fontFamily: 'Inter',
                fontSize: 12,
                fontWeight: FontWeight.w600,
              ),
            ),
          ),
        ],
      ),
    );
  }

  // Emergency & Danger signs CTA in Home Tab
  Widget _buildEmergencyActions() {
    return Column(
      children: [
        // Report Danger signs card (switches to Danger Signs tab)
        InkWell(
          onTap: () => setState(() => _currentTab = 2),
          borderRadius: BorderRadius.circular(18),
          child: Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(18),
              border: Border.all(
                color: Colors.amber.shade200.withValues(alpha: 0.8),
              ),
              boxShadow: [
                BoxShadow(
                  color: Colors.black.withValues(alpha: 0.02),
                  blurRadius: 8,
                ),
              ],
            ),
            child: Row(
              children: [
                Container(
                  width: 36,
                  height: 36,
                  decoration: BoxDecoration(
                    color: Colors.amber.shade50,
                    shape: BoxShape.circle,
                  ),
                  child: Icon(Icons.warning_amber_rounded,
                      color: Colors.amber.shade700, size: 20),
                ),
                const SizedBox(width: 12),
                const Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        'Report Danger Signs',
                        style: TextStyle(
                          fontFamily: 'Inter',
                          fontSize: 13.5,
                          fontWeight: FontWeight.bold,
                          color: colorOnSurface,
                        ),
                      ),
                      Text(
                        'Bleeding, fever, blurred vision or pain',
                        style: TextStyle(
                          fontFamily: 'Inter',
                          fontSize: 11,
                          color: colorOnSurfaceVariant,
                        ),
                      ),
                    ],
                  ),
                ),
                Icon(Icons.chevron_right_rounded,
                    color: Colors.grey.shade400, size: 20),
              ],
            ),
          ),
        ),

        const SizedBox(height: 12),

        // 24/7 Emergency Dispatch CTA Button
        SizedBox(
          width: double.infinity,
          height: 52,
          child: ElevatedButton.icon(
            onPressed: () => _makeCall('112'),
            style: ElevatedButton.styleFrom(
              backgroundColor: const Color(0xFF0F766E),
              foregroundColor: Colors.white,
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(100),
              ),
              elevation: 1,
            ),
            icon: const Icon(Icons.call, size: 20),
            label: const Text(
              'Emergency Call (Toll-Free 24/7)',
              style: TextStyle(
                fontFamily: 'Inter',
                fontSize: 14,
                fontWeight: FontWeight.w600,
              ),
            ),
          ),
        ),
      ],
    );
  }

  // Floating Bottom Navigation Bar
  Widget _buildBottomNav() {
    return Container(
      decoration: BoxDecoration(
        color: Colors.white.withValues(alpha: 0.95),
        border: Border(
          top: BorderSide(color: Colors.grey.shade100, width: 1),
        ),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withValues(alpha: 0.04),
            blurRadius: 20,
            offset: const Offset(0, -4),
          ),
        ],
      ),
      child: SafeArea(
        top: false,
        child: Center(
          child: ConstrainedBox(
            constraints: const BoxConstraints(maxWidth: 720),
            child: SizedBox(
              height: 64,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceAround,
                children: [
                  _buildNavItem(0, Icons.home_rounded, 'Home'),
                  _buildNavItem(1, Icons.monitor_heart_rounded, 'My Health'),
                  _buildNavItem(
                      2, Icons.health_and_safety_rounded, 'Warning Signs'),
                  _buildNavItem(3, Icons.event_available_rounded, 'Visits'),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildNavItem(int index, IconData icon, String label) {
    final isSelected = _currentTab == index;
    return InkWell(
      onTap: () {
        setState(() => _currentTab = index);
      },
      borderRadius: BorderRadius.circular(12),
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(
              icon,
              size: 24,
              color: isSelected
                  ? colorPrimaryContainer
                  : Colors.grey.shade400,
            ),
            const SizedBox(height: 3),
            Text(
              label,
              style: TextStyle(
                fontFamily: 'Inter',
                fontSize: 11,
                fontWeight: isSelected ? FontWeight.w700 : FontWeight.w500,
                color: isSelected
                    ? colorPrimaryContainer
                    : Colors.grey.shade400,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
