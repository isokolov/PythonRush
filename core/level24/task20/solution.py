from requests_html import HTMLSession
import requests


# Функция для загрузки и рендеринга динамического контента с указанного URL
def fetch_dynamic_content(url):
    session = HTMLSession()
    response = session.get(url)
    response.html.render()  # Нужно для обработки динамического контента
    return response.html.html


# Функция для извлечения данных из HTML-контента
def extract_data_from_html(html_content):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    data = soup.find_all('p', class_='data')
    return [d.text for d in data]


# Функция для отправки данных на указанный API
def send_data_to_api(data, api_url):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(api_url, json=data, headers=headers)
    return response.status_code, response.text


# Основная функция для выполнения всех шагов
def main():
    url = "https://example.com/dynamic-content"  # Замените на реальный URL
    api_url = "https://api.example.com/receive-data"  # Замените на реальный URL API

    # Загружаем динамический контент
    html_content = fetch_dynamic_content(url)

    # Извлекаем данные
    data = extract_data_from_html(html_content)

    # Отправляем данные на API
    status_code, response_text = send_data_to_api(data, api_url)

    print(f"Status Code: {status_code}")
    print(f"Response: {response_text}")


main()
