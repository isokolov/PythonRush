# Бесконечность не предел.

# Напишите программу, которая принимает произвольное количество чисел и выводит их сумму.
# Программа должна:
# Определить функцию sum_numbers(*args), которая принимает произвольное количество чисел.
# Вычислить сумму всех переданных чисел.
# Вывести результат.

# Напишите тут ваш код
def sum_numbers(*args):
    return sum(args)


print(sum_numbers(1, 2, 3))