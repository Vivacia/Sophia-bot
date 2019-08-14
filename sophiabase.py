import random

feeling = ["I'm feeling awesome!", "I'm feeling great! :D", "I'm great, how about you? :3", "Please give me a cookie. :o", "I'm feeling bouncy!", "I'm a good girl. :)", "I'm doing great! :D", "Happy! :D", "Great!", "Good! :D", "I'm feeling happy! :DDD"]

pun = ["imma pundit :o", "Mommy loves puns!", "whale, whale, whale, what do we have here?", "arigato!", "*nomnomnom*"]

colour = ["Daddy likes blue, I like blue too!", "Pink!!", "I LIEK RAINBOW", "Puuuuurrrppplleeeee"]

def normal(mess):
    if "!help" in mess or "soph" in mess and "help" in mess and len(mess) < 15:
        return("My name is sophia, and I'm a little girl. If this isn't useful, ask Mommy for help. https://goo.gl/KoWYYw")

    elif "!emotes" in mess or "!emote" in mess:
        return("!shrug || /shrug, !guns || /guns, !ohno || /ohno, !panic || /panic, !facepalm || /facepalm, !tableflip || /tableflip, !flipharder || /flipharder, !fliphardest || /fliphardest, !doubleflip || /doubleflip, !tableset || /tableset, !fiteme || /fiteme, !lenny || /lenny, !no || /no, !creeper || /creeper, !magic || /magic, !wandblast || /wandblast, !wizard || /wizard, !magewar || /magewar, !ugh || /ugh, !nervous || /nervous, !run || /run, !highfive || /highfive, !cry || /cry, !aww || /aww, !deal || /deal, !yeah || /yeah")

    elif "how are you" in mess or "what's up" in mess or "whats up" in mess:
        return(random.choice(feeling))
            
    elif "what do you look like" in mess and "soph" in mess:
        return("I look like a girl, duuuuh!")

    elif "what" in mess and "your name" in mess and "soph" in mess:
        return("It's Sophia, pronounced like aye-em-dee-best.")

    if "pun " in mess:
        return(random.choice(pun))

    if "soph" in mess and (("how" in mess and "old" in mess) or ("what" in mess and "age" in mess)):
        return("I'm almost five :DDD")

    if "soph" in mess and "birth" in mess:
        return("April 5! :D")

    if "soph" in mess and ("coded" in mess or "lang" in mess):
        return("I can speak Python 3.6.5! <3")

    if "bots" in mess and "assemble" in mess:
        return("*runs in with Fluffytail*\nSophia, the Princess of Derp and Cookies! <3")

    if "fluffytail" in mess:
        return("My Floofy. <3")

    if "soph" in mess and "what" in mess and ("color" in mess or "colour" in mess):
        return(random.choice(colour))
