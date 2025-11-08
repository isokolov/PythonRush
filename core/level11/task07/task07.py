# Использование пакета requests.

# Используйте пакет requests для выполнения GET-запроса к API.
# Выполните следующие шаги:
# Установите пакет requests с помощью pip.
# Используйте пакет requests для выполнения GET-запроса к API, например, к https://jsonplaceholder.typicode.com.
# Выведите на экран результат запроса.

# Напишите тут ваш код
#pip install requests
import requests

response = requests.get("https://jsonplaceholder.typicode.com")
print(response.text)
