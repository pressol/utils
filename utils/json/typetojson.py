import json


# supported data type are detailed
# https://docs.python.org/3/library/json.html
def detect_type_return_json(data):
    data_type = type(data)
    if data_type == dict or data_type == list or data_type == tuple:
        return json.dumps(data)
    elif data_type == str or data_type == int or data_type == float or data_type == bool:
        return data
