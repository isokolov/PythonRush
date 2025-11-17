from requests_html import HTMLSession

# URL страницы с новостными элементами (замените 'your_url_here' на фактический URL)
url = 'https://example.com/infinite-scroll'

# Создаем сессию для выполнения HTTP-запросов и рендеринга
session = HTMLSession()
response = session.get(url)

# Выполняем прокрутку страницы для подгрузки контента
response.html.render(scrolldown=5, sleep=1)

# Извлекаем текст элементов с классом 'news-item'
news_items = response.html.find('.news-item')

for new_item in news_items:
    print(new_item.text)
