import json


def readjson(filename: str):
    """

    Returns:
        object:
    """
    with open(filename, "rb") as file:
        raw = json.load(file)
        return raw
