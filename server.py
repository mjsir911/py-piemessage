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

port = 60000
chat = 'chat.db'
sqlrecieve = 'select * from message where not is_from_me order by date desc limit 1'
sqlsender = "select message.guid, chat.chat_identifier from message inner join chat_message_join on message.ROWID = chat_message_join.message_id inner join chat on chat_message_join.chat_id = chat.ROWID where message.guid = '{}'"

import threading
import socket

def dosql(db, command, arg=None):
    """ Send database sqlite script, with or without arguments for {}"""
    conn = sqlite3.connect(db)
    if arg:
        out = conn.execute(command.format(arg))
    else:
        out = conn.execute(command)
    row = out.fetchone()
    conn.close()
    return row


def connect():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(4) #Should be changed to a different number
    while True:
        print("starting")
        conn, addr = sock.accept()
        t = threading.Thread(target=stuff, args = (conn,))
        t.start()
        print("stopping")

def client(sock, machine):
    lguid = sock.recv(60)
    print(lguid)
    contents = b"some stuff"
    sock.sendall(contents)

def apple(sock, machine):
    lguid = b"1234" #call sql later
    print(None == sock.sendall(lguid))
    r = sock.recv(100000);
    print(r)
    #put r into table.

def stuff(sock):
    print("entered socket")
    handshake = sock.recv(16).decode()
    print(handshake)
    machine, flag = handshake.split("\n")
    print("2")
    print(flag)
    print(flag==0)
    if flag=="\x00":
        apple(sock, machine)
    else:
        client(sock, machine)
    print("3")
    sock.close()
    print("4")

connect()
