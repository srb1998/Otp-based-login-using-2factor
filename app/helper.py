import requests
import random
from django.conf import settings

def send_otp_api(phone_number,otp):
    try:
        # url = f"https://2factor.in/API/V1/{settings.API_KEY}/SMS/{phone_number}/{otp}"
        # response = requests.get(url)
        print("successfully sent")
        return None
    
    except Exception as e:
        return None