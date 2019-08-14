import random

cry = ["I love you too, soooo much! :D <3", "You're the apple of my eye! <3", "i wuvs yoo too", "*boops your nose and giggles*", "*hugs you warmly*", "<3 <3 <3"]

#father = ["I love you too, Dad :D", "You're the best, dad!", "i wuv you too <3", "I'll give you all my pudding. <3", "you're my C6H11O6 (glucose) <3", "my papa <3"]

mother = ["I love you too, Mom :D", "You're the best, mommy!", "i wuv you too <3", "I'll not give you all my pudding, just some of it :o", "you're my C6H11O6 (fructose) <3", "mommy <3"]

def love(mess, auth):
    """if "i love you" in mess and "cuisinart8" in str(auth):
        return(random.choice(father))"""

    if "i love you" in mess and "Vivacia" in str(auth): 
        baseFeelingsChange(10)
        return(random.choice(mother))

    elif "i love you" in mess:
    	baseFeelingsChange(-10)
        return(random.choice(cry))
