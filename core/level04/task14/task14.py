# Случайный аргумент

# Напишите функцию  print_random(a,b,c), которая выводит на экран случайно выбранный переданный аргумент.

# Напишите тут ваш
import random
def print_random(a,b,c):
    print(random.choice([a, b, c]))

print_random(1, 2, 3)