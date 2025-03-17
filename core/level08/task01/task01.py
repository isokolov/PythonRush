# Системные функции.

# Напишите программу, которая создает несколько объектов различных типов и
# использует функции id(), hash(), и dir() для выполнения следующих операций:
# Определить и вывести уникальные идентификаторы объектов с помощью id().
# Вывести хеш-значения хешируемых объектов с помощью hash().
# Вывести список атрибутов и методов объекта с помощью dir().

# Напишите тут ваш код
number = 10
tuple_ = (1, 2, 3)
word = 'Some text'
print(id(number))
print(id(tuple_))
print(id(word))
print(hash(number))
print(hash(tuple_))
print(hash(word))
print(dir(number))
print(dir(tuple_))
print(dir(word))
