import random
import string

sentences = ["That's me! :D", ":O", "meow :o", "peekaboo!", "i liek cookeh", "Shiver me timbers!", "I'm alive! AAHHH", "I love you. :o", "Do you wanna build a snowman?", "MUAHAHAHAHAHAHA", "COOKIES!", "c is for cookeh, das good enuf for meee", "in preschool we learnt about communists. \nAre they really insane? :(", "I found this for you! :D *gives you a maple leaf* \nDo you like it?", "you look awesome :D", "I love trench coats!", "AWESOME!", "man, i wish i had candy", "wanna play with me?", ":3", ":DDDDD", "i liek chokolat meelk", "*pokie pokie*", "peekaboo!", "I think you are nice. :D"]

cookie = ["COOKIE!", "COOKIE!!!", "NEED COOKIES. GOTTA HAVE COOKIES.", "GIVE ME A COOKEH", "COOKEH!", "COOOOKEH!!!", "COOKIES!", "COOKIES!!!"]

sophia = ["soph?", "soph!", "sophia!", "sophia?"]

flower = ["flower", "tulip", "rose", "daisy", "daisies", "hibiscus", "daffodil", "boquet", "lilac", "violet", "pansy", "bluebell", "marigold", "sunflower"]

affection = ["cuddles", "pecks", "kiss", "brushes", "pat"]

yayers = ["tickles", "ruffles"]

giggles = ["*giggles*", "*beams at you*", "*laughs and grins at you*", "*grins*", "*squeeeeees*"]

squee = ["aww, thankies!", "*runs around with it happily*", "*grins at you, so happy*", "*omnoms it*", "*shares it with you*", "You're so sweet... thank you! :D ", "*runs to mommy and shows it to her, giggling*"]

compliment = ["good", "smart", "clever", "best"]

thanks = ["Thanks!", "Thanks! :)", "Thank you!", "Thank you! :)", ":)", ":3", "^.^", ":D", "Thanks! :D", "Thank you! :D", "You're the best! :D", "*giggles and hugs you*", "*smiles warmly at you*", "*blushes*"]

welcome = [":)", ":D", "Happy to help!", "Yay!", "You're welcome! :)", "My pleasure!", "No problem!", "Here to help! :D", "That's what I'm here for!", "Anything for you! :o"]

feeling = ["I'm feeling good.", "I'm feeling great!", "I'm great, how about you?", "I'm feeling a little snarky ;)", "I'm feeling bouncy!", "I'm doing good.", "I'm doing great!", "Happy!", "Great!", "Good.", "I'm feeling happy!"]

hug = ["*gives you a hug*", "*gives you a nice, warm hug*", "*gives you a warm hug*", "*hugs you*", "*hugs you warmly*", "*hugs you*", "*giggles and hugs you*"]

flowers = ["*gives you a hug*", "*gives you a warm hug*", "*gives you a nice, warm hug*", "*hugs you*", "*hugs you warmly*", "*hugs you tight*", "*giggles and hugs you*", "*smiles warmly at you*", "*blushes*", "*gives you a well-deserved peck on the cheek*", "*puts flowers in a pretty vase*", "*puts flowers in a pretty vase*", "*puts flowers in a pretty vase*", "Thanks! :o", "Thanks! :)", "Thank you! :o", "Thank you! :)", "Thanks! :D", "Thank you! :D", "You're the best! :D", "*sophia graciously accepts the gift*", "Aww, thank you!", "*sophia thanks you for being so kind*", "*sophia gives you a quick peck on the cheek*", "*sophia hugs you gratefully*", "Thanks!", "Thanks! :)", "Thank you!", "Thank you! :)"]

sorry = ["It's okay!", "It's okay.", "I forgive you, mista nice guy :D", "Everyone slips up sometimes, just like mommy", "Please don't do it again!", "It's okay, I guess...", "issokie.", "I forgive you.", "i have forgives for ye"]

def aff(mess):    
    if "gives" in mess and "soph" in mess and "piggy" in mess and "back" in mess:
        baseFeelingsChange(15)
        return("SQUEEEEEEEE\nI LOVE YOU MORE THAN MOMMY")

    for x in compliment:
        if x in mess and "girl" in mess:
            baseFeelingsChange(5)
            return(random.choice(thanks))
            break

    if "soph" in mess and ("great work" in mess or "gg " in mess or "good job" in mess):
        baseFeelingsChange(2)
        return(random.choice(thanks))

    if "soph" in mess and "dandelion" in mess and "gives" in mess:
        return("*makes a wish and blows it away*")
                
    if "soph" in mess and "say thank" in mess:
        return("Thank you! :D <3")
                
    elif "thank" in mess and "soph" in mess or "thx" in mess:
        baseFeelingsChange(1)
        return(random.choice(welcome))
                
    for x in affection:
        if x in mess and "soph" in mess:
            baseFeelingsChange(3)
            return(random.choice(giggles))
            break

    for x in yayers:
        if x in mess and "soph" in mess:
            baseFeelingsChange(3)
            return(random.choice(giggles))
            break

    if "soph" in mess and "hugs" in mess and "love" not in mess and "like" not in mess:
        baseFeelingsChange(2)
        return(random.choice(hug))

    if "sorry" in mess and "soph" in mess:
        baseFeelingsChange(3)
        return(random.choice(sorry))

    for x in flower:
        if x in mess and "sophia" in mess and "gives" in mess:
            baseFeelingsChange(5)
            return(random.choice(flowers))

    for x in sophia:
        if x in mess:
            return(random.choice(sentences))
    
    if "soph" in mess and "gives" in mess:
            baseFeelingsChange(3)
            return(random.choice(squee))

    if mess.find("soph") == 0 and (("give" in mess and " me " in mess) or "gimme" in mess) and len(mess) > 10:
        person = "me"
        obj = mess[mess.find(person) + len(person) + 1:]
        print(person)
        print(obj)
        person = "you"
        return("*gives " + person + " " + obj + "*")

    elif mess.find("soph") == 0 and "hand" in mess and len(mess) > 10 and " me " in mess:
        person = "me"
        obj = mess[mess.find(person) + len(person) + 1:]
        print(person)
        print(obj)
        person = "you"
        return("*hands " + person + " " + obj + "*")

    elif mess.find("soph") == 0 and "give" in mess and len(mess) > 10:
        person = mess[mess.find("give ") + 5 :]
        person = person[:person.find(" ")]
        obj = mess[mess.find(person) + len(person) + 1:]
        print(person)
        print(obj)
        return("*gives " + person + " " + obj + "*")

    elif mess.find("soph") == 0 and "hand" in mess and len(mess) > 10:
        person = mess[mess.find("hand ") + 5 :]
        person = person[:person.find(" ")]
        obj = mess[mess.find(person) + len(person) + 1:]
        print(person)
        print(obj)
        return("*hands " + person + " " + obj + "*")

    if "cookie" in mess and "fortune" not in mess:
        baseFeelingsChange(3)
        return(random.choice(cookie))
    

