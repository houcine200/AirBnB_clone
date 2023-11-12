#!/usr/bin/python3

import unittest
from models.user import User
from models.base_model import BaseModel
from models import storage


class TestUser(unittest.TestCase):

    def setUp(self):
        self.new_user = User()

    def tearDown(self):
        del self.new_user

    def test_user_type(self):
        self.assertEqual(self.new_user.email, "")
        self.assertEqual(self.new_user.password, "")
        self.assertEqual(self.new_user.first_name, "")
        self.assertEqual(self.new_user.last_name, "")

    def test_user_attribute(self):
        self.new_user.first_name = "Houcine"
        self.new_user.last_name = "Hamza"
        self.new_user.email = "my_airbnb98@mail.com"
        self.new_user.password = "azerty"

        self.assertEqual(self.new_user.email, "my_airbnb98@mail.com")
        self.assertEqual(self.new_user.password, "azerty")
        self.assertEqual(self.new_user.first_name, "Houcine")
        self.assertEqual(self.new_user.last_name, "Hamza")
        


if __name__ == '__main__':
    unittest.main()
