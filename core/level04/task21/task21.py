# Суммируем все числа

# Напишите функцию sum_numbers(*args: int) -> int, которая принимает произвольное количество целых чисел в качестве аргументов и возвращает их сумму.
# Затем напишите программу, которая вызывает эту функцию с различными наборами аргументов и выводит результат.

# Напишите тут ваш код
def sum_numbers(*args: int) -> int:
    sums = 0
    for x in args:
        sums += x
    return sums

print(sum_numbers(3, 4, 5))
