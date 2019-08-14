import string
import json

keyLearn = []

learnDict = {}

def inputLearn(mess, message):
    if "soph" in mess and "sophia" not in mess and "learn" in mess or "!learn" in mess:
        if ":" not in mess:
            return
        foo = message[message.find("n") + 2: message.find(":")]
        bar = message[message.find(":") + 1:]
        learnDict[foo] = bar
        jsonString = json.dumps(learnDict)
        f = open("learndict.json", "w+")
        f.write(jsonString)
        f.close()
        return("I've got new vocabulary!")

def outputLearn(mess):
    g = open("learndict.json", "r")
    jsonString = g.read()
    learnDict = json.loads(jsonString)
    keyLearn = list(learnDict.keys())
    g.close()
    for x in keyLearn:
        if str(x) in mess:
             return(learnDict[x])
    else:
        return
