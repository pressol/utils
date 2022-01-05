# this file checks to see if the system is setup to run the tests
from shutil import which

app_list = [
    "7z",
    "mega-get"
]
# app check
is_avalible = []
for a in app_list:
    if not which(a) is None:
        is_avalible.append(True)
    else:
        is_avalible.append(False)

if not all(is_avalible):
    exit(1)


