#!/usr/bin/env python

"""
Sophia
created by Meghavarnika "Vivacia" Budati on April 5, 2018
"""

import discord
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
import youtube
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
import feelings

client = discord.Client()

timerDict = {}

asleep = ["*snores louder in disapproval*", "*dreams of cookies*", "*hides head under pillow*", "*frowns a bit in her sleep*", "*tosses in bed* zzz...", "*throws a pillow at you*", "*curls up in her sleep*", "*purrs in her sleep*"]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
A:  10 -  0 ==> angery/sleepy. 
B: 100 -  0 ==> base feelings.
   100 - 70 ==> very happy, joyful, couldn't be happier. She's a toddler so she's bound to get excited by the little things in life.
    50 - 70 ==> okayish, calm, a bit sleepy. Can't be happy for too long. She needs to recharge.
    30 - 40 ==> feeling kinda sad but for no reason. Could be really sleepy though.
     0 - 20 ==> so fucking cranky she's a child so she might cry or rip shit up

A applies for B <= 50. For 30 - 40, it's her sleepiness meter. For B <= 30, it's her anger meter.
"""

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

@client.event
async def on_message(message):
      j = random.choice(numbers)
      await client.change_presence(game=discord.Game(name='with Mommy.'))
      mess = message.content.lower()
      chan = message.channel
      auth = str(message.author)
      modules = [
            rude.notnice,
            ping.pong,
            parents.parent,
            sophiabase.normal,
            goodnight.goodnight,
            youtube.youtube2,
            wiki.wiki,
            gSearch.gSearch,
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
            if message.author == x:
                  return
      
      if message.author == client.user:
            return
      else:
            if "soph" in mess and "sophia" not in mess and ("reboot" in mess or "restart" in mess) and len(mess) < 17 and "Vivacia" in auth:
                  await client.send_typing(chan)
                  await client.send_message(chan, "Okay, mommy.")
                  os.execv(sys.executable, ['python', __file__])

            if "soph" in mess and "sophia" not in mess and "nap" in mess and "Vivacia" in auth:
                  await client.send_typing(chan)
                  await client.send_message(chan, "*runs into bed and hugs fluffytail*")
                  await client.send_typing(chan)
                  await client.send_message(chan, "*slowly falls asleep...*")

                  sleepCheck = open("sleep.txt", "w")
                  sleepCheck.write("sleeping")
                  print("nap")
                  sleepCheck.close()

            if "soph" in mess and "sophia" not in mess and ("wake up" in mess or "rise and shine" in mess or "wakey wakey" in mess) and "Vivacia" in auth:
                  sleepCheck2 = open("sleep.txt", "w+")
                  if not os.path.exists("sleep.txt"):
                      open("sleep.txt",'w+').close()
                  checker = sleepCheck2.read()
                  await client.send_typing(chan)
                  await client.send_message(chan, "*rubs her eyes and hugs Mommy*")
                  sleepCheck2.write("")
                  sleepCheck2.close()

            sleeper = open("sleep.txt", "r")
            checker2 = sleeper.read()
            sleeper.close()
            for function in modules:
                  if function == youtube.youtube2:
                        response = await function(mess)

                  elif function == love.love or function == flashcardgame.flashcard:
                        auth = message.author
                        response = function(mess, auth)

                  elif function == learn.inputLearn:
                        response = function(mess, message.content)

                  else:
                        response = function(mess)
                  if response != None and response != "":
                        if not function.__name__ in timerDict.keys():
                            needed = datetime.datetime.now() - datetime.timedelta(seconds = 300)
                            timerDict[function.__name__] = needed

                        lastTime = timerDict[function.__name__]
                        nowTime = datetime.datetime.now()
                        elapsedTime = (nowTime - lastTime).seconds
                        
                        if function == mattserver.politics:
                              if elapsedTime < 100:
                                    return
                              
                        if function == starwars.star or function == startrek.trek or function == mattserver.memes:
                              if elapsedTime < 20:
                                    return
                                    
                        if elapsedTime < 3:
                              return
                                          
                        if "sleeping" in checker2:
                              if j % 5 == 0:
                                await client.send_typing(chan)
                                time.sleep(2)
                                await client.send_message(chan, random.choice(asleep))
                        else:
                              responseList = response.split("\n")
                              if function == goodnight.goodnight:
                                    if "Vivacia" in auth:
                                        for x in responseList:
                                             await client.send_typing(chan)
                                             await client.send_message(chan, x)
                                             exit(0)
                                    else:
                                          await client.send_typing(chan)
                                          time.sleep(2)
                                          await client.send_message(chan, "You're not my mommy.")

                              else:
                                  currentTime = datetime.datetime.now()
                                  timerDict[function.__name__] = currentTime
                                                  
                                  for x in responseList:
                                      await client.send_typing(chan)
                                      if len(x) > 20:
                                            time.sleep(1)
                                      await client.send_message(chan, x)
                                  break

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print("ID: ")  
  print(client.user.id)
  print('------')

token = "you're a sneaky one :o"
client.run(token)
