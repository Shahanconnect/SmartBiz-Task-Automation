from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_mail import Mail

import os
from dotenv import load_dotenv
from pathlib import Path

# Load .env file (for local development)
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / '.env')

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
mail = Mail()

def create_app():
    app = Flask(__name__)

    # ==============================
    # 🔐 SECRET KEY (Render compatible)
    # ==============================
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback-secret')

    # ==============================
    # 🗄️ DATABASE CONFIG (Render PostgreSQL fix)
    # ==============================
    uri = os.getenv("DATABASE_URL")

    if uri and uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

    app.config['SQLALCHEMY_DATABASE_URI'] = uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # ==============================
    # 📧 MAIL CONFIG
    # ==============================
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'true').lower() == 'true'
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')

    # ==============================
    # 🔌 INIT EXTENSIONS
    # ==============================
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    mail.init_app(app)

    # ==============================
    # 🔐 CSRF TOKEN
    # ==============================
    @app.context_processor
    def inject_csrf_token():
        return dict(csrf_token=generate_csrf())

    # ==============================
    # 👤 USER LOADER
    # ==============================
    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # ==============================
    # 🚏 ROUTES
    # ==============================
    from app.routes import register_routes
    register_routes(app)

    # ==============================
    # 🛠️ CREATE TABLES (FIRST RUN)
    # ==============================
    with app.app_context():
        db.create_all()

    return app