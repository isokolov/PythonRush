# Фильтрация

# Напишите программу, которая создает список из 20 случайных чисел в диапазоне от 1 до 100 с использованием List Comprehension.
# Затем с использованием List Comprehension создает новый список, содержащий только четные числа из исходного списка.
# Программа должна вывести оба списка.

# Напишите тут ваш код
from random import randrange

random_list = [randrange(1, 100) for i in range(20)]
even_list = [x for x in random_list if x % 2 == 0]
print(random_list)
print(even_list)