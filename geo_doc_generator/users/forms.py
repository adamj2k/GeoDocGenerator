from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models.geouser import GeoUser


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = GeoUser
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "phone_number",
            "first_name",
            "last_name",
            "company_name",
            "adress1",
            "adress2",
            "company_phone",
            "nip_number",
            "regon_number",
            "licenced_surveyors",
            "regural_surveyors",
        ]


class UserUpdateForm(UserChangeForm):
    email = forms.EmailField()

    class Meta:
        model = GeoUser
        fields = [
            "email",
            "phone_number",
            "first_name",
            "last_name",
            "company_name",
            "adress1",
            "adress2",
            "company_phone",
            "nip_number",
            "regon_number",
            "licenced_surveyors",
            "regural_surveyors",
        ]
