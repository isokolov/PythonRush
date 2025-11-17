import requests

# Определяем URL для проверки
url = "http://example.com/some-nonexistent-page"

# Пытаемся выполнить GET-запрос к указанному URL
try:
    # Выполняем GET-запрос и проверяем статус ответа
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    # Если запрос прошел успешно, выводим информацию о доступности страницы
    print('Страница доступна: ', url)

# Обработка исключений HTTP ошибок с подробным выводом по коду ошибки
except requests.exceptions.HTTPError as http_err:
    status_code = http_err.response.status_code
    if status_code == 404:
        print(f"Ошибка 404: Страница не найдена по адресу {url}")
    elif status_code ==403:
        print(f"Ошибка 403: Доступ к странице запрещен по адресу {url}")
    elif status_code == 500:
        print(f"Ошибка 500: Внутренняя ошибка сервера по адресу {url}")
    else:
        print(f"Произошла HTTP ошибка {status_code}: {http_err}")

# Обработка ошибок сетевого подключения
except requests.exceptions.ConnectionError:
    print(f"Ошибка подключения: Невозможно подключиться к {url}")

# Обработка таймаута запроса
except requests.exceptions.Timeout:
    print(f"Ошибка: Время ожидания запроса к {url} истекло")

# Общая обработка всех остальных ошибок
except Exception as err:
    print(f"Произошла ошибка: {err}")
