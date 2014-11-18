from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from airport.models import Airport


class AirportAdmin(ModelAdmin):
    model = Airport
    list_display = ('code', 'city')


admin.site.register(Airport, AirportAdmin)