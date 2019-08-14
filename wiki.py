import wikipedia
import re
import json
import hashlib

def wiki(mess):
        if "!wiki" in mess:
                string = mess[mess.find("!wiki"):]
                search = string[string.find(" ") + 1:].rstrip("/n")
                result = wikipedia.page(search)
                return(result.url)
