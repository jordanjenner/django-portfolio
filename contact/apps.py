from django.apps import AppConfig
from django.core.mail import send_mail
from django.conf import settings


class ContactConfig(AppConfig):
    name = 'contact'


def send_email(email_address, message_body, date_time):
    date = date_time.strftime("%Y-%m-%d %H:%M:%S")
    message = """You recieved a message from {} at {}.
    
    \"{}\"
    
    This message was sent from the contact form on jordanjenner.com
    """.format(email_address, date, message_body)


    send_mail(
        'New email from contact form @ jordanjenner.com',
        message,
        email_address,
        [settings.CONTACT_EMAIL],
        fail_silently=False
    )

