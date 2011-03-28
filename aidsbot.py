#!/usr/bin/env python

'''

aidsbot - A simple irc bot library for python
Copyright (C) 2011 Adam Höse <adisbladis@m68k.se>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

'''

import socket
import thread
import time
import threading

class aidsbot ():
    '''Handle IRC connections'''
    def __init__(self, botname, network, port, owner, debug = False):
        self.network = network
        self.port    = port
        self.botname = botname
        self.owner   = owner
        self.debug   = debug
        self.run     = True
        self.handler = {}

    def connect(self):
        self.socket = socket.socket()
        self.socket.connect((self.network, self.port))
        self.socket.send("NICK %s\r\n" % self.botname)
        self.socket.send("USER %s %s bla :%s\r\n" % (self.botname, self.network, self.botname))
    
    def join(self, channel, message = ''):
        '''Join channel'''
        self.socket.send("JOIN :%s\r\n" % channel)
        
        if message != '':
            self.send(channel, message)
    
    def send(self, target, message):
        '''Send message to target'''
        self.socket.send("PRIVMSG %s :%s\r\n" % (target, message))
    
    def stop(self):
        '''Stop the server'''
        self.run = False
        self.socket.send('QUIT')
        self.socket.close()

    def handler_add(self,command,function):
        '''Add function as handler for command'''
        self.handler[command]=function

    def defaulthandler(self,function):
        '''Define a default handler'''
        self.defaulthandler=function

    def data_split(self,data):
        '''Split data for easy usage'''
        data = data.split()
        user_info = data[0]
        msg_type = data[1]
        channel = data[2]
        message = data[3]
        for i in range(4,len(data)):
            message = message + " " + data[i]
        return user_info, msg_type, channel, message        

    def listen(self):
        '''Start listener in thread'''
        thread.start_new_thread(self.listener, ())

    def listener(self):
        '''Listener, should be started from listen() instead'''
        while self.run:
            data = self.socket.recv(4096)
            
            if data.find('PING') != -1:
                self.socket.send('PONG ' + data.split()[1] + "\r\n")

            user_input = data.split()

            #Handle user commands
            try:
                command = user_input[3]
                try: thread.start_new_thread(self.handler[command], (self,data))
                except KeyError: pass #Unhandled
            except:
                pass #Not a trigger

            if self.debug == True:
                print data

