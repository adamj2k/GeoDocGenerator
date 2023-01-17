from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.translation import gettext_lazy as _


class GeodeticWork(models.Model):
    id_work = models.CharField(max_length=25, null=False, default="XX.6640.XXXX.RRRR")
    voivodeship = models.CharField(
        max_length=50, null=True, default="zachodniopomorskie"
    )
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

    class Status(models.TextChoices):
        INPROGRESS = "INP", _("W trakcie")
        ENDED = "END", _("Zakończona")
        CANCELLED = "CAN", _("Anulowana")

    status = models.CharField(
        max_length=3, null=True, choices=Status.choices, default=Status.INPROGRESS
    )

    def __str__(self) -> str:
        return f"{self.id_work} - {self.work_object}"