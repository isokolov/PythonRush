# Сортировка без сортировки

# Напишите программу, которая создает список из 10 случайных чисел в диапазоне от 1 до 100.
# Затем программа должна создать копию этого списка и отсортировать копию по возрастанию, не изменяя исходный список.
# Программа должна вывести исходный и отсортированный списки.

# Напишите тут ваш код
from random import randrange

random_list = [randrange(1, 100) for i in range(10)]
copy_list = sorted(random_list)
print(random_list)
print(copy_list)