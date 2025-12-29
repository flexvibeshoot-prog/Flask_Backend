from app.celery_app import celery
from app import mail
from flask_mail import Message
from flask import render_template

@celery.task(bind=True, autoretry_for=(Exception,), retry_kwargs={"max_retries": 3},queue="email_queue", name="app.tasks.send_mail.send_mail_task")
def send_mail_task(self, email, otp, name):
    template = render_template(
        "email_config.html",
        otp=otp,
        name=name
    )

    msg = Message(
        subject="Register to Flex and vibe",
        recipients=[email],
        body="This is register otp, don't share to other person.\n OTP is valid for 5 minutes.",
        html=template
    )
    mail.send(msg)
