# Иерархия пользовательских исключений

# Создайте базовый класс исключений ApplicationError и два подкласса NegativeValueError и ValueTooLargeError.
# Реализуйте функцию check_number, которая будет вызывать соответствующее исключение, если число отрицательное или слишком большое.
# Обработайте исключения в блоке try-except.

# Напишите тут ваш код
class ApplicationError(Exception):
    pass


class NegativeValueError(ApplicationError):
    pass


class ValueTooLargeError(ApplicationError):
    pass


def check_number(num):
    if num < 0:
        raise NegativeValueError
    elif num > 100:
        raise ValueTooLargeError
    else:
        return num


try:
    nm = int(input())
    check_number(nm)
except NegativeValueError as e:
    print(f"{e}")
except ValueTooLargeError as e:
    print(f"{e}")
