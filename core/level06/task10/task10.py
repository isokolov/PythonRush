# Фруктовица

# Напишите программу, которая создает множество, содержащее названия нескольких фруктов.
# Затем программа должна запросить у пользователя название фрукта для удаления и удалить его из множества с использованием метода discard().
# Программа должна вывести обновленное множество.
# Если элемент не найден, программа должна продолжить выполнение без ошибки.

# Напишите тут ваш код
fruits_set = {'Apple', 'Grape', 'Peach', 'Banana'}
your_fruit_guess = input("Guess a fruit? ")
fruits_set.discard(your_fruit_guess)
print(fruits_set)