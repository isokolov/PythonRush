# Машины.

# Создайте базовый класс Vehicle, который будет иметь атрибут brand.
# Затем создайте два дочерних класса Car и Motorcycle, которые будут наследовать от Vehicle
# и добавлять свои уникальные атрибуты и методы.
# Например, класс Car может иметь метод drive, а класс Motorcycle — метод ride.



class Vehicle:
    def __init__(self, brand):
        self.brand = brand

# Напишите тут ваш код
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is driving.")

class Motorcycle(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def ride(self):
        print(f"{self.brand} {self.model} is riding.")

# Примеры использования классов:
car = Car("Toyota", "Corolla")
print(car.drive())  # Output: Toyota Corolla is driving.

motorcycle = Motorcycle("Yamaha", "R1")
print(motorcycle.ride())  # Output: Yamaha R1 is riding.
