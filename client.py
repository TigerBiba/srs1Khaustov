import socket
from _thread import*


client = socket.socket()
hostname = socket.gethostname()
port = 12345
client.connect((hostname, port))

def send_message(client):
    while True:
        message = input()
        client.send(message.encode())
        if message == "":
            break

def receive_message(client):
    while True:
        data = client.recv(1024)
        print("Кто то написал: ", data.decode())



start_new_thread(send_message, (client,))
start_new_thread(receive_message, (client,))

while True:
    pass

client.close()
