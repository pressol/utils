import json


def readjson(filename: str):
    with open(filename, "r") as file:
        raw = json.load(file)
        return raw
