# Поиск подстроки.

# Напишите программу, которая принимает строку и подстроку от пользователя.
# Программа должна проверить, входит ли подстрока в строку с использованием оператора in,
# найти первое вхождение подстроки с использованием метода find() и
# подсчитать количество вхождений подстроки с использованием метода count().
# Программа должна вывести все результаты.

# Напишите тут ваш код
stroka = input("Enter your string: ")
podstroka = input("Enter your substring: ")
print(podstroka in stroka)
if podstroka in stroka:
    print(stroka.find(podstroka))
    print(stroka.count(podstroka))