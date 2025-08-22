# Супермашины.

# Создайте базовый класс Vehicle, который будет иметь атрибуты brand и model.
# Затем создайте дочерний класс Car, который будет наследовать от Vehicle и добавлять атрибут fuel_type.
# Используйте метод super() для вызова конструктора базового класса.

# Напишите тут ваш код
# Машины.

# Создайте базовый класс Vehicle, который будет иметь атрибут brand.
# Затем создайте два дочерних класса Car и Motorcycle, которые будут наследовать от Vehicle
# и добавлять свои уникальные атрибуты и методы.
# Например, класс Car может иметь метод drive, а класс Motorcycle — метод ride.



class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Напишите тут ваш код
class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
