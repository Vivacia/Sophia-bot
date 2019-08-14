import random

star = ["Firing phasers!", "Firing photon torpedoes!", "Shields up, red alert!", "Captain on the bridge!", "Warp core breach! D:"]

def trek(mess):
        if "star trek" in mess or "startrek" in mess:
                return(random.choice(star))
