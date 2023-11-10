from core.router import DefaultRouter
from api.management.urls import router as management_router
from api.smartapp.urls import router as smartapp_router

router = DefaultRouter()
router.extend(management_router)
router.extend(smartapp_router)


