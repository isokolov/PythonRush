# Хеш-функция

# Напиши свою хеш-функцию, которая возвращает целое число от 0 до 10к для строки произвольной длинны.

# Напишите тут ваш код
def custom_hash(str_):
    hash_value = 0
    for char in str_:
        hash_value += ord(char)
    return hash_value % 10000
