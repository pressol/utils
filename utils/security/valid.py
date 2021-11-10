def in_nodes(token, node_list: list):
    for node in node_list:
        if node["token"] == token:
            return True
    return False


def valid_token(token, check, TOKEN_SIZE=64):
    if token.__len__() - TOKEN_SIZE == TOKEN_SIZE:
        if in_nodes(token, check):
            return True
    return False
