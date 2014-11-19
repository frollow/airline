from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django import forms
from flight.models import Flight
from city.models import City


class AdminFlightForm(forms.ModelForm):
    cities = City.objects.all()
    departure_city = forms.ModelChoiceField(queryset=cities, required=True)
    arrival_city = forms.ModelChoiceField(queryset=cities, required=True)


class FlightAdmin(ModelAdmin):
    model = Flight
    form = AdminFlightForm


admin.site.register(Flight, FlightAdmin)