from flask import Blueprint, request, jsonify
from models import db, User, UserRecovery
from services.email_service import send_recovery_email

auth_bp = Blueprint('auth', __name__)

# Ruta de login
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = User.hash_password(data.get('password'))

    user = User.query.filter_by(email=email, password=password, deleted_at=None).first()

    if user:
        return jsonify({"message": "Login exitoso", "user": user.to_dict()}), 200
    return jsonify({"error": "Credenciales incorrectas"}), 401

# Registro de usuario
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = User.hash_password(data.get('password'))

    new_user = User(
        rol_id=data.get('rol_id'),
        name=data.get('name'),
        last_name=data.get('last_name'),
        email=data.get('email'),
        password=hashed_password
    )
    
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Usuario registrado correctamente"}), 201

# Recuperación de contraseña
@auth_bp.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.json
    email = data.get('email')
    user = User.query.filter_by(email=email, deleted_at=None).first()

    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    # Crear un nuevo token de recuperación
    recovery = UserRecovery(user_id=user.id)
    db.session.add(recovery)
    db.session.commit()

    # Enviar correo con token
    send_recovery_email(user.email, recovery.token)
    return jsonify({"message": "Correo de recuperación enviado", "token": recovery.token})

# Resetear contraseña
@auth_bp.route('/reset-password', methods=['POST'])
def reset_password():
    data = request.json
    token = data.get('token')
    new_password = data.get('password')

    recovery = UserRecovery.query.filter_by(token=token, status='pending').first()

    if not recovery:
        return jsonify({"error": "Token inválido o expirado"}), 400

    user = User.query.get(recovery.user_id)
    user.password = User.hash_password(new_password)

    # Marcar el token como usado
    recovery.status = 'used'
    db.session.commit()

    return jsonify({"message": "Contraseña actualizada correctamente"})
