from django import forms
from unique_flight.models import UniqueFlight
from aircraft.models import Aircraft

class UniqueFlightForm(forms.ModelForm):
    try:
        unique_id = forms.IntegerField(initial=UniqueFlight.objects.values('id').count() + 1000)
    except Exception:
        unique_id = forms.IntegerField(initial=0)
    left_seats_F = forms.CharField(max_length=3, initial=Aircraft.objects.values('seat_count_F'))


'''select from aircraft_aircraft where company=(select flight_id from )'''
