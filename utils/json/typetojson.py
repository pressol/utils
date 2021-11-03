import json


# supported data type are detailed
# https://docs.python.org/3/library/json.html
def detect_type_return_json(data):
    data_type = type(data)
    if data_type is dict or list or tuple:
        return json.dumps(data)
    elif data_type == str or int or float or bool:
        return data
