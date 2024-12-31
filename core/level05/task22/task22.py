# Номер кортежа

# Напишите программу, которая создает кортеж из 5 элементов, запрашиваемых у пользователя.
# Затем программа должна запросить у пользователя индекс элемента и вывести значение элемента по этому индексу.
# Если индекс выходит за пределы кортежа, программа должна вывести соответствующее сообщение.

# Напишите тут ваш код
print("Enter 5 tuple elements")
my_tuple = tuple(input() for i in range(5))
tuple_index = int(input("Enter index to get from the tuple: "))
if tuple_index >= len(my_tuple):
    print("Index out of tuple")
else:
    print(my_tuple[tuple_index])