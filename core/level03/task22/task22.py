# Таблица Пифагора

# Напишите программу, которая запрашивает у пользователя число N и выводит таблицу умножения Пифагора размером NxN, используя вложенные циклы.
# Программа должна выводить только числа таблицы.
# Пример:
# 1   2   3   ...
# 2   4   6   ...
# 3   6   9   ...
# ...
# Напишите тут ваш код
number = int(input("Enter a number: "))
for i in range(1, number + 1):
    for j in range(1, number + 1):
        print(i * j, end=" ")
    print()