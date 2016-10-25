#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import uuid
import socket
import sqlite3
import os
import sys
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
sqlchecknull = "select text, guid, date from message where not is_from_me"
sqlcheck = sqlchecknull + " and date > (select date from message where guid = ?)"
sqlsender = "select message.guid, chat.chat_identifier from message inner join chat_message_join on message.ROWID = chat_message_join.message_id inner join chat on chat_message_join.chat_id = chat.ROWID where message.guid = ?"
address = ('localhost', 5350)


def eprint(*args, **kwargs):
    """ Print to stderr. from http://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python """
    print(*args, file=sys.stderr, **kwargs)

try:
    portfile = open('address', 'r')
    fileconts = portfile.read()
    port = int(fileconts.split()[1])
    address = (fileconts.split()[0], port)
    eprint('using port {} on address {}'.format(address[1], address[0]))
except FileNotFoundError:
    eprint('address file not found, booting on port {}.'.format(port))


""" this isnt needed anymore i think
def dosql(db, command, args=None):
    "" Send database sqlite script, with or without arguments for {}""
    conn = sqlite3.connect(db)
    if args:
        out = conn.execute(command, [args])

    else:
        out = conn.execute(command)
    rows = out.fetchall()
    conn.close()
    return rows
    """


def connect():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    sock.send((hex(uuid.getnode()) + "\n").encode() + bytes(True))
    lguid = sock.recv(64).decode()
    eprint('received ' + lguid)
#
    conn = sqlite3.connect(chat)
    if lguid == '0':
        print('Starting initial send')
        rows = conn.execute(sqlchecknull).fetchall()
    else:
        rows = conn.execute(sqlcheck, [lguid]).fetchall()

    for row in rows:
        msg = list(row)  # lol
        conn = sqlite3.connect(chat)
        msg.append(conn.execute(sqlsender, [msg[1]]).fetchall()[0][1])
        eprint(msg)
        contents = chr(1).join(str(rowc) for rowc in msg) + chr(2)
        sock.send(contents.encode())
        # It turns out you dont need sendall you scrub
    if lguid == '0':
        print('Finishing initial send')

    conn.close()

    sock.close()


oldsize = 0
x = 0
while True:
    try:
        newsize = os.stat(chat + '-wal').st_size
        # you were right, sometimes this file doesnt exist
    except FileNotFoundError:
        eprint('owr')  # Owen was right
        #connect()
        newsize = 1
    if newsize != oldsize:
        connect()
        #pass
    oldsize = newsize
    time.sleep(0.2)
    x +=1
    if x > 300:
        eprint('pinging')
        connect()
        x = 0
