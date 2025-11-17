from bs4 import BeautifulSoup

# Открываем HTML файл и читаем его содержимое
with open('document.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создаем объект BeautifulSoup для парсинга HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Находим первый элемент <p>
p = soup.find('p')

# Извлекаем и выводим текстовое содержимое найденного элемента <p>
print(p.text)
