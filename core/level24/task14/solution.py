import random
import requests

# Список прокси-серверов. Для примера указаны фиктивные адреса, замените их на реальные.
proxy_list = [
    'https://114.80.40.128:3081',
    'https://185.252.24.213:3128',
    'https://61.91.202.211:8080'
]

# Случайный выбор прокси-сервера из списка
selected_proxy = random.choice(proxy_list)

# Настройка прокси для библиотеки requests
proxies = {
    'http': selected_proxy,
    'https': selected_proxy
}

# Отправка GET-запроса через выбранный прокси-сервер
response = requests.get( "http://example.com", proxies=proxies)

# Вывод содержимого страницы в консоль
print(response.text)
