from unittest import TestCase

from utils.persistantstorage import rethinkdb


class Rethinking(TestCase):

    def test_connection(self):
        database = rethinkdb.connect()
        server_info = database.server()
        self.assertEquals("84c7d240d877_49g", server_info["name"])

    def test_