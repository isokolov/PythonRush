import requests
import time
import random

# Определяем URL, к которому будем отправлять запросы
url = "https://httpbin.org/get"

# Заголовки для имитации пользовательского агента
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15"
}

# Создаем сессию для сохранения состояния (например, куки)
session = requests.Session()

# Цикл для отправки пяти запросов
for _ in range(5):
    response = session.get(url, headers=headers)
    print(response.status_code)
    time.sleep(random.uniform(2, 5))
