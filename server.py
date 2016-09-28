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
    print('Server booting')
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
    print('handshake data: ' + handshake)
    ident, flag = handshake.split("\n")
    print('uuid is {}'.format(ident))
    print('flag bool is {}'.format(flag is bytes(True).decode()))
    if flag == bytes(True).decode():
        apple(sock, ident)
    else:
        client(sock, ident)
    sock.close()


def client(sock, ident):
    #if 'lguid' not in locals():  # And this isnt any better
    #    lguid = '0'
    #print('client connection')
    lguid = sock.recv(16).decode()
    print('latest guid is {}'.format(lguid))
    #print('recieved guid: ' + lguid)
    #lconts is a list of contenets of the server database.
    #lconts = ['first string', 'second string/second line', 'third string, same line']
    #for contents in lconts:
        #sock.send(contents.encode())
    sock.send(full)
    #sock.send(contents.encode())


#lguid = "0"  # call sql later
def apple(sock, ident):
    global full
    #global lguid  # I shouldnt need to do this
    if 'lguid' not in locals():  # And this isnt any better
        lguid = '0'
    #print('apl connection')
    #print(lguid)
    serror = sock.send(lguid.encode())
    #print('error is {}'.format(serror))
    if serror != None: #you scrub this isnt accurate, serror is the # of bytes sent
        #print('Error')
        pass
    rec = True
    full = ''
    while rec:
        rec = sock.recv(4048).decode()
        #print(rec)
        #print('Received message: ')# "{}"'.format(rec))
        full += rec
    full = full.split(chr(2))
    full.remove(full[-1])
    #print(full[-2])
    #print(len(full[-2]))
    for num, row in enumerate(full):
        #full[full.index(m)] = m.split('yo')
        full[num] = row.split(chr(1))
    #print(rec)
    #print(full[-2])
    if full:
        print('received "{}" from apple'.format(full[-1][0]))
        lguid = full[-1][1]
        #print(lguid)
    else:
        print('NaN')


connect()
