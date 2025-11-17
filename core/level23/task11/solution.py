import requests
from bs4 import BeautifulSoup

# Загрузка HTML с помощью requests
url = "http://example.com"
response = requests.get(url)
html_content = response.text

# Анализ HTML с помощью BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Извлечение всех тегов <a>
links = soup.find_all('a')

# Вывод ссылок и их атрибутов href
for link in links:
    # Получение атрибута href, если он существует
    href = link.get('href', None)
    if href:
        print(f"Link: {link.text}, Href: {href}")
    else:
        print(f"Link: {link.text}, Href: None")
