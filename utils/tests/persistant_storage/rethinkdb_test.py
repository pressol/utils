from unittest import TestCase

from utils.persistantstorage.rethinkdb import RethinkStore


class Rethinking(TestCase):

    def test_connection(self):
        objrethinkdb = RethinkStore()
        server_info = objrethinkdb.server_info()
        self.assertEqual("84c7d240d877_49g", server_info["name"])

    def test_create_db(self):
        objrethinkdb = RethinkStore()
        if objrethinkdb.server_info()["name"] == "84c7d240d877_49g":
            objrethinkdb.create_database(database="test")

    def test_create_table(self):
        objrethinkdb = RethinkStore()
        if objrethinkdb.server_info()["name"] == "84c7d240d877_49g":
            objrethinkdb.create_table(table_name="test", database="test")
            print()
