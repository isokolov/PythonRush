# Многократый декоратор.

# Напишите программу, которая создает декоратор для повторного вызова функции заданное количество раз.
# Программа должна:
# Определить декоратор repeat(num_times), который принимает количество повторов в качестве аргумента.
# Применить декоратор к функции say_hello(name), которая выводит приветственное сообщение.
# Вызвать функцию say_hello(name).

# Напишите тут ваш код
def repeat(num_times):
    def internal(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)

        return wrapper

    return internal

@repeat(num_times=4)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("John Wick")
