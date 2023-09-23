from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils import timezone

DOCUMENTS_PATH = "documents/"


def get_upload_path(instance, filename):
    """Generates the file path for the TDocuments."""
    return f"{DOCUMENTS_PATH}/{instance.id}/{filename}"


class GeodeticWork(models.Model):
    class Status(models.TextChoices):
        INPROGRESS = "INP", _("W trakcie")
        ENDED = "END", _("Zakończona")
        CANCELLED = "CAN", _("Anulowana")

    class WorkScope(models.TextChoices):
        MDCP = "MDCP", _("sporządzenie mapy do celów projektowych")
        INWENT = "INW", _("geodezyjna inwentaryzacja powykonawcza obiektów budowalnych")
        WZNOW = "WZNOW", _(
            "wznowienie znaków granicznych, wyznaczenie pkt granicznych lub ustalenie przebiegu granic"
        )
        MZPPN = "MZPPN", _("sporządzenie mapy z projektem podziału nieruchomości")
        PSCPN = "PSCPN", _("sporządzenie projeku scalenia i podziału nieruchomości")
        MDCPRAW = "MDCPRAW", _("sporządzenie innej mapy do celów prawnych")
        PSWG = "PSWG", _("sporządzenie projektu scalenia lub wymiany gruntów")
        ROZG = "ROZG", _(
            "sporządzenie dokumentacji geodezyjnej na potrzeby rozgranicznenia nieruchomości"
        )
        INNE = "INNE", _("wykonanie innych czynności lub dokumentacji geodezyjnej")

    id_work = models.CharField(
        "identyfikator pracy", max_length=25, null=False, default="XX.6640.XXXX.RRRR"
    )
    voivodeship = models.CharField(
        "województwo", max_length=50, null=True, default="zachodniopomorskie"
    )
    county = models.CharField("powiat", max_length=50, null=True)
    commune = models.CharField("gmina", max_length=50, null=True)
    precinct = models.CharField("obręb", max_length=50, null=True)
    work_object = models.CharField("obiekt", max_length=100, null=True)
    plots = models.CharField("działki", max_length=50, null=True)
    work_scope = models.CharField(
        "cel pracy",
        max_length=10,
        null=True,
        choices=WorkScope.choices,
        default=WorkScope.MDCP,
    )
    survey_date = models.DateField(
        "data pomiaru", blank=True, null=True, default=timezone.now
    )
    begin_date = models.DateField(
        "data rozpoczęcia", blank=True, null=True, default=timezone.now
    )
    area = models.CharField("obszar", max_length=10, null=True)
    change_bdot_database = models.BooleanField(
        "zmiana BDOT500", default=False, null=True
    )
    change_gesut_database = models.BooleanField(
        "zmiana GESUT", default=False, null=True
    )
    change_egib_database = models.BooleanField("zmiana EGiB", default=False, null=True)
    documentation_date = models.DateField(
        "data dokumentacji", default=timezone.now, blank=True, null=True
    )
    contractor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1, editable=False
    )

    status = models.CharField(
        "status",
        max_length=3,
        null=True,
        choices=Status.choices,
        default=Status.INPROGRESS,
    )
    pdf_documentation = models.FileField(
        upload_to=get_upload_path, null=True, blank=True
    )

    def __str__(self) -> str:
        return f"{self.id_work} - {self.work_object}"
