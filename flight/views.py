# coding: utf-8
from django.shortcuts import render
from django.template.context import RequestContext
from django.utils.dateparse import parse_datetime
from django.views.generic import ListView
from django.shortcuts import render_to_response
from blog.models import Post
from datetime import timedelta
from flight.models import Flight
from forms import *
from unique_flight.models import UniqueFlight


class ListFlightView(ListView):
    model = Flight
    template_name = 'flights.html'


def index(request):
    search_form = SearchForm()
    posts = Post.objects.all()
    return render(request, 'index.html', {'search_form': search_form,
                                          'object_list': posts}, context_instance=RequestContext(request))


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
                uniq_diff = flight.arrival_date_begin - flight.departure_date_begin
                arrival_date = departure_datetime.date() + timedelta(days=uniq_diff.days)
                arrival_time = flight.arrival_time
                db_unique_flights = UniqueFlight.objects.filter(flight__exact=flight,
                                                                departure_datetime=departure_datetime)

                if db_unique_flights.count() == 0:
                    unique_flight = UniqueFlight(flight_id=flight.id,
                                                 departure_datetime=departure_datetime,
                                                 arrival_date=arrival_date,
                                                 arrival_time=arrival_time,
                                                 left_seats_F=flight.aircraft.seat_count_F,
                                                 left_seats_B=flight.aircraft.seat_count_B,
                                                 left_seats_E=flight.aircraft.seat_count_E)
                    unique_flight.save()
                else:
                    unique_flight = db_unique_flights[0]

                unique_flights.append(unique_flight)

            return render_to_response('flights.html', {'unique_flights': unique_flights,
                                                       'search_form': search_form},
                                      context_instance=RequestContext(request))
    else:
        search_form = SearchForm()
    return render_to_response('search.html', {'search_form': search_form},
                              context_instance=RequestContext(request))


# def timetable(request):
#     for flight in Flight.objects.all():
#         day = flight.departure_date_begin.strftime("%A")
#         interval = flight.repeat_interval
#         if interval == 1:
#             interval = 'Every day'
#         elif interval == 7:
#             interval = 'Every %s' % day
#         else:
#             interval = None
#         day_diff = flight.arrival_date_begin - flight.departure_date_begin
#         flight_time = ''
#         if day_diff.days > 1:
#             flight_time = (1440 - (flight.departure_time.hour * 60 + flight.departure_time.minute)) \
#                           + flight.arrival_time.hour * 60 + flight.arrival_time.minute + day_diff.days * 1440
#         elif day_diff.days == 1:
#             flight_time = (1440 - (flight.departure_time.hour * 60 + flight.departure_time.minute)) \
#                           + flight.arrival_time.hour * 60 + flight.arrival_time.minute
#         elif day_diff.days == 0:
#             flight_time = (flight.arrival_time.hour * 60 + flight.arrival_time.minute) - \
#                           (flight.departure_time.hour + flight.departure_time.minute)
#         flight_time_hours = flight_time // 60
#         flight_time_minutes = flight_time - flight_time_hours * 60
#         return render_to_response('timetable.html', {'flight': flight,
#                                                      'day': day,
#                                                      'interval': interval,
#                                                      'flight_time_hours': flight_time_hours,
#                                                      'flight_time_minutes': flight_time_minutes},
#                                   context_instance=RequestContext(request))