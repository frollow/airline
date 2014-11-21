# coding: utf-8
from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from order.forms import OrderForm
from order.models import Order
from django.template.context import RequestContext


# class ListOrderView(ListView):
#     model = Order
#     template_name = 'order.html'

# TODO: Должна формочка открываться по адресу fill_data/число. А говорит, что передано слишном много параметров методу. Хотя если отредактироваить urls.py, так чтобы формочка открывалась сразу по fill_data, то все ОК.
def make_order(request):
    order_form = OrderForm()
    return render(request, 'order.html', {'order_form': order_form})
