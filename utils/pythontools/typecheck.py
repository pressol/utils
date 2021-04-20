def typecheck(ctype, checkvar):
    if type(checkvar) == ctype:
        return True
    else:
        return False