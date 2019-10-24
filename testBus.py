import unittest
from unittest import TestCase
import view


class TestNextBus(TestCase):

    def test_get_route(self):
        # testing get route method with a route string and
        # comparing it to the expected route id returned
        correct_route = "992"
        route_id = view.get_route("METRO Green Line Bus")
        self.assertEqual(correct_route, route_id)

        correct_route_2 = "4"
        route_id = view.get_route("4 - New Brighton - Johnson St - Bryant Av - Southtown")
        self.assertEqual(correct_route_2, route_id)

    def test_wrong_route(self):
        # providing an invalid route and confirming
        # it raises a value error
        with self.assertRaises(ValueError):
            view.get_uri("METRO Green Linea", "Victoria St Station", "west")

        with self.assertRaises(ValueError):
            view.get_uri("16 - University Av - Midwayyy", "University Ave and Fairview Ave", "east")

    def test_get_direction(self):
        # testing direction method with a direction string and
        # comparing it to the expected direction id
        correct_direction = "2"
        direction = view.get_direction("902", "east")
        self.assertEqual(correct_direction, direction)

        correct_direction_2 = "1"
        direction = view.get_direction("4", "south")
        self.assertEqual(correct_direction_2, direction)

    def test_wrong_direction(self):
        # providing invalid direction strings and
        # confirming it raises value error
        with self.assertRaises(ValueError):
            view.get_uri("4 - New Brighton - Johnson St - Bryant Av - Southtown", "Johnson St and Broadway St", "northa")

        with self.assertRaises(ValueError):
            view.get_uri("6 - U of M - Hennepin - Xerxes - France - Southdale", "4th St and 15th Ave", "western")

    def test_get_stop(self):
        # testing get stop method with a stop string and confirming
        # it returns the proper stop code
        correct_stop = "LXUN"
        stop = view.get_stop("16", "2", "University Ave and Lexington Pkwy")
        self.assertEqual(correct_stop, stop)

        correct_stop_2 = "GHXE"
        stop = view.get_stop("9", "2", "Xenia Ave and Golden Hills Dr")
        self.assertEqual(correct_stop_2, stop)

    def test_wrong_stop(self):
        # providing a mis spelled stop and confirming that
        # it raises a value error
        with self.assertRaises(ValueError):
            view.get_uri("9 - Glenwood - Wayzata Blvd - Cedar Lk Rd - 46 St Sta", "Xenia Ave and Galden Hills Dr", "east")

        with self.assertRaises(ValueError):
            view.get_uri("16 - University Av - Midway", "University Ave and Laxington Pkwy", "east")


if __name__ == '__main__':
    unittest.main()
