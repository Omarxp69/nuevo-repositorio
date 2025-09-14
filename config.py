import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clave_super_segura_y_unica')
    DB_HOST = os.environ.get('DB_HOST', 'localhost')
    DB_USER = os.environ.get('DB_USER', 'root')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '')
    DB_NAME = os.environ.get('DB_NAME', 'mi_base_datos')