# Самый главный кортеж

# Напишите программу, которая создает кортеж, содержащий несколько вложенных кортежей из целых чисел.
# Программа должна использовать цикл for для поиска максимального элемента во вложенных кортежах и вывести результат.

# Напишите тут ваш код
my_tuple = ((1, 2, 3), (11, 12, 13))
maximum = my_tuple[0][0]
for i in range(len(my_tuple)):
    for j in range(len(my_tuple[i])):
        if my_tuple[i][j] > maximum:
            maximum = my_tuple[i][j]

print(maximum)
