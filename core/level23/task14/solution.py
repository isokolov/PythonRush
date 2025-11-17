from bs4 import BeautifulSoup

# Загрузка HTML-файла
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создаем объект BeautifulSoup для парсинга HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Находим все теги <a> с классом link
links = soup.find_all('a', class_='link')

# Извлекаем значения атрибутов href
hrefs = []
for link in links:
    hrefs.append(link['href'])

# Вывод извлеченных ссылок
for href in hrefs:
    print(href)
