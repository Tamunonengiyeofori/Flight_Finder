from multiprocessing import connection
import smtplib, ssl
import os
from dotenv import load_dotenv
from twilio.rest import Client
from datetime import datetime
load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
SENDER_PHONE_NO = os.getenv("SENDER_PHONE_NO")
RECIEVER_PHONE_NO = os.getenv("RECIEVER_PHONE_NO")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        
    def send_sms(self, message):
        message = self.client.messages.create(
            body= message, 
            from_=SENDER_PHONE_NO , 
            to=RECIEVER_PHONE_NO ,
        )
        print(message.sid)
        
    def send_mails(self ,message, recipient_emails, google_link):
        # create a secure SSL context
        context = ssl.create_default_context()
        smtp_server = "smtp@gmail.com"
        port = 587
        
        
        # self.port = port
        
        with smtplib.SMTP_SSL(smtp_server , port, context=context) as connection:
            connection.starttls(context=context)
            connection.login(SENDER_EMAIL , SENDER_PASSWORD)
            for email in recipient_emails:
                connection.sendmail(
                    from_addr=SENDER_EMAIL,
                    to_addrs=email, 
                    msg = f"Subject:New Low Price Flight!\n\n{message}\n{google_link}".encode("utf-8")
                )
        
        
        