# Использование прокси-сервера с модулем requests

# Напишите программу, которая отправляет GET-запрос через прокси-сервер с использованием библиотеки requests.

# Напишите тут ваш код
import requests

url = "http://httpbin.org/ip"
proxies = {
    "http":  "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080",
}
response = requests.get(url, proxies=proxies)
print(response.json())
