# Считаем деньги

# Напишите программу, которая запрашивает у пользователя числа и суммирует их, пока пользователь не введет отрицательное число.
# Используйте цикл while и оператор break для завершения ввода при отрицательном числе.

# Напишите тут ваш код
number = int(input("Enter a number: "))
sum = number
while number >= 0:
    number = int(input("Enter a number: "))
    if number >= 0:
        sum += number
    else:
        break
print("sum", sum)