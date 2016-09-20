#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import socket
import sqlite3
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

chat = 'chat.db'
sqlrecieve = 'select * from message where not is_from_me order by date desc limit 1'
sqlsender = "select message.guid, chat.chat_identifier from message inner join chat_message_join on message.ROWID = chat_message_join.message_id inner join chat on chat_message_join.chat_id = chat.ROWID where message.guid = '{}'"
address = ('192.168.1.7', 8000)

def sqlite(db, script, arg=None):
    """ Send database sqlite script, with or without arguments for {}"""
    conn = sqlite3.connect(db)
    if arg:
        cursor = conn.execute(script.format(arg))
    else:
        cursor = conn.execute(script)
    row = cursor.fetchone()
    conn.close()
    return row

def forwardsock(info):
    text = pickle.dumps(info)
    #print(text)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    try:
        sock.send(text)
    finally:
        sock.close()
def pendingsock():
    forwardsock('')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    fulldata = sock.recv(1024)
    #data = True
    #fulldata = b''
    #while b'\x00.' not in fulldata:
        #data = sock.recv(16)
        #fulldata += data
    sock.close()
    #print(fulldata)
    if fulldata != b'':
        fullinfo = pickle.loads(fulldata)
    else:
        fullinfo = fulldata
    return fullinfo


class Irecieve(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        while True:
            forwardsock('aR')
            msg = pendingsock()
            if msg == b'':
                pass
            else:
                print(msg)


Irecieve()
while True:
    pass
