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
    return render(request, 'index.html')


def search(request):
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            departure_city = search_form.cleaned_data['departure_city']
            arrival_city = search_form.cleaned_data['arrival_city']
            departure_date = search_form.cleaned_data['departure_date']
            arrival_date = search_form.cleaned_data['arrival_date']
            class_of_service = search_form.cleaned_data['class_of_service']
            adults = search_form.cleaned_data['adults']
            children = search_form.cleaned_data['children']
            return render_to_response('search_results.html', {'departure_city': departure_city,
                                                              'arrival_city': arrival_city,
                                                              'departure_date': departure_date,
                                                              'arrival_date': arrival_date,
                                                              'class_of_service': class_of_service,
                                                              'adults': adults,
                                                              'children': children})
    else:
        search_form = SearchForm()
    return render_to_response('search_form.html', {'search_form': search_form},
                              context_instance=RequestContext(request))

