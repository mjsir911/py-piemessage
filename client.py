#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import uuid
import socket
import time

__appname__    = "pyMessage"
__author__     = "Marco Sirabella, Owen Davies"
__copyright__  = ""
__credits__    = "Marco Sirabella, Owen Davies"
__license__    = "new BSD 3-Clause"
__version__    = "0.0.1"
__maintainers__= "Marco Sirabella, Owen Davies"
__email__      = "msirabel@gmail.com, dabmancer@dread.life"
__status__     = "Prototype"
__module__     = ""

address = ('localhost', 5350)
address = ('sirabella.org', 8000)

def connect():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    sock.send("{}\n".format(hex(uuid.getnode())).encode() + bytes(False)) #ik this is such BAD CODE
    print("sent")
    lguid = 'this is my latest guid'
    sock.send(lguid.encode())
    print('sent latest guid: {}'.format(lguid))
    #contents = "latest guid +5: {}".format(lguid + '5')
    msg = True
    while msg:
        msg = sock.recv(16).decode() # low byte count for whatever reason
        print('message recieved: {}'.format(msg))

    sock.close()


connect()
