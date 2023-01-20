from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class GeoUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(blank=True, region="PL")
    company_name = models.CharField(max_length=25, null=True)
    adress1 = models.CharField(max_length=50, null=True, blank=True)
    adress2 = models.CharField(max_length=50, null=True, blank=True)
    company_phone = PhoneNumberField(blank=True, region="PL")
    nip_number = models.CharField(max_length=50, null=True, blank=True)
    regon_number = models.CharField(max_length=100, null=True, blank=True)
    licenced_surveyors = models.TextField(max_length=250, null=True, blank=True)
    regural_surveyors = models.TextField(max_length=250, null=True, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self) -> str:
        return f"User: {self.email}; {self.first_name} {self.last_name}\n Company: {self.company_name}"
