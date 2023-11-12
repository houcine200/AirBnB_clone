#!/usr/bin/python3

import unittest
from models.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        self.new_state = State()

    def tearDown(self):
        del self.new_state

    def test_state_attributes(self):
        self.assertEqual(self.new_state.name, "")

    def test_state_attribute_assignment(self):
        self.new_state.name = "Florida"

        self.assertEqual(self.new_state.name, "Florida")


if __name__ == '__main__':
    unittest.main()
