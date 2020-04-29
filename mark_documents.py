import datetime

"""
Example to mark an existing document as 'sent' and 'paid'
(Can also be marked as 'sent', 'confirmed', 'accepted', or 'cancelled'
 depending on type of document)
"""

# Get url of document to mark
url = f'https://api.makeleaps.com/api/partner/{partner_mid}/document/{document_mid}/'

# Get current local time in ISO 8601 format with timezone offset
current_time = datetime.datetime.now().astimezone().isoformat()

# Mark document as sent
document['date_sent'] = current_time

# After some time, get current local time again
current_time = datetime.datetime.now().astimezone().isoformat()

# Mark document as paid
document['date_paid'] = current_time

# Make an authorized reauest to update document
requests.post(url, data=document, headers=headers)
