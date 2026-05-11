import smtplib
import logging
import os

from email.message import EmailMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
DRY_RUN = os.getenv("DRY_RUN", "True") == "True"


def send_email(to_email, subject, body):

    try:

        # DRY RUN MODE
        if DRY_RUN:

            print(f"\n[DRY RUN]")
            print(f"To: {to_email}")
            print(f"Subject: {subject}")
            print("Email simulated successfully.\n")

            logging.info(f"[DRY RUN] Email simulated for {to_email}")

            return "DRY_RUN_SUCCESS"

        # REAL EMAIL MODE
        msg = EmailMessage()

        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email

        msg.set_content(body)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            smtp.send_message(msg)

        print(f"Email sent to {to_email}")

        logging.info(f"Email sent successfully to {to_email}")

        return "SUCCESS"

    except Exception as e:

        print(f"Failed to send email to {to_email}")

        logging.error(f"Email sending failed for {to_email}: {e}")

        return f"FAILED: {e}"