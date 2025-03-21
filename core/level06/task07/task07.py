# Случайные множества

# Напишите программу, которая сгенерирует:
# Один список случайных элементов от 0 до 99.
# Второй список случайных элементов от 50 до 125.
# Затем преобразуйте списки во множества.
# Добавьте первое множество ко второму.
# Выведите количество элементов полученного множества на экран.

# Напишите тут ваш код
from random import randint
list1 = [randint(0, 99) for i in range(20)]
list2 = [randint(50, 125) for i in range(20)]
set1 = set(list1)
set2 = set(list2)
set_combined = set1 | set2
print(len(set_combined))
print(set_combined)