# coding: utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView
from flight.models import Flight


class ListFlightView(ListView):
    model = Flight
    template_name = 'flights.html'


def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))
