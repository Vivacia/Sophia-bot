def pong(mess):
    if (mess.find("test") == 0 or mess.find("test") == 1) and len(mess) < 8:
        return("Passed!")

    elif "!ping" == mess:
        return("Pong!")

    elif "!pong" == mess:
        return("Ping!")

    elif "beep boop" in mess:
        return("boop beep")
