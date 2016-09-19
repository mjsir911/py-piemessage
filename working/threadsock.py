#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import pickle
import threading

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


rec = False
msg = True
guid = False
rmsg = False

"""
def check():
    global msg
    global rec
    data = True
    fulldata = b''
    if not rec:
        while data:
            #print('rec')
            data = connection.recv(16)
            fulldata += data
    #if rec == True and msg:
        #print('sending')
        #connection.send(pickle.dumps(msg))
        #msg = False
        #rec = False
        #return 0
    connection.close()
    if fulldata != b'':
        fulldata = pickle.loads(fulldata)
    if fulldata == 'aR' or fulldata == 'iS':
        pass
    elif fulldata == '':
        rec = True
    else:
        return fulldata
        """

connections = {'aR' : None, 'iS' : None}
while True:
    connection, client_address = sock.accept()
    if client_address[0] == connections['aR']:# and msg[0] != guid:
        if rmsg == True:
            connection.send(pickle.dumps(msg))
            connection.close()
            rmsg = False
        else:
            connection.close()
    elif client_address[0] == connections['iS']:
        data = True
        fulldata = b''
        if not rec:
            while data:
                data = connection.recv(16)
                fulldata += data
        connection.close()
        if fulldata != b'':
            fulldata = pickle.loads(fulldata)
        if fulldata == 'aR' or fulldata == 'iS':
            pass
        msg = fulldata
        rmsg = True
    else:
        try:
            data = connection.recv(16)
        finally:
            fulldata = pickle.loads(data)
            if fulldata == "iS":
                connections['iS'] = client_address[0]
            elif fulldata == "aR":
                connections['aR'] = client_address[0]
            connection.close()
        print(connections)
