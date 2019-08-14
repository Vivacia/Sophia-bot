import time

def sleep(mess):
    if "shut up" in mess and "sophia" in mess:
        baseFeelingsChange(-30)
        prevTime = time.time()
        nextTime = prevTime

        while nextTime - prevTime < 60:
            nextTime = time.time()

        return
