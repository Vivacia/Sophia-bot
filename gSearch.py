from bs4 import BeautifulSoup

queries = ["sophia who is", " sophia, who is", "sophia who's", "sophia, who's", "sophia whos", "sophia, whos", "sophia tell me whos", "sophia, tell me whos", "sophia tell me who is", "sophia, tell me who is", "sophia tell me who's", "sophia, tell me who's", "sophia, please tell me whos", "sophia, please tell me who is", "sophia, please tell me who's", "sophia please tell me whos", "sophia please tell me who is", "sophia please tell me who's", "sophia who are", "sophia, who are", "sophia tell me who are", "sophia, tell me who are", "sophia, please tell me who are", "sophia please tell me who are", "sophia, tell me whats", "sophia tell me whats", "sophia, tell me what's", "sophia tell me what's", "sophia please tell me whats", "sophia, please tell me whats", "sophia, tell me what is", "sophia tell me what is", "sophia please tell me what is", "sophia, please tell me what is", "sophia please tell me what's", "sophia, please tell me what's", "sophia, google", "sophia google", "sophia please google", "sophia, please google", "sophia please search", "sophia, please search" "sophia, google", "sophia search", "sophia, search", "sophia lookup", "sophia please lookup", "sophia, please lookup", "sophia, please look up", "sophia please look up", "sophia, please look-up", "sophia please look-up", "sophia, lookup", "sophia look-up", "sophia, look-up", "sophia, look up", "sophia look up", "sophia, what is", "sophia what is", "sophia, what\'s", "sophia what\'s", "sophia whats", "sophia, whats", "sophia what are", "sophia, what are", "sophia tell me what are", "sophia, tell me what are", "sophia please tell me what are", "sophia, please tell me what are"]

notQueries = ["what's up", "whats up"]

def gSearch(mess):
    for x in queries:
        for y in notQueries:
            if mess.find(x) == 0 and y not in mess:
                try:
                    import google
                except ImportError: 
                    print("No module named 'google' found")
                    return("Oops... Something's not right. :/")
                term = x
                leng = len(x) + 1
                break
                
                # to search
                query = mess[mess.find(term) + leng:]
                 
                for result_ in search(query, tld="us", num=2, stop=1, pause=3):
                    return(result_)
