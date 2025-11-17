from bs4 import BeautifulSoup

# Путь к HTML-файлу, который будем анализировать
file_path = "example.html"  # Укажите путь к вашему HTML-файлу

# Открываем HTML-файл и читаем его содержимое
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создаем объект BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Извлекаем данные из таблицы
table = soup.find('table')
fruits_in_table = []
for row in table.find_all('tr')[1:]:
    # fruit = [td.text for td in row.find('td')]
    fruit = row.find('td').text
    fruits_in_table.append(fruit)

# Извлекаем данные из списка
ul = soup.find('ul')
fruits_in_ul = [fruit.text for fruit in ul.find_all('li')]

# print(fruits_in_table)
# print(fruits_in_ul)
# Сравниваем и получаем общее множество
fruits = [fruit for fruit in fruits_in_table if fruit in fruits_in_ul]

# Выводим результат
print(fruits)

'''
from bs4 import BeautifulSoup

# Путь к HTML-файлу, который будем анализировать
file_path = "example.html"  # Укажите путь к вашему HTML-файлу

# Открываем HTML-файл и читаем его содержимое
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создаем объект BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Извлекаем данные из таблицы
table_fruits = {row.find('td').text for row in soup.find_all('tr')[1:]}

# Извлекаем данные из списка
list_fruits = {li.text for li in soup.find_all('ul')[0].find_all('li')}

# Сравниваем и получаем общее множество
common_fruits = list(table_fruits & list_fruits)

# Выводим результат
print(common_fruits)
'''
