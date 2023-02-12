from geodetic_work.models.geodetic_work import GeodeticWork
from geodetic_work.models.document import *
from django.core.exceptions import ObjectDoesNotExist


class GeodeticWorkDocumentsSerializer:
    def __init__(self, instance):
        self.instance = instance

    def serialize(self):
        try:
            table_of_content = TableOfContent.objects.get(id_work=self.instance.id)
        except:
            table_of_content = None

        try:
            technical_description = TechnicalDescription.objects.get(
                id_work=self.instance.id
            )
        except ObjectDoesNotExist:
            technical_description = None

        try:
            geodetic_network_survey = GeodeticNetworkSurveyData.objects.get(
                id_work=self.instance.id
            )
        except ObjectDoesNotExist:
            geodetic_network_survey = None

        try:
            geodetic_network_coordinates = GeodeticNetworkCoordinates.objects.get(
                id_work=self.instance.id
            )
        except ObjectDoesNotExist:
            geodetic_network_coordinates = None

        try:
            comparision_map = ComaparisionMap.objects.get(id_work=self.instance.id)
        except ObjectDoesNotExist:
            comparision_map = None

        try:
            geodetic_network_draft = GeodeticNetworkDraft.objects.get(
                id_work=self.instance.id
            )
        except ObjectDoesNotExist:
            geodetic_network_draft = None

        try:
            field_draft = FieldDraft.objects.get(id_work=self.instance.id)
        except ObjectDoesNotExist:
            field_draft = None

        try:
            list_coordinates = ListOfCoordinates.objects.get(id_work=self.instance.id)
        except ObjectDoesNotExist:
            list_coordinates = None

        try:
            change_list_building = ChangeListBuilding.objects.get(
                id_work=self.instance.id
            )
        except:
            change_list_building = None

        try:
            change_list_plot = ChangeListPlot.objects.get(id_work=self.instance.id)
        except:
            change_list_plot = None

        return {
            "work": self.instance,
            "work_id": self.instance.id_work,
            "voivodeship": self.instance.voivodeship,
            "county": self.instance.county,
            "commune": self.instance.commune,
            "precinct": self.instance.precinct,
            "work_object": self.instance.work_object,
            "plots": self.instance.plots,
            "work_scope": self.instance.work_scope,
            "survey_date": self.instance.survey_date,
            "documentation_date": self.instance.documentation_date,
            "begin_date": self.instance.begin_date,
            "technical_description": technical_description,
            "geodetic_network": geodetic_network_survey,
            "geodetic_coordinates": geodetic_network_coordinates,
            "list_coordinates": list_coordinates,
            "comparision_map": comparision_map,
            "network_draft": geodetic_network_draft,
            "field_draft": field_draft,
            "change_list_buildings": change_list_building,
            "change_list_plot": change_list_plot,
            "table_of_content": table_of_content,
        }
