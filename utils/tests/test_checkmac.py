import unittest
from unittest import TestCase

from utils.network.checkmac import checkMAC


class MacCheck(TestCase):

    def test_valid_check_mac(self):
        mac = "77-FF-44-AB-17-7A"
        self.assertEqual(checkMAC(mac), True)

    def test_valid_colons_check_mac(self):
        mac = "26:C2:05:5B:66:81"
        self.assertEqual(checkMAC(mac), True)

    def test_valid_dots_check_mac(self):  # should be valid but the regex doesn't allow it
        mac = "961B.7095.92B6"
        self.assertEqual(checkMAC(mac), True)


    def test_valid_no_delimiter_check_mac(self):
        mac = "8E50A4E3728D"
        self.assertEqual(checkMAC(mac), True)

    # lower case
    def test_lower_valid_check_mac(self):
        mac = "77-FF-44-AB-17-7A".lower()
        self.assertEqual(checkMAC(mac), True)

    def test_lower_valid_colons_check_mac(self):
        mac = "26:C2:05:5B:66:81".lower()
        self.assertEqual(checkMAC(mac), True)


    def test_lower_valid_dots_check_mac(self):  # should be valid but the regex doesn't allow it
        mac = "961B.7095.92B6".lower()
        self.assertEqual(checkMAC(mac), True)

    def test_lower_valid_no_delimiter_check_mac(self):
        mac = "8E50A4E3728D".lower()
        self.assertEqual(checkMAC(mac), True)


if __name__ == '__main__':
    unittest.main()
