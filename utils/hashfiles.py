import hashlib

'''
this reader will chunk into 64kb chunks otherwise a 2gb file will use 2gb of ram
'''
_BUF_SIZE = 65536  # 64kb chunks


def hashfilesha512(file):
    if not type(file) is str: return TypeError
    sha512 = hashlib.sha512()
    with open(file, 'rb') as f:
        while True:
            data = f.read(_BUF_SIZE)
            if not data:
                break
            sha512.update(data)
    return sha512.hexdigest()


def hashfilemd5(file):
    if not type(file) is str: return TypeError
    md5 = hashlib.md5()
    with open(file, 'rb') as f:
        while True:
            data = f.read(_BUF_SIZE)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()


def hashfilesha256(file):
    if not type(file) is str: return TypeError
    sha256 = hashlib.sha256()
    with open(file, 'rb') as f:
        while True:
            data = f.read(_BUF_SIZE)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()
