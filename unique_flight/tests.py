import unittest
from aircraft.models import Aircraft
from airport.models import Airport
from city.models import City
from country.models import Country
from flight.models import Flight
from unique_flight.models import UniqueFlight


class UniqueFlightTest(unittest.TestCase):
    def setUp(self):
        self.country = Country.objects.create(country='Russia')
        self.city = City.objects.create(city='Tomsk', country=self.country)
        self.airport = Airport.objects.create(city=self.city, code='K01')
        self.aircraft = Aircraft.objects.create(seat_count_F=10,
                                                seat_count_B=10,
                                                seat_count_E=10,
                                                seats_in_a_row_F=2,
                                                seats_in_a_row_B=2,
                                                seats_in_a_row_E=2)
        self.flight = Flight.objects.create(aircraft=self.aircraft,
                                            arrival_airport=self.airport,
                                            departure_airport=self.airport)
        self.left_seats = 1
        self.unique_flight = UniqueFlight.objects.create(flight=self.flight,
                                                         left_seats_E=self.left_seats,
                                                         left_seats_B=self.left_seats,
                                                         left_seats_F=self.left_seats)

    def tearDown(self):
        self.unique_flight.delete()
        self.flight.delete()
        self.aircraft.delete()
        self.airport.delete()
        self.city.delete()
        self.country.delete()

    def try_taking_seat(self, class_of_service):
        result = self.unique_flight.try_take_seat(class_of_service)
        self.assertTrue(result)
        self.assertEqual(self.unique_flight.get_left_seats(class_of_service), 0)
        result = self.unique_flight.try_take_seat(class_of_service)
        self.assertFalse(result)
        self.assertEqual(self.unique_flight.get_left_seats(class_of_service), 0)

    def test_try_taking_seat(self):
        self.try_taking_seat(Flight.ECONOMY_CLASS)
        self.try_taking_seat(Flight.BUSINESS_CLASS)
        self.try_taking_seat(Flight.FIRST_CLASS)
