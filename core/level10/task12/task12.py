# Переупаковка исключения

# Напишите функцию validate_input, которая принимает строку и проверяет,
# что она не пустая и что ее длина не превышает 10 символов.
# Если строка пустая, запустите ValueError с сообщением "Input cannot be empty".
# Если строка слишком длинная, запустите ValueError с сообщением "Input is too long".
# Затем перехватите это исключение и переупакуйте его в пользовательское исключение InputValidationError, сохранив исходное исключение как причину.

# Напишите тут ваш код
class InputValidationError(Exception):
    original_exception = Exception()

def validate_input(s):
    try:
        if not s:
            raise ValueError("Input cannot be empty")
        elif len(s) > 10:
            raise ValueError("Input is too long")
        else:
            return s
    except ValueError as e:
        raise InputValidationError() from e
# Пример использования:
try:
    validate_input("sss")
    validate_input("")
    validate_input("dsfdsdfsdfsdfsdf")
except ValueError as e:
    print(f"{e}")

