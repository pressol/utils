import csv
import os
from unittest import TestCase

from utils.persistantstorage.pickledb.libpickledb import *


class Libpickledb(TestCase):
    database = "/tmp/unittest.db"

    def test_connection(self):
        objpickle = open_store(self.database)
        self.assertEqual(type(objpickle) == pickledb.PickleDB, True)

    def test_insert_single_data(self):
        objpickle = open_store(self.database)
        store(objpickle, key="test", value="test")

    def test_get_single_data(self):
        objpickle = open_store(self.database)
        get_data(objpickle, key="test")

    def test_remove_single_entry(self):
        objpickle = open_store(self.database)
        remove_data(objpickle, key="test")

    def test_bulk_insert(self):
        file = '/test/repo/AnimalAge.csv'
        objpickle = open_store(self.database)
        try:
            # gets AnimalAge.csv
            if os.path.exists(file):
                with open(file) as csvfile:
                    reader = csv.reader(csvfile, delimiter=",")
                    for row in reader:
                        print(row)
                        store(objpickle, key=row[0], value=row[1])
            else:
                self.fail("File failed to download")
        finally:
            self.fail()

    def test_bulk_get(self):
        file = '/test/repo/AnimalAge.csv'
        objpickle = open_store(self.database)
        data_compare = []
        try:
            # gets AnimalAge.csv
            if os.path.exists(file):
                with open(file) as csvfile:
                    reader = csv.reader(csvfile, delimiter=",")
                    for row in reader:
                        odata = get_data(objpickle, key=row[0])
                        if odata == row[1]:
                            data_compare.append(True)
                        else:
                            data_compare.append(False)
            else:
                self.fail("File failed to download")

            self.assertEqual(all(data_compare), True)

