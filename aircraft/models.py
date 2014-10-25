# -*- coding: utf-8 -*-
from django.db import models


class Aircraft(models.Model):
    company = models.CharField(max_length=16)
    model = models.CharField(max_length=16)
    seat_count = models.CharField(max_length=3)

    def __unicode__(self):
        return '{} {}'.format(self.company, self.model)