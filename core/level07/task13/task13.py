# Обход словаря.

# Напишите программу, которая создает словарь с информацией о человеке (например, имя, возраст, адрес, и контактная информация).
# Программа должна:
# Перебрать все элементы словаря, включая вложенные словари, с использованием циклов.
# Реализовать функцию для обхода всех уровней вложенности и вывода ключей и значений.

# Напишите тут ваш код
address = {"city": "LA", "street": "Baker Str. 5"}
contact = {"phone": 12345, "email": "sherlock@gmail.com"}
person = {"name": "Sherlock Holmes", "age": 35, "address": address,
          "contact": contact}
def round_dict(item):
    for key, value in item.items():  # Обходим родительский словарь
        if isinstance(value, dict):  # Если значение - это словарь
            for key2, value2 in value.items():  # Обходим элементы дочернего словаря
                print(f"{key} --> {key2}: {value2}")
round_dict(person)