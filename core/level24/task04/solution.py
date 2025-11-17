import requests
from requests.exceptions import RequestException

# Список фиктивных прокси-серверов
proxies = [
    {"http": "http://123.45.67.89:8080", "https": "https://123.45.67.89:8080"},
    {"http": "http://98.76.54.32:8000", "https": "https://98.76.54.32:8000"},
    {"http": "http://11.22.33.44:3128", "https": "https://11.22.33.44:3128"}
]

# URL для запроса
url = "https://httpbin.org/ip"

# Функция для отправки запроса
def get_ip_via_proxy(proxy):
    try:
        response = requests.get(url, proxies=proxy, timeout=5)
        response.raise_for_status()
        ip = response.json().get("origin")
        return ip
    except RequestException as e:
        return f"Ошибка при запросе через прокси {proxy}: {e}"

# Отправка запросов и вывод результата
for i, proxy in enumerate(proxies, start=1):
    ip = get_ip_via_proxy(proxy)
    print(f"Запрос {i}, IP-адрес, видимый сервером: {ip}")
