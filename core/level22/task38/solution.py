import requests

# URL первого AJAX-запроса, скопированный из вкладки Network DevTools
url = 'https://openweathermap.org/themes/openweathermap/assets/js/smart_banner_android.js'

# Выполнение HTTP-запроса
response = requests.get(url)

# Вывод статус-кода ответа
print("Статус-код ответа:", response.status_code)
