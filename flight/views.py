from django.views.generic import ListView
from flight.models import Flight

class ListFlightView(ListView):
    model = Flight
    template_name = 'flights.html'