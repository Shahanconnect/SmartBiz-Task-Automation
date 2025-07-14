import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))  
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'True') == 'True'
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
