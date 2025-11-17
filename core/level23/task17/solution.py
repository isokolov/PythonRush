from bs4 import BeautifulSoup

# Загрузка HTML-файла
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создание объекта BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Использование CSS-селектора для поиска всех заголовков (теги h2) с классом "headline"
headers = soup.select('h2.headline')

# Извлечение и печать заголовков
for header in headers:
    print(header.text)
