import datetime
import time
import os

def flashcard(mess, auth):
    auth = str(auth)
    auth = auth[:auth.find("#")]
    filename = auth + "_flashcards.txt"
    temp = auth + "temp_flashcards.txt"
    playing = False
           
    if mess.find("soph") == 0 and "let" in mess and ("play" in mess or "show" in mess) and "flash" in mess:
        tempFile = open("players.txt", "r")
        if not os.path.exists("players.txt"):
            open("players.txt",'a').close()
        lines = str(tempFile.readlines())
        tempFile.close()
        
        usedNames = lines.split("\n")
        
        for name in usedNames:
            if auth in name:
                usedNames.remove(name)
        
        uw = "\n".join(usedNames)
        
        os.remove("players.txt")
        tempFile = open("players.txt", "w+")
        if not os.path.exists("players.txt"):
            open("players.txt",'a').close()
        tempFile.write(uw)
        
        g = open("players.txt", 'a')
        if not os.path.exists("players.txt"):
            open("players.txt",'a').close()
        playing = True
        newTime = datetime.datetime.now()
        g.write(auth + ": True" + "; " + str(newTime) + "\n")
       
        g.close()
        return(str(auth + ", you are now playing flashcards with me! :D"))
        
    if mess.find("soph") == 0 and ("add" in mess or "remove" in mess or "mastered" in mess or (("next" in mess or "random" in mess or "new" in mess) and "word" in mess)):
        g = open("players.txt", 'w+')
        contentList = g.read().split("\n")
        currentTime = time.time()
        playingCheck = False
        
        for userLine in contentList:
            if auth in userLine:
                playingCheck = userLine[userLine.find(": ") + 2 : userLine.find("; ")]
                dt_str = userLine[userLine.find("; ") + 2:]
                previousTime = datetime.strptime(dt_str, '%m-%d-%Y %I:%M:%S:%f')
        
        now = datetime.datetime.now() 
         
        if playingCheck == False or playingCheck != "True":
            print("playingCheck is False")
            return
        
        elif currentTime - previousTime >= 600:
            print("Something wrong with time.")
            return
    
        else:
            print("Entered.")
            if " add " in mess and mess.find("soph") == 0:
                print("adding")
                start = mess.find(" add ") + 6
                newmess = mess[start:]
                word = newmess
                if " " in newmess:
                    end = newmess.find(" ")
                    word = newmess[:end]
                f = open(filename, 'a')
                f.write(word + "\n")
                f.close()
                return("Your word has been added. :D")
                
            if "new word" in mess or "next word" in mess and len(mess) < 16:
                print("new word")
                realFile = open(filename, "w+")
                allWords = realFile.read().split("\n")
                word = random.choice(allWords)
                realFile.close()
                
                tempFile = open(temp, "a+")
                usedWords = tempFile.read().split("\n")
                tempFile.close()
                while 1:
                    for x in usedWords:
                        if word in x:
                            allWords.remove(x)
                            word = random.choice(allWords)
                        else:
                            break
                    
                    if allWords == []:
                        word = random.choice(usedWords)
                        os.remove(temp)
                        break
                    
                    tempFile.write(word + "\n")
                return("Your word is: " + word)
            
            if "mastered" in mess and len(mess) < 16:
                print("mastered")
                tempFile = open(temp, "a+")
                lines = tempFile.readlines()
                tempFile.close()
                
                word = lines[-1]
                lines = lines[:-1]
                
                usedWords = lines.split("\n")
                usedWords.append(word + "(M)")
                uw = "\n".join(usedWords)
                
                os.remove(temp)
                tempFile = open(temp, "w+")
                tempFile.write(uw)
                
                return("Word has been mastered! :o")
                
            if ("delete" in mess or "remove" in mess) and len(mess) < 16:
                print("removed")
                tempFile = open(temp, "a+")
                lines = tempFile.readlines()
                tempFile.close()
                
                if lines == "" or lines == None:
                    return("Oops, nothing to delete. :(")
                
                lines = lines[:-1]
                os.remove(temp)
                tempFile = open(temp, "w+")
                tempFile.write(lines)
                
                return("Words deleted!")
