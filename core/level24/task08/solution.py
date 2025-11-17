from requests import RequestException
from requests_html import HTMLSession
import csv

# Указываем URL страницы для рендеринга
url = 'https://example.com'

# Создаем сессию для выполнения HTTP-запросов и рендеринга страницы
session = HTMLSession()

# Пытаемся загрузить и рендерить страницу
try:
    # Загружаем страницу с помощью GET-запроса
    response = session.get(url, timeout=10)
    # Выполняем рендеринг JavaScript с тайм-аутом 20 секунд
    response.html.render(timeout=20)

    # Извлекаем заголовки, подзаголовки и ссылки
    headers = response.html.find('h1')
    subheaders = response.html.find('h2')
    links = response.html.find('a')

# Обрабатываем возможные ошибки при рендеринге или запросе
except RequestException as e:
    print(f"Произошла ошибка: {e}")
except RuntimeError as e:
    print(f"Произошла ошибка: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
    headers, subheaders, links = [], [], []  # Если произошла ошибка, присваиваем пустые списки

# Имя файла для сохранения данных
filename = 'output.csv'

# Открываем файл для записи данных
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Записываем заголовки колонок в CSV-файл
    writer.writerow(['Headers', 'Subheaders', 'Links'])

    # Определяем максимальное количество элементов среди заголовков, подзаголовков и ссылок
    max_len = max(len(headers), len(subheaders), len(links))

    # Записываем данные построчно в CSV-файл
    for i in range(max_len):
        row = [
            headers[i].text if i < len(headers) else '',  # Текст заголовка, если существует
            subheaders[i].text if i < len(subheaders) else '',  # Текст подзаголовка, если существует
            links[i].attrs['href'] if i < len(links) else ''  # Ссылка, если существует
        ]
        writer.writerow(row)


'''
Добавить явную установку таймаута при GET-запросе (например, session.get(url, timeout=10))
и раздельную обработку разных исключений (requests.exceptions.RequestException, RuntimeError и т.д.).
Можно также логировать ошибку и безопасно завершать работу.

При извлечении данных лучше получать текст заголовков/подзаголовков и абсолютные ссылки (использовать .text 
и проверять attrs['href']). Также учесть случаи отсутствия атрибута href и пропускать или подставлять пустую 
строку — сейчас это частично реализовано.

Использование модуля csv корректно. Рекомендуется сохранять полные URL (если нужна абсолютная ссылка) и 
обрабатывать случаи отсутствия href. При большом числе элементов можно записывать дополнительные колонки 
или нормализовать данные, но в целом требование выполнено.
'''
