# Создание сокет-сервера

# Напишите программу, которая создает сокет-сервер, принимает входящие соединения от клиентов и отвечает им "Hello, client!".

# Напишите тут ваш код
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost',12345))

server_socket.listen(10)
client_socket, client_address = server_socket.accept()
print(f"Connection created with {client_address}")

data = client_socket.recv(1024)
print(f"Getted: {data.decode('utf-8')}")

client_socket.sendall(b"Hello, client!")
client_socket.close()
