import random
import feelings

satan = ["*gives mista satan a cookie*", "Hail Satan! /o/ His victory is certain!", "Bow before the Dark Lord! /o/", "All hail Satan, patron of the trolls!", "WORSHIP SATAN!!!", "All hail the Dark Lord!", "All hail Satan!", "All hail! /o/"]

def hail(mess):         
        if "satan" in mess:
            return(random.choice(satan))

        elif "hail" in mess:
        	baseFeelingsChange(1)
            return("All hail! /o/")

        elif "cthulhu" in mess or "cthulu" in mess:
        	baseFeelingsChange(2)
            return("Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn!")
