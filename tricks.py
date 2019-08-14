import random

coin = ["Heads!", "Tails"]

ans = ["Nuh-uh.", "Of course! :D", "I love that idea.", "meow meow \n*purrs*", "Yeah!", "Totally!", "Nope", "uhhh...", "I'm not sure.", "Auntie said no :(\n...but I disagree.", "Uncle somberero said that I have to decide...\nI say no. :o", "I'll ask Daddy :)", "meow", "Daddy said yes, so I say no.", "Mommy said to say yes.", "I don't know what that means. :(", "Can you explain the question...?", "What's that?", "Sorry, mommy told me to say no."]

hmm = ["uhhh... ", "Mommy told me to choose ", "OOOH! ", "yay! ", "I choose... ", "I choose "]

idk = ["Probably sleeping...", "Tired, maybe :(", "I miss them.", "Mommy misses them.", "Awesome!", "Doing great!", "squaddlidoo"]

ooh = ["Pretty great!", "I think it's really nice!", "You should try it!", "I don't like it. :(", "I didn't like it.", "Dad said he hates me.", "Mommy loves it!", "I'm sorry, I didn't hear you."]

ball = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no.", "My sources say no", "Outlook not so good", "Very doubtful."]

where = ["With my baby brother Kyle! :D", "In bed.", "In the sky!", "*thinks*\n*thinks harder...*", "On Youtube!", "On the Moon!", "In my pocket! <3", "Under the bed. ;-;", "In Mommy's heart.", "In your hand. :D"]

def trick(mess):
    if mess.find("soph") == 0 and ("8-ball" in mess or "8ball" in mess):
        return(random.choice(ball))
    
    elif "soph" in mess and "choose" in mess or "!choose" in mess and "t!choose" not in mess:
        choices = []
        foo = mess[mess.find("choose ") + 7 : mess.find(";")]
        choices.append(foo)
        right = False
        while ";" in mess:
            mess = mess[mess.find(";") + 2 :]
            if ";" in mess:
                bar = mess[: mess.find(";")]
            else:
                bar = mess
            choices.append(bar)
            right = True
        print(choices)
        if right == False:
            return
        else:
            return(random.choice(hmm) + " " + random.choice(choices) + "!")

    elif "flip a coin" in mess or "!coinflip" in mess:
        return(random.choice(coin))

    elif "soph" in mess and "where" in mess:
        return(random.choice(where))

    elif ("wanna" in mess or "will " in mess or "should" in mess or "could" in mess or " can " in mess or "right" in mess or "are you" in mess or " am i" in mess or " do you" in mess) and "soph" in mess or ("soph" in mess and "are" in mess and "?" in mess):
        return(random.choice(ans))

    elif "soph" in mess and ("how is the" in mess or "hows the" in mess or "how's the" in mess):
        return(random.choice(ooh))  
    
    elif "soph" in mess and ("how is" in mess or "hows" in mess or "how's" in mess):
        return(random.choice(idk))
