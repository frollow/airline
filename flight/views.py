# coding: utf-8
from django.shortcuts import render
from django.template.context import RequestContext
from django.utils.dateparse import parse_datetime
from django.views.generic import ListView
from django.shortcuts import render_to_response

from flight.models import Flight
from forms import *
from unique_flight.models import UniqueFlight


class ListFlightView(ListView):
    model = Flight
    template_name = 'flights.html'


def index(request):
    return render(request, 'index.html', context_instance=RequestContext(request))


def search(request):
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            departure_city = search_form.cleaned_data['departure_city']
            arrival_city = search_form.cleaned_data['arrival_city']
            departure_date = search_form.cleaned_data['departure_date']

            unique_flights = []

            for flight in Flight.objects.all():
                diff = int((departure_date - flight.departure_date_begin).total_seconds() / 86400)

                if diff < 0 or diff % flight.repeat_interval != 0 \
                        or flight.departure_airport.city != departure_city \
                        or flight.arrival_airport.city != arrival_city:
                    continue

                departure_datetime = parse_datetime('{} {}'.format(departure_date, flight.departure_time))
                db_unique_flights = UniqueFlight.objects.filter(flight__exact=flight,
                                                                departure_datetime=departure_datetime)

                if db_unique_flights.count() == 0:
                    unique_flight = UniqueFlight(flight_id=flight.id,
                                                 departure_datetime=departure_datetime,
                                                 left_seats_F=flight.aircraft.seat_count_F,
                                                 left_seats_B=flight.aircraft.seat_count_B,
                                                 left_seats_E=flight.aircraft.seat_count_E)
                    unique_flight.save()
                else:
                    unique_flight = db_unique_flights[0]

                unique_flights.append(unique_flight)

            return render_to_response('flights.html', {'unique_flights': unique_flights},
                                      context_instance=RequestContext(request))
    else:
        search_form = SearchForm()
    return render_to_response('search_form.html', {'search_form': search_form},
                              context_instance=RequestContext(request))

