# Мешанина

# Напишите программу, которая запрашивает у пользователя целое число, вещественное число и строку.
# Затем преобразуйте целое число в вещественное, вещественное число в строку, и строку в целое число (если это возможно).
# Выведите результаты преобразований и их типы.

# Напишите тут ваш код
num1 = int(input("Enter integer number: "))
num2 = float(input("Enter float number: "))
str1 = input("Enter string: ")
num1 = float(num1)
num2 = str(num2)
str1 = int(str1)
print(type(num1))
print(type(num2))
print(type(str1))