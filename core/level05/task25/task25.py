# Добавление элемента

# Напишите программу, которая создает кортеж из 5 элементов, запрашиваемых у пользователя.
# Затем программа должна запросить у пользователя новый элемент и добавить его в конец кортежа, создавая новый кортеж.
# Программа должна вывести обновленный кортеж.

# Напишите тут ваш код
my_tuple = tuple(input("Enter your word: ") for i in range(5))
new_element = input("Enter a new tuple element")
my_list = list(my_tuple)
my_list.append(new_element)
new_tuple = tuple(my_list)
print(new_tuple)