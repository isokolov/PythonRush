import csv

# Определяем имя файла, с которым будем работать
filename = 'students.csv'

# Создаем пустой список для хранения информации о студентах
studs = []

# Чтение данных студентов из CSV-файла
with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
    # Создаем объект csvreader для чтения строк из файла
    csvreader = csv.DictReader(csvfile)

    for row in csvreader:
        # Проверяем, что в строке ровно 3 элемента (имя, возраст, курс)
        if len(row.keys())==3:
            studs.append(row)
            # Добавляем данные студента в список в виде словаря

# Пример добавления нового студента
studs.append({'name': 'Alice', 'age': '25', 'course': 'Biology'})

# Запись обновленных данных студентов в CSV-файл
with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
    # Создаем объект csvwriter для записи строк в файл
    writer = csv.DictWriter(csvfile, fieldnames=['name','age','course'])
    writer.writeheader()
    writer.writerows(studs)

    # Записываем данные каждого студента в файл
