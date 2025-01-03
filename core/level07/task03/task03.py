# Проверка на пустоту.

# Напишите программу, которая создает несколько словарей с различным количеством элементов.
# Программа должна:
# Вывести количество элементов в каждом словаре.
# Проверить, пустой ли каждый словарь, и вывести соответствующее сообщение.
# Для проверки пустоты словаря нужно создать функцию check_empty

# Напишите тут ваш код
def check_empty(some_dict):
    if len(some_dict) == 0:
        print("Dictionary is empty")
    else:
        print("Dictionary is not empty")

dict1 = {"name": "JJ", "age": 12}
dict2 = {"test": 1, "test2": 2}
print(len(dict1))
check_empty(dict1)
print(len(dict2))
check_empty(dict2)