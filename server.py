#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__appname__    = "pymessage"
__author__     = "Marco Sirabella, Owen Davies"
__copyright__  = ""
__credits__    = "Marco Sirabella, Owen Davies"
__license__    = "new BSD 3-Clause"
__version__    = "0.0.1"
__maintainers__= "Marco Sirabella, Owen Davies"
__email__      = "msirabel@gmail.com, dabmancer@dread.life"
__status__     = "Prototype"
__module__     = ""

def forwardsock(info):
    text = pickle.dumps(info)
    sock.connect(address)
    try:
        sock.send(text)
    finally:
        sock.close()

def connect():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((socket.gethostname, port))
    sock.listen(4) #Should be changed to a different number
    while True:
        conn, addr = socket.accept()
        thread(conn)

class thread(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.start(sock)
    def run(self sock):
        handshake = sock.recv(16)
        machine, flag = handshake.split("\n")
        if flag==0:
            apple(sock, machine)
        else:
            client(sock, machine)
        sock.close()
