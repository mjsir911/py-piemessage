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
    sock.bind(('', port))  # Interesting find, not sure best practice tho
    sock.listen(4)  # Should be changed to a different number #But does the number DO anything??
    while True:
        print("starting")
        conn, addr = sock.accept()
        t = threading.Thread(target=stuff, args=([conn]))  # So apparently this comma is needed # Replaced with tuple to look BETTER # is a list of tuple required?
        t.start()
        print("Looping")


def stuff(sock):
    print("entered socket")
    handshake = sock.recv(16).decode()
    # print('handshake data: ' + handshake)
    machine, flag = handshake.split("\n")  # I question why you named this machine
    # print("2") # these numbers arent needed anymore probs
    # print('flag is {}'.format(type(flag)))
    # print('flag data is {}'.format(flag))
    print('uuid is {}'.format(machine))
    print('flag bool is {}'.format(flag == bytes(True).decode()))
    if flag == bytes(True).decode():
        apple(sock, machine)
    else:
        client(sock, machine)
    # print("3")
    sock.close()
    # print("4")


# We might want to make this a class cuz variables will be transferred between apple and client
def client(sock, machine):
    print('client connection')
    lguid = sock.recv(64).decode()
    print('guid: ' + lguid)
    lconts = ['first string', 'second string/second line', 'third string, same line']
    for contents in lconts:
        sock.send(contents.encode())
        # Ok so this is wierd, it sends the first line on its own but then it sends the rest of the lines together in one
    #contents = "nun"
    # right now 'nun' is the closing string, stuff after it still gets sent but it closes the while loop # OUTDATED
    #sock.send(contents.encode())


def apple(sock, machine):
    print('apl connection')
    lguid = "1234"  # call sql later
    serror = sock.send(lguid.encode())
    # print('Any errors?: {}'.format([if serror is None]))  # Pep likes this line but it doesnt work
    print('Any errors?: {}'.format([serror == None]))
    rec = sock.recv(1024).decode()
    print('Received message: "{}"'.format(rec))
    # put r into table.


connect()
