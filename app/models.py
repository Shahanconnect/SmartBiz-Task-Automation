from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime 

# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    phone = db.Column(db.String(20))
    password_hash = db.Column(db.String(200))
    is_admin = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)

    # Services flags
    service_scraper = db.Column(db.Boolean, default=True)
    service_price_alert = db.Column(db.Boolean, default=True)
    service_description_gen = db.Column(db.Boolean, default=True)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class ProductDescription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_name = db.Column(db.String(150))
    product_category = db.Column(db.String(150))
    product_features = db.Column(db.Text)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow) 
    

# PriceAlert Model
class PriceAlert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_name = db.Column(db.String(200), nullable=False)
    product_url = db.Column(db.String(500), nullable=False)
    target_price = db.Column(db.Float, nullable=False)
    email = db.Column(db.String(200), nullable=False)


class ScrapeHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    title = db.Column(db.String(255))
    price = db.Column(db.String(100))
    image = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('scrape_histories', lazy='dynamic'))
from app import db
from datetime import datetime

class InvoiceCounter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_number = db.Column(db.Integer, default=0)

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice_number = db.Column(db.String(20), unique=True, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    
    company_name = db.Column(db.String(100))
    company_email = db.Column(db.String(100))
    client_name = db.Column(db.String(100))
    client_email = db.Column(db.String(100))

    gst_percent = db.Column(db.Float, default=0.0)
    discount = db.Column(db.Float, default=0.0)
    total_amount = db.Column(db.Float)
    
    items = db.relationship("InvoiceItem", backref="invoice", cascade="all, delete", lazy=True)

class InvoiceItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'), nullable=False)
    description = db.Column(db.String(255))
    quantity = db.Column(db.Integer)
    unit_price = db.Column(db.Float)
