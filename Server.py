import socket
from _thread import*

clients = []

def client_thread(con):
    while True:
        data = con.recv(1024)
        if not data:
            break
        message = data.decode()
        for client in clients:
            if client == con:
                continue
            print(f"Client {_} sent: {message}")
            client.send(message.encode())


server = socket.socket()  # создаём объект хоста
hostname = socket.gethostname()  # получаем имя хоста локальной машины
port = 12345  # Устанавливаем порт сервера
server.bind((hostname, port))  # связываем сокет к хосту и порту
server.listen(20)



print("Server running")
while True:
    client, _ = server.accept()  # принимаем клиента
    clients.append(client)
    start_new_thread(client_thread, (client,))  # Запускаем поток клиента
