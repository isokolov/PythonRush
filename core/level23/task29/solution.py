from bs4 import BeautifulSoup

# Путь к HTML-файлу, который будем анализировать
file_path = "example.html"  # Укажите путь к вашему HTML-файлу

with open(file_path,'r',encoding='utf-8') as file:
    html_file = file.read()
soup = BeautifulSoup(html_file,'html.parser')
zag = soup.find('table').find('tr')
header = []
for th in zag.find_all('th'):
    header.append(th.text.strip())

print(header)
