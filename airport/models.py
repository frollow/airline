# -*- coding: utf-8 -*-
from django.db import models


class Airport(models.Model):
    code = models.CharField(max_length=3, verbose_name='Код', unique=True)
    # country = models.ForeignKey(Country, default='')
    # city = models.ForeignKey(City, default='')