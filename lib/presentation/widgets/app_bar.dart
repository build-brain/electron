import 'package:electron/presentation/utils/assets.dart';
import 'package:flutter/material.dart';
import 'package:flutter_screenutil/flutter_screenutil.dart';

// class CustomAppBar extends StatelessWidget {
//   const CustomAppBar({super.key});

//   @override
//   Widget build(BuildContext context) {
//     return AppBar(
//       automaticallyImplyLeading: false,
//       elevation: 0.0,
//       backgroundColor: Colors.white,
//       title: Container(
//         height: 150.0.h,
//         color: Colors.amber,
//       ),
//       // bottom: PreferredSize(
//       //   preferredSize: Size.fromHeight(50.0.h),
//       //   child: Container(
//       //     height: 40.0.h,
//       //     // color: Colors.amber,
//       //     decoration: BoxDecoration(
//       //       // borderRadius: BorderRadius.horizontal(
//       //       //   left: Radius.circular(30.0.r),
//       //       // ),
//       //       borderRadius: BorderRadius.only(
//       //         bottomLeft: Radius.circular(20.0.r),
//       //         bottomRight: Radius.circular(20.0.r),
//       //       ),
//       //       color: Colors.white,
//       //       boxShadow: [
//       //         BoxShadow(
//       //           offset: const Offset(1, 5),
//       //           color: Colors.grey,
//       //           blurRadius: 3.0.r,
//       //           // spreadRadius: 1.0,
//       //         ),
//       //       ],
//       //     ),
//       //   ),
//       // ),
//     );
//   }
// }

class CustomAppBar extends StatelessWidget {
  const CustomAppBar({super.key});

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Container(
        height: 145.0.h,
        padding: EdgeInsets.only(
          left: 20.0.w,
          right: 20.0.w,
          bottom: 30.0.h,
        ),
        decoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.only(
            bottomLeft: Radius.circular(30.0.r),
            bottomRight: Radius.circular(30.0.r),
          ),
          boxShadow: [
            BoxShadow(
              offset: Offset(1.0.w, 5.0.h),
              color: Colors.grey,
              blurRadius: 3.0.r,
            ),
          ],
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      'November 11, 2023',
                      style: TextStyle(
                          fontSize: 14.0.sp,
                          fontWeight: FontWeight.w400,
                          color: const Color(0xFF2666DE)),
                    ),
                    SizedBox(height: 10.0.h),
                    Text(
                      'Electron',
                      style: TextStyle(
                        fontSize: 25.0.sp,
                        fontWeight: FontWeight.w700,
                      ),
                    ),
                  ],
                ),
                SizedBox(
                  height: 53.0.h,
                  width: 53.0.w,
                  child: const CircleAvatar(
                    backgroundImage: AssetImage(
                      ElectronAssets.avatar,
                    ),
                  ),
                ),
              ],
            ),
            Row(
              children: [
                Expanded(
                  child: Row(
                    children: [
                      Badge(
                        smallSize: 12.0.dm,
                        backgroundColor: Color(0xFF1BE08E),
                      ),
                      SizedBox(
                        width: 10.0.w,
                        height: 17.0.h,
                      ),
                      Text(
                        '20 devices running',
                        style: TextStyle(
                          fontSize: 14.sp,
                          fontWeight: FontWeight.w400,
                        ),
                      ),
                    ],
                  ),
                ),
                Text('damage - 48%'),
              ],
            ),
            Row(
              children: [
                Expanded(
                  child: Row(
                    children: [
                      Badge(
                        smallSize: 12.0.dm,
                        backgroundColor: Color(0xFF1BE08E),
                      ),
                      SizedBox(
                        width: 10.0.w,
                        height: 17.0.h,
                      ),
                      Text(
                        'Solar battery level',
                        style: TextStyle(
                          fontSize: 14.sp,
                          fontWeight: FontWeight.w400,
                        ),
                      ),
                    ],
                  ),
                ),
                Text('38% not charging'),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
