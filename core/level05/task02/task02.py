# Ожидание стопа

# Напишите программу, которая создает пустой список с использованием квадратных скобок [] и добавляет в него элементы, запрашиваемые у пользователя.
# Ввод элементов должен продолжаться до тех пор, пока пользователь не введет слово "стоп". Затем программа должна вывести итоговый список.

# Напишите тут ваш
my_list = []
while True:
    value = input("Enter your value: ")
    if value == "стоп":
        break
    my_list.append(value)
print(my_list)