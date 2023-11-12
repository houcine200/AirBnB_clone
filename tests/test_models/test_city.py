#!/usr/bin/python3

import unittest
from models.city import City
from models.state import State

class TestCity(unittest.TestCase):

    def setUp(self):
        self.new_city = City()
        self.s_id = State()

    def tearDown(self):
        del self.new_city

    def test_city_attributes(self):
        self.assertEqual(self.new_city.state_id, "")
        self.assertEqual(self.new_city.name, "")

    def test_city_attribute_assignment(self):
        self.new_city.name = "Tokyo"
        self.new_city.state_id = self.s_id.id

        self.assertEqual(self.new_city.name, "Tokyo")
        self.assertEqual(self.new_city.state_id, self.s_id.id)

if __name__ == '__main__':
    unittest.main()
