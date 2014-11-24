from django import forms
from aircraft.models import Aircraft



class AircraftForm(forms.Form):
    aircraft = forms.ModelChoiceField(queryset=Aircraft.objects.all(), required=True)
