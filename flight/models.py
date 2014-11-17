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
    departure_city = forms.ModelChoiceField(queryset=City.objects.all(), required=True)
    arrival_city = models.CharField(max_length=255, verbose_name='Arrival city')
    # date_departure = models.DateField('Дата вылета', default=timezone.datetime.now().date())
    #date_return = models.DateField('Дата прилёта', default=timezone.datetime.now().date() + datetime.timedelta(days=7))
    departure_date = models.TimeField(verbose_name='Departure date', default=timezone.datetime.now())
    arrival_date = models.TimeField(verbose_name='Arrival date', default=timezone.datetime.now())
    class_of_service = models.CharField(choices=CLASS_OF_SERVICE, max_length=1, default=ECONOMY_CLASS)
    def __unicode__(self):
        return '{} {} {} {} {} {}'.format(self.flight_number, self.departure_city, self.arrival_city, self.departure_time, self.arrival_time, self.class_of_service)