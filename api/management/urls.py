from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'user', UserViewSet)
router.register(r'panel', PanelViewSet)

urlpatterns = router.urls
