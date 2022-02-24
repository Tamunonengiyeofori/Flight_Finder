import os 
from dotenv import load_dotenv
from twilio.rest import Client
from datetime import datetime
load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
SENDER_PHONE_NO = os.getenv("SENDER_PHONE_NO")
RECIEVER_PHONE_NO = os.getenv("RECIEVER_PHONE_NO")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def send_message(self, price, dept_city, dept_airpot_code, arrival_city, arriv_airport_code, out_date, in_date):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        
        message = self.client.messages.create(
            body=f"""
            Low price Alert !!! Only #{price} to fly from {dept_city}-{dept_airpot_code}
            to {arrival_city}-{arriv_airport_code}, from {out_date} to {in_date}
            """ , 
            from_=SENDER_PHONE_NO , 
            to=RECIEVER_PHONE_NO
        )
        
        print(message.sid)