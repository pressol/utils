import os
import urllib.request
from unittest import TestCase

from utils.hash.hashfiles import *


class hashfiles(TestCase):

    def setUp(self):
        with urllib.request.urlopen(
                "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt") as response, open(
            "/tmp/rockup.txt", 'wb') as out_file:
            data = response.read()  # a `bytes` object
            out_file.write(data)

    def tearDown(self):
        os.remove("/tmp/rockup.txt")

    def test_hashfilesha512(self):
        infile = "/tmp/rockup.txt"
        self.assertEqual(
            hashfilesha512(file=infile),
            "6359fe9a1fee8b593072489d9c6a54fc4df05bbe268a8c68e4ca97a222dc3d3173b2440417360ad205f8358466c85a1b1db75bd1ae284232117cbb7edb8e7acd"
        )

    def test_hashfilemd5(self):
        infile = "/tmp/rockup.txt"
        self.assertEqual(
            hashfilemd5(file=infile),
            "9076652d8ae75ce713e23ab09e10d9ee"
        )

    def test_hashfilesha256(self):
        infile = "/tmp/rockup.txt"
        self.assertEqual(
            hashfilesha256(file=infile),
            "6dfa76aa0e02303994fd1062d0ac983f0b69ece5474d85a5bba36362e19c1076"
        )
