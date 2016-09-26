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

port = 77865
chat = 'chat.db'
sqlrecieve = 'select * from message where not is_from_me order by date desc limit 1'
sqlsender = "select message.guid, chat.chat_identifier from message inner join chat_message_join on message.ROWID = chat_message_join.message_id inner join chat on chat_message_join.chat_id = chat.ROWID where message.guid = '{}'"
address = ('sirabella.org', 8000)

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
    sock.listen(4) #can be changed to a different number
    while True:
        conn, addr = socket.accept()
        thread(conn)

class thread(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.start(sock)
    def run(self, sock):
        handshake = handshake(sock)
        machine, flag = handshake.split("\n")
        if flag==0:
            apple(sock)
        else:
            client(sock)
        sock.close()