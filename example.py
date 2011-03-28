#!/usr/bin/env python

from aidsbot import aidsbot

def hello(irc,data):
    '''A Simple handler function'''
    user_info, msg_type, channel, message = irc.data_split(data)
    irc.send(channel, "Hello to you too :)")

irc = IRC('aidsbot', 'irc.oftc.net', 6667, 'adisbladis') #Set up the object
irc.connect() #Actually connect
irc.join('#mycoolchannel', 'Yo!') #Join a channel
irc.handler_add(":hello", hello) #Add the handlerfunction hello to trigger hello
irc.listen() # Start listening

while True:
    time.sleep(10) #Important, will die otherwise
