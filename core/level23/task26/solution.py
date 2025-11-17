from bs4 import BeautifulSoup

# Открываем и читаем содержимое HTML-файла
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создаем объект BeautifulSoup для парсинга HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Находим все элементы с тегом <a>
a_tags = soup.find_all('a')

# Извлекаем href-атрибуты из каждого найденного элемента
hrefs = [a.get('href') for a in a_tags if a.get('href')]

# Выводим список href-атрибутов
for href in hrefs:
    print(href)
