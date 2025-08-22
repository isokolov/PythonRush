# Фигуры.

# Создайте базовый класс Shape, который будет иметь метод area для вычисления площади.
# Затем создайте два дочерних класса Rectangle и Circle, которые будут наследовать от Shape
# и переопределять метод area для вычисления площади прямоугольника и круга соответственно.



import math

class Shape:
    def area(self):
        pass

# Напишите тут ваш код
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.width * self.length

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pow(self.radius, 2) * math.pi
# Пример использования
rect = Rectangle(3, 4)
print(f"Area of rectangle: {rect.area()}")

circle = Circle(5)
print(f"Area of circle: {circle.area()}")
