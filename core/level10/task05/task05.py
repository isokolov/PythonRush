# Обработка исключений.

# Напишите функцию safe_division, которая принимает два числа и выполняет их деление.
# Обработайте исключения, которые могут возникнуть при делении на ноль
# и при передаче некорректных значений (например, строки вместо чисел).
# Функция должна возвращать сообщение об ошибке или результат деления.

# Напишите тут ваш код
def safe_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed."
    except TypeError:
        return "Only numbers are allowed"
    else:
        return result

print(safe_division(3, 4))
print(safe_division(3, 'a'))
print(safe_division(3, 0))
print(safe_division(30, 3))
