import logging
import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout

# Настраиваем логирование, указываем файл для записи ошибок и формат сообщений
logging.basicConfig(filename='scraper.log', level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')
# Указываем URL, который будем сканировать
url = 'http://example.com'

# Пытаемся выполнить GET-запрос к указанному URL с тайм-аутом 5 секунд
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    page_content = response.text

# Обработка исключений при возникновении HTTP ошибки
except HTTPError as http_err:
    logging.error(f'Произошла HTTP ошибка: {http_err}')

# Обработка исключений при возникновении ошибки соединения
except ConnectionError as conn_err:
    logging.error(f'Произошла ошибка соединения: {conn_err}')

# Обработка исключений при превышении времени ожидания
except Timeout as timeout_err:
    logging.error(f'Произошло превышение времени ожидания: {timeout_err}')

# Общая обработка всех остальных ошибок
except Exception as err:
    logging.error(f'Произошла ошибка: {err}')
