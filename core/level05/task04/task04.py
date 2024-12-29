# Пятый элемент.

# Напишите программу, которая создает список из 5 элементов, запрашиваемых у пользователя.
# Программа должна вывести список, затем запросить у пользователя индекс элемента и вывести значение элемента по этому индексу.

# Напишите тут ваш код
my_list = list()
value_1 = input("Enter value 1: ")
value_2 = input("Enter value 2: ")
value_3 = input("Enter value 3: ")
value_4 = input("Enter value 4: ")
value_5 = input("Enter value 5: ")
my_list.extend([value_1, value_2, value_3, value_4, value_5])
print(my_list)
my_index = int(input("Enter index: "))
my_index = my_index % 5
print(my_list[my_index])
