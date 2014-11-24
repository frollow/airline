import datetime
from django.db import models
from flight.models import Flight


class UniqueFlight(models.Model):
    flight = models.ForeignKey(Flight, verbose_name='Flight')
    departure_datetime = models.DateTimeField(verbose_name='Departure date and time', default=datetime.datetime.now())
    left_seats_F = models.IntegerField(verbose_name='Left seats of first class', default=0)
    left_seats_B = models.IntegerField(verbose_name='Left seats of business class', default=0)
    left_seats_E = models.IntegerField(verbose_name='Left seats of economic class', default=0)

    def get_price(self, class_of_service):
        if class_of_service == Flight.ECONOMY_CLASS:
            return self.flight.price_E
        elif class_of_service == Flight.BUSINESS_CLASS:
            return self.flight.price_B
        else:
            return self.flight.price_F

    def try_take_seat(self, class_of_service):
        if class_of_service == Flight.ECONOMY_CLASS and self.left_seats_E > 0:
            self.left_seats_E -= 1
            self.save()
            return True
        elif class_of_service == Flight.BUSINESS_CLASS and self.left_seats_B > 0:
            self.left_seats_B -= 1
            self.save()
            return True
        elif class_of_service == Flight.FIRST_CLASS and self.left_seats_F > 0:
            self.left_seats_F -= 1
            self.save()
            return True
        else:
            return False

    def __unicode__(self):
        return "{} {} - {} : {} {} {}".format(self.departure_datetime, self.flight.departure_airport,
                            self.flight.arrival_airport, self.left_seats_E, self.left_seats_B,
                            self.left_seats_F)