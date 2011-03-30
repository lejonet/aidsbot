#!/usr/bin/env python

from aidsbot import aidsbot
import time

def hello(irc,data):
    '''A Simple handler function'''
    user_info, msg_type, channel, message = irc.data_split(data)
    username, real_user, host = irc.user_split(user_info)
    irc.send(channel, "Hello to you too %s :)" % (username))

def join(irc,data):
    '''Handle joins'''
    print data

def part(irc,data):
    print "LOLOL PART"

irc = aidsbot('aidsbot-dev', 'irc.oftc.net', 6667, 'adisbladis', True) #Set up the object
irc.connect() #Actually connect
irc.join('#bottest') #Join a channel
irc.send('#bottest', 'Yo!') #Send a message
irc.handler_add("!hello", hello) #Add the handlerfunction hello to trigger hello
irc.joinhandler(join)
irc.parthandler(part)
irc.listen() #Start listening

while True:
    time.sleep(10) #Important, will die otherwise
