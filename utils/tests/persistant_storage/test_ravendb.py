from unittest import TestCase

from utils.persistantstorage.ravendb.ravendb import ravendb


class Testravendb(TestCase):
    class Test(object):
        def __init__(self, name, key=None):
            self.name = name
            self.key = key

    def setUp(self) -> None:
        self.conn = ravendb(database_name="test")

    def test_get_server_info(self):
        self.assertEqual(
            self.conn.get_server_info(),
            {
                'server_ip': ['127.0.0.1'],
                'servers': ['http://localhost:8080']
            }
        )

    def test_get_one_obj(self):
        self.conn.get_one(
            document_name="testing",
            obj_type=self.Test
        )

    def test_get_one(self):
        self.conn.get_one(document_name="testing")

    def test_get_lots(self):
        self.conn.get_lots(
            document_name=["testing"],
            obj_type=self.Test
        )

    def test_delete_one(self):
        document_name = "testing"
        self.conn.delete_one(
            document_name=document_name
        )

    def test_delete_lots(self):
        document_name = ["testing"]
        self.conn.delete_lots(
            document_name=document_name
        )

    def test_insert_one(self):
        test = self.Test("testing")
        self.conn.insert_one(
            obj_document=test
        )

    def test_query_object_type(self):
        t = self.conn.query_object_type(
            document_obj=self.Test
        )
        self.assertEqual(type(t), list)

    """
    def test_query_key_value(self):
        t = self.conn.query_key_value(
            key="name",
            value="testing"
        )
        print()
    """

    def test_query_object_type_key_value(self):
        t = self.conn.query_object_type_key_value(
            document_obj=self.Test,
            key="name",
            value="testing"
        )
        self.assertEqual(type(t), list)
