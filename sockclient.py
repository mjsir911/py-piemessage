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

# Create a TCP/IP socket

# Connect the socket to the port where the server is listening
server_address = ('192.168.1.7', 8000)
print('connecting to %s port %s' % server_address)

#try:
    #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock.connect(server_address)
    #sock.send(pickle.dumps('aR'))
#finally:
    #print('closing socket')
    #sock.close()
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)
    message = 'This is the message.  It will be repeated.'
    message = ''
    print('sending "%s"' % message)
    messagedump = pickle.dumps(message)
    sock.send(messagedump)
finally:
    print('closing socket')
    #sock.close()
