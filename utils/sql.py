import sqlite3
from rtcclient.files import file
import datetime
from shared_lib.utils.pythontools.code import warning

DEFAULT_PATH = ("state.sqlite3")



def db_connect(db_path=DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con

# this should be used with caution as if the database
# is very large you will run out of RAM
@warning
def select_all():
    conn = db_connect()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM "file"''')
    all_data = cur.fetchall()
    conn.close()
    return all_data

def select_by_filename(filename):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM "file" WHERE file_name=?''', (filename,))
    all_data = cur.fetchall()
    conn.close()
    return all_data


def select_by_hash(hash):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM "file" WHERE current_file_hash=?''', (hash,))
    all_data = cur.fetchall()
    conn.close()
    return all_data


def addfiletotbl(file, newhash, currenthash, date, dmstate, dmtype):
    conn = db_connect()
    cur = conn.cursor()
    sql = '''INSERT INTO "file"(file_name,original_file_hash,current_file_hash,mod_date,dmstate) 
    VALUES(?,?,?,?,?)'''
    cur.execute(sql, (file, currenthash, newhash, date, dmstate, dmtype))
    conn.commit()
    data = cur.lastrowid
    conn.close()
    return data


def current_hash_addfiletotbl(file, newhash, date, dmstate, dmtype):
    conn = db_connect()
    cur = conn.cursor()
    sql = '''INSERT INTO "file"(file_name,current_file_hash,mod_date,dmstate,dmtype) 
    VALUES(?,?,?,?,?)'''
    cur.execute(sql, (file, newhash, date, dmstate, dmtype))
    conn.commit()
    data = cur.lastrowid
    conn.close()
    return data


def updatefiletable(file, hash):
    conn = db_connect()
    cur = conn.cursor()
    sql = '''UPDATE file SET current_file_hash=?
    WHERE file_name=?'''
    cur.execute(sql, (hash, file))
    conn.commit()
    conn.close()


# there will be no update or delete as this is something that RTC doesn't allow
# and therefore will break the world
def addfile2changeset(id, file_id, workitemid):
    id = str(id)
    conn = db_connect()
    cur = conn.cursor()
    sql = '''INSERT INTO change_set(id, file_id, workitem) 
        VALUES(?,?,?)'''
    cur.execute(sql, (id, file_id, workitemid))
    conn.commit()
    return cur.lastrowid


def file_in_db(filename):
    if select_by_filename(filename).__len__() >= 1:
        return True
    else:
        return False


def add_obj_file_2_db(obj):
    obj = obj
    return current_hash_addfiletotbl(
        file=obj.get_filename(),
        newhash=obj.get_sha512(),
        date=datetime.datetime.now(),
        dmstate=obj.get_dmstate(),
        dmtype=obj.get_dmtype(),
    )


# assumes there is only one returned
def return_file_obj(filename):
    tmp = select_by_filename(filename)
    print()
    if tmp[0][6] == None:
        tmp[0][5] = ""
    return_obj = file(
        tmp[0][1],
        tmp[0][3],
        "",
        "",
        tmp[0][6],
        tmp[0][5]
    )
    return_obj.set_fileid(tmp[0][0])
    return return_obj


# this will be redundant when this can be retrieved from RTC
def get_file_id(filename):
    files_list = select_by_filename(filename)
    for files in files_list:
        return files[0]


def add_workitem(workitem_id, current_workitem_state):
    conn = db_connect()
    cur = conn.cursor()
    sql = '''INSERT INTO work_item(workitemid, current_state) 
            VALUES(?,?)'''
    cur.execute(sql, (workitem_id, current_workitem_state))
    conn.commit()
    return cur.lastrowid


def get_workitem(id):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM "work_item" WHERE workitemid=?''', (id,))
    all_data = cur.fetchall()
    conn.close()
    return all_data


def workitem_in_db(workitem_id):
    if get_workitem(workitem_id).__len__() >= 1:
        return True
    else:
        return False

def check_table_exists(TableName):
    q = "SELECT name FROM sqlite_master WHERE type='table' AND name='{}'".format(TableName)
    conn = db_connect()
    cur = conn.cursor()
    cur.execute(q)
    if cur.rowcount > 0:
        return True
    else:
        return False
