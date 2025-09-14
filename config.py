import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clave_local')
    DB_HOST = os.environ.get('MYSQLHOST')          # no 'localhost'
    DB_USER = os.environ.get('MYSQLUSER')          # normalmente 'root'
    DB_PASSWORD = os.environ.get('MYSQL_ROOT_PASSWORD')
    DB_NAME = os.environ.get('MYSQL_DATABASE')     # 'railway'
    DB_PORT = int(os.environ.get('MYSQLPORT', 3306))