# Импортируем библиотеку BeautifulSoup для парсинга HTML
from bs4 import BeautifulSoup

# Путь к HTML-файлу, который будем анализировать
file_path = "example.html"  # Укажите путь к вашему HTML-файлу

# Открываем HTML-файл и читаем его содержимое
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создаем объект BeautifulSoup для парсинга HTML-контента
soup = BeautifulSoup(html_content, 'html.parser')

# Ищем таблицу с классом 'data-table'
table = soup.find('table', class_='data-table')

# Если таблица не найдена, выводим пустой список данных
table_data = []
if table:
    # Находим все строки таблицы (теги <tr>)
    rows = table.find_all('tr')

    # Проходим по каждой строке
    for row in rows:
        # Извлекаем все ячейки строки (теги <td>)
        cells = row.find_all('td')
        # Извлекаем текст из каждой ячейки и формируем список данных для строки
        row_data = [cell.get_text(strip=True) for cell in cells]
        # Добавляем список строки в общий список данных, если строка не пуста
        if row_data:
            table_data.append(row_data)

# Выводим полученные данные из таблицы
print(table_data)
