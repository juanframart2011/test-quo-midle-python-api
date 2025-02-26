from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
from database import db
from routes.auth_routes import auth_bp
from services.email_service import mail

app = Flask(__name__)
app.config.from_object(Config)

# Configurar extensiones
db.init_app(app)
mail.init_app(app)
migrate = Migrate(app, db)
CORS(app)  # Habilita CORS para llamadas externas

# Registrar rutas
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=True)
