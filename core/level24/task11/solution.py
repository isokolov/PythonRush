import requests

# Задаем URL для проверки IP-адреса
url = 'http://httpbin.org/ip'

# Список прокси-серверов
proxies = [
    {'http': 'http://ip1:port', 'https': 'http://ip1:port'},
    {'http': 'http://ip2:port', 'https': 'http://ip2:port'},
    {'http': 'http://ip3:port', 'https': 'http://ip3:port'}
]

# Проходим по каждому прокси из списка
for proxy in proxies:
    try:
        # Печатаем используемый прокси-сервер
        print(f"Использование прокси: {proxy['http']}")

        # Выполняем GET-запрос к URL с указанным прокси
        response = requests.get(url, proxies=proxy, timeout=5)

        # Проверяем статус ответа
        print(f"HTTP-статус: {response.status_code}")

        # Если статус успешен, выводим IP-адрес, с которого был выполнен запрос
        if response.status_code == 200:
            print(f"IP-адрес: {response.json()['origin']}")
        else:
            print("Ошибка получения данных от httpbin.org")

    # Обрабатываем возможные ошибки запроса
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
