

from requests import get

url = 'https://danepubliczne.imgw.pl/api/data/synop/'

response = get(url)
pogoda_stacje=response.json()

for stacja in pogoda_stacje:
    print(stacja['stacja'], stacja['temperatura'], sep=' \t')





