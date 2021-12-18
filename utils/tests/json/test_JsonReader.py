import os

from unittest import TestCase
from utils.json.JsonReader import readjson


class JsonReader(TestCase):
    # json file generated using https://json-generator.com/
    def setUp(self) -> None:
        # gets a file
        os.system("mega-get 'https://mega.nz/file/phtVEApA#ypC12v33zEB0itkvqlonTlmiAdzwvav7zrAjFyF5ASE' '/tmp/generated.json'")
        os.path.exists("/tmp/generated.json")

    def tearDown(self):
        os.remove("/tmp/generated.json")

    def test_type_check_readjson(self):
        self.assertEqual(type(readjson("/tmp/generated.json")), list)
