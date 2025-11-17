import requests
from bs4 import BeautifulSoup

# URL-адрес для извлечения данных
url = "http://example.com"

# Выполняем GET-запрос к указанному URL
response = requests.get(url)

# Парсим HTML-документ с помощью BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

soup_title = soup.find('h1')
print(soup_title.getText())
print(soup_title.find_next('p').text)


soup_title = soup.find('h2')
print(soup_title.getText())
print(soup_title.find_next('p').text)

soup_title = soup.find('h3')
print(soup_title.getText())
print(soup_title.find_next('p').text)



# tags = ['h1', 'h2', 'h3', 'p']
# for child in soup.recursiveChildGenerator():
#     if child.name in tags:
#         print(child.text)




# h1 = soup.h1
# print(h1.text)
#
# h1_childs = [e.name for e in h1.descendants if e.name is not None]
# for h1_child in h1_childs:
#     print(h1_childs.text)




# Извлекаем и выводим все заголовки (h1, h2, h3)
for heading in soup.find_all(['h1', 'h2', 'h3']):
    # Получаем текст заголовка и выводим его
    print(heading.get_text())

# Извлекаем и выводим содержимое всех параграфов
for paragraph in soup.find_all('p'):
    # Получаем текст параграфа
    paragraph_text = paragraph.get_text()
    # Выводим текст только если он превышает 100 символов
    if len(paragraph_text) > 100:
        print(paragraph_text)

