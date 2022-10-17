import requests

def a():
    url = 'https://animechan.vercel.app/api/random'
    r = requests.get(url)
    j = r.json()


    #print(f'_**Anime :**_ {anime}\n _**Personaje :_** {character}\n _**Cita :_** {quote}')

def b():
    url = 'https://animechan.vercel.app/api/quotes/anime?title=naruto'
    r = requests.get(url)
    j = r.json()
    total =(len(j))
    on = j[0]
    print(on['anime'])
    print(on['character'])
    print(on['quote'])
    print(on)
    print(type(j))
    #character = j["character"]
    #quote = j["quote"]
    #Personaje : {character}\n Cita : {quote}

b()