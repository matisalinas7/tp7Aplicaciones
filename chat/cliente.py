import socket, threading

HOST = "127.0.0.1"
PORT = 5000

def recibir(sock):
    while True:
        data = sock.recv(1024).decode()
        print(data)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

threading.Thread(target=recibir, args=(sock,)).start()

while True:
    msg = input()
    sock.sendall(msg.encode())

## 👉 Protocolo: TCP (aplicación tipo chat)
## 👉 Demostración: abrir 2 consolas cliente y ver mensajes compartidos.