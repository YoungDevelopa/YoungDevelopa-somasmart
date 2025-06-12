import requests
from django.http import JsonResponse
from django.conf import settings
from datetime import datetime
import base64

def get_access_token():
    r = requests.get(
        'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials',
        auth=(settings.MPESA_CONSUMER_KEY, settings.MPESA_CONSUMER_SECRET)
    )
    return r.json().get('access_token')

def initiate_stk_push(request):
    access_token = get_access_token()
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    password = base64.b64encode(
        f"{settings.MPESA_SHORTCODE}{settings.MPESA_PASSKEY}{timestamp}".encode()
    ).decode()

    headers = {"Authorization": f"Bearer {access_token}"}
    payload = {
        "BusinessShortCode": settings.MPESA_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 500,
        "PartyA": "2547XXXXXXXX",  # User's phone
        "PartyB": settings.MPESA_SHORTCODE,
        "PhoneNumber": "2547XXXXXXXX",
        "CallBackURL": settings.MPESA_CALLBACK_URL,
        "AccountReference": "SomaSmart",
        "TransactionDesc": "SomaSmart Subscription"
    }

    response = requests.post(
        'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest',
        json=payload,
        headers=headers
    )
    return JsonResponse(response.json())
