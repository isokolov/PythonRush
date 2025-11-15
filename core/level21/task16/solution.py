import pandas as pd
from random import randint


# Генерация тестовых данных для температуры и влажности
def generate_data():
    return {
        'day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        'temperature_source_1': [randint(20, 30) for _ in range(7)],
        'humidity_source_1': [randint(50, 70) for _ in range(7)],
        'temperature_source_2': [randint(20, 30) for _ in range(7)],
        'humidity_source_2': [randint(50, 70) for _ in range(7)]
    }

# Объединение данных


# Запись DataFrame в Excel с отдельными листами по дням
