#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import socket
import sys

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

port = 5350 #Random Nubmer, should be changed.
chat = 'chat.db'
sqlrecieve = 'SELECT * FROM message WHERE NOT is_from_me ORDER BY date DESC LIMIT 1'
sqlsender = "SELECT message.guid, chat.chat_identifier FROM message INNER JOIN chat_message_join ON message.rowid = chat_message_join.message_id INNER JOIN chat ON chat_message_join.chat_id = chat.rowid WHERE message.guid = '{}'"

def errorprint(*args, **kwargs):
    """ Print to stderr. from http://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python """
    print(*args, file=sys.stderr, **kwargs)

try:
    portfile = open('address', 'r')
    port = int(portfile.read().split()[1])
    errorprint('using port {}'.format(port))
except FileNotFoundError:
    errorprint('address file not found, booting on port {}.'.format(port))

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


def init():
    print('Server booting')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(4)  # Should be changed to a different number
    while True:
        conn, addr = sock.accept()
        # t is for thread
        t = threading.Thread(target=connect, args=([conn]))  # the second t is for the function t.
        t.start()


def connect(sock):
    errorprint("entered socket")
    handshake = sock.recv(16).decode()
    errorprint('handshake data: ' + handshake)
    ident, flag = handshake.split("\n")
    errorprint('uuid is {}'.format(ident))
    errorprint('flag bool is {}'.format(flag is bytes(True).decode()))
    if flag == bytes(True).decode():
        apple(sock, ident)
    else:
        client(sock, ident)
    sock.close()


def client(sock, ident):
    #if 'lguid' not in locals():  # And this isnt any better
    #    lguid = '0'
    #print('client connecting')
    lguid = sock.recv(16).decode()
    errorprint('latest guid is {}'.format(lguid))
    #print('recieved guid: ' + lguid)
    #lconts is a list of contenets of the server database.
    #lconts = ['first string', 'second string/second line', 'third string, same line']
    #for contents in lconts:
        #sock.send(contents.encode())
    errorprint(full[-1][0])
    b = full[-1][0].encode()
    sock.send(b)
    #sock.send(contents.encode())


full = "0"
lguid = "0"  # call sql later
def apple(sock, ident):
    global lguid, full  # I shouldnt need to do this
    if full:
        oldfull = full
    #print(locals())
    #if 'lguid' not in locals():  # And this isnt any better
        #lguid = '0'
        #print('lguid not found')
    #print('apl inition')
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
        full = oldfull
        errorprint('NaN')


init()
