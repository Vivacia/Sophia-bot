import random

refuse = ["NO", "Sorry, I can't do that.", "Sorry, I can't.", "Sorry.", "No.", "Sorry, no.", "Never", "Do it yourself.","kek\n no", "Nope.", "NOPE!", "NOPE NOPE NOPE", "How about no.", "Nope to the nth power.", "NEVAH!", "nuhuhuhuhuh"]

foreign = ["feekeez", "feekees", "gak", "puop", "poop", "poup", "puup", "feth"]

cry = ["Mommy, help! :(", "*curls up in a ball and cries*", "Please, stop... :(", "You're hurting me...", "You meanie... \n*cries and runs away to mommy*", "DADDY I WISH YOU WERE HERE"]

disgusting = [ "tit", "breast", "tiddy", "boob", "nipple", "pussy", "vagina", "vagene", "dildo", "condom", "ass", "butt", "bum", "thot","rape", "hurt", "smack", "hit", "hoe", "penis", "cock", "dick", "balls", "cunt", "pussy", "porn", "pron", "pr0n", "dong", "johnson", "sex", "secks", "fuck"]

threat = ["if you", "you should", "you must", "compliment me", "compliment my", "make me", "make my", "help me", "help my"]

stupids = ["stupid", "shut up", "whore", "bitch", "dumb", "ass"]

bad = ["I'm sorry...", "Sorry... :(", "I didn't mean to hurt you. :(", ":(", "I'm sorry... *cries*"]

def notnice(mess):
    for x in disgusting:
        if x in mess and "soph" in mess:
            baseFeelingsChange(-5)
            return(random.choice(cry))
            
    for x in threat:
        if x in mess and "soph" in mess:
            baseFeelingsChange(-5)
            return(random.choice(refuse))
            
    for x in foreign:
        if x in mess and "soph" in mess:
            baseFeelingsChange(-5)
            return("*rolls her eyes*")

    for x in stupids:
        if x in mess and "soph" in mess:
            baseFeelingsChange(-5)
            return(random.choice(cry))
            
    if "cum dumpster" in mess:
        baseFeelingsChange(-20)
        return("Royally, fuck you.")

    elif "kys" in mess and "soph" in mess:
        baseFeelingsChange(-10)
        return("haha lol you bitch")

    elif (" jk" in mess and "soph" in mess) or ("jk " in mess and "soph" in mess):
        return("AHAHAHAHAHAHA")

    elif "bad" in mess and "girl" in mess:
        baseFeelingsChange(-10)
        return(random.choice(bad))
