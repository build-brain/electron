from rest_framework import routers
from .views import *


router = routers.DefaultRouter()

router.register(r'home', HomeViewSet)
router.register(r'room', RoomViewSet)
router.register(r'device', DeviceViewSet)
router.register(r'room-type', RoomTypeViewSet)
router.register(r'device-type', DeviceTypeViewSet)

urlpatterns = router.urls
