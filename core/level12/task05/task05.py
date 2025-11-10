# Создание файла

# Напишите программу, которая создает новый файл example.txt и записывает в него строку "This is a new file."

# Напишите тут ваш код
with open('example.txt', 'w') as file:
    file.write("This is a new file.")
