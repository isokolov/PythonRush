# Ищем ключи.

# Напишите программу, которая создает словарь с информацией о книге (например, название, автор, год издания). Программа должна:
# Вывести все ключи словаря с использованием метода keys().
# Итерировать по всем ключам и вывести их на экран.

# Напишите тут ваш код
book = {"title": "War and peace", "author": "Tolstoy",
        "year": 1844}
book_keys = book.keys()
print(book_keys)
for item in book.keys():
    print(item)