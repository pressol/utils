# this should be used drectly where needed and not placed into a variable
def secure_read(secret_file):
        with open(secret_file, "r") as sf:
            return sf.readline()

