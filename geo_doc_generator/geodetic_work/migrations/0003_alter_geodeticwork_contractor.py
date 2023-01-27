# Generated by Django 4.1.5 on 2023-01-20 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("geodetic_work", "0002_geodeticwork_contractor_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="geodeticwork",
            name="contractor",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]