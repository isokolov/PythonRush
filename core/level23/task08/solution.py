import requests
from bs4 import BeautifulSoup

# Загрузить HTML-страницу
url = "http://example.com"  # Замените на URL вашей страницы
response = requests.get(url)

# Парсить HTML с помощью BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Найти первую ссылку с классом "external-link"
# external_link = soup.find('a', class_='external-link')
external_link = soup.select_one('a.external-link')

# Проверить, что ссылка найдена, и вывести её URL
if external_link:
    print(external_link['href'])
