# Импортируем библиотеку BeautifulSoup для парсинга HTML
from bs4 import BeautifulSoup

# Имя HTML-файла, который будем читать
html_filename = 'example.html'  # Замените на имя вашего HTML файла
# Имя выходного текстового файла для записи результатов
output_filename = 'output.txt'

# Открываем HTML-файл и читаем его содержимое
with open(html_filename, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Парсим HTML-контент с помощью BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Находим все элементы <p> внутри классов content и highlighted-content
content_paragraphs = soup.select('.content p')
highlighted_paragraphs = soup.select('.highlighted-content p')

# Создаём пустой список для хранения информации о параграфах
paragraphs = []

# Проходим по всем найденным параграфам в классе content
for p in content_paragraphs:
    paragraphs.append(f"Class: content\n{p.get_text(strip=True)}\n")

# Проходим по всем найденным параграфам в классе highlighted-content
for p in highlighted_paragraphs:
    paragraphs.append(f"Class: highlighted-content\n{p.get_text(strip=True)}\n")

# Записываем все извлечённые параграфы в выходной файл
with open(output_filename, 'w', encoding='utf-8') as file:
    for paragraph in paragraphs:
        # Пишем каждый параграф с новой строки
        file.write(paragraph + "\n")
