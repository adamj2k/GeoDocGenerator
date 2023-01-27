from rest_framework.serializers import ModelSerializer
from geodetic_work.models.geodetic_work import GeodeticWork


class GeodeticWorkSerializer(ModelSerializer):
    class Meta:
        model = GeodeticWork
        fields = "__all__"
