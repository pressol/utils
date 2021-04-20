import requests
import urllib3
from time import time


def request(url):
    url = url
    fullurl = "https://" + url
    error = ""
    timetaken = float()
    stop = time()
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    try:
        start = time()
        page = requests.get(fullurl, verify=False)
        if page.ok:
            stop = time()
            timetaken = stop - start
        else:
            error = "device unreachable"

        return timetaken, error
    except requests.exceptions.ConnectionError as e:
        print(e)
        fullurl = "http://" + url
        start = time()
        page = requests.get(fullurl, verify=False)
        if page.ok:
            stop = time()
            timetaken = stop - start
        else:
            error = "device unreachable"

        return str(timetaken), error

