# software will run a client mqtt that will listen to a server which will serve up updates
# when they are made available
from paho.mqtt import publish


def send_message(message, topic, hostname, authenication=AUTH):
    publish.single(topic=topic, payload=message, hostname=hostname)


def getupdate(url):
    pass

def client_listener(message, url, channel, auth):
    pass

def server_sender(url, channel, auth, message):
    send_message(message=message, topic=channel, hostname=url, authenication=auth)

def update_server(dir, certificate):
    pass

