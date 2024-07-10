import os
from flask_mail import Mail

mail = Mail()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///jose.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuración de correo
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'tomasbroda13@gmail.com'
    MAIL_PASSWORD = 'inmv umfu fqiw lvhl'
    MAIL_DEFAULT_SENDER = 'tomasbroda13@gmail.com'
