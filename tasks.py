from celery_config import celery
import smtplib

@celery.task
def send_email(recipient):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'oludamolaonarinde6@gmail.com'
    sender_password = 'xoxrtsheibisonuk'

    message = f"Subject: HNG Stage 3 Assignment\n\nThis is a test of RabbitMQ, Celery on python flask."

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            print("Connecting to server")
            server.starttls()
            print("Logging in")
            server.login(sender_email, sender_password)
            print("Sending email")
            server.sendmail(sender_email, recipient, message)
    except Exception as e:
        print(f"Error: {e}")