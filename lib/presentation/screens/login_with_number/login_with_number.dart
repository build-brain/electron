import 'package:electron/presentation/screens/verify/verify_screen.dart';
import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';

class LoginWithNumberScreen extends StatelessWidget {
  const LoginWithNumberScreen();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: SafeArea(
        child: Center(
          child: Column(
            children: [
              SizedBox(height: 83.0.h),
              Text(
                'Log in with\nNumber',
                textAlign: TextAlign.center,
                style: TextStyle(
                  fontSize: 32.0.sp,
                  fontWeight: FontWeight.w900,
                ),
              ),
              SizedBox(height: 125.0.h),
              TextField(
                decoration: InputDecoration(
                  // prefix: Text('+998', style: TextStyle(color: Colors.black)),
                  // prefixStyle: TextStyle(
                  //   color: Color(0xFFA1A4B2),
                  // ),
                  // prefixText: '+998',
                  // labelText: '+998',
                  // prefixText: '+998',
                  // prefixStyle: TextStyle(
                  //   fontSize: 16.0.sp,
                  //   color: const Color(0xFFA1A4B2),
                  // ),

/*****************************************************************************/
                  // prefixText: '+998  ',
                  // prefixStyle: TextStyle(
                  //   fontSize: 16.0.sp,
                  //   color: const Color(0xFFA1A4B2),
                  // ),
/*****************************************************************************/

                  prefixIcon: ConstrainedBox(
                    constraints: BoxConstraints.tightFor(width: 60.0.w),
                    child: Center(
                      child: Text(
                        '+998',
                        style: TextStyle(
                          fontSize: 16.0.sp,
                          color: const Color(0xFFA1A4B2),
                        ),
                      ),
                    ),
                  ),
                  // prefixIconConstraints:
                  //     BoxConstraints.tightFor(height: 63.0.h),
                  // contentPadding: EdgeInsets.only(left: 19.0.w, right: 19.0.w),
                  // hintText: '+998',

                  // hintStyle: TextStyle(
                  //   color: Color(0xFFA1A4B2),
                  // ),
                  filled: true,
                  fillColor: const Color(0xFFF2F3F7),
                  border: OutlineInputBorder(
                    borderSide: BorderSide.none,
                    borderRadius: BorderRadius.circular(15.0.r),
                  ),
                  constraints: BoxConstraints.tight(
                    Size(350.0.w, 63.0.h),
                  ),
                ),
              ),
              SizedBox(height: 101.h),
              Hero(
                tag: 'button',
                child: ElevatedButton(
                  onPressed: () {
                    Navigator.of(context).pushAndRemoveUntil(
                      MaterialPageRoute(
                        builder: (context) => const VerifyScreen(),
                      ),
                      (route) => false,
                    );
                    // Navigator.of(context).push();
                  },
                  style: ButtonStyle(
                    backgroundColor: MaterialStateProperty.all<Color>(
                      const Color(0xFF2666DE),
                    ),
                    shape: MaterialStateProperty.all<OutlinedBorder>(
                      RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(15.0.r),
                      ),
                    ),
                    fixedSize: MaterialStateProperty.all(Size(300.0.w, 60.0.h)),
                  ),
                  child: Text(
                    'Continue',
                    style: TextStyle(
                      fontSize: 24.0.sp,
                      fontWeight: FontWeight.w800,
                      color: Colors.white,
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
}
