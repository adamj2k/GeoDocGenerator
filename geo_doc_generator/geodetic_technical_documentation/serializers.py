from geodetic_work.models.geodetic_work import GeodeticWork
from geodetic_work.models.document import *


class GeodeticWorkDocumentsSerializer:
    def __init__(self, instance):
        self.instance = instance

    def serialize(self):
        technical_description = TechnicalDescription.objects.get(
            id_work=self.instance.id
        )
        geodetic_network_survey = GeodeticNetworkSurveyData.objects.get(
            id_work=self.instance.id
        )
        geodetic_network_coordinates = GeodeticNetworkCoordinates.objects.get(
            id_work=self.instance.id
        )
        list_coordinates = ListOfCoordinates.objects.get(id_work=self.instance.id)

        return {
            "work_id": self.instance.id_work,
            "voivodeship": self.instance.voivodeship,
            "county": self.instance.county,
            "comune": self.instance.commune,
            "precintcts": self.instance.precinct,
            "work_object": self.instance.work_object,
            "plots": self.instance.plots,
            "work_scope": self.instance.work_scope,
            "survey_date": self.instance.survey_date,
            "documentation_date": self.instance.documentation_date,
            "begin_date": self.instance.begin_date,
            "technical_description": technical_description.comparision_description,
            "geodetic_network": geodetic_network_survey.raport,
            "geodetic_coordinates": geodetic_network_coordinates.list_of_coordinates,
            "list_coordinates": list_coordinates.list_of_coordinates,
        }
