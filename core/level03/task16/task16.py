# Хитрый раджа

# Напишите программу, которая вычисляет, сколько зерен окажется на каждой клетке шахматной доски,
# если на первую клетку кладется 1 зернышко, на вторую — 2 зернышка, на третью — 4 зернышка и так далее.
# Всего на шахматной доске 64 клетки.
# Используйте цикл for и функцию range() для итерации по клеткам и функцию print() для вывода результата.
# Пример:
# Для первых трех клеток программа должна вывести:
# Клетка 1: 1 зерна
# Клетка 2: 2 зерна
# Клетка 3: 4 зерна
# ...

# Напишите тут ваш код
for i in range (0, 64, 1):
    print(f"Клетка {i + 1}: {2 ** i} зерна")