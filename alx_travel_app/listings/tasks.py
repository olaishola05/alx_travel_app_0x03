from celery import shared_task
import time
import logging

from django.core.mail import send_mail
from django.conf import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@shared_task
def send_payment_confirmation_email(user_email):
    logger.info(f'Sending payment confirmation email to {user_email}')
    time.sleep(5)
    logger.info(f'Payment confirmation email sent to {user_email}')
    
    
@shared_task
def send_booking_confirmation_email(user_email, booking_details):
    """
    This is an asynchronous task that sends a booking confirmation email.
    
    Args:
        user_email (str): The email address of the user.
        booking_details (str): A string containing the booking information.
    """
    details = "\n".join([f"{key}: {value}" for key, value in booking_details.items()])
    subject = 'Your Booking is Confirmed!'
    message = f'Hello,\n\nYour booking has been successfully confirmed. Here are the details:\n\n{details}\n\nThank you!'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)