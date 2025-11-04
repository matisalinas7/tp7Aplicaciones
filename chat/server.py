import socket, threading

HOST = "127.0.0.1"
PORT = 5000
clientes = []

def manejar_cliente(conn, addr):
    print(f"Conexión desde {addr}")
    with open("chat_log.txt", "a", encoding="utf-8") as f:
        f.write(f"Cliente conectado: {addr}\n")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        print(f"{addr}: {data}")

        # Registrar mensaje en log
        with open("chat_log.txt", "a", encoding="utf-8") as f:
            f.write(f"{addr}: {data}\n")

        for c in clientes:
            if c != conn:
                c.sendall(f"{addr}: {data}".encode())

    print(f"Cliente {addr} desconectado.")
    with open("chat_log.txt", "a", encoding="utf-8") as f:
        f.write(f"Cliente desconectado: {addr}\n")
    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print("Servidor de chat iniciado...")

# Registrar inicio del servidor
with open("chat_log.txt", "a", encoding="utf-8") as f:
    f.write(f"Servidor de chat iniciado en {HOST}:{PORT}\n")

while True:
    conn, addr = server.accept()
    clientes.append(conn)
    threading.Thread(target=manejar_cliente, args=(conn, addr)).start()
