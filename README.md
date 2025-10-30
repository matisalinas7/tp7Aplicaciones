# 🧠 TP7 – Implementación de Aplicaciones

**Materia:** Redes de Datos – Ingeniería en Sistemas (2025)

---

## 📘 Objetivo

Implementar y probar aplicaciones reales de la **capa de aplicación del modelo TCP/IP**, para comprender el funcionamiento de sus principales protocolos:  
**HTTP, SMTP, FTP y TCP (Chat).**

---

## ⚙️ Estructura del proyecto

tp7_aplicaciones/
├── webserver/ → Servidor Web (HTTP)
├── chat/ → Chat Cliente/Servidor (TCP)
├── correo/ → Cliente de Correo (SMTP)
├── ftpcliente/ → Cliente FTP
├── common/ → Configuración de logs
└── logs/ → Registros de actividad

---

## 🌐 Servidor Web – HTTP

Ejecutar:

python webserver/server.py
Abrir en el navegador http://localhost:8080
Sirve archivos HTML desde www/ y registra accesos en logs/webserver.log.

💬 Chat – TCP

Servidor:

python chat/server.py

Cliente (en otra consola):

python chat/client.py

-> Permite comunicación en tiempo real entre varios clientes conectados al mismo servidor.
-> Registros en logs/chat.log.

📧 Correo – SMTP

Envía mails mediante Gmail usando una clave de aplicación.
Editar en correo/mail_client.py tus datos y ejecutar:

python correo/mail_client.py

-> Registra el envío en logs/correo.log.

📁 FTP – FTP

Conecta a un servidor público de prueba (test.rebex.net).
Ejecutar:

python ftpcliente/ftp_client.py

-> Lista archivos y descarga readme.txt.
-> Log: logs/ftp.log.

🧾 Conclusión

Se desarrollaron cuatro aplicaciones que implementan los protocolos HTTP, SMTP, FTP y TCP, demostrando cómo la capa de aplicación permite la comunicación entre sistemas a través de servicios reales y registrados.
