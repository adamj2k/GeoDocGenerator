from django.urls import path

from .views import BatchFileGeoInfoView, GeodeticToolsView, HeightConversionView

urlpatterns = [
    path("", GeodeticToolsView.as_view(), name="geodetic-tools"),
    path("heightconv/", HeightConversionView.as_view(), name="height-conversion"),
    path("batchgeoinfo/", BatchFileGeoInfoView.as_view(), name="batch-file-geo-info"),
]
