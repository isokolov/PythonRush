# Полиморфизм.

# Создайте базовый класс Shape с методом area, который будет возвращать площадь фигуры.
# Затем создайте дочерние классы Circle и Rectangle, которые будут переопределять метод area для расчета площади своих фигур.
# Используйте полиморфизм, чтобы создать список фигур и вычислить их площади.

import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses should implement this method!")



# Напишите тут ваш код
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


shapes = [Circle(5), Rectangle(4, 6), Circle(3)]
areas = [shape.area() for shape in shapes]

for area in areas:
    print(area)
