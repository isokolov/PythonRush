from bs4 import BeautifulSoup

# Открываем и читаем HTML файл
with open('src/ru/javarush/python/core/level22/task24/index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Парсим содержимое HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Находим все элементы input, у которых атрибут 'name' содержит 'user'
user_inputs = soup.find_all('input', attrs={'name': lambda x: x and 'user' in x.lower()})

# Извлекаем и выводим значения найденных элементов input
print("Найденные поля с 'user' в атрибуте name:")
for input_tag in user_inputs:
    name = input_tag.get('name', '')
    value = input_tag.get('value', '')
    input_type = input_tag.get('type', 'text')
    print(f" - Поле: name='{name}', type='{input_type}', value='{value}'")
