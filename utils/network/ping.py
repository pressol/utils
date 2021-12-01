import os
import platform

import pyping2

def ping(host: str):
    current_os = platform.system().lower()
    if current_os == "windows":
        parameter = "-n"
    else:
        parameter = "-c"
    return os.system(f"ping {parameter} 1 -w2 {host} > /dev/null 2>&1")


def request(host: str):
    r = ping(host)
    if r == 0:
        return True
    else:
        return False


def ping_web_single_host_up(host: str):
    r = pyping2.ping(host)
    if r.ret_code == 0:
        return True
    else:
        return False


def ping_web_multi_host_up(hosts: list):
    r = pyping2.multiping(hosts)
    if r.ret_code == 0:
        return True
    else:
        return False
