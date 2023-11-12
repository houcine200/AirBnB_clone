#!/usr/bin/python3

import unittest
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.user import User


class Testplace(unittest.TestCase):

    def setUp(self):
        self.new_user = Place()
        self.a_id = Amenity()
        self.u_id = User()
        self.c_id = City()

    def tearDown(self):
        del self.new_user

    def test_user_type(self):
        self.assertEqual(self.new_user.city_id, "")
        self.assertEqual(self.new_user.user_id, "")
        self.assertEqual(self.new_user.description, "")
        self.assertEqual(self.new_user.name, "")
        self.assertEqual(self.new_user.number_rooms, 0)
        self.assertEqual(self.new_user.number_bathrooms, 0)
        self.assertEqual(self.new_user.max_guest, 0)
        self.assertEqual(self.new_user.price_by_night, 0)
        self.assertEqual(self.new_user.longitude, 0.0)
        self.assertEqual(self.new_user.latitude, 0.0)
        self.assertEqual(self.new_user.amenity_ids, [])

    def test_user_attribute(self):
        self.new_user.city_id = self.c_id.id
        self.new_user.user_id = self.u_id.id
        self.new_user.name = "Houcine"
        self.new_user.description = "Nice Place"
        self.new_user.number_rooms = 4
        self.new_user.number_bathrooms = 2
        self.new_user.max_guest = 3
        self.new_user.price_by_night = 299
        self.new_user.latitude = 8.245
        self.new_user.longitude = 31.45
        self.new_user.amenity_ids = [self.a_id.id]

        self.assertEqual(self.new_user.city_id, self.c_id.id)
        self.assertEqual(self.new_user.user_id, self.u_id.id)
        self.assertEqual(self.new_user.description, "Nice Place")
        self.assertEqual(self.new_user.name, "Houcine")
        self.assertEqual(self.new_user.number_rooms, 4)
        self.assertEqual(self.new_user.number_bathrooms, 2)
        self.assertEqual(self.new_user.max_guest, 3)
        self.assertEqual(self.new_user.price_by_night, 299)
        self.assertEqual(self.new_user.latitude, 8.245)
        self.assertEqual(self.new_user.longitude, 31.45)
        self.assertEqual(self.new_user.amenity_ids,
                         [self.a_id.id])


if __name__ == '__main__':
    unittest.main()
