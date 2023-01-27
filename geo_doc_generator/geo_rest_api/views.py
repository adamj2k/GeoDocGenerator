from django.shortcuts import render
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from geodetic_work.models.geodetic_work import GeodeticWork
from geo_rest_api.serializers import GeodeticWorkSerializer


class GeodeticWorkDeleteApiView(DestroyAPIView):
    queryset = GeodeticWork.objects.all()
    serializer_class = GeodeticWorkSerializer
    permission_classes = [IsAuthenticated]


class GeodeticWorkEditApiView(UpdateAPIView):
    queryset = GeodeticWork.objects.all()
    serializer_class = GeodeticWorkSerializer
    permission_classes = [IsAuthenticated]
