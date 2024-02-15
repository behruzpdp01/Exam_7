from celery import shared_task
from django.core.mail import send_mail

from root.settings import EMAIL_HOST_USER

def send_email_function(subject, message, to_email: list):
    send_mail('TEMASI', 'saytimizga xush kelibsiz', EMAIL_HOST_USER, to_email, False)
    return {"status": "success", "message": f"{', '.join(to_email)} pochtaga yuborildi"}


@shared_task
def task_send_email(subject, msg, recipient_list):
    send_email_function(subject, msg, recipient_list)
    return {'emails': recipient_list, 'success': True}


