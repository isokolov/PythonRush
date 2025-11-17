from bs4 import BeautifulSoup

# Путь к HTML-файлу, который будем анализировать
file_path = "example.html"  # Укажите путь к вашему HTML-файлу

# Открываем HTML-файл и читаем его содержимое
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создание объекта BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Извлечение элементов списка <li>
tag_li = soup.find_all('ul')

# Формирование списка Python из текста элементов
lis_ = []
for li in tag_li:
    try:
        li_ = li.findAll('li')
        for elem in li_:
            lis_.append(elem.text)
    except:
        pass

# Вывод результата
print(lis_)
