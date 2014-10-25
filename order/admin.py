from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from flight.models import Flight
from aircraft.models import Aircraft
from airport.models import Airport


class AircraftAdmin(ModelAdmin):
    model = Aircraft
    list_display = ('company', 'model', 'seat_count')


admin.site.register(Flight)
admin.site.register(Aircraft, AircraftAdmin)
admin.site.register(Airport)