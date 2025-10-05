# app/services/price_alert_notifier.py

from app import db
from app.models import PriceAlert
from app.services.scraper import scrape_product_details

def check_price_alerts():
    """
    Check all price alerts and notify users if current price <= desired price.
    Currently prints to console; can be extended to send emails.
    """
    alerts = PriceAlert.query.all()
    for alert in alerts:
        url = alert.product_url
        desired_price = alert.desired_price
        user_id = alert.user_id

        scraped_data = scrape_product_details(url)

        if not scraped_data or 'price' not in scraped_data:
            print(f"[!] Could not fetch price for URL: {url}")
            continue

        try:
            current_price = float(scraped_data['price'])

            if current_price <= desired_price:
                print(f"[ALERT] User {user_id} - Price dropped for {url}")
                print(f"Desired: ₹{desired_price}, Current: ₹{current_price}")
            else:
                print(f"[INFO] User {user_id}: Price for {url} is ₹{current_price} (Above desired ₹{desired_price})")
        except ValueError:
            print(f"[ERROR] Invalid price format for URL: {url}")
