# -*- coding: utf-8 -*-
from django import forms

class OrderForm(forms.Form):
    first_name = forms.CharField(max_length=255, initial='John')
    last_name = forms.CharField(max_length=255, initial='Doe')
    document_id = forms.CharField(max_length=11, min_length=7, initial='N373702')