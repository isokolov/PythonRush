from requests_html import HTMLSession

# Указываем URL динамической страницы и CSS селектор для извлечения
url = 'https://example.com/dynamic-page'  # Пример URL
selector = '.list-item'  # Пример CSS селектор элемента, который необходимо извлечь
selector = 'h1'

# Создаем новую сессию для выполнения HTTP-запросов
session = HTMLSession()

# Отправляем GET-запрос к указанному URL
response = session.get(url)

# Выполняем JavaScript на странице, чтобы загрузить динамические данные
response.html.render()

# Извлекаем элементы по указанному CSS селектору
data = response.html.find(selector)

# Проходим по каждому найденному элементу и выводим его текстовое содержимое
for d in data:
    print(d.text)
