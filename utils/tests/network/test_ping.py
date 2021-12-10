from unittest import TestCase

from utils.network.ping import request, ping_web_multi_host_up, ping_web_single_host_up


class Ping(TestCase):
    def test_pass_request(self):
        host = "1.1.1.1"
        self.assertEqual(request(host), True)

    """
    ip address should not work - but may in some instances
    https://en.wikipedia.org/wiki/Carrier-grade_NAT
    """

    def test_fail_request(self):
        host = "100.64.0.1"  # Carrier-grade_NAT IP should probably never be pingable
        self.assertEqual(request(host), False)

    def test_pass_request_domain(self):
        host = "google.co.uk"
        self.assertEqual(request(host), True)

    def test_fail_request_domain(self):
        host = "invalid.ope.uk.net"  # Carrier-grade_NAT IP should probably never be pingable
        self.assertEqual(request(host), False)


class Ping_Web_Single(TestCase):
    def test_ping_web_single_host_up(self):
        host = "1.1.1.1"
        self.assertEqual(ping_web_single_host_up(host), True)

    def test_ping_web_single_host_down(self):  # will take a long time to run this test
        host = "invalid.ope.uk.net"
        self.assertEqual(ping_web_single_host_up(host), False)


class Ping_Web_Multi(TestCase):
    def test_ping_web_multi_host_up(self):
        host = ["1.1.1.1", "google.co.uk", "bing.com"]
        self.assertEqual(ping_web_multi_host_up(host), True)
