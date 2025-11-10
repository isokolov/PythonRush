# Сериализация словаря в строку

# Напишите программу, которая сериализует словарь в строку с использованием модуля pickle,
# а затем десериализует этот словарь из строки.

import pickle

# Пример словаря для сериализации
data = {
    'name': 'Alice',
    'age': 30,
    'city': 'Wonderland'
}


# Напишите тут ваш код
serialization_data = pickle.dumps(data)

load_data = pickle.loads(serialization_data)

print(load_data)
