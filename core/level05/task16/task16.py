# Сортировка строк по длинне

# Напишите программу, которая создает список из 5 строк, запрашиваемых у пользователя.
# Затем программа должна отсортировать список по длине строк и вывести отсортированный список.

# Напишите тут ваш код
some_list = [input() for i in range(5)]
some_list.sort(key=len)
print(some_list)