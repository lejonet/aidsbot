#!/usr/bin/env python

from aidsbot import aidsbot
import time

def hello(irc,data):
    '''A Simple handler function'''
    user_info, msg_type, channel, message = irc.data_split(data)
    username, real_user, host = irc.user_split(user_info)
    irc.send(channel, "Hello to you too %s :)" % (username))

irc = aidsbot('aidsbot-dev', 'irc.oftc.net', 6667, 'adisbladis', True)
irc.connect()
irc.join('#bottest', 'Yo!')
irc.handler_add(":hello", hello)
irc.listen()

while True:
    time.sleep(10) #Important, will die otherwise
