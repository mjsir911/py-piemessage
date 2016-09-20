#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle, socket

__appname__    = ""
__author__     = "Marco Sirabella"
__copyright__  = ""
__credits__    = ["Marco Sirabella"]  # Authors and bug reporters
__license__    = "GPL"
__version__    = "1.0"
__maintainer__ = "Marco Sirabella"
__email__      = "msirabel@gmail.com"
__status__     = "Prototype"  # "Prototype", "Development" or "Production"
__module__     = ""

address = ('sirabella.org', 8000)

def forwardsock(info):
    text = pickle.dumps(info)
    #print(text)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    try:
        sock.send(text)
    finally:
        sock.close()

forwardsock('aR')
#forwardsock('')

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    msg = sock.recv(1024)
    if msg != b'':
        print(pickle.loads(msg))
    else:
        print(msg)
    sock.close()
