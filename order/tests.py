import unittest
from aircraft.models import Aircraft
from airport.models import Airport
from city.models import City
from country.models import Country
from flight.models import Flight
from order.models import Order
from unique_flight.models import UniqueFlight


class OrderTest(unittest.TestCase):
    def setUp(self):
        self.country = Country.objects.create(country='Russia')
        self.city = City.objects.create(city='Tomsk', country=self.country)
        self.airport = Airport.objects.create(city=self.city, code='Key')
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

    def try_take_seat_by_class(self, class_of_service):
        order = Order.objects.create(unique_flight=self.unique_flight, class_of_service=class_of_service)
        free_seats = Order.get_free_seats(self.unique_flight.id, self.unique_flight.flight.aircraft, class_of_service)
        self.assertEqual(len(free_seats), 10)
        order.try_take_seat(free_seats[0])
        free_seats = Order.get_free_seats(self.unique_flight.id, self.unique_flight.flight.aircraft,
                                          class_of_service)
        self.assertEqual(len(free_seats), 9)
        order.delete()

    def test_free_seats(self):
        self.try_take_seat_by_class(Flight.ECONOMY_CLASS)
        self.try_take_seat_by_class(Flight.BUSINESS_CLASS)
        self.try_take_seat_by_class(Flight.FIRST_CLASS)