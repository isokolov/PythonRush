# Настоящий массив.

# Создай массив с использованием библиотеки array.
# Добавь в него 10 случайных чисел от 0 до 1000. Отсортируй и выведи на экран.
# Класс list использовать нельзя.

# Напишите тут ваш код
# Write your code here
import array as arr
import random

my_arr = arr.array("i", [])
for i in range(10):
    my_arr.append(random.randint(0, 1000))

sorted_arr = arr.array("i", sorted(my_arr))
print(sorted_arr)
