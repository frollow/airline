# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class Order(models.Model):
    registration_time = models.DateTimeField(verbose_name='Flight registration time', default=timezone.now)
    first_name = models.CharField(max_length=255, verbose_name='First name', default='')
    last_name = models.CharField(max_length=255, verbose_name='Last name', default='')


