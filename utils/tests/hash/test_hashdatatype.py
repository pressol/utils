import time
from unittest import TestCase

from utils.hash.hashdatatype import sha512list


class SHA512List(TestCase):


    def test_sha512list_list_pass(self):
        listof: list = [
            "nvpVdSqEectBp63gwt2DzuA8",
            "RWLvxd9eyW6d2TLYVCLBMaRz",
            "dcY3RZQBJNtpHpC2nV9BFRuz",
            "PvnwHteEx4s3KBWMMk3SBgMv",
            "tCQNJJ9DRMzabBRKqS3arLwX",
            "rHrDb7DQRhLdyzxbqkWPnuPa",
            "ZCHcBF58Rgcxv87ab9Z85S4K",
            "HWnXHVMWJ4v2EhnYAtvJTuNE",
            "MGsVsASA4aM4vaYrpcjfHLjX",
            "TRyxZNtnsW9E2RrnCPr2dgQe"
        ]
        self.assertEqual(
            sha512list(listof),
            "3ae5b8fd1f742407bdb725f4ef66e6c47d021f266e3819fe50d27ed9d10c43b7b3834ab39eb53cbfea907b159bc30422ca214ef757c4eaf4f56bc0ca7e16eeda"
        )

    def test_sha512list_string_pass(self):
        listof: str = "thisisatest"
        self.assertEqual(
            sha512list(listof),
            "976faae22277b98ebd5979fb717e6f842e0082d95b633a20b8181922ba32c9d92dd9af66b2632f7d130fdf444ab79cac69c91a6b44c5d2b6a8cbe965a35b76e4"
        )

    def test_sha512list_dict_pass(self):
        listof: dict = {
            "test": "this is a test",
            "time": 1
        }
        self.assertEqual(
            sha512list(listof),
            "970da6f664712806dbf2c1d69d5be43f4f80f08a58b9cc24aa119535dca59981d513ddab4099def2e3841d95095012d4ac1d6d60bb2a74260d76ff0c6087104e"
        )

    def test_sha512list_int_pass(self):
        listof: int = 1
        self.assertEqual(
            sha512list(listof),
            "cb0b42c73bc373fa2c695ffb4d4c801571f23397aead7c5b793269801e740ed666f83149b1eed6eaab5f07876236f166da5ae3deb8ab52e85dfd9bdd7c3c9432"
        )

    def test_sha512list_tuple_pass(self):
        listof: tuple = ("apple", "banana", "cherry")
        self.assertEqual(
            sha512list(listof),
            "85682c417b51ec64b66f49bf292eaf6fafca6a6649ecb542cb76489169a08f96fdc011c0546d4fff9bde46f94eeede7e86e6f830a9c0c11f488938b4b1e2840f"
        )