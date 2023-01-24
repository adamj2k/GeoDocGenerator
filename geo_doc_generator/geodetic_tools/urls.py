from django.urls import path
from .views import HeightConversionView


urlpatterns = [
    path("heightconv/", HeightConversionView.as_view(), name="height-conversion")
]
