from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from aircraft.models import Aircraft


class AircraftAdmin(ModelAdmin):
    model = Aircraft
    list_display = ('company', 'model', 'seat_count')


admin.site.register(Aircraft, AircraftAdmin)