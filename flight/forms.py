# -*- coding: utf-8 -*-
from django import forms
from city.models import City
from functools import partial
from models import Flight

class SearchForm(forms.Form):
    DateInput = partial(forms.DateInput, {'class': 'datepicker'})
    FIRST_CLASS = 'F'
    BUSINESS_CLASS = 'B'
    ECONOMY_CLASS = 'E'
    CLASS_OF_SERVICE = (
        (FIRST_CLASS, 'First'),
        (BUSINESS_CLASS, 'Business'),
        (ECONOMY_CLASS, 'Econom'),
    )
    departure_city = forms.ModelChoiceField(queryset=City.objects.all(), required=True)
    arrival_city = forms.ModelChoiceField(queryset=City.objects.all())
    departure_date = forms.DateField(widget=DateInput())
    arrival_date = forms.DateField(widget=DateInput())
    class_of_service = forms.ChoiceField(initial=ECONOMY_CLASS, choices=CLASS_OF_SERVICE)
    adults = forms.ChoiceField(choices=(('1','1'),('2','2'),('3','3')))
    children = forms.ChoiceField(choices=(('0','0'),('1','1'),('2','2'),('3','3')))