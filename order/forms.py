# -*- coding: utf-8 -*-
from functools import partial
from django import forms


class OrderForm(forms.Form):
    # TODO: Сделать, чтобы формочка рисовалась из модели
    # class Meta:
    #     model = Order
    #     fields = ['first_name']
    #fields = ['first_name', 'last_name', 'document_id', 'birth_day', 'email']
    DateInput = partial(forms.DateInput, {'class': 'datepicker'})
    first_name = forms.CharField(max_length=255, initial='John')
    last_name = forms.CharField(max_length=255, initial='Doe')
    document_id = forms.CharField(max_length=11, min_length=7, initial='N373702')
    birth_day = forms.DateField(initial='1990-01-01', widget=DateInput())
    email = forms.EmailField(max_length=255, initial='airline-test@no-spam.ws')
