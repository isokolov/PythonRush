# Декоратор.

# Напишите программу, которая создает простой декоратор для логирования вызовов функции.
# Программа должна:
# Определить декоратор log_decorator, который выводит сообщение перед и после вызова функции.
# Применить декоратор к функции greet(), которая выводит приветственное сообщение.
# Вызвать функцию greet().

# Напишите тут ваш код
def log_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@log_decorator
def greet():
    print("Hello, Russian")

greet()
