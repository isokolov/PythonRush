# Сравнивать очень просто

# Напишите программу, которая запрашивает у пользователя два вещественных
# числа и сравнивает их с использованием допустимой погрешности epsilon.
# Выведите результат сравнения на экран.

# Напишите тут ваш
number1 = float(input("Enter a float number: "))
number2 = float(input("Enter a float number: "))

if abs(number1 - number2) < 0.00001:
    print(True)
else:
    print(False)