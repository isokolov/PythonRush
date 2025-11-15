import requests

# Пример: предполагается, что вы уже получили cookies из вкладки Application в DevTools
cookies = {
    'PHPSESSID': 'NW8TwlaiX5pwhnzA7iMPBiprwlPlb2LL',
    # 'auth_token': 'your_auth_token'
}

# URL защищенной страницы
url = 'https://vitaminsan.ru/order/'


# Отправка GET-запроса с cookies
# response = requests.get(url, cookies=cookies) # рабочий вариант
headers = {'Cookie': 'PHPSESSID=NW8TwlaiX5pwhnzA7iMPBiprwlPlb2LL'}
response = requests.get(url, headers=headers, cookies=cookies)

# Проверка успешности запроса
if response.status_code == 200:
    # Вывод данных на экран
    print("Данные с защищенной страницы:")
    print(response.text)
else:
    print("Не удалось получить доступ к защищенной странице. Код ошибки:", response.status_code)
