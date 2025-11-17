import requests
from bs4 import BeautifulSoup

# URL для загрузки HTML-страницы
url = "http://example.com"  # замените на URL страницы, которую нужно загрузить

# Загрузка HTML-страницы
response = requests.get(url)

# Парсинг HTML-страницы с использованием BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Выборка всех элементов h2 с использованием CSS-селекторов
headers = soup.select('h2')

# Извлечение и вывод текстов
for header in headers:
    print(header.get_text())
