# Детектив

# Напиши функцию set_detector, которая проходится по списку(кортежу) своих аргументов и определяет - есть среди них множество или нет.
# Вызови функцию set_detector с разными вариантами параметров (с множеством и без).

# Напишите тут ваш
def set_detector(*args):
    for element in args:
        if type(element) == set:
            return True
    return False

print(set_detector(1, 'dd', {1, 2, 3}))
print(set_detector(1, 'test'))