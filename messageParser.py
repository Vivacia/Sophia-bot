"""
FORMAT:
'<:username><IP> PRIVMSG <channel> :<message>\r'
"""

def usefulText(text, chan):
    start = text.find(str(chan) + " :") + len(str(chan)) + 2
    end = text.find("\r'")
    text = text[ start : end ].lower()
    return(text)

def username(text):
    uName = text[2 : text.find("!~")]
    return(uName)

def IPAddress(text):
    ipa = text[text.find("~") + 1 : text.find(" ")]
    return(ipa)


