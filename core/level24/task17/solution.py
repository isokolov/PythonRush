from requests_html import HTMLSession

# URL страницы с динамическим контентом, загружаемым через JavaScript
url = 'https://your-example-website.com/path-to-page-with-dynamic-content'

# Создаем сессию для выполнения HTTP-запросов и рендеринга
session = HTMLSession()
response = session.get(url)

# Выполняем JavaScript на странице для загрузки динамического контента
response.html.render()

# Извлекаем текст из элемента с id 'dynamic-content'
content = response.html.find('#dynamic-content', first=True)

# Выводим извлеченный динамический контент
print(content.text)
