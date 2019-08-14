import random
import feelings

fsm = ["Bow before His Noodly Goodness!", "Let me fetch my colander real quick...", "*puts on colander hat*", "Each of our souls have been touched by His Noodly Appendages!", "All hail the Flying Spaghetti Monster!", "Pastafarianism is even better than Satanism!", "All hail the FSM!", "All hail! /o/"]

fsm_names = ["fsm", "flying spaghetti monster", "his noodly", "pastafarian"]

def pasta(mess):        
        for x in fsm_names:
            if x in mess:
                baseFeelingsChange(1)
                return(random.choice(fsm))
