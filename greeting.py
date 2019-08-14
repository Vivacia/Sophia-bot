import random
import string

greetings = ["hi ", " hi", "hello", "hey", "hola", "howdy", "ciao", "namaste", "heya", "hiya", "hocus pocus", "more stuff", "hallo", "hellooooo", "hola",]

bye = ["bye", "goodbye", "see you", "adios", "seeya", "come back soon", "have a good one", "see you later", "goodnight", "night"]

def greet(mess):
    for x in greetings:
        if x in mess and "soph" in mess and "sophia" not in mess:
            return(random.choice(greetings).strip() + "!")
    if "good morning" in mess or "goodmorning" in mess:
        return("Good morning! :D")

def gbye(mess):    
    for x in bye:
        if x in mess and "soph" in mess and "sophia" not in mess:
            return(random.choice(bye) + "!")
