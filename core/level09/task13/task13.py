# Домашние животные.

# Напишите функцию check_type для проверки, является ли переданный объект экземпляром класса Animal или его подклассов.
# Используйте функцию isinstance() для выполнения проверки.
# Затем создайте классы Animal, Dog, Cat и проверьте несколько объектов.

# Напишите тут ваш код
def check_type(obj):
    return isinstance(obj, Animal)
class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

cat = Cat()
dog = Dog()
animal = Animal()
print(check_type(cat))
print(check_type(dog))
print(check_type(animal))
