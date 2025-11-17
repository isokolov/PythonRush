from bs4 import BeautifulSoup

# Загрузка HTML-файла
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создаем объект BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Находим все элементы <p>
paragraphs = soup.find_all('p')

# Выводим текст из каждого элемента <p>
for paragraph in paragraphs:
    print(paragraph.text)
