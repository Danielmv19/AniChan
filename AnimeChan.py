import random

import requests
def a():
    url = 'https://animechan.vercel.app/api/random'
    r = requests.get(url)
    j = r.json()

    anime = j['anime']
    character = j['character']
    quote = j['quote']
    print(f'Anime: {anime}\nPersonaje: {character}\nCita: {quote}')
    #------- _** = negrita en discord :v -------------
    #print(f'_**Anime :**_ {anime}\n _**Personaje :_** {character}\n _**Cita :_** {quote}')
a()

print('----------------------------------------------------------------')
def b():
    animeName = input("Ingrese el nombre del anime: ")
    url = f'https://animechan.vercel.app/api/quotes/anime?title={animeName}'
    r = requests.get(url)
    j = r.json()
    total =(len(j))
    totalRandom = random.choice(range(0, total))
    print(f'cita {totalRandom} de {total}')
    one = j[totalRandom]
    anime = one['anime']
    character = one['character']
    quote = one['quote']

    print(f'Anime: {anime}\nPersonaje: {character}\nCita: {quote}')

b()
print('----------------------------------------------------------------')
def c():
    characName = input("Ingrese el nombre del personaje: ")
    url = f'https://animechan.vercel.app/api/quotes/character?name={characName}'
    r = requests.get(url)
    j = r.json()
    total =(len(j))
    totalRandom = random.choice(range(0, total))
    print(f'cita {totalRandom} de {total}')

    one = j[totalRandom]
    anime = one['anime']
    character = one['character']
    quote = one['quote']

    print(f'Anime: {anime}\nPersonaje: {character}\nCita: {quote}')

c()