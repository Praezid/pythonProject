from .views import RestaurantViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r's', RestaurantViewSet, basename='restaurant')
urlpatterns = router.urls
