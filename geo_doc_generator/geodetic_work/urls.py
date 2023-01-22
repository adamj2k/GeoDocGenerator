from django.urls import path
from .views import GeodeticWorkListView, GeodeticWorkHome

urlpatterns = [
    path("", GeodeticWorkHome.as_view(), name="geodetic-work-home"),
    path("worklist/", GeodeticWorkListView.as_view(), name="geodetic-work-list"),
]
