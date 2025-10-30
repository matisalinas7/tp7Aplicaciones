from common.logger_config import setup_logger
logger = setup_logger("chat.log")

import socket, threading

HOST = "127.0.0.1"
PORT = 5000
clientes = []

def manejar_cliente(conn, addr):
    print(f"Conexión desde {addr}")
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"{addr}: {data}")
        for c in clientes:
            if c != conn:
                c.sendall(f"{addr}: {data}".encode())
    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print("Servidor de chat iniciado...")

while True:
    conn, addr = server.accept()
    clientes.append(conn)
    threading.Thread(target=manejar_cliente, args=(conn, addr)).start()
