# Извлечение информации из исключения

# Напишите функцию read_integer, которая принимает строку и пытается преобразовать её в целое число.
# Если возникает ValueError, обработайте исключение и выведите аргументы ошибки и тип ошибки.
# Дополнительно, сохраните исключение в переменной и выведите её за пределами блока except.

# Напишите тут ваш код
def read_integer(i):
    try:
        return int(i)
    except ValueError as e:
        exception = e
        print(f"Error {e.args} of type {type(e)}")

    print(exception)


read_integer("25")
read_integer("25d")
