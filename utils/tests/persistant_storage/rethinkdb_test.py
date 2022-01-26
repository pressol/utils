import csv
import os
from unittest import TestCase

from utils.persistantstorage.rethinkdb.librethinkdb import RethinkStore


class Rethinking(TestCase):
    server_name = "e0824b21bc5f_y7k"

    def test_connection(self):
        objrethinkdb = RethinkStore()
        server_info = objrethinkdb.server_info()
        name = server_info["name"]
        name = name.split("_")
        self.assertIs(name[0].__len__() == 12, name[1].__len__() == 3, "Server name matches the length requiremnt")

    def test_create_db(self):
        objrethinkdb = RethinkStore()
        if objrethinkdb.server_info()["name"] == self.server_name:
            objrethinkdb.create_database(database="test")

    def test_create_table(self):
        objrethinkdb = RethinkStore()
        if objrethinkdb.server_info()["name"] == self.server_name:
            objrethinkdb.create_table(table_name="test", database="test")

    def test_import_data_from_csv(self):
        file = '/tmp/AnimalAge.csv'
        objrethinkdb = RethinkStore()
        try:
            # gets AnimalAge.csv
            os.system("mega-get 'https://mega.nz/file/808mCbDJ#66I9HXeV8HcLIajf8vrWPMlJt3kfJl4nCnci6UvuAko' '/tmp'")
            if os.path.exists(file):
                if objrethinkdb.server_info()["name"] == self.server_name:
                    with open('/tmp/AnimalAge.csv') as csvfile:
                        reader = csv.reader(csvfile, delimiter=",")
                        for row in reader:
                            print(row)
                            # test
                            self.assertEqual(True, True)
            else:
                self.fail("File failed to download")
        finally:
            # tear it down
            os.remove(file)
