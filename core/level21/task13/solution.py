import pandas as pd

# Создание DataFrame с данными о студентах
data = {
    'Имя студента': ['Иванов', 'Петров', 'Сидоров'],
    'Средний балл': [4.5, 3.7, 4.2]
}
df = pd.DataFrame(data)

# Запись DataFrame в Excel-файл без индексов
df.to_excel("students.xlsx",sheet_name="Группа 1",index=False)
