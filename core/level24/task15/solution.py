import requests

# URL целевой страницы и список прокси-серверов
url = "http://example.com"
proxy_list = [
    "https://41.57.6.30:6060",
    "https://190.94.212.249:999",
    "https://158.69.185.37:3129",
]

# Проходим по каждому прокси из списка
for proxy in proxy_list:
    try:
        proxies = {
            'http' : proxy,
            'https' : proxy,
        }

        response = requests.get(url, proxies=proxies, timeout=5)

        if response.status_code == 200:
            print(response.text)
            break
    except requests.RequestException:
        print(f"Прокси {proxy} недоступен, пробуем следующий...")

# Если ни один прокси не сработал, выводим сообщение о неудаче
else:
    print("Запрос не удался")
