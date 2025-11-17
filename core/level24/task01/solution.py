import requests

# Устанавливаем URL
url = "https://httpbin.org/user-agent"

# Определяем поддельный User-Agent для Safari на macOS
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15"
}

# Отправляем HTTP-запрос с поддельным User-Agent
response = requests.get(url, headers=headers)

# Выводим содержимое ответа сервера
print(response.content)
