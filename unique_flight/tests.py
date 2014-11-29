import unittest
from aircraft.models import Aircraft
from airport.models import Airport
from city.models import City
from country.models import Country
from flight.models import Flight
from unique_flight.models import UniqueFlight


class UniqueFlightTest(unittest.TestCase):
    def setUp(self):
        country = Country.objects.create(country='Russia')
        city = City.objects.create(city='Tomsk', country=country)
        airport = Airport.objects.create(city=city)
        aircraft = Aircraft.objects.create(seat_count_F=10,
                                           seat_count_B=10,
                                           seat_count_E=10,
                                           seats_in_a_row_F=2,
                                           seats_in_a_row_B=2,
                                           seats_in_a_row_E=2)
        flight = Flight.objects.create(aircraft=aircraft,
                                       arrival_airport=airport,
                                       departure_airport=airport)
        left_seats = 1
        self.unique_flight = UniqueFlight.objects.create(flight=flight,
                                                         left_seats_E=left_seats,
                                                         left_seats_B=left_seats,
                                                         left_seats_F=left_seats)

    def test_try_taking_seat(self):
        result = self.unique_flight.try_take_seat(Flight.ECONOMY_CLASS)
        self.assertTrue(result)
        self.assertEqual(self.unique_flight.left_seats_E, 0)
        result = self.unique_flight.try_take_seat(Flight.ECONOMY_CLASS)
        self.assertFalse(result)
        self.assertEqual(self.unique_flight.left_seats_E, 0)

        result = self.unique_flight.try_take_seat(Flight.BUSINESS_CLASS)
        self.assertTrue(result)
        self.assertEqual(self.unique_flight.left_seats_B, 0)
        result = self.unique_flight.try_take_seat(Flight.BUSINESS_CLASS)
        self.assertFalse(result)
        self.assertEqual(self.unique_flight.left_seats_B, 0)

        result = self.unique_flight.try_take_seat(Flight.FIRST_CLASS)
        self.assertTrue(result)
        self.assertEqual(self.unique_flight.left_seats_F, 0)
        result = self.unique_flight.try_take_seat(Flight.FIRST_CLASS)
        self.assertFalse(result)
        self.assertEqual(self.unique_flight.left_seats_F, 0)