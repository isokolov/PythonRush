# Работа с директориями.

# Напишите программу, которая создает директорию, переходит в нее, создает файл внутри этой директории,
# записывает в файл текст, а затем читает и выводит его содержимое.
# Программа должна:
# Создать директорию test_directory.
# Перейти в директорию test_directory.
# Создать файл test_file.txt и записать в него строку "Hello, World!".
# Прочитать содержимое файла test_file.txt и вывести его на экран.
# Удалить файл и директорию.

# Напишите тут ваш код
import os

os.mkdir('test_directory')
os.chdir('test_directory')
f= open('test_file.txt','w')
f.write("Hello, World!")
f.close()
f1= open('test_file.txt','r')
print(f1.read())
f1.close()
os.remove('test_file.txt')
os.rmdir('test_directory')