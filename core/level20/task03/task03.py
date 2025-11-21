# Профилирование

# Определите узкие места в производительности кода с использованием модуля cProfile и оптимизируйте наиболее затратные по времени функции.

# Подсказка: Используйте профилирование, чтобы понять, какие части вашего кода занимают больше всего времени, и оптимизируйте их.


import cProfile

def example_function():
    total = 0
    for i in range(10000):
        total += i
    return total

def optimized_example_function():
# Напишите тут ваш код


# Профилирование исходной функции
print("Profiling example_function:")
cProfile.run('example_function()')

# Профилирование оптимизированной функции
print("Profiling optimized_example_function:")
cProfile.run('optimized_example_function()')
