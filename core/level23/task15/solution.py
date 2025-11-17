from bs4 import BeautifulSoup

# Загрузка HTML-файла
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создаем объект BeautifulSoup для парсинга HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Извлечение текста из всех тегов <h1> и <h2>
'''
contents = soup.find_all('div', class_='content')
for content in contents:
    h1 = content.find('h1')
    sub_contens = content.find_all('h2')
'''

'''
# Создаем объект BeautifulSoup для парсинга HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Извлечение текста из всех тегов <h1> и <h2>
headings = soup.find_all(['h1', 'h2'])

# Выводим все заголовки и подзаголовки
for heading in headings:
    print(heading.get_text())
'''

h1 = soup.find('h1')
sub_contens = soup.find_all('h2')

# Выводим все заголовки и подзаголовки
print(h1.text)
for sub_content in sub_contens:
    print(sub_content.text)
