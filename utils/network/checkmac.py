import re


def checkMAC(x):
    if re.match("^([0-9a-f]{2}[:.-]?){5}[0-9a-f]{2}$", x.lower()):
        return True
    else:
        return False
