# Пользовательский кортеж

# Напишите программу, которая создает кортеж из произвольного количества элементов, запрашиваемых у пользователя.
# Затем программа должна вывести последний элемент кортежа.
# Если кортеж пустой, программа должна вывести сообщение об этом.

# Напишите тут ваш код
number = int(input("Enter number of tuple elements to enter: "))
if number == 0:
    print("Tuple is empty")
else:
    my_tuple = tuple(input("Enter your word: ") for i in range(number))
    print(my_tuple[-1])

