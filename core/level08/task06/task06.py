# Замыкание.

# Напишите программу, которая создает функцию фильтра с использованием замыканий.
# Программа должна:
# Определить внешнюю функцию make_filter(threshold), которая создает и возвращает внутреннюю функцию filter_func(value).
# Внутренняя функция filter_func(value) должна возвращать True, если value больше threshold.
# Создать несколько функций фильтров с различными пороговыми значениями и
# использовать их для фильтрации списка данных, выводя результат на экран.

# Напишите тут ваш код
def make_filter(threshold):

    def filter_func(value):
        return value > threshold

    return filter_func

filter_above_10 = make_filter(10)
filter_above_6 = make_filter(6)
data = [5, 10, 15, 20]
filtered_data = list(filter(filter_above_10, data))
filtered_data2 = list(filter(filter_above_6, data))
print(filtered_data)
print(filtered_data2)
