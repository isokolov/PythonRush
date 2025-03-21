# Чистим список

# Напишите программу, которая создает список из 10 случайных чисел в диапазоне от 1 до 20.
# Затем программа должна удалить из списка все четные числа с использованием цикла.
# Программа должна вывести исходный и обновленный списки.

# Напишите тут ваш код
from random import randrange

random_list = [randrange(1, 20) for i in range(10)]
new_list = [x for x in random_list if x % 2 == 1]
print(random_list)
print(new_list)