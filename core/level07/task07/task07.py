# Три проверки.

# Напишите программу, которая создает словарь с информацией о книге (например, название, автор, год издания).
# Программа должна:
# Проверить наличие ключа "author" с использованием оператора in.
# Проверить наличие ключа "publisher" с использованием метода get().
# Проверить наличие ключа "title" с использованием метода keys().

# Напишите тут ваш код
book = {"title": "War and peace", "author": "Tolstoy",
        "publisher": "Spring"}
print("author" in book)
print(book.get("publisher") is not None)
print("title" in book.keys())