# Перегрузка операторов сравнения

# Напишите класс Person, который будет представлять человека с атрибутами name и age.
# Реализуйте перегрузку операторов сравнения == и < для сравнения людей по возрасту.

# Напишите тут ваш код
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age


    def __lt__(self, other):
        return self.age < other.age

