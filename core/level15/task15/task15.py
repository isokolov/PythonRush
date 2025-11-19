# Подсчет времени сортировки

# Напиши программу, которая будет считать сколько будет длиться сортировка 1 млрд. чисел тремя алгоритмами.
# Сложность первого алгоритма 100*n*ln(n).
# Сложность второго алгоритма 10*n^2.
# Сложность третьего алгоритма n^3.
# Выведите три этих числа на экран.

# Напишите тут ваш код
import numpy as np
import time

n = 10 ** 9

# x1 = 100 * x * np.log(x)
# x2 = 10 * x ** 2
# x3 = x ** 3

t_n1 = time.time()
#for x_ in range(1,n):
x1 = 100 * n * np.log(n)
t_f1 = time.time()
print(t_f1 - t_n1)
print(x1)

t_n2 = time.time()
#for x_ in range(1,n):
x2 = 10 * n ** 2
t_f2 = time.time()
print(t_f2 - t_n2)
print(x2)

t_n3 = time.time()
#for x_ in range(1,n):
x3 = n ** 3
t_f3 = time.time()
print(t_f3 - t_n3)
print(x3)
