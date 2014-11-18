# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from city.models import City
from django import forms


class Flight(models.Model):
    FIRST_CLASS = 'F'
    BUSINESS_CLASS = 'B'
    ECONOMY_CLASS = 'E'
    CLASS_OF_SERVICE = (
        (FIRST_CLASS, 'Первый'),
        (BUSINESS_CLASS, 'Бизнес'),
        (ECONOMY_CLASS, 'Эконом'),
    )
    flight_number = models.CharField(max_length=8, verbose_name='Flight Number')
    departure_city = models.CharField(max_length=255, verbose_name='Departure city')
    arrival_city = models.CharField(max_length=255, verbose_name='Arrival city')
    departure_date = models.DateTimeField(verbose_name='Departure date')
    arrival_date = models.DateTimeField(verbose_name='Arrival date')
    class_of_service = models.CharField(choices=CLASS_OF_SERVICE, max_length=1, default=ECONOMY_CLASS)

    def __unicode__(self):
        return '{} {} {} {} {} {}'.format(self.flight_number, self.departure_city, self.arrival_city,
                                          self.departure_date, self.arrival_date, self.class_of_service)