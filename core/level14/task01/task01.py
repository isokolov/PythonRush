# Использование класса Timer

# Напишите программу, которая использует класс Timer для выполнения функции с задержкой
# и демонстрирует отмену таймера до его срабатывания.

# Напишите тут ваш код
import threading

def hello():
    print("Hello")

t = threading.Timer(3, hello)
t.start()
t.cancel()
