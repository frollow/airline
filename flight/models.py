# -*- coding: utf-8 -*-
from django.db import models


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
    departure_date = models.DateField(verbose_name='Departure date')
    arrival_date = models.DateField(verbose_name='Arrival date')
    departure_time = models.TimeField(verbose_name='Departure time', default="08:00")
    arrival_time = models.TimeField(verbose_name='Arrival time', default="10:00")

    class_of_service = models.CharField(choices=CLASS_OF_SERVICE, max_length=1, default=ECONOMY_CLASS)

    def __unicode__(self):
        return '{} : {} {} {} -> {} {} {} : {}'.format(self.flight_number, self.departure_date, self.departure_time,
                                                  self.departure_city, self.arrival_city,
                                                  self.arrival_date, self.arrival_time, self.class_of_service)