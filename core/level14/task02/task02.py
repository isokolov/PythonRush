# Использование ThreadLocal

# Напишите программу, которая использует класс ThreadLocal для хранения данных, уникальных для каждого потока.

# Напишите тут ваш код
import threading

my_data = threading.local()

def process():
    my_data.value = threading.current_thread().name
    print(f"Value in {threading.current_thread().name}: {my_data.value}")

threads = []
for i in range(3):
    t = threading.Thread(target=process)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
