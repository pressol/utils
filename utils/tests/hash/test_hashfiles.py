import os
from unittest import TestCase

from utils.hash.hashfiles import hashfilemd5, hashfilesha256, hashfilesha512


class hashfiles(TestCase):
    file = "/test/repo/rockyou.txt"
    def setUp(self):
        # gets rock-you password list
        if not os.path.exists(self.file):
            exit(1)

    def test_hashfilesha512(self):
        self.assertEqual(
            hashfilesha512(file=self.file),
            "6359fe9a1fee8b593072489d9c6a54fc4df05bbe268a8c68e4ca97a222dc3d3173b2440417360ad205f8358466c85a1b1db75bd1ae284232117cbb7edb8e7acd"
        )

    def test_hashfilemd5(self):
        self.assertEqual(
            hashfilemd5(file=self.file),
            "9076652d8ae75ce713e23ab09e10d9ee"
        )

    def test_hashfilesha256(self):
        self.assertEqual(
            hashfilesha256(file=self.file),
            "6dfa76aa0e02303994fd1062d0ac983f0b69ece5474d85a5bba36362e19c1076"
        )
