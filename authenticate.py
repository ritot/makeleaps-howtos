import requests
import base64

"""
Authentication with the MakeLeaps app via API using OAuth2
"""

# Retrieve access token
url = 'https://api-meetup.makeleaps.com/user/oauth2/token/'

# Encode credentials to pass into header
creds = f'{self.client_id}:{self.client_secret}'.encode('utf-8')
creds_encoded = base64.b64encode(creds).decode('utf-8')

# Create valid Authorization header
headers = {'Authorization': f'Basic {creds_encoded}'}
data = {'grant_type': 'client_credentials'}

# Send request to retrieve Bearer token
response = requests.post(url, data=data, headers=headers)

## Retrieve Bearer token from server's response
return response.json()['access_token']
