# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class Order(models.Model):
    registration_time = models.DateTimeField(verbose_name='Flight registration time', default=timezone.datetime.now())
    is_registered = models.BooleanField(verbose_name='Is registered?', default=False)
    first_name = models.CharField(max_length=255, verbose_name='First name', default='')
    last_name = models.CharField(max_length=255, verbose_name='Last name', default='')
    document_id = models.CharField(max_length=11, verbose_name='Document ID', default='')
    birth_day = models.DateField(verbose_name='Date of birth', default=timezone.now().date())
    email = models.EmailField(max_length=255, verbose_name='Email', default='')
