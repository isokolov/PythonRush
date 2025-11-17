import requests

# Укажите адрес и порт вашего прокси-сервера в этой переменной
proxy = "http://101.96.117.169:1080"

# Настройки прокси
proxies = {
    "http": proxy,
    "https": proxy
}

# Выполнение GET-запроса к сайту "http://example.com" с использованием прокси
response = requests.get("http://example.com", proxies=proxies)

# Проверка успешности запроса
response.raise_for_status()

# Вывод содержимого страницы
print(response.text)
