# coding: utf-8
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.http import request
from unique_flight.forms import UniqueFlightForm
from unique_flight.models import UniqueFlight


class UniqueFlightAdmin(ModelAdmin):
    # TODO: Нужно, чтобы поля с классами мест на страничке с уникальными рейсами в админке была заполнена дефолтными значениями из соответствующего Aircraft
    #
    # def __call__(self, request, url):
    #     global uniqueflight_id
    #     uniqueflight_id = request.GET['uniqueflight']
    #     return super(UniqueFlightAdmin, self).__call__(request, url)
    form = UniqueFlightForm
    list_display = ('flight', 'unique_id', 'left_seats_F', 'left_seats_B', 'left_seats_E')
    #readonly_fields = ('unique_id',)

admin.site.register(UniqueFlight, UniqueFlightAdmin)