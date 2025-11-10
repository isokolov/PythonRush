# Сериализация списка в файл

# Напишите программу, которая сериализует список в файл с использованием модуля pickle,
# а затем десериализует этот список из файла.

import pickle

# Пример списка для сериализации
data = [1, 2, 3, 'a', 'b', 'c']


# Напишите тут ваш код
with open('serialization.bin', 'wb') as file:
    pickle.dump(data, file)

with open('serialization.bin', 'rb') as file:
    serialization_data = pickle.load(file)

print(serialization_data)
