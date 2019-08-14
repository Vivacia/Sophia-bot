import random
import feelings

sw = ["*runs around with her lightsaber*", "SQUEEE STAR WARS!!", "May the force be with you.", "*hums the Star Wars theme*", "I WANNA WATCH STAR WARS NOW DADDY\nNOW", "*swings her lightsaber at you*"]
        
def star(mess): 
    if "star wars" in mess:
        return(random.choice(sw))
        
    elif "hello there" in mess:
        return("General Kenobi! :grievous:  *swings lightsabers*")
                
    elif ("i'm your father" in mess or "im your father" in mess) and "sophia" in mess:
    	baseFeelingsChange(-10)
        return("NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\n*runs away into mommy's arms*")
