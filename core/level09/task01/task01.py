# Создаем объекты.

# Создайте класс Car с атрибутами make, model и year.
# Добавьте метод display_info(), который выводит информацию о машине.
# Затем создайте объект этого класса и вызовите метод display_info().

# Напишите тут ваш код
class Car:
    make = 'Japan'
    model = 'Honda'
    year = 1988

    def display_info(self):
        print(f"Made in {self.make}, model {self.model} and year {self.year}")

car = Car()
car.display_info()
