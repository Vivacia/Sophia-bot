import random
import feelings

narwhal = ["Narwhals, Narwhals! Swimming in the ocean\nCausing a commotion, coz they are so awesome", "Narwhals, narwhals!", "Narwhals, Narwhals! Swimming in the ocean\nPretty big and pretty white\nThey beat a polar bear in a fight!", "Narwhals! They are Narwhals!\nNarwhals! Inventors of the Shish Kebab"]

lego = ["Yay LEGO! :D", "little building blocks :o", "*builds a little car for you*\nvroom vroom!", "Can you take me to LEGOland?", "Mommy loves LEGO, so do I!"]

bacon = ["BACON!? WHERE?!", "*sniffs around for the bacon you mentioned*", "gimme some bacon T_T", "baconbaconbacon", "no bacon, only cookie", "You bake cookies but you cook bacon."]

dino = ["DINOSAUR!!!", "*runs around* ROAAAR!", "*puts on a dino-mask and walks like one*", "Why don't dinosaurs exist anymore? :( Did we hunt them all?", "Daddy, can we go see Jurassic World again?\nPlease? Pleeeaasse?"]

pun = ["imma pundit :o", "Mommy loves puns!", "whale, whale, whale, what do we have here?", "arigato!", "*nomnomnom*"]

flamingo = ["FLAMINGO!! :DDD", "*sings in Japanese*", "I love pink birbs!", "How many shrimps do you have to eat before your skin turns pink?", "rainbow flamingos!"]

squirrel = ["Hey look over there! It's a Squirrel!", "Hey look over there! It's a Squirrel!", "Hey look over there! It's a Squirrel!", "Hey look over there! It's a Squirrel!", "Where!?", "Daddy, I want a squirrel. :I", "SQUIRREL!", "squirrellidirrelidoo", "I love squirrels <3"]

baconsoup = ["*gives some bacon soup to Uncle Keith*", "Bacon soup?", "Do you want some bacon soup?", "Uncle Keith loves it. :D"]

boo = ["*is frightened by you*", "*hides behind Mommy*", "*runs to Daddy for help*", "don't boo me ;-;*"]

def funners(mess):
    if "bacon soup" in mess:
        return(random.choice(baconsoup))
    
    elif "bacon" in mess:
        return( random.choice(bacon))
        
    elif "soup" in mess:
        baseFeelingsChange(-1)
        return("*soop :o")

    elif "dinosaur" in mess:
        return( random.choice(dino))

    elif " lego" in mess and "soph" in mess:
        return( random.choice(lego))

    elif "badger" in mess:
        return( "MUSHROOOOM\nMUSHROOOOOOOOOM")

    elif "squirrel" in mess:
        return(random.choice(squirrel))

    elif " narwhal " in mess:
        return( random.choice(narwhal))
        
    elif "idiot" in mess:
        return( "Idiots. Idiots everywhere!")
        
    elif "like such as" in mess:
        baseFeelingsChange(-5)
        return( "*headdesk*")

    elif "face " in mess:
        baseFeelingsChange(-5)
        return( "Your cara!")
    
    elif "cara " in mess:
        baseFeelingsChange(-5)
        return( "Your face!")
        
    elif "nananana" in mess:
        return("BATMAN! :O")

    elif "yay" in mess:
        baseFeelingsChange(5)
        return( "Yay!")
    
    elif "coats" in mess:
        return( "I love coats! \nSo nice and warm! <3")

    elif "flamingo" in mess:
        baseFeelingsChange(2)
        return( random.choice(flamingo))
        
    elif " yee " in mess:
        baseFeelingsChange(-2)
        return("https://media.giphy.com/media/3oKIPDhAQCe6ZrY25i/giphy.gif")
        
    elif " ree " in mess:
        baseFeelingsChange(-2)
        return("https://media.giphy.com/media/DTdDZQUWmf9tK/giphy.gif")

    if "soph" in mess and "pokes" in mess:
        return("*pokes you back*")
        
    elif "boo!" in mess:
        return(random.choice(boo))
