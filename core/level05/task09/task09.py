# Первый на выход

# Напишите программу, которая создает список из 5 элементов, запрашивает у пользователя элемент для удаления
# и удаляет первый найденный элемент из списка с использованием метода remove().
# Программа должна вывести обновленный список.

# Напишите тут ваш код
my_list = ['1', '2', 'test', '4', '5']
value = input("Enter a value: ")
if value in my_list:
    my_list.remove(value)
print(my_list)
