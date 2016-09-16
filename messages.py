#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import time
import datetime
import os
from subprocess import Popen, PIPE

__appname__    = ""
__author__     = "Marco Sirabella"
__copyright__  = ""
__credits__    = ["Marco Sirabella"]  # Authors and bug reporters
__license__    = "GPL"
__version__    = "1.0"
__maintainer__ = "Marco Sirabella"
__email__      = "msirabel@gmail.com"
__status__     = "Prototype"  # "Prototype", "Development" or "Production"
__module__     = ""

chat = '/var/msirabella/Library/Messages/chat.db'
command = 'select * from message where not is_from_me order by date desc limit 1'

guid = ''
while True:
    conn = sqlite3.connect(chat)
    cursor = conn.execute(command)
    row = cursor.fetchone()
    text = row[2]
    #if row[15]+978307200 ==
    tempguid = row[1]
    guid2 = row[1]
    aguid = row[13]
    #print(guid)
# select message.guid, chat.chat_identifier from message inner join chat_message_join on message.ROWID = chat_message_join.message_id inner join chat on chat_message_join.chat_id = chat.ROWID where guid = '12345'
    #accountcommand =  "select message.guid, chat.chat_identifier from message inner join chat_message_join on message.ROWID = chat_message_join.message_id inner join chat on chat_message_join.chat_id = chat.ROWID where message.guid = '2CA8A022-DB4A-4C80-912E-0EE1E5E3F812"
    accountcommand = "select message.guid, chat.chat_identifier from message inner join chat_message_join on message.ROWID = chat_message_join.message_id inner join chat on chat_message_join.chat_id = chat.ROWID where message.guid = '{}'".format(guid)
    cursor = conn.execute("select message.guid, chat.chat_identifier from message inner join chat_message_join on message.ROWID = chat_message_join.message_id inner join chat on chat_message_join.chat_id = chat.ROWID where message.guid = '{}'".format(guid2))
    row = cursor.fetchone()
    if tempguid != guid:
        print([text, row[1]])
        print(text)
        #os.system('./sendmessage.py {} {}'.format(row[1], text))
        os.system("osascript sendMessage.scpt {} '"'{}'"'".format(row[1], text))
        #call("/usr/bin/osascript sendMessage.scpt {} '"'{}'"'".format(row[1], text), shell=False)
        p = Popen(['osascript sendMessage.scpt'], stdin=PIPE, shell=True)
        textinput = "{} '"'{}'"'".format(row[1], text)
        p.communicate(input=textinput.encode())
        #p.communicate(input='hi yo')
    guid = tempguid
    conn.close()
