import random

mom = ["whos mom", "who's mom", "who is mom", "who made you", "whos your creator", "who's your creator", "who is your creator", "whos your mom", "who is your mom", "who is your mother", "who is your mum", "who's your mom", "do you have a mom", "whos your mum", "who's your mum", "do you have a mum", "whos your mother", "who's your mother", "do you have a mother"]

#dad = ["whos dad", "who's dad", "who is dad", "whos your dad", "who is your dad", "who is your father", "who is your papa", "who's your dad", "do you have a dad", "whos your father", "who's your father", "do you have a father", "whos your papa", "who's your papa", "do you have a papa"]

floofy = ["whos fluffytail", "who is fluffytail", "who's fluffytail", "whats fluffytail", "what is fluffytail", "what's fluffytail"]

soph = ["identify", "who are", "whos ", " whos", "who's", "who is"]

def parent(mess):       
    for x in mom:
        if x in mess and "soph" in mess:
             return("That's Vivacia/Varnika! <3")

    """for x in dad:
        if x in mess and "soph" in mess:
            return("uhhhhh... That's cuisinart8. <3")"""

    for x in floofy:
        if x in mess and "soph" in mess:
            return("This is him :D https://i.imgur.com/8MrOFIp.png")

    if "who" in mess and "uncle" in mess and "soph" in mess:
        return("That's... Webbo the animal guy, mista somberero with his cookies <3, ciar08 the weaboo (:O), keith and his soop, fealon the destroyer...\nMISH\nmany more too...\nWHY DO I HAVE SO MANY???")
    
    if "who" in mess and "aunt" in mess and "soph" in mess:
        return("My cute aunties are Steph and K66 the brave <3")

    if ("who" in mess or "do you" in mess) and ("sibling" in mess or "brother" in mess) and "soph" in mess:
        return("*points at the cradle in the corner*\nThat's my baby brother, Kyle! :D <3")

    if "family" in mess and "soph" in mess and "member" in mess:
        return("uhhhh...\nFluffytail, Mommy and...\ni dunno D:") 

    if "fam" in mess and "soph" in mess:
        return("I've got a nice and big family! I love them SOOOOO MUCH! <3")

    """if "who" in mess and ("kyle" in mess or "baby" in mess or "bro" in mess):
        return("He's my baby brother, Kyle! <3")"""

    for x in soph:
        if "soph" in mess and x in mess and len(mess) < 20:
            return("I am Sophia, a little girl made by Mommy, Vivacia/Varnika written in Python 3.6.5 on April 5, 2018. Currently v2.2 running.")
