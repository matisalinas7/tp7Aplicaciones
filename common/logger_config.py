# common/logger_config.py
import logging
import os

def setup_logger(nombre_archivo):
    """
    Crea y configura un logger que escribe en la carpeta ../logs/
    Cada módulo (web, chat, correo, ftp) puede llamar a esta función.
    """
    logs_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
    os.makedirs(logs_dir, exist_ok=True)

    ruta_log = os.path.join(logs_dir, nombre_archivo)

    logging.basicConfig(
        filename=ruta_log,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        force=True  # reinicia configuración si ya estaba inicializada
    )

    return logging.getLogger()
