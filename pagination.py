import requests
import json

"""
Example to use pagination
(Go to next Document in Document List)
"""

# Make an authorized GET request to the paginated resource normally
url = f'https://api.makeleaps.com/api/partner/{partner_mid}/document/'
response = requests.get(url, headers=headers)

# Get the pagination url (in this case, next) from the response body’s meta object
pagination_url = response.json()['meta']['next']

# Make an authorized GET request to the pagination url to get next results
next_response = requests.get(pagination_url, headers=headers)
