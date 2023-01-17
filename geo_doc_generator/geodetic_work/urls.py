from django.urls import path

urlpatterns = [
    path("", GeodeticWorkList.as_view(), name="geodetic-work-home"),
]
