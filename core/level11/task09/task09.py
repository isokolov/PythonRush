# Создание простого итератора

# Напишите класс SimpleIterator, который будет итерироваться по последовательности чисел от start до end.
# Реализуйте методы __iter__ и __next__.

# Напишите тут ваш код
class SimpleIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        current = self.current
        self.current += 1
        return current
