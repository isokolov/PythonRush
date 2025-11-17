import requests
import time
from itertools import cycle

# Функция для загрузки списка прокси из файла
def load_proxies(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

# Функция для отправки тестового запроса для проверки доступности прокси
def send_test_request(proxy_url):
    try:
        response = requests.get('http://example.com', proxies={"http": proxy_url, "https": proxy_url}, timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False

# Функция для фильтрации доступных прокси
def filter_available_proxies(proxies):
    return [proxy for proxy in proxies if send_test_request(proxy)]

# Функция для записи успешного запроса в лог
def log_request(proxy, log_filename):
    with open(log_filename, 'a') as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {proxy}\n")

# Функция для выполнения запроса через определенный прокси и логирования его результата
def make_request_with_proxy(url, proxy, log_filename):
    try:
        response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            print(f"Страница успешно получена с использованием прокси {proxy}")
            log_request(proxy, log_filename)
            return True
    except requests.RequestException:
        print(f"Не удалось получить страницу с использованием прокси {proxy}. Переходим к следующему прокси.")
    return False

# Основная функция для управления прокси-пулом и отправки запросов
def send_requests_with_proxy_pool(proxies, url, log_filename, request_limit=5):
    proxy_pool = cycle(proxies)
    for _ in range(request_limit):
        proxy = next(proxy_pool)
        if make_request_with_proxy(url, proxy, log_filename):
            continue

# Главная функция программы
def main():
    filename = 'proxies.txt'
    log_filename = 'requests_log.txt'
    url = "http://example.com"

    # Шаг 1: Загрузить прокси из файла
    proxies = load_proxies(filename)

    # Шаг 2: Фильтрация доступных прокси
    available_proxies = filter_available_proxies(proxies)

    # Шаг 3: Отправка запросов через прокси-пул
    send_requests_with_proxy_pool(available_proxies, url, log_filename)

# Запускаем основную функцию
main()
