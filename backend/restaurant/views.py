from .permissions import IsAdminUserOrReadOnly
from .models import Restaurant
from .serializer import RestaurantSerializer
from rest_framework import viewsets


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = (IsAdminUserOrReadOnly, )
