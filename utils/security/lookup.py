def inlookuptable(value: str, lookuptable: str):
    with open(lookuptable, "r") as lookuptablestream:
        for table in lookuptablestream.readline():
            if table == value:
                return True
    return False
