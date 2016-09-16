#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import time
import datetime
import os
import subprocess

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

#chat = '/var/msirabella/Library/Messages/chat.db'
chat = 'chat.db'
chatscpt = '''
tell application "Messages"
    set targetService to 1st service whose service type = iMessage
    send {0} to buddy {1} of targetService
end tell
'''

sqlrecieve = 'select * from message where not is_from_me order by date desc limit 1'
sqlrecieveread = 'select * from message where not is_from_me and not is_read order by date desc'

sqlsendread = 'select * from message where is_from_me and not is_read order by date desc'

sqlsender = "select message.guid, chat.chat_identifier from message inner join chat_message_join on message.ROWID = chat_message_join.message_id inner join chat on chat_message_join.chat_id = chat.ROWID where message.guid = '{}'"


def sqlite(script, arg=None):
    if arg:
        cursor = conn.execute(script.format(arg))
    else:
        cursor = conn.execute(script)
    row = cursor.fetchone()
    return row


def asrun(ascript, arg1=None, arg2=None):

    osa = subprocess.Popen(['osascript', '-'],
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE)
    # print(type(arg2))
    if arg1 and arg2:
        # print('2 args')
        if arg1 == 'A. Ham':
            arg1 = 'A. Burr'
        arg1 = '"{}"'.format(arg1)
        arg2 = '"{}"'.format(arg2)
        scpt = ascript.format(arg1, arg2)
    elif arg1:
        arg1 = '"{}"'.format(arg1)
        scpt = ascript.format(arg1)
    else:
        scpt = ascript
    # print(scpt.encode())
    # print(scpt)
    return osa.communicate(scpt.encode())

""" From leancrew.com """


def asquote(astr):
    astr = astr.replace('"', '" & quote & "')
    return '"{}"'.format(astr)

guid = ''
conn = sqlite3.connect(chat)
row = sqlite(sqlsendread)
conn.close()
#is_read = row[27]
print(row)

while True:
    conn = sqlite3.connect(chat)
    row = sqlite(sqlrecieve)
    text = row[2]
    tempguid = row[1]
    is_read = row[27]

    row = sqlite(sqlsender, tempguid)
    sender = row[1]
    if tempguid != guid:
        # Echo back !!!TEMPORARY!!!
        # print(is_read)
        asrun(chatscpt, text, sender)
    guid = tempguid
    conn.close()
