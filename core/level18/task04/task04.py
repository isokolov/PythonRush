# Близкий друг

# Напишите рекурсивный алгоритм для поиска элемента, наиболее близкого к заданному значению в отсортированном массиве.


def closest_element(arr, low, high, target, best=None):
# Напишите тут ваш код


# Пример использования:
arr = [1, 3, 5, 8, 10, 14, 17]
target = 9
result = closest_element(arr, 0, len(arr) - 1, target)
print(f"Element closest to {target} is {result}") # 8
