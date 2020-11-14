import os
from twilio.rest import Client
from dotenv import load_dotenv
import logging

logging.basicConfig(format="%(levelname)s %(asctime)s %(message)s", level=logging.INFO)


def send_sms(message):
    load_dotenv()
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    PHONE_NUMBER_FROM = os.getenv('PHONE_NUMBER_FROM')
    PHONE_NUMBER_TO = os.getenv('PHONE_NUMBER_TO')
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.http_client.logger.setLevel(logging.CRITICAL)
    try:
        message = client.messages.create(
            body=message,
            from_=PHONE_NUMBER_FROM,
            to=PHONE_NUMBER_TO,
            )
        logging.info('Сообщение отправлено')
    except Exception:
        logging.error('Сообщение не отправлено')
