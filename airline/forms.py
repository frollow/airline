# -*- coding: utf-8 -*-
from django import forms


class SearchForm(forms.Form):
    departure_city = forms.CharField(label='Откуда', max_length=100)
    arrival_city = forms.CharField(label='Куда', max_length=100)