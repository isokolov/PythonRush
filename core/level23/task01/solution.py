import requests
import json

# Отправляем HTTP-запрос на сайт
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

# Извлекаем данные из JSON-ответа
todo_data = response.json()

# Выводим данные в отформатированном виде
print(json.dumps(todo_data, indent=4))
