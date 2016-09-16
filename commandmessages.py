#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import time
import datetime
import os
import subprocess
from sys import argv

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
    """ Send database sqlite script, with or without arguments for {}"""
    if arg:
        cursor = conn.execute(script.format(arg))
    else:
        cursor = conn.execute(script)
    row = cursor.fetchone()
    return row


def asrun(ascript, arg1=None, arg2=None):
    """ Run applescript 'ascript' and maybe arguments if you want. """

    osa = subprocess.Popen(['osascript', '-'],
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE)
    # print(type(arg2))
    # checks for commands here

    for x in commands:
        if len(x) == 2 and arg1 == x[0]:
            arg1 = x[1]

    if arg1 == '!fortune':
        arg1 = subprocess.check_output('fortune').decode()
        if "\n" not in arg1:
            arg1 = arg1 + "\n"
        print(arg1)

    if arg1 and arg2:
        # print('2 args')
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
    """ Format string to be parsed by asrun """
    astr = astr.replace('"', '" & quote & "')
    return '"{}"'.format(astr)


def readcommands(filename):
    """ To read all commands to be parsed by daemon in a file, seperated by ' | ' """
    global commandfile_read
    if not commandfile_read:
        commandfile_read = True
    with open(filename) as f:
            y = [tuple(i.split(' | ')) for i in f]
    # print(y)

    return y


guid = ''
conn = sqlite3.connect(chat)
row = sqlite(sqlsendread)
conn.close()
commandfile_read = False
commands = readcommands('commands.compy')
#is_read = row[27]
# print(row)


while True:
    conn = sqlite3.connect(chat)
    row = sqlite(sqlrecieve)
    conn.close()
    text = row[2]
    tempguid = row[1]
    is_read = row[27]

    row = sqlite(sqlsender, tempguid)
    sender = row[1]
    if tempguid != guid:
        asrun(chatscpt, text, sender)
    guid = tempguid
