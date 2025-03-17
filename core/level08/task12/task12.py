# Длительность работы.

# Напишите программу, которая создает декоратор для измерения времени выполнения функции.
# Программа должна:
# Определить декоратор time_decorator, который измеряет и выводит время выполнения функции.
# Применить декоратор к функции compute_square(n), которая вычисляет квадрат числа и имитирует задержку с помощью time.sleep().
# Вызвать функцию compute_square(n).

# Напишите тут ваш код
import time
# print(time.mktime())


def time_decorator(func):
    def wrap(n):
        t1 = time.time()
        func(n)
        t2 = time.time()
        print(t2 - t1)

    return wrap


@time_decorator
def compute_square(n):
    time.sleep(1)
    return n ** 2


compute_square(5)