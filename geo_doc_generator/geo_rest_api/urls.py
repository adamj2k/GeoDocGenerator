from django.urls import path
from geo_rest_api.views import GeodeticWorkDeleteApiView, GeodeticWorkEditApiView

urlpatterns = [
    path(
        "workdeleteapi/<int:pk>",
        GeodeticWorkDeleteApiView.as_view(),
        name="geodetic-work-delete-api",
    ),
    path(
        "workeditapi/<int:pk>",
        GeodeticWorkEditApiView.as_view(),
        name="geodetic-work-edit-api",
    ),
]
