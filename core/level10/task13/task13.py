# Пользовательское исключение

# Создайте пользовательское исключение InvalidAgeError, которое будет вызываться в функции check_age,
# если возраст меньше 0 или больше 150. Обработайте это исключение в блоке try-except.

# Напишите тут ваш код
class InvalidAgeError(Exception):
    pass


def check_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError
    else:
        return age


check_age(55)

try:
    age = int(input("Enter your age: "))
    check_age(age)
    print("Age is valid.")
except InvalidAgeError as e:
    print(e)
except ValueError:
    print("Please enter a valid integer for age.")
