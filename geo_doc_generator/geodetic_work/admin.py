from django.contrib import admin
from .models.geodetic_work import GeodeticWork
from .models.document import TechnicalDescription

# Register your models here.
admin.site.register([TechnicalDescription, GeodeticWork])
