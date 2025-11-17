import requests
import base64
import time

# Указываем API-ключ для сервиса 2Captcha и URL изображения CAPTCHA
API_KEY = 'ВАШ_API_КЛЮЧ_2CAPTCHA'  # Замените на ваш реальный API-ключ
CAPTCHA_URL = 'https://rucaptcha.com/auth/register'  # Замените на реальный URL изображения CAPTCHA

# Загружаем изображение CAPTCHA
captcha_image = requests.get(CAPTCHA_URL).content

# Кодируем изображение CAPTCHA в base64
captcha_base64 = base64.b64encode(captcha_image).decode('utf-8')

# Отправляем изображение на решение в сервис 2Captcha
response = requests.post(
    'http://2captcha.com/in.php',
    data={
        'key': API_KEY,
        'method': 'base64',
        'body': captcha_base64,  # Передаем закодированное изображение CAPTCHA в base64
        'json': 1  # Запрашиваем ответ в формате JSON
    }
)

# Получаем идентификатор запроса для решения CAPTCHA
request_id = response.json().get('request')

# Начинаем цикл проверки статуса решения CAPTCHA
while True:
    # Отправляем запрос на проверку статуса решения
    result = requests.get(f'http://2captcha.com/res.php?key={API_KEY}&action=get&id={request_id}&json=1').json()

    # Если CAPTCHA решена, выводим решение
    if result.get('status') == 1:
        captcha_solution = result.get('request')
        print("Решение CAPTCHA:", captcha_solution)
        break
    # Если решение еще не готово, ждем 5 секунд и повторяем запрос
    elif result.get('request') == 'CAPCHA_NOT_READY':
        time.sleep(5)
    # Если произошла ошибка, выводим сообщение и прекращаем выполнение
    else:
        raise Exception('Ошибка при решении CAPTCHA: ' + result.get('request'))
