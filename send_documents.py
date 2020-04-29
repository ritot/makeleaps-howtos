import requests
import json
import time

"""
Send a document using a Sending Order
"""

# Create a Sending Order
sending_order = {
    "recipient_organization": f"{client_res['url']}",
    "securesend_selected": True,
    "to_emails": ["sato@example.com"],
    "subject": "Invoices for March",
    "message": "Invoices are attached. Thank you for your business.",
    "enable_cc_payments": False,
    "sendbypost_selected": False,
    "stamp_type": "invoice",
}

# Send request with authorized header
sending_order_url = f'https://api-meetup.makeleaps.com/api/partner/{partner_mid}/sending/order/'
response = requests.post(url=sending_order_url, data=sending_order, headers=headers)

# Get url to add items to
order_response = response.json()['response']

# Add items to the Sending Order
item = {"position": 0, "document": document_response['url']}
requests.post(url=order_response['items_url'], data=item, headers=headers)

# Check for completion of processing (max wait time: 1 minute)
for i in range(20):
    response = requests.get(url=order_res['url'], headers=headers)
    ready_response = response.json()['response']
    if ready_response['ready_to_order']:
        # When finished processing, send Sending Order
        requests.post(url=order_response['send_url'], data={}, headers=headers)
        break
    else:
        time.sleep(3)
