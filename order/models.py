# -*- coding: utf-8 -*-
import datetime
from django.db import models
from unique_flight.models import UniqueFlight


class Order(models.Model):
    registration_time = models.DateTimeField(verbose_name='Flight registration time', default=datetime.datetime.now())
    is_registered = models.BooleanField(verbose_name='Is registered', default=False)
    first_name = models.CharField(max_length=255, verbose_name='First name', default='')
    last_name = models.CharField(max_length=255, verbose_name='Last name', default='')
    document_id = models.CharField(max_length=11, verbose_name='Document ID', default='')
    birth_day = models.DateField(verbose_name='Date of birth', default='1990-01-01')
    email = models.EmailField(max_length=255, verbose_name='Email', default='')
    unique_flight = models.ForeignKey(UniqueFlight, verbose_name='Unique flight', default='')
    order_hash = models.CharField(max_length=256, verbose_name='Hash', default='')
    class_of_service = models.CharField(max_length=1, verbose_name='Class of service', default='E')
