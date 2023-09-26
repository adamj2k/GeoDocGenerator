from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _
from .geodetic_work import GeodeticWork

DOCUMENTS_PATH = "documents/"


def get_upload_path(instance, filename):
    """Generates the file path for the TDocuments."""
    return f"{DOCUMENTS_PATH}/{instance.id_work.id}/{filename}"


class Document(models.Model):
    id_work = models.OneToOneField(GeodeticWork, on_delete=CASCADE)
    pdf_file = models.FileField(
        upload_to="static/geodetic_work/", null=True, blank=True
    )
    docx_file = models.FileField(
        upload_to="static/geodetic_work/", null=True, blank=True
    )
    pdf_file = models.FileField(upload_to=get_upload_path, null=True, blank=True)

    class Meta:
        abstract = True


class TechnicalDescription(Document):
    source_data = models.TextField(
        "dane źródłowe", default="Po analizie materiałów pozyskanych z PZGiK do..."
    )
    comparision_description = models.TextField(
        "wywiad terenowy:", default="Wykonano porównanie mapy..."
    )
    geodetic_network_description = models.TextField(
        "opis osnowy geodezyjnej", default="Założono osnowę pomiarową ..."
    )
    control_survey_description = models.TextField(
        "opis pomiaru kontrolnego", default="Wykonano pomiar kontrolny ..."
    )
    land_survey_descrption = models.TextField(
        "opis pomiaru", default="Wykonano pomiar systuacyjny metodą ..."
    )
    results_descrption = models.TextField(
        "wyniki pomiaru", default="Wyniki uzyskano w układzie ..."
    )
    zudp_building_permit = models.TextField(
        "ZUD, pozwolenia", default="ZUD i pozwolenie na budowe .."
    )
    boundary_plots = models.TextField(
        "informacja o granicach", default="Granice spełniają/nie spełniają ..."
    )
    output_documents = models.TextField(
        "dokumentacja dla klienta", default="Dla zamawiającego przygotowano..."
    )
    update_county_database = models.TextField(
        "dane przekazywane do PZGiK", default="Przekazno pliki w formacie ..."
    )
    update_egib_database = models.TextField(
        "zmiany egib", default="Kierownik prac stwierdził/nie stwierdził ..."
    )

    def __str__(self) -> str:
        return f"Sprawozdanie {self.id_work}"


class ComaparisionMap(Document):
    def __str__(self) -> str:
        return f"Mapa porównania z terenem - {self.id_work}"


class GeodeticNetworkSurveyData(Document):
    raport = models.TextField("Raport")

    def __str__(self) -> str:
        return f"Dane obserwacyjne osnowy pomiarowej - {self.id_work}"


class GeodeticNetworkDraft(Document):
    def __str__(self) -> str:
        return f"Szkic osnowy geodezyjnej - {self.id_work}"


class GeodeticNetworkCoordinates(Document):
    list_of_coordinates = models.TextField("Wykaz współrzędnych")

    def __str__(self) -> str:
        return f"Wykaz współrzędnych punktów osnowy pomiarowej - {self.id_work}"


class FieldDraft(Document):
    def __str__(self) -> str:
        return f"Szkice polowy - {self.id_work}"


class ListOfCoordinates(Document):
    list_of_coordinates = models.TextField("Wykaz współrzędnych")

    def __str__(self) -> str:
        return f"Wykaz współrzednych - {self.id_work}"


class ChangeListBuilding(Document):
    def __str__(self) -> str:
        return f"Wykaz zmian danych ewidencyjnych dot. budynku - {self.id_work}"


class ChangeListPlot(Document):
    def __str__(self) -> str:
        return f"Wykaz zmian danych ewidencyjnych dot. działki - {self.id_work}"


class TableOfContent(Document):
    def __str__(self) -> str:
        return f"Spis Treści - {self.id_work}"
