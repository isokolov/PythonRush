# Лучший алгоритм
# Дан массив из 10 элементов, определи какой из алгоритмов сортировки лучше всего подойдет для него.
# Подсказка: попробуй различный алгоритмы и оставь лучший

import time

def measure_time(func, arr):
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return end_time - start_time

array = [5, 3, 8, 6, 2, 7, 1, 0, 9, 4]

# Напишите тут ваш код
