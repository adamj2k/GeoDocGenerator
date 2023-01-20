from django.urls import path
from .views import GeodeticWorkListView

urlpatterns = [
    path("", GeodeticWorkListView.as_view(), name="geodetic-work-home"),
]
