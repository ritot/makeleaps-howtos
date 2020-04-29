import requests
import base64

"""
Revoke an active access token
"""

url = 'https://api.makeleaps.com/user/oauth2/revoke-token/'

# Encode credentials to pass into header
creds = f'{self.client_id}:{self.client_secret}'.encode('utf-8')
creds_encoded = base64.b64encode(creds).decode('utf-8')

# Create valid Authorization header
headers = {'Authorization': f'Basic {creds_encoded}'}

# Pass in token to revoke
data = {'token': f'{token}'}

# Send request to revoke token
response = requests.post(url, data=data, headers=headers)
