import requests
from bs4 import BeautifulSoup

# Задайте URL страницы, которую нужно загрузить
url = 'http://example.com'  # Вы можете заменить этот URL на нужный

# Загрузите HTML-страницу
response = requests.get(url)

# Преобразуйте контент страницы в объект BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Найдите все теги <p> и извлеките текст
paragraphs = soup.find_all('p')

# Выведите текст каждого абзаца
for p in paragraphs:
    print(p.get_text())
