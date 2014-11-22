# coding: utf-8
from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from flight.models import Flight
from order.forms import OrderForm
from order.models import Order
from django.template.context import RequestContext


# class ListOrderView(ListView):
# model = Order
# template_name = 'order.html'

# TODO: Должна формочка открываться по адресу fill_data/число. А говорит, что передано слишном много параметров методу. Хотя если отредактироваить urls.py, так чтобы формочка открывалась сразу по fill_data, то все ОК.
from unique_flight.models import UniqueFlight


def make_order(request):
    if request.method == 'POST':
        flight_id = request.POST['flight_id']
        departure_date = request.POST['departure_date']
        flight = Flight.objects.filter(id__exact=flight_id)[0]
        unique_flights = UniqueFlight.objects.filter(flight__exact=flight)

        if unique_flights.count() == 0:
            # unique_flight = UniqueFlight.objects.create(flight=flight, departure_date=departure_date)
            unique_flight = UniqueFlight(flight_id=flight_id,
                                         departure_date=departure_date,
                                         left_seats_F=flight.aircraft.seat_count_F,
                                         left_seats_B=flight.aircraft.seat_count_B,
                                         left_seats_E=flight.aircraft.seat_count_E)
            unique_flight.save()

        else:
            unique_flight = unique_flights[0]
        order_form = OrderForm()
        return render_to_response('order.html', {'order_form': order_form, 'unique_flight': unique_flight},
                                  context_instance=RequestContext(request))
    else:
        order_form = OrderForm()
        return render(request, 'order.html', {'order_form': order_form})


        # '''select * from flight_flight where id=flight_id'''