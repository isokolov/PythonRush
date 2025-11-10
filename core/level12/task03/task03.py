# Чтение всего файла

# Напишите программу, которая читает и выводит на экран содержимое файла example.txt полностью.

# Напишите тут ваш код
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
