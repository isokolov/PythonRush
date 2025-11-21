# Случайный миллион

# Создайте массив из 1 миллиона элементов случайных значений.
# Используйте функции merge_sort и quick_sort для сортировки значений.
# Выедите результаты на экран.


import random
import time

# Генерация массива из 1 миллиона случайных значений
array = [random.randint(0, 1000000) for _ in range(1000000)]

# Реализация функции merge_sort
def merge_sort(arr):
# Напишите тут ваш код

# Реализация функции quick_sort
def quick_sort(arr):
# Напишите тут ваш код

# Сортировка и вывод времени выполнения для merge_sort
start_time = time.time()
sorted_array_merge = merge_sort(array.copy())
merge_sort_time = time.time() - start_time
print(f"Merge Sort Time: {merge_sort_time} seconds")

# Сортировка и вывод времени выполнения для quick_sort
start_time = time.time()
sorted_array_quick = quick_sort(array.copy())
quick_sort_time = time.time() - start_time
print(f"Quick Sort Time: {quick_sort_time} seconds")
