# Отправка POST-запроса

# Напишите программу, которая отправляет POST-запрос с JSON-данными на URL и обрабатывает полученный JSON-ответ.

# Напишите тут ваш код
import requests

data = {
    "userId": 1,
    "title": "Learn Python POST request",
    "completed": False
}

response = requests.post("https://jsonplaceholder.typicode.com/todos/", json=data)
print(response.status_code)
print(response.json())
