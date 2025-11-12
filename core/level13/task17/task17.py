# Google Maps API

# Напишите программу, которая использует Google Maps API для получения координат (широта и долгота) по указанному адресу.

# Напишите тут ваш код
import requests

API_KEY = 'Key'
adress = '10000 Janirova 12, Prague, Czech Republic'
url = f'https://maps.googleapis.com/maps/api/geocode/json?address={adress}&key={API_KEY}'
resp = requests.get(url)
dat = resp.json()

if dat['status'] == 'OK':
    location = dat['results'][0]['geometry']['location']
    lat = location['lat']
    lng = location['lng']
    print(f"{lat},{lng}")
else:
    print("We hae a problem!")
