from bs4 import BeautifulSoup

# Загружаем HTML с локального файла 'example.html'
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создаем объект BeautifulSoup для анализа HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Извлекаем текст из первого тега <h1>
header = soup.find('h1')
print(header.text)
