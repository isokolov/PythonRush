# Круглый математик

# Напишите программу, которая запрашивает у пользователя вещественное число и округляет
# его вниз (с использованием math.floor()),
# вверх (с использованием math.ceil()) и до ближайшего целого числа (с использованием round()).
# Выведите результаты всех трех округлений.

# Напишите тут ваш код
import math

number = float(input("Enter a float number: "))
print(math.floor(number))
print(math.ceil(number))
print(round(number))