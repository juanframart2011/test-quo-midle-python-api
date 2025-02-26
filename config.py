import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://quo:test2025-*@104.237.149.181/quo-test-python-midle'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'haa8a8haha9*s'

    # Configuración de correo para recuperación de contraseña
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'tu_correo@gmail.com'
    MAIL_PASSWORD = 'tu_contraseña'