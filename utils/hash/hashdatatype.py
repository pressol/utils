import hashlib
from utils.json.typetojson import detect_type_return_json


def sha512list(data):
    json_string: list = []
    for l in data:
        json_string.append(detect_type_return_json(l))
    return hashlib.sha512(detect_type_return_json(json_string).encode("utf-8")).hexdigest()
