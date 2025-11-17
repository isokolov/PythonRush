import requests
from bs4 import BeautifulSoup

# Загрузка HTML-страницы
url = "http://example.com"
response = requests.get(url)

# Создание объекта BeautifulSoup для парсинга HTML
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

# Извлечение текста заголовка страницы
title = soup.title.text

# Вывод текста заголовка
print('Title: ', title)
