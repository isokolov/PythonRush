# Создаем свой массив

# Создай массив с использованием библиотеки numpy.
# Добавь в него 10 случайных чисел от 0 до 1000. Отсортируй и выведи на экран.
# Класс list использовать нельзя.

# Напишите тут ваш код
import numpy as np
arr = np.random.randint(0, 1001, size=10)
print(arr)
arr = np.sort(arr)
print(f"After sorting: {arr}")
