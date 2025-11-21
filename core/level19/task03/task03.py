# Сумма чисел

# Найти два числа в отсортированном массиве, которые в сумме дают заданное число target


def find_two_numbers(arr, target):
# Напишите тут ваш код


# Пример использования
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10
result = find_two_numbers(sorted_array, target)
if result:
    print(f"Сумма чисел {result[0]} и {result[1]} равна {target}")
else:
    print(f"Пары чисел, дающих в сумме {target}, не найдено")\
