# Запуск стандартного исключения

# Напишите функцию check_positive, которая принимает число и проверяет, является ли оно положительным.
# Если число отрицательное или равно нулю, функция должна запустить исключение ValueError с сообщением "Number must be positive".

# Напишите тут ваш код
def check_positive(number):
    if number <= 0:
        raise ValueError("Number must be positive")
    return number
