# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class Flight(models.Model):
    FIRST_CLASS = 'F'
    BUSINESS_CLASS = 'B'
    ECONOMY_CLASS = 'E'
    CLASS_OF_SERVICE = (
        (FIRST_CLASS, 'Первый'),
        (BUSINESS_CLASS, 'Бизнес'),
        (ECONOMY_CLASS, 'Эконом'),
    )
    flight_number = models.CharField(max_length=8, verbose_name='Номер рейса')
    departure_city = models.CharField(max_length=255, verbose_name='Пункт вылета')
    arrival_city = models.CharField(max_length=255, verbose_name='Пункт прибытия')
    # date_departure = models.DateField('Дата вылета', default=timezone.datetime.now().date())
    #date_return = models.DateField('Дата прилёта', default=timezone.datetime.now().date() + datetime.timedelta(days=7))
    departure_time = models.TimeField(verbose_name='Время вылета', default=timezone.datetime.now().time())
    arrival_time = models.TimeField(verbose_name='Время прилёта', default=timezone.datetime.now().time())
    class_of_service = models.CharField(choices=CLASS_OF_SERVICE, max_length=1, default=ECONOMY_CLASS)