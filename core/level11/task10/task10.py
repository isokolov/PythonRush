# Итератор для коллекции

# Напишите класс CollectionIterator, который будет итерироваться по произвольной коллекции (список, строка и т.д.).
# Реализуйте методы __iter__ и __next__.

# Напишите тут ваш код
class CollectionIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        curr_ind = self.index
        self.index += 1
        return self.data[curr_ind]
