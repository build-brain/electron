import 'package:electron/presentation/screens/root.dart';
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

final GlobalKey<NavigatorState> _rootNavigatorKey = GlobalKey<NavigatorState>();
final GlobalKey<NavigatorState> _shellNavigatorKey =
    GlobalKey<NavigatorState>();

final GoRouter _router = GoRouter(
  navigatorKey: _rootNavigatorKey,
  initialLocation: '/',
  routes: [
    ShellRoute(
      navigatorKey: _shellNavigatorKey,
      builder: (context, state, child) {
        return RootScreen(child: child);
      },
      routes: [
        GoRoute(
          path: '/dashboard',
          builder: (context, state) {
            return Container();
          },
          routes: <RouteBase>[
            GoRoute(
              path: 'details',
              builder: (BuildContext context, GoRouterState state) {
                return Container();
              },
            ),
          ],
        ),
        GoRoute(
          path: '/rooms',
          builder: (BuildContext context, GoRouterState state) {
            return Container();
          },
          routes: <RouteBase>[
            GoRoute(
              path: 'details',
              parentNavigatorKey: _rootNavigatorKey,
              builder: (BuildContext context, GoRouterState state) {
                return Container();
              },
            ),
          ],
        ),
        GoRoute(
          path: '/devices',
          builder: (BuildContext context, GoRouterState state) {
            return Container();
          },
          routes: <RouteBase>[
            GoRoute(
              path: 'details',
              parentNavigatorKey: _rootNavigatorKey,
              builder: (BuildContext context, GoRouterState state) {
                return Container();
              },
            ),
          ],
        ),
      ],
    ),
  ],
);
