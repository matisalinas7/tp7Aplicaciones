from common.logger_config import setup_logger
logger = setup_logger("correo.log")

import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Este es un correo de prueba desde Python.")
msg["Subject"] = "Prueba TP7"
msg["From"] = "matisalinas.2000@gmail.com"
msg["To"] = "emilianoserey1@gmail.com"

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login("matisalinas.2000@gmail.com", "rtii idoe ymyb onzw")
    server.send_message(msg)

print("Correo enviado correctamente.")

## 👉 Protocolo: SMTP
## 👉 Demostración: mostrar envío real (usando clave de aplicación, no contraseña).