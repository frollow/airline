# -*- coding: utf-8 -*-
from django.db import models


class Aircraft(models.Model):
    FIRST_CLASS = 'F'
    BUSINESS_CLASS = 'B'
    ECONOMY_CLASS = 'E'
    CLASS_OF_SERVICE = (
        (FIRST_CLASS, 'First'),
        (BUSINESS_CLASS, 'Business'),
        (ECONOMY_CLASS, 'Economy'),
    )
    company = models.CharField(max_length=16)
    model = models.CharField(max_length=16)
    seat_count_F = models.CharField(max_length=3, default=0)
    seat_count_B = models.CharField(max_length=3, default=0)
    seat_count_E = models.CharField(max_length=3, default=0)
    seat_conf = models.CharField(max_length=10000, default=0)

    def get_seat_count(self, class_of_service):
        if class_of_service == self.FIRST_CLASS:
            return self.seat_count_F
        elif class_of_service == self.BUSINESS_CLASS:
            return self.seat_count_B
        else:
            return self.seat_count_E

    def seat_map_generator(self):
        a_row = []
        self.seat_count_B = int(self.seat_count_B)
        if self.seat_count_F != 0:
            pass
        if self.seat_count_B != 0:
            if self.seat_count_B % 4 == 0:
                for i in xrange(1, self.seat_count_B, 4):
                    a_row.append('A%s' % i)
        return a_row


    def __unicode__(self):
        return '{} {}'.format(self.company, self.model, self.seat_count_F, self.seat_count_B, self.seat_count_E)
