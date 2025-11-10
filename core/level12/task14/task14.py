# Получение списка файлов и директорий
# Напишите программу, которая выводит содержимое текущей рабочей директории и
# для каждого файла или директории указывает, является ли это файлом или директорией.
# Напишите тут ваш код
import os

current_directory = os.getcwd()
contents = os.listdir(current_directory)
print(contents)

with os.scandir(current_directory) as entries:
    for entry in entries:
        print(f"Имя: {entry.name}, Это директория: {entry.is_dir()}, Это файл: {entry.is_file()}")
