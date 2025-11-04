import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Este es un correo de prueba desde Python.")
msg["Subject"] = "Prueba TP7"
msg["From"] = "matisalinas.2000@gmail.com"
msg["To"] = "cervienzo7@gmail.com"

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login("matisalinas.2000@gmail.com", "rtii idoe ymyb onzw")
    server.send_message(msg)

print("Correo enviado correctamente.")

# Registrar el envío
with open("correo_log.txt", "a", encoding="utf-8") as f:
    f.write(f"Correo enviado a: {msg['To']}\n")

## 👉 Protocolo: SMTP
## 👉 Demostración: mostrar envío real (usando clave de aplicación, no contraseña).
