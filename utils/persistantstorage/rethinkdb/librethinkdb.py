from rethinkdb import RethinkDB
from typing import List


class RethinkStore:

    def __init__(self, hostname: str = "localhost", port: int = 28015):
        self.r = RethinkDB()
        self.hostname = hostname
        self.port = port
        self.conn = self.connect()

    def connect(self, hostname: str = "localhost", port: int = 28015):
        return self.r.connect(hostname, port)

    def create_database(self, database: str):
        self.r.db_create(database).run()

    def create_table(self, database: str, table_name: str):
        self.conn.db(database).table_create(table_name).run()

    def insert_data_dict(self, data: dict, table_name: str):
        self.conn.table(table_name).insert(data).run()

    def insert_data_json(self, data: List[dict], table_name: str):
        self.conn.table(table_name).insert(data).run()

    def server_info(self):
        return self.conn.server()
