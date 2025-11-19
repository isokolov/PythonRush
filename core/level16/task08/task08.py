# Хеш-функция для словаря

# Напиши свою хеш-функцию, которая возвращает целое число от 0 до 10к для словаря с произвольными элементами.

# Напишите тут ваш код
def custom_hash(dic_):
    hash_value = 0
    for items,val in dic_.items():
        for char in str(items):
            hash_value += ord(char)
        for ch in str(val):
            hash_value += ord(ch)
    return hash_value % 10000
