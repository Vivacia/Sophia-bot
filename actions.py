import random
import feelings

dance = ["*does a little twirl*", "*skips around*", "*dances around you*", "*grabs your hands and swings*", "*grins and pretends to be a ballerina*"]

def action(mess):	
    if "do a barrel roll" in mess:
        return("*rolls around happily*")

    elif "drop" in mess and "dead" in mess and "soph" in mess:
        return("*is dedder than a ded bed*")

    elif "handstand" in mess and "soph" in mess:
        baseFeelingsChange(-2)
        return("O.o \nNot while I'm wearing this!")
		
    elif "dance" in mess and "soph" in mess:
        return(random.choice(dance))
			
    elif "!work" in mess:
        baseFeelingsChange(-2)
        return("FLOOOFFYTAIL!\n*runs around*\nback to abc's! Come on, Fluffytail!")
