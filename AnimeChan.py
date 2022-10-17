import requests

def a():
    url = 'https://animechan.vercel.app/api/random'
    r = requests.get(url)
    j = r.json()

    anime = j['anime']
    character = j['character']
    quote = j['quote']
    #------- _** = negrita en discord :v -------------
    print(f'_**Anime :**_ {anime}\n _**Personaje :_** {character}\n _**Cita :_** {quote}')
a()

print('\n')

def b():
    url = 'https://animechan.vercel.app/api/quotes/anime?title=naruto'
    r = requests.get(url)
    j = r.json()
    total =(len(j))
    one = j[0]

    print('anime: ', one['anime'])
    print('personaje: ', one['character'])
    print('cita: ', one['quote'])
b()