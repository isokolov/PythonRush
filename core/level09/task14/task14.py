# Автопарк.

# Напишите функцию check_subclass для проверки, является ли один класс подклассом другого.
# Используйте функцию issubclass() для выполнения проверки.
# Затем создайте классы Vehicle, Car, Bicycle, и проверьте, являются ли Car и Bicycle подклассами Vehicle.

# Напишите тут ваш код
def check_subclass(cls1, cls2):
    return issubclass(cls1, cls2)

class Vehicle:
    pass

class Car(Vehicle):
    pass

class Bicycle:
    pass

print(check_subclass(Car, Vehicle))
print(check_subclass(Vehicle, Vehicle))
print(check_subclass(Bicycle, Vehicle))
