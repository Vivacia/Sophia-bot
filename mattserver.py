import random

waifu = ["WAIFU? Is that kung-fu, but with your wife?", "I love waifus and tofus!", "yumyum in me tumtum", "can I have a waifu too?", "MOOOOOOM they're not sharing their waifus with me D:", "ooh", "OOH"]

putin = ["let's put it in, let's put it out", "what does that mean, mommy?", "is that true?", "are you joking?", "mista russia man is on the news?", "why?", "how?", "when?", "is that real?""POOOOOTEEEEEEEEN <3", "Can Putin actually funk?", "funking with junkies", "poutini, the magic man", "My hero! <3", "putinputinputin", "woah!", "wowie"]

russia = ["ruuusssssiiiaaa", "Рад тебя видеть", ":O", ":o", "woah", "Russia! America!", "mista man, I want some candy. Pleeeeeeaaaase? D:", "*flies in her toy stuka bomber*\nWEEEEE", "what even", "i can't like even i'm dying omg lol", "kek", "mommy, they're talking about Russia!", "is Russia a real place?", "can we go there in summer, dad?", "Olive doesn't like Russia. I don't like it too, then.", "them rooskies"]

pentagon = ["AAAAAAH! The five sided triangle with an eye!", "america's favourite shape!", "why though?", "are you serious?", "mommy, is he lying?", "why didn't they name it octagon because octagons are cool!", "triangles too!", "yay! :D", "little squares and triangles mate to become a pentagon", "I love shapes!", "Why do people e'splode nukes in a shape in school?"]

stalin = ["STALIN, MY HERO <3", ":O", "WOW!", "that's awesome!", "Unf.", "cool!  :D", "woah", "kek"]

kim = ["kimichi!", "kiiiiiim D:", "mista nukes!", ":O", "o.O", "wowzers!", "Why would my friend's parents name her Kim? :(", "no D:"]

us = ["The you-ess of ayaah!", "united but divided but united in three states of matter but does that matter?", "mommy wants to go there!", "can you take me there?", "Olive and matt and kep and so many peeps live here :o"]

soviet = ["the union of onions!", ":kappa:", "potato", "wow", "woah", "really?", "is that true?", "BIG FAT DEAD COUNTRY", "Mista russia man might be sad it's dead", "dedder than roadkill", "i prefer cookies :o", "Доброе утро!", "Рад познакомиться с вами", "Я плохо говорю по-русски"]

german = ["Belgium!", "german engineering is da best", "Mommy is scared of Germans. She's tiny, like me.", "Dad thinks Germans are cool", "ooh!?", ":kappa:", "Cool!", "KEEEPPPLLEEEEEERRRR", "keps the germanophile", "Nein", "natürlich", "richtig", "Ich spreche nicht viel Deutsch.", "Ich brauche Auskunft.", "Kein Mensch versteht es"]

poland = ["poooooland", "red and white!", "mmmmm polish people", ":kappa:", "polandpoLANDPOLAND", ":kappa:"]

jew = ["just like mista nazi likes", "mista olive man", "the bad jew-jew", "i love me some juice", "jewjewjewjewjew"]

AA = ["*gives you more bombs*", "KABOOM!", "*explodes*", "oh noes.", "peeekaaaa-BOOM!", ":DDD"]

    
def politics(mess):
        if "the iraq" in mess:
            baseFeelingsChange(-5)
            return("Sometimes, I hate you guys. Furthermore, like such as.")

        elif "putin" in mess:
            return(random.choice(putin))

        elif "cooking" in mess or "recipe" in mess:
            return("http://www.youtube.com/watch?v=K5tVbVu9Mkg")

        elif "russia" in mess:
            return(random.choice(russia))

        elif " kim " in mess:
            return(random.choice(kim))

        elif "pentagon" in mess:
            return(random.choice(pentagon))

        elif "stalin" in mess:
            return(random.choice(stalin))
                
        elif "jew" in mess:
            return(random.choice(jew))

        elif "soviet" in mess:
            return(random.choice(soviet))

        elif " usa " in mess:
            return(random.choice(us))

        elif "german" in mess:
            return(random.choice(german))

        elif "poland" in mess:
            return(random.choice(poland))
                

def memes(mess):
        if "mom" in mess and "gay" in mess:
            baseFeelingsChange(5)
            return("Daddy doesn't think so.")

        elif "allahu akbar" in mess:
            return(random.choice(AA))

        elif "america" in mess:
            return("MURIKAH!")
                        
        elif "your waifu" in mess or "my waifu" in mess:
            return(random.choice(waifu))
                        
        elif "donald trump" in mess:
            return("Tronald Dump!?")

        elif "triggered" in mess:
            return("AAAAAAAAAAAAAAAAAAAH")

        elif "y u do dis" in mess:
            return("but mooooooooooom")

        elif "whomst" in mess:
            return("https://www.youtube.com/watch?v=QoCcDi8zH8M")

        elif "we are number one" in mess:
            return("HEY!")
