from google import search 

def googlesearch(term):
    q = []
    for j in search(term, tld="co.in", num=1, stop=1, pause=2):
        q.append(j)
    return(q[-1])
print(googlesearch('Django'))
