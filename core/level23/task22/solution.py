# Импортируем библиотеку BeautifulSoup для парсинга HTML
from bs4 import BeautifulSoup

# Открываем HTML-файл и читаем его содержимое
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создаем объект BeautifulSoup для парсинга HTML-контента
soup = BeautifulSoup(html_content, 'html.parser')

# Находим все теги <a> в HTML-коде
links = soup.find_all('a')

# Извлекаем ссылки из каждого тега <a>, получая значения атрибута href
hrefs = []
for link in links:
    hrefs.append(link['href'])

# Выводим каждую ссылку на новой строке
for href in hrefs:
    print(href)
