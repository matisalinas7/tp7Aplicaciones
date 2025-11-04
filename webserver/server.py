from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

PORT = 8080
DIRECTORIO = os.path.join(os.getcwd(), "webserver", "www")

os.chdir(DIRECTORIO)

with HTTPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Servidor Web activo en http://localhost:{PORT}")
    # Registro simple de inicio del servidor
    with open("webserver_log.txt", "a", encoding="utf-8") as f:
        f.write(f"Servidor iniciado en puerto {PORT}\n")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Servidor detenido manualmente.")
        with open("webserver_log.txt", "a", encoding="utf-8") as f:
            f.write("Servidor detenido manualmente.\n")
