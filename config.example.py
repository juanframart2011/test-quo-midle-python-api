import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://usuario:password@localhost/tu_base_de_datos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'tu_clave_secreta'

    # Configuración de correo para recuperación de contraseña
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'tu_correo@gmail.com'
    MAIL_PASSWORD = 'tu_contraseña'
