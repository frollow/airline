# coding: utf-8
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from django.template.context import RequestContext
from django.views.generic import ListView
from flight.models import Flight
from city.models import City
from django import forms
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response
from forms import *


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

            flights = []

            for flight in Flight.objects.all():
                diff = int((departure_date - flight.departure_date_begin).total_seconds() / 86400)

                if diff >= 0 and diff % flight.repeat_interval == 0 \
                        and flight.departure_airport.city == departure_city \
                        and flight.arrival_airport.city == arrival_city:
                    flights.append(flight)

            return render_to_response('flights.html', {'object_list': flights,
                                                       'departure_date': departure_date},
                                      context_instance=RequestContext(request))
    else:
        search_form = SearchForm()
    return render_to_response('search_form.html', {'search_form': search_form},
                              context_instance=RequestContext(request))

