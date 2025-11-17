# Импортируем библиотеку BeautifulSoup для парсинга HTML-контента
from bs4 import BeautifulSoup

# Загрузка HTML-файла
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Парсим HTML-контент с помощью BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Находим все элементы с классом 'article'
articles = soup.find_all('div', class_='article')

# Создаём пустой список для сохранения результатов
results = []

# Проходим по каждому найденному элементу статьи
for article in articles:
    # results.append([article.find('h3', class_='headline').text, article.find('a')['href']])
    headline = article.find('h3', class_='headline').text
    link = article.find('a', class_='read-more')['href']
    results.append(f"Статья: {headline}, Ссылка: {link}")

# Выводим каждую статью с её заголовком и ссылкой
for result in results:
    print(result)
