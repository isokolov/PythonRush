# Импортируем библиотеку BeautifulSoup для парсинга HTML
from bs4 import BeautifulSoup

# Путь к HTML-файлу, который будем анализировать
file_path = "example.html"  # Укажите путь к вашему HTML-файлу

# Открываем HTML-файл и читаем его содержимое
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создаем объект BeautifulSoup для парсинга HTML-контента
soup = BeautifulSoup(html_content, 'html.parser')

# Находим все заголовки <h2> с классом 'article-title'
titles = soup.find_all('h2', class_='article-title')

# Проходим по каждому найденному заголовку
for title in titles:
    # Извлекаем текст заголовка, убирая лишние пробелы
    text = title.get_text(strip=True)
    # Пытаемся найти тег <a> внутри заголовка, чтобы получить ссылку
    tag_a = title.find('a')
    # Если тег <a> существует и содержит атрибут href, извлекаем URL
    url = ''
    if tag_a and tag_a.get('href'):
        url = tag_a.get('href')

    # Выводим информацию в заданном формате
    print(f'Title: {text}, Link: {url}')
