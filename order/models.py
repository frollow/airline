# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class Order(models.Model):
    registration_time = models.DateTimeField(verbose_name='Registration time', default=timezone.now)

