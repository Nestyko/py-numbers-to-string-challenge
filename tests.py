import unittest
from index import number_to_string


class TestNumbersToString(unittest.TestCase):

    def test_numbers_to_string(self):
        self.assertEqual(number_to_string(1), "one")
        self.assertEqual(number_to_string(2), "two")
        self.assertEqual(number_to_string(26), "twenty six")
        self.assertEqual(number_to_string(128), "one hundred twenty eight")
        self.assertEqual(number_to_string(1528), "one thousand five hundred twenty eight")
        self.assertEqual(number_to_string(150671), "one hundred fifty thousand six hundred seventy one")
