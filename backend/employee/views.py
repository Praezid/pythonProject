from .models import Employee
from .serializer import EmployeeSerializer
from .permissions import IsAdminUserOrReadOnly
from rest_framework import viewsets


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAdminUserOrReadOnly, )
