import hashlib

from utils.json.typetojson import detect_type_return_json


def sha512list(data):
    list_string: list = []
    if not type(data) == int:
        for l in data:
            list_string.append(detect_type_return_json(l))
    else:
        list_string.append(data)
    return hashlib.sha512(detect_type_return_json(list_string).encode("utf-8")).hexdigest()
