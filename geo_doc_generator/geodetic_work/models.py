from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _

class GeodeticWork(models.Model):
    id_work = models.CharField(max_length=25, null=False, default="XX.6640.XXXX.RRRR")
    voivodeship = models.CharField(max_length=50, null=True, default="zachodniopomorskie")
    county = models.CharField(max_length=50, null=True)
    commune = models.CharField(max_length=50, null=True)
    precinct = models.CharField(max_length=50, null=True)
    work_object = models.CharField(max_length=100, null=True)
    plots = models.CharField(max_length=50, null=True)
    survey_date = models.DateField(auto_now=True)
    begin_date = models.DateField(auto_now=True)
    change_bdot_database = models.BooleanField(default=False, null=True)
    change_gesut_database = models.BooleanField(default=False, null=True)
    change_egib_database = models.BooleanField(default=False, null=True)
    documentation_date = models.DateField(auto_now=True)
    
    class Status (models.TextChoices):
        INPROGRESS = "INP", _("W trakcie")
        ENDED = "END", _("Zakończona")
        CANCELLED = "CAN", _("Anulowana")
            
    status = models.CharField(
        max_length=3, 
        null=True, 
        choices=Status.choices,
        default=Status.INPROGRESS
        )


    def __str__(self) -> str:
        return f"{self.id_work} - {self.work_object}"


class Document(models.Model):
    id_work = models.OneToOneField(GeodeticWork, on_delete=CASCADE)
    pdf_file = models.FieldFile(upload_to = 'static/geodetic_work/', null=True)
    
    class Meta:
        abstract = True


class TechnicalDescription(Document):
    source_data = models.TextField(default="Po analizie materiałów pozyskanych z PZGiK do...")
    comparision_description = models.TextField(default="Wykonano porównanie mapy...")
    geodetic_network_description = models.TextField(default="Założono osnowę pomiarową ...")
    control_survey_description = models.TextField(default="Wykonano pomiar kontrolny ...")
    land_survey_descrption = models.TextField(default="Wykonano pomiar systuacyjny metodą ...")
    results_descrption = models.TextField(default="Wyniki uzyskano w układzie ...")
    zudp_building_permit = models.TextField(default="ZUD i pozwolenie na budowe ..")
    boundary_plots = models.TextField(default="Granice spełniają/nie spełniają ...")
    output_documents = models.TextField(default="Dla zamawiającego przygotowano...")
    update_county_database = models.TextField(default="Przekazno pliki w formacie ...")
    update_egib_database = models.TextField(default="Kierownik prac stwierdził/nie stwierdził ...")

    def __str__(self) -> str:
        return f"Sprawozdanie {self.id_work}"


class ComaparisionMap(Document):

    def __str__(self) -> str:
        return f"Mapa porównania z terenem - {self.id_work}"


class GeodeticNetworkSurveyData(Document):
    raport = models.TextField()

    def __str__(self) -> str:
        return f"Dane obserwacyjne osnowy pomiarowej - {self.id_work}"


class GeodeticNetworkDraft(Document):

    def __str__(self) -> str:
        return f"Szkic osnowy geodezyjnej - {self.id_work}"


class GeodeticNetworkCoordinates (Document):
    list_of_coordinates = models.TextField()

    def __str__(self) -> str:
        return f"Wykaz współrzędnych punktów osnowy pomiarowej - {self.id_work}"


class FieldDraft (Document):

    def __str__(self) -> str:
        return f"Szkice polowy - {self.id_work}"

class ListOfCoordinates (Document):
    list_of_coordinates = models.TextField()

    def __str__(self) -> str:
        return f"Wykaz współrzednych - {self.id_work}"

