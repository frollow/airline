from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django import forms
from django.http import request
from airport.models import Airport
from flight.models import Flight
from city.models import City


class AdminFlightForm(forms.ModelForm):
    airports = Airport.objects.all()
    departure_airport = forms.ModelChoiceField(queryset=airports, required=True)
    arrival_airport = forms.ModelChoiceField(queryset=airports, required=True)


class FlightAdmin(ModelAdmin):
    model = Flight
    form = AdminFlightForm

admin.site.register(Flight, FlightAdmin)