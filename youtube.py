from bs4 import BeautifulSoup
import urllib
import urllib.parse
import urllib.request
import re
import json
import hashlib

def youtube(mess, search):
        result_list = []
        search_query = urllib.parse.urlencode({"search_query": search})
        url = "http://www.youtube.com/results?" + search_query
        response = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(response, "html.parser")
        for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
                result_list.append("http://www.youtube.com" + vid['href'])

        if "/user/" in result_list[0]:
                result_list.remove(result_list[0])
        return(result_list)
        
async def youtube2(mess):
    if "!y " in mess or "!yt " in mess or "!youtube" in mess:
            string = mess[mess.find("!y"):]
            search = string[string.find(" ") + 1:].rstrip("\n")
            result = youtube(mess, search)
            return(result[0] + " | " + result[1])
    elif "soph" in mess and "play" in mess:
            string = mess[mess.find("play "):]
            search = string[string.find(" ") + 1:].rstrip("\n")
            result = youtube(mess, search)
            return(result[0] + " | " + result[1])
    else:
        return

