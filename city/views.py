# coding: utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import ListView
from flight.models import Flight
from city.models import City


class ListFlightView(ListView):
    model = Flight
    template_name = 'flights.html'


def index(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def selectview(request):
    item  = City.objects.all()
    form = request.POST
    if request.method == 'POST':
        selected_item = get_object_or_404(City, pk=request.POST.get('city'))
        user.item = selected_item
