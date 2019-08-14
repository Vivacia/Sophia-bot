#!/usr/bin/env python

import asyncio
import json
import hashlib
import string
import sys
import os
import datetime
import random
import time

#user defined:
import wiki
import greeting
import fortunecookie
import techno
import emoji
import fsm
import mattserver
import funnies
import rude
import happy
import tricks
import sophiabase
import goodnight
import hail
import muskers
#import battleshipinsophia
import actions
import nerdtalk
import parents
import starwars
import love
import learn
import timer
import gSearch
import dictSophia
import varun
import ping
import narrate
import flashcardgame
import startrek
from irc import *
import messageParser

hate = []

"""ACTION eats pudding\n"""

asleep = ["ACTION snores louder in disapproval", "ACTION dreams of cookies", "ACTION hides head under pillow", "ACTION frowns a bit in her sleep", "ACTION throws a pillow at you", "ACTION curls up in her sleep", "ACTION purrs in her sleep"]

baseFeelings = 80;
auxFeelings = 0;

def getBaseFeelings():
  return baseFeelings

def getAuxFeelings():
  return auxFeelings

def setBaseFeelings(number):
  if number >= 0 and number <= 100:
      baseFeelings = number
  elif number < 0:
    baseFeelings = 0
  else:
    baseFeelings = 100

def setAuxFeelings(number):
  if number >= 0 and number <= 10:
      auxFeelings = number
  elif number < 0:
    baseFeelings = 0
  else:
    baseFeelings = 10

j = [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]
      
channel = "#talstest"
server = "irc.gamesurge.net"
nickname = "Sophia"

timerDict = {}
 
irc = IRC()
irc.connect(server, nickname, channel)
 
while 1:
  k = random.choice(j)
  text = irc.get_text()
  chan = str(channel)
  text2 = str(text)
  mess = messageParser.usefulText(text2, chan)
  auth = messageParser.username(text2)
  ip = messageParser.IPAddress(text2)
  mess = mess.lower()
  if "001 sophia" in str(mess):
        irc.join(channel)
  modules = [
            rude.notnice,
            ping.pong,
            parents.parent,
            sophiabase.normal,
            goodnight.goodnight,
            wiki.wiki,
            dictSophia.wordApplications,
            learn.inputLearn,
            learn.outputLearn,
            flashcardgame.flashcard,
            tricks.trick,
            happy.aff,
            fortunecookie.fortune,
            techno.technobabble,
            emoji.emotes,
            fsm.pasta,
            mattserver.memes,
            mattserver.politics,
            funnies.funners,
            hail.hail,
            nerdtalk.nerdtalk,
            actions.action,
            starwars.star,
            startrek.trek,
            muskers.elon,
            love.love,
            narrate.narrate,
            varun.stuff,
            greeting.greet,
            greeting.gbye
      ]
  for x in hate:
            if x in ip:
                  continue
      
  if "Sophia" in ip:
        continue
  else:
        if "soph" in mess and ("reboot" in mess or "restart" in mess) and len(mess) < 17 and "Vivacia" in ip:
              irc.send(channel, "Okay, mommy.")
              irc.quitting("Mommy told me to restart!")
              time.sleep(2)
              os.execv(sys.executable, ['python', __file__])

        if "soph" in mess and "join" in mess:
            irc.send(channel, "Okay, mommy.")
            channel = mess[mess.find("join ") + 6:]
            irc.join(channel)

        if "soph" in mess and "nap" in mess and "Vivacia" in ip:
              irc.send(channel, "ACTION runs into bed and hugs fluffytail")
              irc.send(channel, "ACTION slowly falls asleep...")

              sleepCheck = open("sleepIRC.txt", "w")
              sleepCheck.write("sleeping")
              print("nap")
              sleepCheck.close()

        if "soph" in mess and "wake up" in mess and "Vivacia" in ip:
              sleepCheck2 = open("sleepIRC.txt", "w+")
              if not os.path.exists("sleepIRC.txt"):
                  open("sleepIRC.txt",'w+').close()
              checker = sleepCheck2.read()
              irc.send(channel, "ACTION rubs her eyes and hugs Mommy")
              sleepCheck2.write("")
              sleepCheck2.close()

        sleeper = open("sleepIRC.txt", "r")
        checker2 = sleeper.read()
        sleeper.close()
        for function in modules:
              if function == love.love or function == flashcardgame.flashcard:
                    response = function(mess, ip)

              elif function == learn.inputLearn:
                    response = function(mess, mess)

              else:
                    response = function(mess)
              if response != None and response != "":
                    if not function.__name__ in timerDict.keys():
                        needed = datetime.datetime.now() - datetime.timedelta(seconds = 300)
                        timerDict[function.__name__] = needed

                    lastTime = timerDict[function.__name__]
                    nowTime = datetime.datetime.now()
                    elapsedTime = (nowTime - lastTime).seconds
                    
                    if function == mattserver.politics or function == nerdtalk.nerdtalk or function == hail.hail:
                          if elapsedTime < 100:
                                continue
                          
                    if function == starwars.star or function == startrek.trek or function == mattserver.memes or function == funnies.funners or function == fsm.pasta:
                          if elapsedTime < 30:
                                continue
                                
                    if elapsedTime < 10:
                          continue
                                      
                    if "sleeping" in checker2:
                          if k % 9 == 0:
                            irc.send(channel, random.choice(asleep))
                    else:
                          responseList = response.split("\n")
                          if function == goodnight.goodnight:
                                if "Vivacia" in ip:
                                    for x in responseList:
                                         if x.find("*") == 0 and "soop" not in x:
                                              x = "ACTION " + x[1:-1] + ""
                                         irc.send(channel, x)
                                         time.sleep(2)
                                         irc.quitting("Going to bed... Goodnight!") 
                                         exit(0)
                                else:
                                      irc.send(channel, "You're not my mommy.")

                          else:
                              currentTime = datetime.datetime.now()
                              timerDict[function.__name__] = currentTime
                                              
                              for x in responseList:
                                  if x.find("*") == 0 and "soop" not in x:
                                        x = "ACTION " + x[1:-1] + ""
                                  irc.send(channel, x)
                              break

