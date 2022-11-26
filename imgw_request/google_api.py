from os import environ
from requests import get
from dotenv import load_dotenv

load_dotenv()
api_key = environ.get('API_KEY')
url = "https://maps.googleapis.com/maps/api/distancematrix/json"

origin = input('Skąd jedziesz?')
destination = input('Dokąd jedziesz')
consumption = float(input('Ile pali Twój samochód'))
prize = float(input('Cena paliwa'))

payload = {
    'origins': origin,
    'destinations': destination,
    'key': api_key
}

response = get(url, payload)
body = response.json()
print(body)

distance = body['rows'][0]['elements'][0]['distance']
duration = body['rows'][0]['elements'][0]['duration']

cost = prize*distance['value']/1000*consumption/100
print(f'Koszt przejazdu wynosi: {cost}')