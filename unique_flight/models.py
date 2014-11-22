from django.db import models
from django.utils import timezone
from flight.models import Flight


class UniqueFlight(models.Model):
    flight = models.ForeignKey(Flight, verbose_name='Flight')
    departure_date = models.DateField(verbose_name='Departure date', default=timezone.datetime.now().date())
    # unique_id = models.IntegerField(verbose_name='Flight unique id', default=0)
    left_seats_F = models.IntegerField(verbose_name='Left seats of first class', default=0)
    left_seats_B = models.IntegerField(verbose_name='Left seats of business class', default=0)
    left_seats_E = models.IntegerField(verbose_name='Left seats of economic class', default=0)
