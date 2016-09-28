#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import uuid
import socket
import sqlite3
import os
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

chat = '{}/Library/Messages/chat.db'.format(os.path.expanduser("~"))
sqlrecieve = 'select text, guid from message where not is_from_me order by date desc limit 1'
sqlchecknull = "select text, guid from message"
sqlcheck = sqlchecknull + " where date > (select date from message where guid = '{}')"
sqlsender = "select message.guid, chat.chat_identifier from message inner join chat_message_join on message.ROWID = chat_message_join.message_id inner join chat on chat_message_join.chat_id = chat.ROWID where message.guid = '{}'"
address = ('localhost', 5350)

def dosql(db, command):
    """ Send database sqlite script, with or without arguments for {}"""
    conn = sqlite3.connect(db)
    out = conn.execute(command)
    rows = out.fetchall()
    conn.close()
    return rows


def connect():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    sock.send((hex(uuid.getnode()) + "\n").encode() + bytes(True))
    lguid = sock.recv(64).decode()
    print('recieved ' + lguid)
#
    if lguid == '0':
        rows = dosql(chat, sqlchecknull)
    else:
        rows = dosql(chat, sqlcheck.format(lguid))
    for row in rows:
        msg = list(row)  # lol
        #print(msg)
        msg.append(dosql(chat, sqlsender.format(msg[1]))[0][1])
        #print(sender)
        #splitchar = '\x11'
        #linechar = '\x12'
        #contents = [str(x) for x in msg]
        #contents = chr(1).join(msg) + chr(2)
        contents = 'yo'.join(msg) + chr(2)
        print(contents)
        sock.send(contents.encode())  # It turns out you dont need sendall you scrub
    sock.close()


oldsize = 0
x = 0
while True:
    newsize = os.stat(chat + '-wal').st_size
    if newsize != oldsize:
        connect()
        #pass
    oldsize = newsize
    time.sleep(0.2)
    x +=1
    if x > 300:
        print('pinging')
        connect()
        x = 0
