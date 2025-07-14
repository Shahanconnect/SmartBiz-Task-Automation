import smtplib
from email.mime.text import MIMEText
from app.models import PriceAlert
from app.services.scraper import scrape_product_details  # Use the new function directly
from app import db

def send_price_alert_email(to_email, product_name, product_url, current_price, target_price):
    msg = MIMEText(f"The price for '{product_name}' has dropped to ₹{current_price}.\n\nLink: {product_url}")
    msg['Subject'] = f"Price Alert: {product_name}"
    msg['From'] = 'testsmartbiz@gmail.com'
    msg['To'] = to_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login('testsmartbiz@gmail.com', 'wwhv xgey yiuu wgnx')  # Use App Password!
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Email sending failed: {e}")
        return False

def check_price_alerts(app):
    with app.app_context():
        alerts = PriceAlert.query.all()
        for alert in alerts:
            scraped_data = scrape_product_details(alert.product_url)
            if scraped_data['status'] == 'success':
                current_price_str = scraped_data['price'].replace('₹', '').replace(',', '').strip()
                try:
                    current_price = float(current_price_str)
                except ValueError:
                    continue  # Skip if price is not a valid float

                if current_price <= alert.target_price:
                    send_price_alert_email(
                        alert.email,
                        alert.product_name,
                        alert.product_url,
                        current_price,
                        alert.target_price
                    )
                    db.session.delete(alert)
        db.session.commit()
