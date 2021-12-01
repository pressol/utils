
def inlookuptable(value: str, lookuptable: str):
    with open(lookuptable, "r") as lookuptablestream:
        for table in lookuptablestream:
            if table.strip("\n") == value:
                return True
    return False


