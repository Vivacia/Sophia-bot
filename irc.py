import socket
import sys
from time import sleep

class IRCCommands:
    def __init__(self,socket):
            self.socket = socket

    def raw(self,message):
            for c in ("\r","\n"):
                    message = message.replace(c, "")
            if not message.startswith("PONG"):
                    print("sending raw: {}".format(message))
            self.socket.send('{}\r\n'.format(message).encode('UTF-8'))

    def send(self,command,payload):
            self.raw("{} {}".format(command,payload))

    def pong(self,payload):
            self.send("PONG",payload)

    def irc_pass(self,password):
            self.send("PASS",password)

    def nick(self,nick):
            self.send("NICK",nick)

    def user(self,ident,mode):
            if mode != 0 and mode != 8:
                    mode = 8
            self.send("USER","{0} {1} serv :{0}".format(ident,mode))

    def auth(self,nick,mode=8):
            self.nick(nick)
            self.user(nick,mode)

    def privmsg(self,target,message):
            self.send("PRIVMSG","{} :{}".format(target,message))

    def notice(self,target,message):
            self.send("NOTICE","{} :{}".format(target,message))

    def join(self,channel):
            if channel:
                    if not channel.startswith("#"):
                            channel = "#" + channel
                    self.send("JOIN",channel)

    def multijoin(self,channel_list):
            for channel in channel_list:
                    self.join(channel)

    def part(self,channel):
            if channel:
                    if not channel.startswith("#"):
                            channel = "#" + channel
            self.send("PART",channel)

    def names(self,channellist):
            self.send("NAMES",",".join(channellist))

    def away(self,message):
            self.send("AWAY",":{}".format(message))

    def unaway(self,my_nick):
            self.send(":{}".format(my_nick),"AWAY")

    def quit(self,reason="quitting"):
            self.send("QUIT", ":{}".format(reason))

    def ctcp_ask(self,target,ctcp_type):
            self.privmsg(target,"\x01{}\x01".format(ctcp_type))

    def ctcp_reply(self,target,ctcp_type,reply_string):
            self.notice(target,"\x01{0} {1}\x01".format(ctcp_type,reply_string))

    def action(self,target,action):
            self.privmsg(target,"\x01ACTION {}\x01".format(action))
 
class IRC:
    buffer = ""
    def __init__(self):  
        self.IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.commands = IRCCommands(self.IRC)

    def send(self, chan, msg):
        self.commands.privmsg(chan, msg)
 
    def join(self, channel):
        self.commands.join(channel)

    def quitting(self, reason):
        self.commands.quit(reason)

    def connect(self, server, botnick, channel):
        #defines the socket
        print ("connecting to:"+server)
        self.IRC.connect((server,6667)) #connects to the server
        self.IRC.setblocking(0)
        self.IRC.settimeout(2)
        self.commands.auth(botnick)
        self.commands.join(channel)

    def get_text(self):
        try:
            self.buffer += self.IRC.recv(2040).decode('utf-8')  #receive the text
        except:
            pass
        text = ""
        if '\n' in self.buffer:
                text = self.buffer.split('\n',1)[0]
                self.buffer = self.buffer.split('\n',1)[1]
     
        if text.find('PING') != -1:                      
            self.IRC.send(bytes('PONG ' + text.split() [1] + '\r\n', "utf-8"))
        return text
