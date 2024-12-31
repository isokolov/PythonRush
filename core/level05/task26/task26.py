# Группировка кортежей

# Напишите программу, которая создает кортеж из 6 элементов, запрашиваемых у пользователя.
# Затем программа должна сгруппировать их в 3 картежа по 2 элемента.
# Затем объединить 1 и 3 кортежи и вывести обновленный кортеж на экран.

# Напишите тут ваш
my_tuple = tuple(input("Enter your word: ") for i in range(6))
new_tuple = ((my_tuple[0],my_tuple[1]), (my_tuple[2],my_tuple[3]), (my_tuple[4],my_tuple[5]))
update_tuple = new_tuple[0] + new_tuple[2]
print(update_tuple)