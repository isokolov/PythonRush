# Множество декораторов.

# Напишите программу, которая использует несколько декораторов для одной функции.
# Программа должна:
# Определить два декоратора decorator1 и decorator2, которые логируют свои вызовы.
# Применить оба декоратора к функции say_hello.
# Вызвать функцию say_hello.

# Напишите тут ваш код
def decorator1(func):
    def wrapper():
        print("Декоратор 1")
        func()

    return wrapper

def decorator2(func):
    def wrapper():
        print("Декоратор 2")
        func()

    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello!")

say_hello()
