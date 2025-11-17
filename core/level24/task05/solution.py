from requests_html import HTMLSession

# Запрашиваем у пользователя URL веб-страницы
url = input("Введите URL веб-страницы: ")

# Создаем сессию для выполнения HTTP-запросов
session = HTMLSession()

# Пытаемся выполнить запрос к указанной веб-странице и извлечь заголовок
try:
    # Выполняем GET-запрос к веб-странице
    response = session.get(url)

    # Ищем элемент заголовка (тег <title>) на странице
    # response.html.encoding = 'windows-1251'
    title = response.html.find('title', first=True)

    # Проверяем, найден ли элемент заголовка
    if title:
        # Если заголовок найден, выводим его текст
        print(title.text)
        # Если заголовок не найден, выводим сообщение
    else:
        print('Заголовок не найден.')

# Обработка ошибок при запросе или парсинге
except Exception as e:
    print("Произошла ошибка:", e)
