import requests

# Запрос пользователя на ввод userId
userId = int(input('Input userID: '))

# URL для обращения к API
url = "https://jsonplaceholder.typicode.com/posts"

# Параметры запроса
params = {'userId': userId}

# Отправка GET-запроса
response = requests.get(url, params=params)

# Обработка ответа в формате JSON
posts = response.json()

# Извлечение и вывод заголовков (title) всех постов
for post in posts:
    print(post['title'])
