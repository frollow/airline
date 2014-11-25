from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from aircraft.forms import ExtFileField
from aircraft.models import Aircraft


class AircraftAdmin(ModelAdmin):
    model = Aircraft
    seat_map_picture = ExtFileField(ext_whitelist=(".jpg", ".png"))

    list_display = ('company', 'model', 'seat_count_F', 'seat_count_B', 'seat_count_E')



admin.site.register(Aircraft, AircraftAdmin)