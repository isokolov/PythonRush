# Сортировки

# Напишите программу, которая создает список из 10 случайных чисел в диапазоне от 1 до 100.
# Затем сортирует его по возрастанию и убыванию.
# Программа должна вывести исходный список, отсортированный по возрастанию и по убыванию списки.

# Напишите тут ваш код
from random import randrange

random_list = [randrange(1, 100) for i in range(10)]
sorted_asc = sorted(random_list)

sorted_desc = sorted(random_list)
sorted_desc.sort(reverse=True)
print(random_list)
print(sorted_asc)
print(sorted_desc)