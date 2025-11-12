# OpenWeatherMap API

# Напишите программу, которая использует OpenWeatherMap API для получения текущей погоды в указанном городе.

# Напишите тут ваш код
import requests
API_KEY = 'Key'
city = input("Enter city: ")
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

resp = requests.get(url)
dat = resp.json()

if resp.status_code == 200:
    weather = dat['weather'][0]['description']
    temp = dat['main']['temp']
    print(f'Погода в {city}: {weather}, температура: {temp}°C')
else:
    print("We have error!")
