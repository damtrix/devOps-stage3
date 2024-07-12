from celery_config import celery
import smtplib

@celery.task
def send_email(recipient):
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    sender_email = 'your_email@example.com'
    sender_password = 'your_password'

    message = f"Subject: Hi there\n\nThis message is sent from Python."

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient, message)
    except Exception as e:
        print(f"Error: {e}")