from .views import EmployeeViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r's', EmployeeViewSet, basename='employee')
urlpatterns = router.urls
