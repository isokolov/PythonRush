from bs4 import BeautifulSoup
import csv

# Путь к HTML-файлу, который будем анализировать
file_path = "example.html"  # Укажите путь к вашему HTML-файлу

# Открываем HTML-файл и читаем его содержимое
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Парсинг HTML-контента
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table')

# Извлечение заголовков
headers = [th.text for th in table.find_all('th')]

# Извлечение данных строк
# data = soup.find_all('tr')[1:]
rows = []
for row in table.find_all('tr')[1:]:
    cols = [td.text for td in row.find_all('td')]
    rows.append(cols)

# Запись данных в CSV-файл
with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # запись заголовков
    writer.writerows(rows)    # запись строк данных
