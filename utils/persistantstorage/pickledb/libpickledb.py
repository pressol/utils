"""
This is a Key Value database for storing information that should stop the generation of new network names when the
SDN config is read.
"""

import pickledb


def open_store(path: str):
    db = pickledb.load(path, True)
    return db


def store(db: pickledb.PickleDB, key: str, value: str):
    db.set(key, value)


def get_data(db: pickledb.PickleDB, key: str):
    return db.get(key)


def remove_data(db: pickledb.PickleDB, key: str):
    return db.rem(key)

"""
if the libraries open_store is used there is no need to use save
Returns a bool if successful
return: bool
"""


def save(db: pickledb.PickleDB):
    return db.dump()
