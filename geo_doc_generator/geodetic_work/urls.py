from django.urls import path
from .views import (
    GeodeticWorkListView,
    GeodeticWorkHome,
    GeodeticWorkCreatView,
    GeodeticWorkDetailsView,
    GeodeticWorkEditView,
)

urlpatterns = [
    path("", GeodeticWorkHome.as_view(), name="geodetic-work-home"),
    path("worklist/", GeodeticWorkListView.as_view(), name="geodetic-work-list"),
    path("workcreate/", GeodeticWorkCreatView.as_view(), name="geodetic-work-create"),
    path(
        "workdetails/<int:pk>",
        GeodeticWorkDetailsView.as_view(),
        name="geodetic-work-details",
    ),
    path(
        "workedit/<int:pk>", GeodeticWorkEditView.as_view(), name="geodetic-work-edit"
    ),
]
