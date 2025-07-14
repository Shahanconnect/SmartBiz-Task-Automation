import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load .env only once if not already loaded
load_dotenv()

def send_email_alert(app, to_email, subject, body):
    from_email = os.getenv('MAIL_USERNAME')
    from_password = os.getenv('MAIL_PASSWORD')

    # Optional: fallback logger if app is None (for testing without Flask)
    logger = getattr(app, 'logger', None)

    try:
        if logger: logger.debug(f"[DEBUG] Preparing email to {to_email}")

        # Create email content
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))

        if logger: logger.debug("[DEBUG] Connecting to Gmail SMTP...")

        # Connect and send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(from_email, from_password)
            if logger: logger.debug("[DEBUG] Login successful. Sending email...")
            server.send_message(msg)

        if logger: logger.info(f"📧 Email sent to {to_email}")

    except Exception as e:
        if logger:
            logger.error(f"❌ Failed to send email to {to_email}: {e}")
        else:
            print(f"[ERROR] Failed to send email: {e}")
