import 'package:flutter/material.dart';
import '../../../../core/theme/app_colors.dart';

/// Accessibility indicator showcasing offline-first readiness and USSD free access (*920#)
/// designed specifically for mothers in rural and low-connectivity communities.
class OfflineIndicatorBar extends StatefulWidget {
  const OfflineIndicatorBar({super.key});

  @override
  State<OfflineIndicatorBar> createState() => _OfflineIndicatorBarState();
}

class _OfflineIndicatorBarState extends State<OfflineIndicatorBar>
    with SingleTickerProviderStateMixin {
  late AnimationController _pulseController;
  late Animation<double> _pulseScale;

  @override
  void initState() {
    super.initState();
    _pulseController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 2200),
    )..repeat(reverse: true);

    _pulseScale = Tween<double>(begin: 0.85, end: 1.25).animate(
      CurvedAnimation(parent: _pulseController, curve: Curves.easeInOut),
    );
  }

  @override
  void dispose() {
    _pulseController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            // Pulsing Emerald Green Dot
            AnimatedBuilder(
              animation: _pulseScale,
              builder: (context, child) {
                return Container(
                  width: 8,
                  height: 8,
                  decoration: BoxDecoration(
                    color: AppColors.emerald500,
                    shape: BoxShape.circle,
                    boxShadow: [
                      BoxShadow(
                        color: AppColors.emerald500.withValues(alpha: 0.5),
                        blurRadius: 4 * _pulseScale.value,
                        spreadRadius: 1 * _pulseScale.value,
                      ),
                    ],
                  ),
                );
              },
            ),
            const SizedBox(width: 8),

            // "Works offline" label
            const Text(
              'Works offline',
              style: TextStyle(
                fontFamily: 'Plus Jakarta Sans',
                fontSize: 12.5,
                fontWeight: FontWeight.w500,
                color: AppColors.stone600,
              ),
            ),

            const SizedBox(width: 8),
            const Text(
              '•',
              style: TextStyle(
                color: AppColors.stone400,
                fontSize: 12,
              ),
            ),
            const SizedBox(width: 8),

            // USSD pill badge
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
              decoration: BoxDecoration(
                color: AppColors.stone200.withValues(alpha: 0.65),
                borderRadius: BorderRadius.circular(6),
              ),
              child: const Text(
                'Free *920# access',
                style: TextStyle(
                  fontFamily: 'Plus Jakarta Sans',
                  fontSize: 12,
                  fontWeight: FontWeight.w700,
                  letterSpacing: 0.3,
                  color: AppColors.stone700,
                ),
              ),
            ),
          ],
        ),

        const SizedBox(height: 12),

        // iOS Home Bar Indicator
        Container(
          width: 128,
          height: 4,
          decoration: BoxDecoration(
            color: AppColors.stone800.withValues(alpha: 0.2),
            borderRadius: BorderRadius.circular(99),
          ),
        ),
      ],
    );
  }
}
