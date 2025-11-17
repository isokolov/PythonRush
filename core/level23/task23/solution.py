# Импортируем библиотеку BeautifulSoup для парсинга HTML
from bs4 import BeautifulSoup

# Открываем HTML-файл для чтения содержимого
with open('example.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Создаем объект BeautifulSoup для парсинга HTML-контента
soup = BeautifulSoup(content, 'html.parser')

# Находим все теги <img> в HTML-коде
images = soup.find_all('img')

# Проходим по каждому найденному тегу <img>
for img in images:
    # Получаем значение атрибута src (ссылка на изображение)
    src = img.get('src')
    # Получаем значение атрибута alt, если оно отсутствует - возвращаем None
    alt = img.get('alt', None)

    # Проверяем, существует ли атрибут alt
    if alt:
        print(f'{src}, {alt}')
    else:
        print(f'{src}, Атрибут alt отсутствует!')
