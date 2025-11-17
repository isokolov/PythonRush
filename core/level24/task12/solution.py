import requests
import random
import time
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# Укажите свой API-ключ 2Captcha
CAPTCHA_API_KEY = 'YOUR_2CAPTCHA_API_KEY'
# URL целевого сайта
TARGET_URL = 'https://example.com'

# Функция для получения случайного User-Agent
def get_random_user_agent():
    return UserAgent().random

# Функция для добавления случайной задержки
def random_delay():
    delay = random.uniform(2, 5)
    time.sleep(delay)
    print(f"Задержка {delay:.2f} секунд.")

# Функция для запроса решения CAPTCHA
def request_captcha_solution(captcha_site_key, url):
    response = requests.post('http://2captcha.com/in.php', data={
        'key': CAPTCHA_API_KEY,
        'method': 'userrecaptcha',
        'googlekey': captcha_site_key,
        'pageurl': url,
        'json': 1
    }).json()
    return response['request']

# Функция для проверки состояния решения CAPTCHA
def get_captcha_result(captcha_id):
    while True:
        time.sleep(5)
        response = requests.get('http://2captcha.com/res.php', params={
            'key': CAPTCHA_API_KEY,
            'action': 'get',
            'id': captcha_id,
            'json': 1
        }).json()
        if response['status'] == 1:
            return response['request']
        elif response['request'] != 'CAPCHA_NOT_READY':
            raise Exception(f'Ошибка решения CAPTCHA: {response["request"]}')

# Функция для извлечения site-key из HTML
def get_captcha_site_key(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    site_key_element = soup.find('div', {'data-sitekey': True})
    if site_key_element:
        return site_key_element['data-sitekey']
    else:
        raise Exception('Site-key не найден на странице.')

# Основная функция для запроса страницы и решения CAPTCHA
def fetch_page_content():
    session = requests.Session()

    # Первый запрос для получения страницы и site-key
    random_delay()
    headers = {'User-Agent': get_random_user_agent()}
    response = session.get(TARGET_URL, headers=headers)

    # Проверка и решение CAPTCHA при необходимости
    if 'site-key' in response.text:
        captcha_site_key = get_captcha_site_key(response.text)
        print("Решаем CAPTCHA...")

        # Запрос решения CAPTCHA
        captcha_id = request_captcha_solution(captcha_site_key, TARGET_URL)
        captcha_token = get_captcha_result(captcha_id)

        # Повторный запрос с решенной CAPTCHA
        random_delay()
        headers = {'User-Agent': get_random_user_agent()}
        response = session.post(TARGET_URL, data={'g-recaptcha-response': captcha_token}, headers=headers)

    return response.text

# Запуск программы
def main():
    try:
        page_content = fetch_page_content()
        print(page_content)
    except Exception as e:
        print("Произошла ошибка:", e)

main()
