# webserver/server.py

from common.logger_config import setup_logger
logger = setup_logger("webserver.log")

logger.info("Servidor Web iniciado.")

from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

PORT = 8080
DIRECTORIO = os.path.join(os.getcwd(), "webserver", "www")

os.chdir(DIRECTORIO)

with HTTPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Servidor Web activo en http://localhost:{PORT}")
    httpd.serve_forever()


## Crea una carpeta webserver/www con un index.html para probar.
## 👉 Protocolo: HTTP
## 👉 Demostración: abrir localhost:8080 en el navegador.