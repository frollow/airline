# -*- coding: utf-8 -*-
from functools import partial
from django import forms
from city.models import City


class SearchForm(forms.Form):
    DateInput = partial(forms.DateInput, {'class': 'datepicker'})
    departure_city = forms.ModelChoiceField(queryset=City.objects.all(), required=True)
    arrival_city = forms.ModelChoiceField(queryset=City.objects.all())
    departure_date = forms.DateField(widget=DateInput())