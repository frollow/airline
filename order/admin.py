from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.db.models.base import Model
from order.models import Flight, Aircraft, Airport
# Register your models here.

class AircraftAdmin(ModelAdmin):
    model = Aircraft
    list_display = ('company','model','seat_count')

admin.site.register(Flight)
admin.site.register(Aircraft, AircraftAdmin)
admin.site.register(Airport)