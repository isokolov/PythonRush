import requests
from bs4 import BeautifulSoup

# URL для загрузки
url = 'https://example.com'
# url = 'https://www.ozon.ru/seller/santegra-1037570/?miniapp=seller_1037570' # ИП Михайлов

# Выполнение HTTP-запроса для получения HTML-кода страницы
response = requests.get(url)

# Parsing Ozon
response.encoding = 'utf-8'
print(response.encoding)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())
# Parsing Ozon


# Парсинг HTML-кода с помощью BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Извлечение заголовка страницы
title = soup.title.text

# Вывод заголовка страницы
print('Title: ', title)
