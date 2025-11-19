# Двумерный массив.

# Создание одномерного массива для имитации двумерного массива 10x10
# Заполнение массива как таблицы умножения x * y
# Примечание: х от 1 до 10 и y от 1 до 10.
# Класс list использовать нельзя.

# Напишите тут ваш код
import array

x = 10
y = 10

matrix = array.array("I", (1 for _ in range(x * y)))

for i in range(x):
    for j in range(y):
        matrix[i * y + j] = (i + 1) * (j + 1)

for i in range(x):
    base = i * y
    for j in range(y):
        print(matrix[base + j], end=' ')
    print()
