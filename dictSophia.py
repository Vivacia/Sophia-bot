from PyDictionary import PyDictionary as d
from vocabulary.vocabulary import Vocabulary as v
import string

meaningSeparator = ["/'Noun/'", "/'Verb/'"]

ignore = ["define", "antonym", "synonym", "meaning", "of", "definition", "translate", "translation", ""]

def getWord(mess):
    revmess = mess[::-1]
    cutOff = revmess[:revmess.find(" ")]
    cutOff = cutOff.strip(" ")
    word = cutOff[::-1]

    for y in word:
        if y.isalpha() == False:
            y = ""

    for x in ignore:
        if x == word:
            return
    return(word)

def meaningParser(result):  
    resultList = result.split(",")
    option = 1
    resultF = ""
    for x in resultList:
        if len(resultF) >= 1900:
            break

        if "}" in x:
            x = x[:-2]
        elif "]" in x:
            x = x[:-1]

        for y in x:
            if y == "(":
                y = ""

        if "Noun" in x:
            resultF += "\n**Noun:** "
            x = x[x.find("Noun") + 9: -1]
            resultF += (str(option) + ". " + str(x) + "  ")
            option += 1
        elif "Verb" in x:
            resultF += "\n**Verb:** "
            x = x[x.find("Verb") + 9: -1]
            resultF += (str(option) + ". " + str(x) + "  ")
            option += 1
        elif "Adjective" in x:
            resultF += "\n**Adjective:** "
            x = x[x.find("Adjective") + 14: -1]
            resultF += (str(option) + ". " + str(x) + "  ")
            option += 1
        elif "Adverb" in x:
            resultF += "\n**Adverb:** "
            x = x[x.find("Adverb") + 11: -1]
            resultF += (str(option) + ". " + str(x) + "  ")
            option += 1
        else:
            x = x[2 : -1]
            resultF += (str(option) + ". " + str(x) + "  ")
            option += 1
    return(resultF)

def parser(result):
    option = 1

    resultFinal = ""
    resultList = result.split(",")
    for x in resultList:
        x = x[x.find("text") + 8 : x.find("}") - 1]
        if ":" in x:
            continue
        resultFinal += (str(option) + ". " + str(x) + "  ")
        option += 1
    return resultFinal

def wordApplications(mess):
    if mess.find("soph") == 0 and ("define" in mess or "definition" in mess or "meaning" in mess) or mess.find("define") == 0:
        word = getWord(mess)
        if word == None:
            return
        else:
            result = str(d.meaning(word))
            resultF = meaningParser(result)
            return("***" + str(word).upper() + "*** meaning(s)" + str(resultF))

    elif mess.find("soph") == 0 and ("antonym" in mess or "opposite" in mess or "different" in mess and "word" in mess) or mess.find("antonym") == 0:
        word = getWord(mess)
        if word == None:
            return
        else:
            result = str(v.antonym(word))
            resultF = parser(result)
            if resultF == None or resultF == "1.   ":
                return("Couldn't find any :(")
            return("**" + str(word) + "** antonym(s)\n" + str(resultF))

    elif mess.find("soph") == 0 and ("synonym" in mess or "similar to" in mess and "word" in mess) or mess.find("synonym") == 0:
        word = getWord(mess)
        if word == None:
            return
        else:
            result = str(v.synonym(word))
            resultF = parser(result)
            if resultF == None or resultF == "1.   ":
                return("Couldn't find any :(")
            return("**" + str(word) + "** synonym(s)\n" + str(resultF))

    mess = mess[:mess.find("d") + 1]
    revmess = mess[::-1]
    if revmess.find("drow") == 0 and mess.find("soph")== 0 and " is " in mess and " a " in mess:
        word = mess[mess.find(" is ") + 4 : mess.find(" a ")]
        if d.meaning(word) == None:
            return("Well, it's not in my dictionary... :(")
        else:
            return("Yeah, it is! :D")
