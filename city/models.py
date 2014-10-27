# -*- coding: utf-8 -*-
from django.db import models
from country.models import Country


class City(models.Model):
    city = models.CharField(max_length=255, verbose_name='Город')
    country = models.ForeignKey(Country, default='')

    def __unicode__(self):
        return '{} {}'.format(self.city, self.country)