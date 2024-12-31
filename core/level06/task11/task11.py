# Индексация

# Напишите программу, которая создает множество из случайных чисел в диапазоне от 1 до 50.
# Затем программа должна вывести все элементы множества вместе с их "индексами", используя функцию enumerate().

# Напишите тут ваш код
from random import randint

my_set = {randint(1, 50) for i in range(20)}
for index, value in enumerate(my_set):
    print(f"index: {index} value: {value}")