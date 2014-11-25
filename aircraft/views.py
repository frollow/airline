import os
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from aircraft.forms import AircraftForm
from aircraft.models import Aircraft
from airline.settings import BASE_DIR, MEDIA_ROOT


def show_seat_conf(request):
    if request.method == 'POST':
        aircraft_form = AircraftForm(request.POST)
        if aircraft_form.is_valid():
            aircraft_id = int(request.POST['aircraft'])
            aircraft = Aircraft.objects.filter(pk=aircraft_id)
            seat_conf = Aircraft.seat_map_generator(aircraft[0])
            return render_to_response('seat_conf.html', {'seat_conf': seat_conf},
                                      context_instance=RequestContext(request))
    else:
        aircraft_form = AircraftForm()
        return render_to_response('seat_conf.html', {
            'aircraft_form': aircraft_form},
                                  context_instance=RequestContext(request))


# def show_image(request):
#     path = request.path
#     image = path.split('/')[-1]
#     absolute_uri = request.build_absolute_uri(path)
#
#     image_data = open(os.path.join('img/', image), "rb").read()
#     return render_to_response("image.html", {'path': absolute_uri},
#                                context_instance=RequestContext(request))