# Импортируем необходимые библиотеки для выполнения HTTP-запросов, парсинга HTML и работы с CSV
import requests
from bs4 import BeautifulSoup
import csv
import time

# URL страницы, с которой будем извлекать заголовок
url = 'https://example.com'

# Определяем максимальное количество попыток
retries = 3
attempts = 0
title = None

# Пытаемся выполнить запрос к URL несколько раз при ошибках
while attempts < retries:
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string.strip() if soup.title else 'No title Found'
        break
    except (requests.exceptions.RequestException, requests.exceptions.Timeout) as e:
        print(f"Попытка {attempts + 1} не удалась: {e}")
        attempts += 1
        time.sleep(1)

# Если заголовок извлечен успешно, сохраняем его в CSV файл
if title:
    with open('titles.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([title])
    print(f"Заголовок '{title}' сохранен в 'titles.csv'.")
else:
    print("Не удалось извлечь заголовок после нескольких попыток.")
