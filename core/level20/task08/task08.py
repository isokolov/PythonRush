# Параллельный факториал

# Напишите программу, которая использует параллельное программирование для вычисления факториала большого числа.
# Разделите задачу на несколько процессов, каждый из которых будет вычислять часть произведения.
# Подсказка: Используйте модуль multiprocessing в Python для создания нескольких процессов.
# Разделите задачу вычисления факториала на подзадачи, каждая из которых будет вычислять произведение своего подотрезка.


import multiprocessing
from functools import reduce
from operator import mul

def partial_factorial(start, end):
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result

def factorial(n, num_processes):
    if n == 0 or n == 1:
        return 1

# Напишите тут ваш код


if __name__ == '__main__':
    number = 100000  # Example large number
    num_processes = 4  # Number of processes to use
    result = factorial(number, num_processes)
    print(f"The factorial of {number} is {result}")
