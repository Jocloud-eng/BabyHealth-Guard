import 'package:flutter/material.dart';

/// Maternal Profile Registration Screen
/// Matches the official Tailwind / Material Design spec for BabyHealth Guard.
class MotherRegistrationScreen extends StatefulWidget {
  const MotherRegistrationScreen({super.key});

  @override
  State<MotherRegistrationScreen> createState() => _MotherRegistrationScreenState();
}

class _MotherRegistrationScreenState extends State<MotherRegistrationScreen> {
  final _formKey = GlobalKey<FormState>();
  final _nameController = TextEditingController();
  final _ageController = TextEditingController();
  final _villageController = TextEditingController();
  final _phoneController = TextEditingController();

  // State variables matching interactive form controls
  bool _hasPhoto = false;
  String _selectedLanguage = 'Luganda';
  String _maternalStatus = 'expecting'; // 'expecting' or 'baby'
  String _pregnancyStage = '4 - 6 Mo'; // '1 - 3 Mo', '4 - 6 Mo', '7 - 9 Mo'
  String _parity = 'First Baby (1st)'; // 'First Baby (1st)', '2nd or More'
  final Set<String> _selectedConditions = {'None'};
  bool _isLoading = false;

  // Exact theme color palette from spec
  static const Color colorSurface = Color(0xFFFAF8FF);
  static const Color colorOnSurface = Color(0xFF131B2E);
  static const Color colorOnSurfaceVariant = Color(0xFF3F484C);
  static const Color colorPrimary = Color(0xFF005A71);
  static const Color colorPrimaryContainer = Color(0xFF0E7490);
  static const Color colorOnPrimary = Color(0xFFFFFFFF);
  static const Color colorSurfaceLowest = Color(0xFFFFFFFF);
  static const Color colorSurfaceLow = Color(0xFFF2F3FF);
  static const Color colorSurfaceHigh = Color(0xFFE2E7FF);
  static const Color colorOutline = Color(0xFF6F787D);

  @override
  void dispose() {
    _nameController.dispose();
    _ageController.dispose();
    _villageController.dispose();
    _phoneController.dispose();
    super.dispose();
  }

  void _toggleCondition(String condition) {
    setState(() {
      if (condition == 'None') {
        _selectedConditions.clear();
        _selectedConditions.add('None');
      } else {
        _selectedConditions.remove('None');
        if (_selectedConditions.contains(condition)) {
          _selectedConditions.remove(condition);
          if (_selectedConditions.isEmpty) {
            _selectedConditions.add('None');
          }
        } else {
          _selectedConditions.add(condition);
        }
      }
    });
  }

  void _saveProfile() {
    if (_formKey.currentState?.validate() ?? false) {
      setState(() => _isLoading = true);
      Future.delayed(const Duration(milliseconds: 600), () {
        if (!mounted) return;
        setState(() => _isLoading = false);
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            backgroundColor: colorPrimaryContainer,
            behavior: SnackBarBehavior.floating,
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
            content: Row(
              children: [
                const Icon(Icons.check_circle_rounded, color: Colors.white, size: 22),
                const SizedBox(width: 12),
                Expanded(
                  child: Text(
                    'Profile saved for ${_nameController.text.trim().isEmpty ? 'Mother' : _nameController.text.trim()}! Offline & ready to sync.',
                    style: const TextStyle(fontWeight: FontWeight.w600, fontSize: 13),
                  ),
                ),
              ],
            ),
          ),
        );
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: colorSurface,
      appBar: PreferredSize(
        preferredSize: const Size.fromHeight(64),
        child: Container(
          decoration: BoxDecoration(
            color: colorSurface.withValues(alpha: 0.92),
            boxShadow: const [
              BoxShadow(
                color: Color(0x0A000000),
                blurRadius: 8,
                offset: Offset(0, 1),
              ),
            ],
          ),
          child: SafeArea(
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 16.0),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Row(
                    children: [
                      InkWell(
                        onTap: () => Navigator.of(context).pop(),
                        borderRadius: BorderRadius.circular(8),
                        child: Container(
                          width: 44,
                          height: 44,
                          alignment: Alignment.center,
                          child: const Icon(
                            Icons.arrow_back,
                            size: 20,
                            color: colorOnSurface,
                          ),
                        ),
                      ),
                      const SizedBox(width: 8),
                      const Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Text(
                            'BABYHEALTH GUARD',
                            style: TextStyle(
                              fontFamily: 'Inter',
                              fontSize: 11,
                              fontWeight: FontWeight.w600,
                              letterSpacing: 0.8,
                              color: colorPrimary,
                            ),
                          ),
                          Text(
                            'Maternal Profile Details',
                            style: TextStyle(
                              fontFamily: 'Inter',
                              fontSize: 16,
                              fontWeight: FontWeight.w600,
                              color: colorOnSurface,
                              height: 1.2,
                            ),
                          ),
                        ],
                      ),
                    ],
                  ),
                  Container(
                    width: 32,
                    height: 32,
                    decoration: const BoxDecoration(
                      shape: BoxShape.circle,
                      color: colorPrimary,
                    ),
                    alignment: Alignment.center,
                    child: const Icon(
                      Icons.person,
                      size: 18,
                      color: colorOnPrimary,
                    ),
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
      body: SafeArea(
        top: false,
        child: SingleChildScrollView(
          physics: const BouncingScrollPhysics(),
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
          child: Form(
            key: _formKey,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // Page Header Title
                const SizedBox(height: 6),
                const Text(
                  'Create Profile',
                  style: TextStyle(
                    fontFamily: 'Inter',
                    fontSize: 24,
                    fontWeight: FontWeight.w600,
                    letterSpacing: -0.2,
                    color: colorOnSurface,
                  ),
                ),
                const SizedBox(height: 4),
                const Text(
                  'Free for all mothers',
                  style: TextStyle(
                    fontFamily: 'Inter',
                    fontSize: 12,
                    fontWeight: FontWeight.w400,
                    color: colorOnSurfaceVariant,
                  ),
                ),
                const SizedBox(height: 16),

                // Card 1: Add Photo Card
                _buildCard(
                  child: Row(
                    children: [
                      GestureDetector(
                        onTap: () {
                          setState(() => _hasPhoto = !_hasPhoto);
                        },
                        child: Container(
                          width: 64,
                          height: 64,
                          decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            color: colorSurfaceLow,
                            border: Border.all(
                              color: colorPrimary.withValues(alpha: 0.3),
                              width: 1.5,
                            ),
                            boxShadow: const [
                              BoxShadow(
                                color: Color(0x0D000000),
                                blurRadius: 4,
                                offset: Offset(0, 1),
                              ),
                            ],
                          ),
                          alignment: Alignment.center,
                          child: Icon(
                            _hasPhoto ? Icons.check_circle_rounded : Icons.add_a_photo,
                            size: 28,
                            color: colorPrimary,
                          ),
                        ),
                      ),
                      const SizedBox(width: 16),
                      Expanded(
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            InkWell(
                              onTap: () {
                                setState(() => _hasPhoto = !_hasPhoto);
                              },
                              child: Row(
                                mainAxisSize: MainAxisSize.min,
                                children: [
                                  Text(
                                    _hasPhoto ? 'Photo Added' : 'Add Your Photo (Required)',
                                    style: const TextStyle(
                                      fontFamily: 'Inter',
                                      fontSize: 12,
                                      fontWeight: FontWeight.w600,
                                      color: colorPrimary,
                                    ),
                                  ),
                                  const SizedBox(width: 4),
                                  const Icon(
                                    Icons.photo_camera,
                                    size: 16,
                                    color: colorPrimary,
                                  ),
                                ],
                              ),
                            ),
                            const SizedBox(height: 2),
                            const Text(
                              'Helps midwives recognize you at the clinic',
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
                    ],
                  ),
                ),

                const SizedBox(height: 16),

                // Card 2: Personal Details Card
                _buildCard(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      _buildSectionHeader('PERSONAL DETAILS'),
                      const SizedBox(height: 14),

                      // Full Name
                      _buildInputLabel('Full Name'),
                      const SizedBox(height: 6),
                      _buildTextInput(
                        controller: _nameController,
                        hint: 'e.g. Amina Brenda',
                        icon: Icons.person,
                      ),
                      const SizedBox(height: 14),

                      // Mother's Age & Village Grid
                      Row(
                        children: [
                          Expanded(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                _buildInputLabel("Mother's Age"),
                                const SizedBox(height: 6),
                                _buildTextInput(
                                  controller: _ageController,
                                  hint: '24 yrs',
                                  icon: Icons.cake,
                                  keyboardType: TextInputType.number,
                                ),
                              ],
                            ),
                          ),
                          const SizedBox(width: 10),
                          Expanded(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                _buildInputLabel('Village / Location'),
                                const SizedBox(height: 6),
                                _buildTextInput(
                                  controller: _villageController,
                                  hint: 'Village name',
                                  icon: Icons.location_on,
                                ),
                              ],
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 14),

                      // Mobile Phone Number with +256 badge
                      _buildInputLabel('Mobile Phone Number'),
                      const SizedBox(height: 6),
                      Container(
                        height: 48,
                        decoration: BoxDecoration(
                          color: colorSurfaceLow,
                          borderRadius: BorderRadius.circular(12),
                          boxShadow: const [
                            BoxShadow(
                              color: Color(0x08000000),
                              blurRadius: 3,
                              offset: Offset(0, 1),
                            ),
                          ],
                        ),
                        padding: const EdgeInsets.symmetric(horizontal: 14),
                        child: Row(
                          children: [
                            const Icon(Icons.call, size: 18, color: colorPrimary),
                            const SizedBox(width: 6),
                            const Text(
                              '+256',
                              style: TextStyle(
                                fontFamily: 'Inter',
                                fontSize: 13,
                                fontWeight: FontWeight.w600,
                                color: colorOnSurface,
                              ),
                            ),
                            Container(
                              height: 20,
                              width: 1,
                              color: colorOutline.withValues(alpha: 0.25),
                              margin: const EdgeInsets.symmetric(horizontal: 10),
                            ),
                            Expanded(
                              child: TextField(
                                controller: _phoneController,
                                keyboardType: TextInputType.phone,
                                style: const TextStyle(
                                  fontFamily: 'Inter',
                                  fontSize: 15,
                                  color: colorOnSurface,
                                ),
                                decoration: InputDecoration(
                                  hintText: '772 000 000',
                                  hintStyle: TextStyle(
                                    fontFamily: 'Inter',
                                    fontSize: 14,
                                    color: colorOutline.withValues(alpha: 0.6),
                                  ),
                                  border: InputBorder.none,
                                  isDense: true,
                                  contentPadding: EdgeInsets.zero,
                                ),
                              ),
                            ),
                          ],
                        ),
                      ),
                      const SizedBox(height: 14),

                      // Preferred Language for SMS Alerts
                      _buildInputLabel('Preferred Language for SMS Alerts'),
                      const SizedBox(height: 6),
                      Row(
                        children: [
                          _buildLanguageButton('Luganda'),
                          const SizedBox(width: 8),
                          _buildLanguageButton('English'),
                          const SizedBox(width: 8),
                          _buildLanguageButton('Swahili'),
                        ],
                      ),
                    ],
                  ),
                ),

                const SizedBox(height: 16),

                // Card 3: Pregnancy & Health Card
                _buildCard(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      _buildSectionHeader('PREGNANCY & HEALTH'),
                      const SizedBox(height: 14),

                      // Current Maternal Status Toggle
                      _buildInputLabel('Current Maternal Status'),
                      const SizedBox(height: 8),
                      Row(
                        children: [
                          Expanded(
                            child: _buildStatusToggle(
                              title: 'Expecting',
                              icon: Icons.pregnant_woman,
                              isSelected: _maternalStatus == 'expecting',
                              onTap: () => setState(() => _maternalStatus = 'expecting'),
                            ),
                          ),
                          const SizedBox(width: 10),
                          Expanded(
                            child: _buildStatusToggle(
                              title: 'Newborn Baby',
                              icon: Icons.child_care,
                              isSelected: _maternalStatus == 'baby',
                              onTap: () => setState(() => _maternalStatus = 'baby'),
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 14),

                      // Stage / Pregnancy Month (only visible when Expecting)
                      if (_maternalStatus == 'expecting') ...[
                        _buildInputLabel('Stage / Pregnancy Month'),
                        const SizedBox(height: 6),
                        Row(
                          children: [
                            _buildPillButton(
                              text: '1 - 3 Mo',
                              isSelected: _pregnancyStage == '1 - 3 Mo',
                              onTap: () => setState(() => _pregnancyStage = '1 - 3 Mo'),
                            ),
                            const SizedBox(width: 8),
                            _buildPillButton(
                              text: '4 - 6 Mo',
                              isSelected: _pregnancyStage == '4 - 6 Mo',
                              onTap: () => setState(() => _pregnancyStage = '4 - 6 Mo'),
                            ),
                            const SizedBox(width: 8),
                            _buildPillButton(
                              text: '7 - 9 Mo',
                              isSelected: _pregnancyStage == '7 - 9 Mo',
                              onTap: () => setState(() => _pregnancyStage = '7 - 9 Mo'),
                            ),
                          ],
                        ),
                        const SizedBox(height: 14),
                      ],

                      // Number of Births (Parity)
                      _buildInputLabel('Number of Births (Parity)'),
                      const SizedBox(height: 6),
                      Row(
                        children: [
                          _buildPillButton(
                            text: 'First Baby (1st)',
                            isSelected: _parity == 'First Baby (1st)',
                            onTap: () => setState(() => _parity = 'First Baby (1st)'),
                          ),
                          const SizedBox(width: 10),
                          _buildPillButton(
                            text: '2nd or More',
                            isSelected: _parity == '2nd or More',
                            onTap: () => setState(() => _parity = '2nd or More'),
                          ),
                        ],
                      ),
                      const SizedBox(height: 14),

                      // Any Known Health Conditions?
                      _buildInputLabel('Any Known Health Conditions?'),
                      const SizedBox(height: 8),
                      Wrap(
                        spacing: 8,
                        runSpacing: 8,
                        children: [
                          _buildConditionChip('None', Icons.check),
                          _buildConditionChip('High BP', Icons.monitor_heart_outlined),
                          _buildConditionChip('Anemia', Icons.bloodtype_outlined),
                          _buildConditionChip('Other', Icons.medication_outlined),
                        ],
                      ),
                    ],
                  ),
                ),

                const SizedBox(height: 20),

                // Bottom Action: Save & Continue
                SizedBox(
                  width: double.infinity,
                  height: 56,
                  child: ElevatedButton(
                    onPressed: _isLoading ? null : _saveProfile,
                    style: ElevatedButton.styleFrom(
                      backgroundColor: colorPrimaryContainer,
                      foregroundColor: colorOnPrimary,
                      elevation: 2,
                      shadowColor: colorPrimaryContainer.withValues(alpha: 0.35),
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(28),
                      ),
                    ),
                    child: _isLoading
                        ? const SizedBox(
                            width: 22,
                            height: 22,
                            child: CircularProgressIndicator(
                              color: Colors.white,
                              strokeWidth: 2.5,
                            ),
                          )
                        : const Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Text(
                                'Save & Continue',
                                style: TextStyle(
                                  fontFamily: 'Inter',
                                  fontSize: 15,
                                  fontWeight: FontWeight.w600,
                                ),
                              ),
                              SizedBox(width: 8),
                              Icon(Icons.arrow_forward, size: 20),
                            ],
                          ),
                  ),
                ),

                const SizedBox(height: 12),

                // Offline accessibility tag
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Container(
                      width: 8,
                      height: 8,
                      decoration: const BoxDecoration(
                        shape: BoxShape.circle,
                        color: colorPrimary,
                      ),
                    ),
                    const SizedBox(width: 6),
                    const Text(
                      'Works offline • Free *920# access',
                      style: TextStyle(
                        fontFamily: 'Inter',
                        fontSize: 12,
                        fontWeight: FontWeight.w400,
                        color: colorOnSurfaceVariant,
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 24),
              ],
            ),
          ),
        ),
      ),
    );
  }

  // --- Helper Widgets ---

  Widget _buildCard({required Widget child}) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: colorSurfaceLowest,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(
          color: colorOutline.withValues(alpha: 0.18),
          width: 1,
        ),
        boxShadow: const [
          BoxShadow(
            color: Color(0x06000000),
            blurRadius: 4,
            offset: Offset(0, 1),
          ),
        ],
      ),
      child: child,
    );
  }

  Widget _buildSectionHeader(String title) {
    return Container(
      padding: const EdgeInsets.only(bottom: 6),
      decoration: BoxDecoration(
        border: Border(
          bottom: BorderSide(
            color: colorOutline.withValues(alpha: 0.18),
            width: 1,
          ),
        ),
      ),
      child: Text(
        title,
        style: const TextStyle(
          fontFamily: 'Inter',
          fontSize: 11,
          fontWeight: FontWeight.w600,
          letterSpacing: 0.8,
          color: colorPrimary,
        ),
      ),
    );
  }

  Widget _buildInputLabel(String label) {
    return Text(
      label,
      style: const TextStyle(
        fontFamily: 'Inter',
        fontSize: 12,
        fontWeight: FontWeight.w600,
        color: colorOnSurface,
      ),
    );
  }

  Widget _buildTextInput({
    required TextEditingController controller,
    required String hint,
    required IconData icon,
    TextInputType keyboardType = TextInputType.text,
  }) {
    return Container(
      height: 48,
      decoration: BoxDecoration(
        color: colorSurfaceLow,
        borderRadius: BorderRadius.circular(12),
        boxShadow: const [
          BoxShadow(
            color: Color(0x08000000),
            blurRadius: 3,
            offset: Offset(0, 1),
          ),
        ],
      ),
      padding: const EdgeInsets.symmetric(horizontal: 14),
      alignment: Alignment.center,
      child: Row(
        children: [
          Icon(icon, size: 20, color: colorPrimary),
          const SizedBox(width: 10),
          Expanded(
            child: TextField(
              controller: controller,
              keyboardType: keyboardType,
              style: const TextStyle(
                fontFamily: 'Inter',
                fontSize: 15,
                color: colorOnSurface,
              ),
              decoration: InputDecoration(
                hintText: hint,
                hintStyle: TextStyle(
                  fontFamily: 'Inter',
                  fontSize: 14,
                  color: colorOutline.withValues(alpha: 0.6),
                ),
                border: InputBorder.none,
                isDense: true,
                contentPadding: EdgeInsets.zero,
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildLanguageButton(String language) {
    final isSelected = _selectedLanguage == language;
    return Expanded(
      child: InkWell(
        onTap: () => setState(() => _selectedLanguage = language),
        borderRadius: BorderRadius.circular(12),
        child: Container(
          height: 44,
          decoration: BoxDecoration(
            color: isSelected ? colorSurfaceHigh : colorSurfaceLow,
            borderRadius: BorderRadius.circular(12),
            border: Border.all(
              color: isSelected ? colorPrimary.withValues(alpha: 0.25) : Colors.transparent,
              width: 1,
            ),
            boxShadow: const [
              BoxShadow(
                color: Color(0x08000000),
                blurRadius: 3,
                offset: Offset(0, 1),
              ),
            ],
          ),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Icon(
                Icons.sms_outlined,
                size: 16,
                color: isSelected ? colorPrimary : colorOnSurfaceVariant,
              ),
              const SizedBox(width: 4),
              Text(
                language,
                style: TextStyle(
                  fontFamily: 'Inter',
                  fontSize: 12,
                  fontWeight: isSelected ? FontWeight.w600 : FontWeight.w500,
                  color: isSelected ? colorPrimary : colorOnSurfaceVariant,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildStatusToggle({
    required String title,
    required IconData icon,
    required bool isSelected,
    required VoidCallback onTap,
  }) {
    return InkWell(
      onTap: onTap,
      borderRadius: BorderRadius.circular(12),
      child: Container(
        height: 56,
        padding: const EdgeInsets.symmetric(horizontal: 12),
        decoration: BoxDecoration(
          color: isSelected ? colorSurfaceHigh : colorSurfaceLow,
          borderRadius: BorderRadius.circular(12),
          border: Border.all(
            color: isSelected ? colorPrimary.withValues(alpha: 0.3) : Colors.transparent,
            width: 1.2,
          ),
          boxShadow: const [
            BoxShadow(
              color: Color(0x08000000),
              blurRadius: 3,
              offset: Offset(0, 1),
            ),
          ],
        ),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(
              icon,
              size: 20,
              color: isSelected ? colorPrimary : colorOnSurfaceVariant,
            ),
            const SizedBox(width: 8),
            Text(
              title,
              style: TextStyle(
                fontFamily: 'Inter',
                fontSize: 12,
                fontWeight: isSelected ? FontWeight.w600 : FontWeight.w500,
                color: isSelected ? colorPrimary : colorOnSurfaceVariant,
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildPillButton({
    required String text,
    required bool isSelected,
    required VoidCallback onTap,
  }) {
    return Expanded(
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(12),
        child: Container(
          height: 44,
          decoration: BoxDecoration(
            color: isSelected ? colorSurfaceHigh : colorSurfaceLow,
            borderRadius: BorderRadius.circular(12),
            border: Border.all(
              color: isSelected ? colorPrimary.withValues(alpha: 0.25) : Colors.transparent,
              width: 1,
            ),
          ),
          alignment: Alignment.center,
          child: Text(
            text,
            style: TextStyle(
              fontFamily: 'Inter',
              fontSize: 12,
              fontWeight: isSelected ? FontWeight.w600 : FontWeight.w500,
              color: isSelected ? colorPrimary : colorOnSurfaceVariant,
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildConditionChip(String label, IconData icon) {
    final isSelected = _selectedConditions.contains(label);
    return InkWell(
      onTap: () => _toggleCondition(label),
      borderRadius: BorderRadius.circular(20),
      child: Container(
        height: 36,
        padding: const EdgeInsets.symmetric(horizontal: 12),
        decoration: BoxDecoration(
          color: isSelected ? colorSurfaceHigh : colorSurfaceLow,
          borderRadius: BorderRadius.circular(18),
          border: Border.all(
            color: isSelected ? colorPrimary.withValues(alpha: 0.25) : Colors.transparent,
            width: 1,
          ),
        ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(
              icon,
              size: 14,
              color: isSelected ? colorPrimary : colorOnSurfaceVariant,
            ),
            const SizedBox(width: 5),
            Text(
              label,
              style: TextStyle(
                fontFamily: 'Inter',
                fontSize: 11,
                fontWeight: isSelected ? FontWeight.w600 : FontWeight.w500,
                color: isSelected ? colorPrimary : colorOnSurfaceVariant,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
