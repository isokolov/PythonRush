import requests
from bs4 import BeautifulSoup

# Загрузка HTML-контента с заданного URL
response = requests.get("http://example.com")
html_content = response.text

# Анализ HTML-контента с помощью BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Извлечение и вывод текста из тега h1
header = soup.h1.text
paragraph = soup.find('p').text

# Извлечение и вывод текста из первого тега p
print(header)
print(paragraph)
