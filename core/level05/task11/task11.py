# Лес

# Напишите программу, которая создает список из названий деревьев, затем с использованием цикла и функции enumerate() выводит каждый элемент списка и его индекс.

# Напишите тут ваш код
my_list = ['Oak', 'Sholud', 'Beresa', 'Iva']
for index, element in enumerate(my_list):
    print(f"Индекс: {index}, Дерево: {element}")