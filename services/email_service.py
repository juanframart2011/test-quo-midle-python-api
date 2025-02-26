from flask_mail import Mail, Message
from flask import current_app

mail = Mail()

def send_recovery_email(email, token):
    subject = "Recuperación de contraseña"
    body = f"Usa este token para recuperar tu contraseña: {token}"
    msg = Message(subject=subject, recipients=[email], body=body)
    mail.send(msg)