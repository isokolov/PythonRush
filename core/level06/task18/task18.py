# Символы в строке

# Напишите программу, которая принимает строку от пользователя, выводит ее длину,
# а затем запрашивает у пользователя индекс.
# Программа должна вывести символ строки по этому индексу.
# Если индекс выходит за пределы строки, программа должна вывести соответствующее сообщение.

# Напишите тут ваш код
stroka = input("Enter your word: ")
print(len(stroka))
enter_index = int(input())
if enter_index >= len(stroka):
    print("Index out of bound")
else:
    print(stroka[enter_index])