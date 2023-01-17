from django.db import models
from django.contrib.auth.models import AbstractUser

class GeoUser (AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=9)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return f"User: {self.email}; {self.first_name} {self.last_name}"

    
