# В глубинах самых глубин.

# Напишите программу, которая создает словарь с информацией о человеке (например, имя, возраст, адрес, и контактная информация).
# Программа должна:
# Изменить значения верхнего уровня, вложенного словаря и более глубокого уровня вложенности.
# Добавить новый элемент во вложенный словарь.
# Удалить элемент из вложенного словаря и верхнего уровня.

# Напишите тут ваш код
address = {"city": "LA", "street": "Baker Str. 5"}
contact = {"phone": 12345, "email": "sherlock@gmail.com"}
person = {"name": "Sherlock Holmes", "age": 35, "address": address,
          "contact": contact}

person["age"] = 55
person["contact"]["phone"] = 98765
person["contact"]["index"] = 333
del person["age"]
del person["contact"]["phone"]

print(person)
