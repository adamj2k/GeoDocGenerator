# Generated by Django 4.1.5 on 2023-01-18 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GeodeticWork",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "id_work",
                    models.CharField(default="XX.6640.XXXX.RRRR", max_length=25),
                ),
                (
                    "voivodeship",
                    models.CharField(
                        default="zachodniopomorskie", max_length=50, null=True
                    ),
                ),
                ("county", models.CharField(max_length=50, null=True)),
                ("commune", models.CharField(max_length=50, null=True)),
                ("precinct", models.CharField(max_length=50, null=True)),
                ("work_object", models.CharField(max_length=100, null=True)),
                ("plots", models.CharField(max_length=50, null=True)),
                ("survey_date", models.DateField(auto_now=True)),
                ("begin_date", models.DateField(auto_now=True)),
                ("change_bdot_database", models.BooleanField(default=False, null=True)),
                (
                    "change_gesut_database",
                    models.BooleanField(default=False, null=True),
                ),
                ("change_egib_database", models.BooleanField(default=False, null=True)),
                ("documentation_date", models.DateField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("INP", "W trakcie"),
                            ("END", "Zakończona"),
                            ("CAN", "Anulowana"),
                        ],
                        default="INP",
                        max_length=3,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TechnicalDescription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "pdf_file",
                    models.FileField(null=True, upload_to="static/geodetic_work/"),
                ),
                (
                    "source_data",
                    models.TextField(
                        default="Po analizie materiałów pozyskanych z PZGiK do..."
                    ),
                ),
                (
                    "comparision_description",
                    models.TextField(default="Wykonano porównanie mapy..."),
                ),
                (
                    "geodetic_network_description",
                    models.TextField(default="Założono osnowę pomiarową ..."),
                ),
                (
                    "control_survey_description",
                    models.TextField(default="Wykonano pomiar kontrolny ..."),
                ),
                (
                    "land_survey_descrption",
                    models.TextField(default="Wykonano pomiar systuacyjny metodą ..."),
                ),
                (
                    "results_descrption",
                    models.TextField(default="Wyniki uzyskano w układzie ..."),
                ),
                (
                    "zudp_building_permit",
                    models.TextField(default="ZUD i pozwolenie na budowe .."),
                ),
                (
                    "boundary_plots",
                    models.TextField(default="Granice spełniają/nie spełniają ..."),
                ),
                (
                    "output_documents",
                    models.TextField(default="Dla zamawiającego przygotowano..."),
                ),
                (
                    "update_county_database",
                    models.TextField(default="Przekazno pliki w formacie ..."),
                ),
                (
                    "update_egib_database",
                    models.TextField(
                        default="Kierownik prac stwierdził/nie stwierdził ..."
                    ),
                ),
                (
                    "id_work",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="geodetic_work.geodeticwork",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ListOfCoordinates",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "pdf_file",
                    models.FileField(null=True, upload_to="static/geodetic_work/"),
                ),
                ("list_of_coordinates", models.TextField()),
                (
                    "id_work",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="geodetic_work.geodeticwork",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="GeodeticNetworkSurveyData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "pdf_file",
                    models.FileField(null=True, upload_to="static/geodetic_work/"),
                ),
                ("raport", models.TextField()),
                (
                    "id_work",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="geodetic_work.geodeticwork",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="GeodeticNetworkDraft",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "pdf_file",
                    models.FileField(null=True, upload_to="static/geodetic_work/"),
                ),
                (
                    "id_work",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="geodetic_work.geodeticwork",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="GeodeticNetworkCoordinates",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "pdf_file",
                    models.FileField(null=True, upload_to="static/geodetic_work/"),
                ),
                ("list_of_coordinates", models.TextField()),
                (
                    "id_work",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="geodetic_work.geodeticwork",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="FieldDraft",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "pdf_file",
                    models.FileField(null=True, upload_to="static/geodetic_work/"),
                ),
                (
                    "id_work",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="geodetic_work.geodeticwork",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ComaparisionMap",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "pdf_file",
                    models.FileField(null=True, upload_to="static/geodetic_work/"),
                ),
                (
                    "id_work",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="geodetic_work.geodeticwork",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
