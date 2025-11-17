from bs4 import BeautifulSoup
import csv

# Загрузка HTML-файла
with open('products.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создание объекта BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Настройка CSS-селекторов для извлечения данных
products = soup.select('.product')

# Извлечение данных
results = []
for product in products:
    product_name = product.select_one('.product-name').get_text(strip=True)
    product_price = product.select_one('.product-price').get_text(strip=True)
    print(f'Product: {product_name}, Price: {product_price}')
    results.append((product_name, product_price))


# Экспорт данных в CSV
with open('products.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Product Name', 'Price'])
    for name, price in results:
        csv_writer.writerow([name, price])
