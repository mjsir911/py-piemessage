#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import queue
import socket

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
        self.name = self.__name__
        threading.Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            connection, client_address = sock.accept()
            if self.msg:
                msg = self.msg
                msg = pickle.dumps(msg)
                connection.send(msg)
                connection.close()
                print(conn)
            print('closing?')
    def send(self, msg):
        self.msg = msg
