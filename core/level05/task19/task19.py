# Просто и сложно одновременно

# Создай 5 кортежей с разной длинной: 0 элементов, 1 элемент, 5 элементов, 100 элементов, 1000 элементов.
# Выведи их на экран.

# Напишите тут ваш код
tuple1 = ()
tuple2 = (1,)
tuple3 = 1, 2, 3, 4, 5
tuple4 = tuple(i for i in range(100))
tuple5 = tuple(i for i in range(1000))
print(list(tuple4))
