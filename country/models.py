# -*- coding: utf-8 -*-
from django.db import models


class Country(models.Model):
    country = models.CharField(max_length=255, verbose_name='Страна')

    def __unicode__(self):
        return '{}'.format(self.country)