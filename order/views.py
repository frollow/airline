# coding: utf-8
import uuid
import datetime

from django.core.mail import send_mail
from django.http import Http404

from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.utils.dateparse import parse_datetime
from aircraft.models import Aircraft

from flight.models import Flight
from order.forms import OrderForm
from order.models import Order
from unique_flight.models import UniqueFlight


def fill_data(request):
    if request.method == 'POST':
        unique_flight_id = request.POST['unique_flight_id']
        class_of_service = request.POST['class_of_service']

        unique_flight = UniqueFlight.objects.filter(id__exact=unique_flight_id)[0]

        order_form = OrderForm()
        return render_to_response('order.html', {'order_form': order_form, 'unique_flight': unique_flight,
                                                 'class_of_service': class_of_service,
                                                 'price': unique_flight.get_price(class_of_service)},
                                  context_instance=RequestContext(request))
    else:
        return redirect('/search/')


def send_order(order):
    send_mail('Order', 'http://127.0.0.1:8000/show_order/order_id/{}/hash/{}'.format(order.id, order.order_hash),
              'test@mail.com', ['MaximSannikov@localhost'], fail_silently=False)
    return 0


def place_order(request):
    if request.method == 'POST':
        search_form = OrderForm(request.POST)
        if search_form.is_valid():
            unique_flight_id = request.POST['unique_flight_id']
            # TODO: сделать конвертатцию формы в модельку
            first_name = search_form.cleaned_data['first_name']
            last_name = search_form.cleaned_data['last_name']
            document_id = search_form.cleaned_data['document_id']
            birth_day = search_form.cleaned_data['birth_day']
            email = search_form.cleaned_data['email']
            class_of_service = request.POST['class_of_service']

            order = Order(unique_flight_id=unique_flight_id,
                          first_name=first_name,
                          last_name=last_name,
                          document_id=document_id,
                          birth_day=birth_day,
                          email=email,
                          order_hash=uuid.uuid1().hex,
                          class_of_service=class_of_service)

            if order.unique_flight.take_seat(class_of_service):
                order.save()
                send_order(order)
                return render_to_response('status.html', {'status': 'Order created, link sent to you by email'},
                                      context_instance=RequestContext(request))
            else:
                return render_to_response('status.html', {'status': 'We are sorry, but there are no free places of class you have chosen'},
                                      context_instance=RequestContext(request))
    else:
        return redirect('/search/')


def show_order(request, order_id, order_hash):
    try:
        order = Order.objects.get(pk=order_id, order_hash=order_hash)
    except Order.DoesNotExist:
        raise Http404

    return render_to_response('show_order.html', {'order': order,
                                                  'price': order.unique_flight.get_price(order.class_of_service)},
                              context_instance=RequestContext(request))


def register(request):
    order_id = request.POST['order_id']
    order = Order.objects.get(pk=order_id)

    diff = int((order.unique_flight.departure_datetime - datetime.datetime.now()).total_seconds() / 60)

    if order.is_registered:
        return render_to_response('status.html', {'status': 'You have already registered'},
                                  context_instance=RequestContext(request))
    elif 30 < diff < 360:
        # TODO: Здесь нужно предоставить выбор места

        order.is_registered = True
        order.registration_time = datetime.datetime.now()
        return render_to_response('status.html', {'status': 'You are successfully registered'},
                                  context_instance=RequestContext(request))
    elif diff < 30:
        return render_to_response('status.html', {'status': 'Sorry, but registration on this flight completed'},
                                  context_instance=RequestContext(request))
    else:
        return render_to_response('status.html', {'status': 'It is not time for registration yet'},
                                  context_instance=RequestContext(request))