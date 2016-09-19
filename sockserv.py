#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import pickle

__appname__    = ""
__author__     = "Marco Sirabella"
__copyright__  = ""
__credits__    = ["Marco Sirabella"]  # Authors and bug reporters
__license__    = "GPL"
__version__    = "1.0"
__maintainers__ = "Marco Sirabella"
__email__      = "msirabel@gmail.com"
__status__     = "Prototype"  # "Prototype", "Development" or "Production"
__module__     = ""

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
server_address = (host, 8000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(1)

while True:
    #print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        # Wait for a connection
        #print(type(client_address))
        data = True
        fulldata = b''
        while b'\x00.' not in fulldata:
            data=connection.recv(16)
            fulldata += data
        print(fulldata)
    finally:
        #print(fulldata)
        fulldata = pickle.loads(fulldata)
        iS = None
        aR = None
        if fulldata == "iS":
            iS = client_address[0]
            #print('iS = ' + iS)
        if fulldata == "aR":
            aR = client_address[0]
        else:
            if client_address[0] == iS:
                print(fulldata)
            if client_address[0] == aR:
                    message = "THIS IS A MESSAGEEE"
                    connection.send(pickle.dumps(message))
        connection.close()
