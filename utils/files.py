from os import walk

from utils.hashfiles import hashfilesha512, hashfilesha256, hashfilemd5
from utils.sql import *
import datetime

'''
        Will make a sql query to Files table and get current hash for the files in
        the directory given
        If the current hash of the file and the current hash in the database are the same
        then the file hash not changed.

        IMPORTANT
        hash used is hash512 this will mitigate the possibility for collisions to occur
        which could happen in huge databases 

        :param path - this is a full path string
        :return list of changed files

        '''


def find_changed_files(path):
    t, p, filenames = next(walk(path))
    # The var name is a bit miss-leading it will contain any new file
    changed_files = list()
    for file in filenames:
        db_file = select_by_filename(file)
        file_hash = hashfilesha512(t + file)
        if db_file.__len__() == 0:
            db_file = "new_file"
        else:
            for f in db_file:
                if not f[2] == file_hash or not f[3] == file_hash:
                    updatefiletable(file=file, hash=file_hash)
                    filedict = dict()
                    filedict["file_name"] = file
                    filedict["file_hash"] = file_hash
                    changed_files.append(filedict)
        if type(db_file) is str and db_file == "new_file":
            addfiletotbl(file=file, newhash=file_hash, currenthash=file_hash, date=datetime.datetime.now(), dmstate="prepare")
            filedict = dict()
            filedict["file_name"] = file
            filedict["file_hash"] = file_hash
            changed_files.append(filedict)
    return changed_files


def get_all_files(path):
    t, p, filenames = next(walk(path))
    file_list = list()
    for file in filenames:
        path2file = (t + "/" + file)
        tmp = dict()
        # create key:value dict which is then added to a list of files
        tmp["file_name"] = (path2file)
        tmp["hash_sha512"] = hashfilesha512(path2file)
        tmp["hash_sha256"] = hashfilesha256(path2file)
        tmp["hash_md5"] = hashfilemd5(path2file)
        file_list.append(tmp)
        del tmp
    return file_list
