#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import queue
import socket
<<<<<<< HEAD
=======
import pickle
>>>>>>> 18072c213de9136bc913f7f2f9bf63fde823b01e

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

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
server_address = (host, 8000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)
sock.listen(1)

connections = {'aR' : None, 'iS' : None}

conn = 'hi'

class Speak(threading.Thread):
    def __init__(self):
<<<<<<< HEAD
        self.name = self.__name__
        threading.Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            connection, client_address = sock.accept()
=======
        threading.Thread.__init__(self)
        self.name = 'hi'
        self.daemon = True
        self.start()
        connection, client_address = sock.accept()
        self.send(1)
        connection.close()
    def run(self):
        while True:
            self.msg = False
            connection, client_address = sock.accept()
            while not self.msg:
                pass
>>>>>>> 18072c213de9136bc913f7f2f9bf63fde823b01e
            if self.msg:
                msg = self.msg
                msg = pickle.dumps(msg)
                connection.send(msg)
                connection.close()
<<<<<<< HEAD
                print(conn)
            print('closing?')
    def send(self, msg):
        self.msg = msg
=======
                self.msg = False
    def send(self, msg):
        self.msg = msg





connections = {'aR' : None, 'iS' : None}
while not (connections['aR'] and connections['iS']):
    connection, client_address = sock.accept()
    #if 1 == 0:
        #pass
    #elif client_address[0] == connections['aR']:
        #aRs = Speak()
    #elif client_address[0] == connections['iS']:
        #data = connection.recv(1024)
        #info = pickle.loads(data)
        #print(info)
        #try:
            #aRs.send(info)
        #except NameError:
            #print('try connecting a client first')
    #else:
    try:
        data = connection.recv(16)
    finally:
        fulldata = pickle.loads(data)
        if fulldata == b'':
            print('empty')
        elif fulldata == "iS":
            print('iS connected')
            connections['iS'] = client_address[0]
        elif fulldata == "aR":
            print('aR connected')
            connections['aR'] = client_address[0]
        else:
            print('no identifier')
        connection.close()
print('all clients connected!')

while True:
    print('continue1')
    connection, client_address = sock.accept()
    #print(connection.listen(2))
    print('continue2')
    client_address = client_address[0]
    print('continue3')
    c = connection.recv(16)
    print('continue4')
    print(c)
    if pickle.loads(c) == b'':
        if 1 == 0:
            pass
        elif client_address == connections['aR']:
            connection.close()
            aRs = Speak()
        elif client_address == connections['iS']:
            connection.close()
            connection, client_address = sock.accept()
            data = connection.recv(1024)
            info = pickle.loads(data)
            print(info)
            try:
                aRs.send(info)
            except NameError:
                print('try connecting a client first')
    else:
        print('connection isnt 0')
>>>>>>> 18072c213de9136bc913f7f2f9bf63fde823b01e
