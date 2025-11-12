# Создание сокет-клиента

# Напишите программу, которая создает сокет-клиента, подключается к сокет-серверу, отправляет ему сообщение и получает ответ.

# Напишите тут ваш код
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost',8000))

client_socket.sendall(b'Hello, server!')

data = client_socket.recv(1024)
print(f"Get from server: {data.decode('utf-8')}")
client_socket.close()
