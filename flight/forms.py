# -*- coding: utf-8 -*-
from functools import partial
from django import forms
from city.models import City


class SearchForm(forms.Form):
    DateInput = partial(forms.DateInput, {'class': 'datepicker'})
    departure_city = forms.ModelChoiceField(queryset=City.objects.all(), required=True)
    arrival_city = forms.ModelChoiceField(queryset=City.objects.all())
    departure_date = forms.DateField(widget=DateInput())
    # TODO: здесь должен генерироваться номер заказа(или не здесь)
    # try:
    #     unique_id = forms.IntegerField(initial=UniqueFlight.objects.values('id').count() + 1000)
    # except Exception:
    #     unique_id = forms.IntegerField(initial=0)