#!/usr/bin/env python

from aidsbot import aidsbot
import time

def hello(irc,data):
    '''A simple trigger handler function'''
    user_info, msg_type, channel, message = irc.privmsg_split(data)
    username, real_user, host = irc.user_split(user_info)
    irc.privmsg(channel, "Hello to you too %s :)" % (username))

def join(irc,data):
    '''Handle joins'''
    print "A user has joined"

def part(irc,data):
    print "A user has parted"

irc = aidsbot('aidsbot-dev', 'irc.oftc.net', 6667, True) #Set up the object
irc.connect() #Actually connect
irc.join('#bottest') #Join a channel
irc.privmsg('#bottest', 'Yo!') #Send a message
irc.privmsghandler_add("!hello", hello) #Add the handlerfunction hello to trigger hello
irc.chanophandler_add("JOIN",join)
irc.chanophandler_add("PART",part)
irc.listen() #Start listening

while True:
    time.sleep(10) #Important, will die otherwise
