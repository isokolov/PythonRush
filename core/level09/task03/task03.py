# Прямоугольники.

# Создайте класс Rectangle с конструктором, который принимает параметры width и height.
# Добавьте метод area(), который возвращает площадь прямоугольника.
# Создайте объект этого класса и вычислите его площадь.

# Напишите тут ваш код
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

fig1 = Rectangle(3, 4)
print(fig1.area())
