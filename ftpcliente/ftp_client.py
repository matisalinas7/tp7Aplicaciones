from ftplib import FTP

ftp = FTP("test.rebex.net")  # servidor público de prueba
ftp.login("demo", "password")

ftp.set_pasv(True)  # Fuerza modo pasivo (más estable detrás de NAT/firewall)

print("Archivos disponibles:")
ftp.retrlines("LIST")

filename = "readme.txt"
with open(filename, "wb") as f:
    ftp.retrbinary(f"RETR " + filename, f.write)

print(f"Archivo '{filename}' descargado correctamente.")
ftp.quit()

# Registrar descarga
with open("ftp_log.txt", "a", encoding="utf-8") as f:
    f.write(f"Archivo descargado: {filename}\n")

## 👉 Protocolo: FTP
## 👉 Demostración: listar y descargar un archivo de un servidor público.
