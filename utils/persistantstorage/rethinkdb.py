from rethinkdb import r

'''
connect to database
'''


def connect(hostname: str = "localhost", port: int = 28015):
    return r.connect(hostname, port)


'''
create table
'''


def create_table(database: str, table_name: str, rethinkobj):
    rethinkobj.db(database).table_create(table_name).run()


def insert_data_dict(data: dict, table_name: str, rethinkobj):
    rethinkobj.table(table_name).insert(data).run()


def insert_data_json(data: list[dict], table_name: str, rethinkobj):
    rethinkobj.table(table_name).insert(data).run()
