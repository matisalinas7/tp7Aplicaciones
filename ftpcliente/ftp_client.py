from common.logger_config import setup_logger
logger = setup_logger("ftp.log")

from ftplib import FTP

ftp = FTP("test.rebex.net")  # servidor público de prueba
ftp.login("demo", "password")

ftp.set_pasv(True)  # Fuerza modo pasivo (más estable detrás de NAT/firewall)

print("Archivos disponibles:")
ftp.retrlines("LIST")

filename = "readme.txt"
with open(filename, "wb") as f:
    ftp.retrbinary(f"RETR {filename}", f.write)

print(f"Archivo '{filename}' descargado correctamente.")
ftp.quit()

## 👉 Protocolo: FTP
## 👉 Demostración: listar y descargar un archivo de un servidor público.