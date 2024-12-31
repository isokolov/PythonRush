# Замена

# Напишите программу, которая создает множество, содержащее названия нескольких фруктов.
# Программа должна вывести фрукты на экран.
# Затем программа должна запросить у пользователя индекс (с учетом порядка вывода на экран) и новое название фрукта для замены.
# Затем найти фрукт по индексу, заменить его новым названием и вывести обновленное множество.

 # Напишите тут ваш код
fruits_set = {'Apple', 'Grape', 'Peach', 'Banana'}
new_set = {}
print(fruits_set)
your_index = int(input("Enter index number: "))

new_fruit = input("Enter a new fruit: ")
for index, value in enumerate(fruits_set):
    new_set[index] = value
    if your_index == index:
        new_set[index] = new_fruit

print(set(new_set.values()))