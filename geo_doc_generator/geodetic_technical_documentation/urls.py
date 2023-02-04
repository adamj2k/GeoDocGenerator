from django.urls import path
from geodetic_technical_documentation.views import GeneratePdf

urlpatterns = [
    path("<int:pk>", GeneratePdf.as_view(), name="geodetic-generate-doc"),
]
