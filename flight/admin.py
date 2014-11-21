from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from flight.models import Flight

class FlightAdmin(ModelAdmin):
    model = Flight
    list_display = ('flight_number', 'departure_airport', 'arrival_airport', 'departure_date_begin',
                    'arrival_date_begin', 'repeat_interval', 'departure_time', 'arrival_time', 'aircraft')

admin.site.register(Flight, FlightAdmin)