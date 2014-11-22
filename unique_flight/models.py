import datetime
from django.db import models
from flight.models import Flight


class UniqueFlight(models.Model):
    flight = models.ForeignKey(Flight, verbose_name='Flight')
    departure_datetime = models.DateTimeField(verbose_name='Departure date and time', default=datetime.datetime.now())
    left_seats_F = models.IntegerField(verbose_name='Left seats of first class', default=0)
    left_seats_B = models.IntegerField(verbose_name='Left seats of business class', default=0)
    left_seats_E = models.IntegerField(verbose_name='Left seats of economic class', default=0)
