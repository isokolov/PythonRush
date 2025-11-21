# Выбор среднего элемента

# Добавь в функцию quick_sort возможность передавать способ выбора среднего значение через lambda-функцию.
# Предложи 5 вариантов выбора среднего числа для быстрой сортировки.

# Напишите тут ваш код

def quick_sort(arr, pivot_selection):
# Напишите тут ваш код

# 5 вариантов выбора функции pivot_selection
# 1. Первый элемент
pivot_first = lambda arr: arr[0]

# 2. Последний элемент
pivot_last = # Напишите тут ваш код

# 3. Средний элемент
pivot_middle = # Напишите тут ваш код

# 4. Случайный элемент
import random
pivot_random = # Напишите тут ваш код

# 5. Среднее арифметическое из трех: первый, последний и средний
pivot_median_three = # Напишите тут ваш код

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
print(quick_sort(arr, pivot_first))
print(quick_sort(arr, pivot_last))
print(quick_sort(arr, pivot_middle))
print(quick_sort(arr, pivot_random))
print(quick_sort(arr, pivot_median_three))
