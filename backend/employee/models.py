from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    username = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
