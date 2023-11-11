import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';
import 'package:electron/presentation/screens/login/login_screen.dart';

class ElectronEcoApp extends StatelessWidget {
  const ElectronEcoApp({super.key});

  @override
  Widget build(BuildContext context) {
    return ScreenUtilInit(
      designSize: const Size(414, 896),
      minTextAdapt: true,
      splitScreenMode: true,
      builder: (context, child) {
        return MaterialApp(
          home: child,
          theme: ThemeData(
            fontFamily: 'Nunito',
          ),
        );
      },
      child: const LoginScreen(),
    );
  }
}
