# Обработка ошибок запросов с модулем requests

# Напишите программу, которая отправляет GET-запрос на сервер и обрабатывает возможные ошибки, используя исключения.

# Напишите тут ваш код
import requests

try:
    res = requests.get("http://google.com")
    print(res.headers)
    res.raise_for_status()
except requests.exceptions.RequestException as err:
    print(f"Request error occurred: {err}")
except Exception as err:
    print(f"Other error occurred: {err}")
except:
    print("something wring!")
