#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import uuid
import socket
import time

__appname__     = "pymessage"
__author__      = "Marco Sirabella, Owen Davies"
__copyright__   = ""
__credits__     = "Marco Sirabella, Owen Davies"
__license__     = "new BSD 3-Clause"
__version__     = "0.0.3"
__maintainers__ = "Marco Sirabella, Owen Davies"
__email__       = "msirabel@gmail.com, dabmancer@dread.life"
__status__      = "Prototype"
__module__      = ""

address = ('localhost', 5350)


lguid = '0'
def connect():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    sock.send((hex(uuid.getnode()) + '\n').encode() + bytes(False))  # ik this is such BAD CODE
    print("sent")
    sock.send(lguid.encode())
    print('sent latest guid: {}'.format(lguid))
    # contents = "latest guid +5: {}".format(lguid + '5')
    msg = True
    fullmsg = ''
    while msg:
        msg = sock.recv(16).decode()  # low byte count for whatever reason
        #print('mes rec: {}'.format(msg))
        fullmsg += msg
    print('received message: {}'.format(fullmsg))

    sock.close()


connect()
