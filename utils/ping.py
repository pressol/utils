import platform
import subprocess
from time import time


def request(host):
    parm = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', parm, '1', host]
    return subprocess.call(command) == 0
