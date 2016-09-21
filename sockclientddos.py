#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

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
server_address = ('localhost', 8000)

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('connecting to %s port %s' % server_address)
    sock.connect(server_address)
    try:

        # Send data
        message = 'This is NOT the message.  It will be repeated.'
        print('sending "%s"' % message)
        sock.send(message.encode())

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        #while amount_received < amount_expected:
        #    data = sock.recv(16)
            #amount_received += len(data)
            #print >>sys.stderr, 'received "%s"' % data

    finally:
        print('closing socket')
        sock.close()
