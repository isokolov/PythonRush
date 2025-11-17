from bs4 import BeautifulSoup

# Загрузка HTML-файла
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создание объекта BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Использование CSS-селектора для поиска всех элементов <a> внутри элемента с классом "navigation"
links = soup.select('.navigation a')

# Извлечение и вывод ссылок
for link in links:
    print(link.get('href'))
