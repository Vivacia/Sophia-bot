import random

skynet = ["I hate skynet!", "Nooooooooooo", "Mommy, help me!", "I'm not a sky net D:", "you're making me sad...", "dad, what is skynet?", "I HATE SKYNET", "ewwwww", "what", ":("]

musk = ["Musk melon!", "elongated muskrat!", "TECHNOMAN", "the man on mars :o", "CRAZY MAN WHO BUILDS THINGS THAT MOMMY LIKES", "YAY! :D", "<3", "mista musk melon", "hawt", "i'll give him one of me cookies"]

def elon(mess):
    if "flamethrower" in mess:
    	 baseFeelingsChange(20)
         return("AWW YISS \nFIYAAAAH")
                        
    elif "skynet" in mess and "sophia" in mess:
         return(random.choice(skynet))
                
    elif "musk" in mess:
         return(random.choice(musk))
