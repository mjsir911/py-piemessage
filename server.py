#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import threading
import socket

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

port = 5350
chat = 'chat.db'
sqlrecieve = 'select * from message where not is_from_me order by date desc limit 1'
sqlsender = "select message.guid, chat.chat_identifier from message inner join chat_message_join on message.ROWID = chat_message_join.message_id inner join chat on chat_message_join.chat_id = chat.ROWID where message.guid = '{}'"


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
    sock.listen(4)  # Should be changed to a different number
    while True:
        conn, addr = sock.accept()
        t = threading.Thread(target=stuff, args=([conn]))
        t.start()


def stuff(sock):
    print("entered socket")
    handshake = sock.recv(16).decode()
    rint('handshake data: ' + handshake)
    ident, flag = handshake.split("\n")  # I question why you named this ident
    print('uuid is {}'.format(ident))
    print('flag bool is {}'.format(flag == bytes(True).decode()))
    if flag == bytes(True).decode():
        apple(sock, ident)
    else:
        client(sock, ident)
    sock.close()


rec = ''
def client(sock, ident):
    print('client connection')
    lguid = sock.recv(64).decode()
    print('recieved guid: ' + lguid)
    #lconts is a list of contenets of the server database.
    lconts = ['first string', 'second string/second line', 'third string, same line']
    for contents in lconts:
        sock.sendall(contents.encode())
    #sock.sendall(contents.encode())


def apple(sock, ident):
    global rec
    print('apl connection')
    lguid = "1234"  # call sql later
    serror = sock.sendall(lguid.encode())
    if serror != None:
        print('Error')
    rec = sock.recv(1024).decode()
    print('Received message: "{}"'.format(rec))


connect()
