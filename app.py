# app.py
from flask import Flask, request
from celery import Celery
import smtplib
from datetime import datetime

app = Flask(__name__)

# Configure Celery
app.config['CELERY_BROKER_URL'] = 'amqp://guest:guest@localhost:5672'
app.config['CELERY_RESULT_BACKEND'] = 'rpc://'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task(name='send_email')
def send_email(recipient):
    # Your SMTP configuration here
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'oludamolaonarinde6@gmail.com'
    sender_password = 'xoxrtsheibisonuk'

    message = f"""\
    Subject: Hi there

    This message is sent from Python."""

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient, message)
    except Exception as e:
        print(f"Error: {e}")

@app.route('/')
def index():
    sendmail = request.args.get('sendmail')
    talktome = request.args.get('talktome')

    if sendmail:
        send_email.delay(sendmail)
        return f"Email to {sendmail} has been queued."

    if talktome:
        with open('/var/log/messaging_system.log', 'a') as f:
            f.write(f"{datetime.now()}\n")
        return "Current time logged."

    return "No valid parameters provided."

if __name__ == "__main__":
    app.run(debug=True)