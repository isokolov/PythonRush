# Отправка GET-запроса

# Напишите программу, которая отправляет GET-запрос с параметрами на URL и обрабатывает полученный JSON-ответ.

# Напишите тут ваш код
import requests

params = {'userId': 1}
response = requests.get("https://jsonplaceholder.typicode.com/todos/", params=params)
print(response.status_code)
print(response.json())
