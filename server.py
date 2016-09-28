#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__appname__    = "pyMessage"
__author__     = "Marco Sirabella, Owen Davies"
__copyright__  = ""
__credits__    = "Marco Sirabella, Owen Davies"
__license__    = "new BSD 3-Clause"
__version__    = "0.0.1"
__maintainers__= "Marco Sirabella, Owen Davies"
__email__      = "msirabel@gmail.com, dabmancer@dread.life"
__status__     = "Prototype"
__module__     = ""

port = 8000
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
    sock.listen(4) #Should be changed to a different number #But does the number DO anything??
    while True:
        print("starting")
        conn, addr = sock.accept()
        t = threading.Thread(target=stuff, args = ([conn])) # So apparently this comma is needed # Replaced with tuple to look BETTER
        t.start()
        print("Looping")

def stuff(sock):
    print("entered socket")
    handshake = sock.recv(16).decode()
    #print('handshake data: ' + handshake)
    machine, flag = handshake.split("\n") # I question why you named this machine
    #print("2") # these numbers arent needed anymore probs
    #print('flag is {}'.format(type(flag)))
    #print('flag data is {}'.format(flag))
    print('uuid is {}'.format(machine))
    print('flag bool is {}'.format(flag == bytes(True).decode()))
    if flag==bytes(True).decode():
        apple(sock, machine)
    else:
        client(sock, machine)
    #print("3")
    sock.close()
    #print("4")

def client(sock, machine):
    print('client connection')
    lguid = sock.recv(60).decode()
    print('guid: ' + lguid)
    contents = "4321".encode()
    sock.sendall(contents)

def apple(sock, machine):
    print('apl connection')
    lguid = "1234" #call sql later
    print('Any errors?: {}'.format(None == sock.send(lguid.encode())))
    r = sock.recv(1024).decode();
    print(r)
    #put r into table.


connect()
