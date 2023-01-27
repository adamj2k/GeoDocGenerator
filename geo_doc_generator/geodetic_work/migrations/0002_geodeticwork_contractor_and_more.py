# Generated by Django 4.1.5 on 2023-01-20 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("geodetic_work", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="geodeticwork",
            name="contractor",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="geodeticwork",
            name="begin_date",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="geodeticwork",
            name="documentation_date",
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="geodeticwork",
            name="survey_date",
            field=models.DateField(auto_now_add=True),
        ),
    ]