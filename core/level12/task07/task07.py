# Обработка ошибок при работе с файлами

# Напишите программу, которая открывает файл example.txt в режиме добавления, записывает в него строку "Новая линия.".
# Нужно корректно обрабатывать исключение FileNotFoundError, закрывая файл в любом случае.

# Напишите тут ваш код
file = None
try:
    file = open('example.txt', 'a', encoding="utf-8")
    file.write("Новая линия.")
except FileNotFoundError as e:
    print(f"File not found: {e}")
finally:
    if file:
        file.close()
