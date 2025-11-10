# Использованиее метода reduce()

# Напишите класс, который управляет своей сериализацией с помощью метода __reduce__(),
# чтобы при сериализации и десериализации сохранялись только определенные поля.

# Напишите тут ваш код
import pickle

class CustomClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __reduce__(self):
        return self.__class__, (self.name, self.age)

    def __repr__(self):
        return f"CustomClass(name={self.name}, age={self.age})"

obj = CustomClass("John", 25)

data = pickle.dumps(obj)
new = pickle.loads(data)
print(new)
