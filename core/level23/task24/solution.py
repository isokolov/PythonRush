# Импортируем библиотеку BeautifulSoup для парсинга HTML
from bs4 import BeautifulSoup

# Путь к HTML-файлу, который будем анализировать
file_path = 'example.html'

# Открываем HTML-файл и читаем его содержимое
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создаем объект BeautifulSoup для парсинга HTML-контента
soup = BeautifulSoup(html_content, 'html.parser')

# Извлечение всех ссылок (теги <a>)
print("Ссылки:")
links = soup.find_all('a')
# Проходим по каждой ссылке
for link in links:
    # Извлекаем текст ссылки, если он отсутствует, выводим "Нет данных"
    text = link.get_text(strip=True) or "Нет данных"
    # Извлекаем URL ссылки, если он отсутствует, выводим "Нет данных"
    url = link.get('href') or "Нет данных"
    # Выводим текст ссылки и её URL
    print(f"Текст: {text}, URL: {url}")

# Извлечение всех изображений (теги <img>)
print("\nИзображения:")
images = soup.find_all('img')
# Проходим по каждому изображению
for image in images:
    # Извлекаем URL изображения, если он отсутствует, выводим "Нет данных"
    url = image.get('src') or "Нет данных"
    # Извлекаем альтернативный текст, если он отсутствует, выводим "Нет данных"
    alt_text = image.get('alt') or "Нет данных"
    # Выводим URL изображения и его альтернативный текст
    print(f"URL: {url}, Альтернативный текст: {alt_text}")
