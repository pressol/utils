import sqlite3
import os

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), "../file.sqlite3")
def db_connect(db_path=DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con

def db_create():
    db_sql = ""
    with open("database_setup.sql") as f:
        for line in f.readlines():
            db_sql += line

    conn = db_connect()
    cur = conn.cursor()
    cur.execute(db_sql)
    conn.commit()
    conn.close()


